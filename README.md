# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>

这个项目是用来生成animation video。主要的技术路线是：
1. 输入style图像和文本提示给LLaVA，输出animation text。（请参考Research_VS_2025/llava_animation_text）
2. 利用输出的animation text，和style图像，输入至DynamiCrafter，生成animation video。（请参考Research_VS_2025/DynamiCrafter）

## Getting Started <a name = "getting_started"></a>

你需要安装以下环境，我强烈推荐你安装两个conda 环境。一个是llava，一个是DCrafter。能够避免两个子项目之间的冲突问题。


### Installing for LLAVA

安装llava环境：

```python
conda create -n llava python=3.10
conda activate llava
cd Research_VS_2025/llava_animation_text
pip install -r requirements.txt
```

接下来，你需要下载llava的预训练权重。

```bash
bash hugging_downloader.sh llava-hf/llava-1.5-13b-hf
```

下载下来的权重，会保存在 Research_VS_2025/llava_animation_text/checkpoints中

运行以下命令，即可完成animation text的生成。
```bash
python infer_llava_for_animation.py
```
生成的结果存储在：Research_VS_2025/llava_animation_text/style30K/animation_text

---

### Installing for DynamiCrafter

按照下面的命令安装DCrafter环境：

```bash
cd Research_VS_2025
git clone https://github.com/Doubiiu/DynamiCrafter.git
conda create -n DCrafter python=3.8.5
conda activate DCrafter
cd DynamiCrafter
pip install -r requirements.txt
```

下载DCrafter的预训练权重：

```bash
cd Research_VS_2025
export HF_ENDPOINT=https://hf-mirror.com
./hfd.sh Doubiiu/DynamiCrafter_512  --tool aria2c -x 8 --hf_username wyjlu  --hf_token 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
```

下载完成后，执行以下命令：

```bash
cd Research_VS_2025/DynamiCrafter
mkdir -r checkpoints/dynamicrafter_512_v1
cd Research_VS_2025
mv DynamiCrafter_512/* DynamiCrafter/checkpoints/dynamicrafter_512_v1
```

运行以下命令，即可完成animation video的生成。
```bash
sh scripts/run.sh 512
```

请注意，输入的图像和prompts信息，在文件夹 Research_VS_2025/DynamiCrafter/prompts/512 中。参考这里的样式，放置你的数据即可。

