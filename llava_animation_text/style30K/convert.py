import json


def convert_unicode_in_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        # 直接读取内容
        data = file.read()

    # 使用 json.loads 解析 JSON 字符串，自动处理 Unicode
    converted_data = json.loads(data)

    # 将转换后的数据写入新文件
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(converted_data, file, ensure_ascii=False, indent=4)

# 使用示例
input_file = 'style_mapper.json'  # 替换为你的输入文件名
output_file = 'style_mapper_converted.json'  # 输出文件名
convert_unicode_in_json(input_file, output_file)