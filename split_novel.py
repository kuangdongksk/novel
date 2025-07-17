#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小说章节分割脚本
将大文件按每10章分割成小文件
"""

import os
import re
import sys

def split_novel_by_chapters(input_file, output_dir, chapters_per_file=10):
    """
    按章节分割小说文件
    
    Args:
        input_file: 输入文件路径
        output_dir: 输出目录
        chapters_per_file: 每个文件包含的章节数，默认10章
    """
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取原始文件
    print(f"正在读取文件: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式匹配章节标题
    # 匹配格式：第X章 或 第XX章 或 第XXX章
    chapter_pattern = r'(第[一二三四五六七八九十百千万\d]+章.*?)(?=第[一二三四五六七八九十百千万\d]+章|$)'
    chapters = re.findall(chapter_pattern, content, re.DOTALL)
    
    if not chapters:
        print("未找到章节，尝试备用匹配模式...")
        # 备用匹配模式：以"第"字开头的行作为章节标题
        lines = content.split('\n')
        chapters = []
        current_chapter = []
        
        for line in lines:
            if line.strip().startswith('第') and '章' in line.strip():
                if current_chapter:
                    chapters.append('\n'.join(current_chapter))
                current_chapter = [line]
            else:
                current_chapter.append(line)
        
        if current_chapter:
            chapters.append('\n'.join(current_chapter))
    
    total_chapters = len(chapters)
    print(f"共找到 {total_chapters} 章")
    
    if total_chapters == 0:
        print("错误：未能找到任何章节")
        return
    
    # 获取文件基础信息
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    
    # 计算需要创建的文件数
    file_count = (total_chapters + chapters_per_file - 1) // chapters_per_file
    
    # 分割章节并写入文件
    for i in range(file_count):
        start_idx = i * chapters_per_file
        end_idx = min((i + 1) * chapters_per_file, total_chapters)
        
        # 获取当前文件包含的章节范围
        chapters_in_file = chapters[start_idx:end_idx]
        
        # 构建输出文件名
        start_chapter = start_idx + 1
        end_chapter = end_idx
        output_filename = f"{name_without_ext}_{start_chapter:03d}-{end_chapter:03d}章.txt"
        output_path = os.path.join(output_dir, output_filename)
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            # 写入标题
            f.write(f"《万相之王》第{start_chapter}-{end_chapter}章\n")
            f.write("=" * 50 + "\n\n")
            
            # 写入章节内容
            for chapter in chapters_in_file:
                f.write(chapter.strip())
                f.write("\n\n")
        
        print(f"已创建: {output_filename} (包含第{start_chapter}-{end_chapter}章)")
    
    print(f"\n分割完成！共创建 {file_count} 个文件")
    print(f"输出目录: {output_dir}")

def process_all_files(source_dir, target_dir):
    """处理目录下的所有小说文件"""
    
    if not os.path.exists(source_dir):
        print(f"错误：源目录 {source_dir} 不存在")
        return
    
    # 获取所有txt文件
    txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt') and '万相之王' in f]
    
    if not txt_files:
        print("未找到万相之王相关文件")
        return
    
    print(f"找到 {len(txt_files)} 个文件需要处理")
    
    for txt_file in txt_files:
        input_path = os.path.join(source_dir, txt_file)
        
        # 为每个文件创建单独的输出目录
        file_name = os.path.splitext(txt_file)[0]
        output_subdir = os.path.join(target_dir, file_name + "_分割")
        
        print(f"\n{'='*50}")
        print(f"正在处理: {txt_file}")
        
        try:
            split_novel_by_chapters(input_path, output_subdir)
        except Exception as e:
            print(f"处理 {txt_file} 时出错: {e}")

def main():
    """主函数"""
    
    # 设置源文件目录和目标目录
    source_directory = r"C:\A\sy\novel\demo\万相之王"
    target_directory = r"C:\A\sy\novel\demo\万相之王_分割版"
    
    print("万相之王小说分割工具")
    print("=" * 50)
    
    process_all_files(source_directory, target_directory)
    
    print("\n" + "=" * 50)
    print("所有文件处理完成！")

if __name__ == "__main__":
    main()