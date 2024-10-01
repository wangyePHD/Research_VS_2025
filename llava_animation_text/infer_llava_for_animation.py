from transformers import AutoProcessor, LlavaForConditionalGeneration
from transformers import BitsAndBytesConfig
import torch
import requests
from PIL import Image
import os
from tqdm import tqdm
import json



quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

model_id = "./checkpoints/llava-hf/llava-1.5-13b-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(model_id, quantization_config=quantization_config, device_map="auto")



prompts = [            
            "USER: <image>\nPlease Generate a simple text prompt that is suitable for converting this image to a video or animation\nASSISTANT:",
]

text_folder = "/data1/ye_project/Stylized_Video_Project/llava_animation_text/style30K/animation_text"

test_img_folders = "/data1/ye_project/Stylized_Video_Project/llava_animation_text/style30K/dataset"
sub_folders = os.listdir(test_img_folders)

for sub_folder in sub_folders:
    txt_file_path = os.path.join(text_folder, f"{sub_folder}.json")
    
    # 使用 with 确保文件正确关闭
    animation_txt_dict = {}
    
    with open(txt_file_path, "w") as txt_file:
        imgs_list = os.listdir(os.path.join(test_img_folders, sub_folder))

        for img in tqdm(imgs_list):
            img_path = os.path.join(test_img_folders, sub_folder, img)
            try:
                # 打开图像
                image = Image.open(img_path)

                # 处理图像并生成文本
                inputs = processor(prompts, images=[image], padding=True, return_tensors="pt").to("cuda")
                output = model.generate(**inputs, max_new_tokens=50)
                generated_text = processor.batch_decode(output, skip_special_tokens=True)[0].strip()
                generated_text = generated_text.split("ASSISTANT:")[-1]

                # 将生成的文本存入字典
                animation_txt_dict[img.split("/")[-1]] = generated_text
                
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

        # 在循环外写入所有数据
        json.dump(animation_txt_dict, txt_file, ensure_ascii=False, indent=4)
