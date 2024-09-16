import re

def extract_section_urls(md_content):
    """
    解析Markdown内容，提取每个section下的视频URL。

    :param md_content: 字符串，Markdown文件的内容
    :return: 字典，键为section名称，值为URL列表
    """
    sections = {}
    current_section = None
    in_front_matter = False

    # 定义正则表达式
    section_pattern = re.compile(r'^##\s+(.*)')
    link_pattern = re.compile(r'\[.*?\]\((https?://[^)]+)\)')

    for line in md_content.splitlines():
        line = line.strip()

        # 处理YAML前置部分
        if line.startswith('---'):
            in_front_matter = not in_front_matter
            continue
        if in_front_matter:
            continue

        # 检查是否是新的section
        section_match = section_pattern.match(line)
        if section_match:
            current_section = section_match.group(1).strip()
            sections[current_section] = []
            continue

        # 如果当前有section，尝试提取链接
        if current_section:
            link_matches = link_pattern.findall(line)
            if link_matches:
                sections[current_section].extend(link_matches)

    return sections

def main():
    # 指定Markdown文件的路径
    input_md_file = '../_posts/2024-09-16-all-youtube.md'  # 请将此路径替换为你的MD文件路径
    output_txt_file = 'output.txt'  # 输出的TXT文件路径

    try:
        # 读取文件内容
        with open(input_md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
    except FileNotFoundError:
        print(f"错误：未找到文件 {input_md_file}")
        return
    except Exception as e:
        print(f"读取文件时出错：{e}")
        return

    # 提取section和对应的URLs
    sections = extract_section_urls(md_content)

    try:
        # 写入输出文件
        with open(output_txt_file, 'w', encoding='utf-8') as out_file:
            out_file.write("==============================\n⭐⭐⭐⭐⭐\n")
            out_file.write("以下是所有视频。\n\n")
            for section, urls in sections.items():
                out_file.write(f"- {section}\n")
                for url in urls:
                    out_file.write(f"{url}\n")
                out_file.write("\n")  # 添加空行分隔不同的section

        print(f"提取的URL已保存到 {output_txt_file}")
    except Exception as e:
        print(f"写入文件时出错：{e}")

if __name__ == "__main__":
    main()
