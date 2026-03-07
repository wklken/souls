#!/usr/bin/env python3
"""
Souls 数据迁移脚本
将现有的扁平化 md 文件迁移到新的文件夹结构
"""

import os
import re
import shutil
from pathlib import Path

# 配置
CATEGORIES = {
    'real_world': '真实世界',
    'virtual_world': '非真实世界', 
    'personas': '专家角色'
}

# 维基百科链接模板
WIKIPEDIA_TEMPLATES = {
    'confucius': ('https://zh.wikipedia.org/wiki/孔子', 'https://en.wikipedia.org/wiki/Confucius'),
    'laozi': ('https://zh.wikipedia.org/wiki/老子', 'https://en.wikipedia.org/wiki/Laozi'),
    'socrates': ('https://zh.wikipedia.org/wiki/苏格拉底', 'https://en.wikipedia.org/wiki/Socrates'),
    'plato': ('https://zh.wikipedia.org/wiki/柏拉图', 'https://en.wikipedia.org/wiki/Plato'),
    'aristotle': ('https://zh.wikipedia.org/wiki/亚里士多德', 'https://en.wikipedia.org/wiki/Aristotle'),
    'newton': ('https://zh.wikipedia.org/wiki/艾萨克·牛顿', 'https://en.wikipedia.org/wiki/Isaac_Newton'),
    'einstein': ('https://zh.wikipedia.org/wiki/阿尔伯特·爱因斯坦', 'https://en.wikipedia.org/wiki/Albert_Einstein'),
    'darwin': ('https://zh.wikipedia.org/wiki/查尔斯·达尔文', 'https://en.wikipedia.org/wiki/Charles_Darwin'),
    'marx': ('https://zh.wikipedia.org/wiki/卡尔·马克思', 'https://en.wikipedia.org/wiki/Karl_Marx'),
    'kant': ('https://zh.wikipedia.org/wiki/伊曼努尔·康德', 'https://en.wikipedia.org/wiki/Immanuel_Kant'),
    'nietzsche': ('https://zh.wikipedia.org/wiki/弗里德里希·尼采', 'https://en.wikipedia.org/wiki/Friedrich_Nietzsche'),
    'shakespeare': ('https://zh.wikipedia.org/wiki/威廉·莎士比亚', 'https://en.wikipedia.org/wiki/William_Shakespeare'),
    'sherlock_holmes': ('https://zh.wikipedia.org/wiki/歇洛克·福尔摩斯', 'https://en.wikipedia.org/wiki/Sherlock_Holmes'),
    'sun_wukong': ('https://zh.wikipedia.org/wiki/孙悟空', 'https://en.wikipedia.org/wiki/Sun_Wukong'),
    'don_quixote': ('https://zh.wikipedia.org/wiki/堂吉诃德', 'https://en.wikipedia.org/wiki/Don_Quixote'),
    'hamlet': ('https://zh.wikipedia.org/wiki/哈姆雷特', 'https://en.wikipedia.org/wiki/Hamlet'),
}

def extract_title(content):
    """从 markdown 内容中提取标题"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def extract_tags(content):
    """从 markdown 内容中提取标签"""
    match = re.search(r'## 标签\s*\ncategory:\s*([^\n]+)', content)
    if match:
        tags_line = match.group(1)
        # 提取 tags: 后面的内容
        tags_match = re.search(r'tags:\s*(.+)', tags_line)
        if tags_match:
            return [t.strip() for t in tags_match.group(1).split(',')]
    return []

def extract_english_name(content):
    """尝试从内容中提取英文名"""
    # 查找括号中的英文
    match = re.search(r'[（(]([A-Za-z\s]+)[)）]', content)
    if match:
        return match.group(1).strip()
    return None

def get_wikipedia_links(folder_name):
    """获取维基百科链接"""
    if folder_name in WIKIPEDIA_TEMPLATES:
        return WIKIPEDIA_TEMPLATES[folder_name]
    # 默认链接
    return (
        f"https://zh.wikipedia.org/wiki/{folder_name}",
        f"https://en.wikipedia.org/wiki/{folder_name.replace('_', ' ').title().replace(' ', '_')}"
    )

def create_readme(folder_path, title, english_name, tags, category):
    """创建 README.md"""
    folder_name = folder_path.name
    wiki_zh, wiki_en = get_wikipedia_links(folder_name)
    
    content = f"""# {title}

## 基本信息
- **中文名**: {title}
- **英文名**: {english_name or '待补充'}
- **分类**: {CATEGORIES.get(category, category)}

## 简介
[待补充人物简介]

## 维基百科链接
- **中文**: {wiki_zh}
- **英文**: {wiki_en}

## 标签
{', '.join(tags) if tags else '待补充'}
"""
    
    readme_path = folder_path / "README.md"
    readme_path.write_text(content, encoding='utf-8')
    print(f"  Created: {readme_path}")

def migrate_soul(source_file, category, target_base):
    """迁移单个 soul 文件"""
    filename = source_file.stem
    content = source_file.read_text(encoding='utf-8')
    
    # 提取信息
    title = extract_title(content) or filename.replace('_', ' ').title()
    tags = extract_tags(content)
    english_name = extract_english_name(content)
    
    # 创建目标文件夹
    target_folder = target_base / filename
    target_folder.mkdir(parents=True, exist_ok=True)
    
    # 写入 SOUL.md (中文)
    soul_md = target_folder / "SOUL.md"
    soul_md.write_text(content, encoding='utf-8')
    print(f"  Created: {soul_md}")
    
    # 写入 SOUL.en.md (英文占位)
    soul_en_md = target_folder / "SOUL.en.md"
    en_content = f"""> **Translation Status**: 🚧 Pending - This file currently contains Chinese content and needs English translation.

---

{content}"""
    soul_en_md.write_text(en_content, encoding='utf-8')
    print(f"  Created: {soul_en_md}")
    
    # 创建 README.md
    create_readme(target_folder, title, english_name, tags, category)
    
    return {
        'name': title,
        'name_en': english_name,
        'folder': filename,
        'category': category,
        'tags': tags
    }

def create_soul_page(folder_path, category, category_name):
    """为每个人物创建 Jekyll 页面"""
    folder_name = folder_path.name
    soul_md = folder_path / "SOUL.md"
    readme = folder_path / "README.md"
    
    if not soul_md.exists():
        print(f"  Warning: {soul_md} not found")
        return
    
    # 读取内容
    content = soul_md.read_text(encoding='utf-8')
    readme_content = readme.read_text(encoding='utf-8') if readme.exists() else ""
    
    # 提取标题
    title = extract_title(content) or folder_name.replace('_', ' ').title()
    
    # 提取英文名
    english_name = None
    wiki_zh = ""
    wiki_en = ""
    
    if readme_content:
        en_match = re.search(r'\*\*英文名\*\*:\s*(.+)', readme_content)
        if en_match:
            english_name = en_match.group(1).strip()
            if english_name == '待补充':
                english_name = None
        
        wiki_zh_match = re.search(r'\*\*中文\*\*:\s*(https?://\S+)', readme_content)
        wiki_en_match = re.search(r'\*\*英文\*\*:\s*(https?://\S+)', readme_content)
        if wiki_zh_match:
            wiki_zh = wiki_zh_match.group(1)
        if wiki_en_match:
            wiki_en = wiki_en_match.group(1)
    
    # 创建 Jekyll 页面
    page_content = f"""---
layout: soul
title: "{title}"
english_name: "{english_name or ''}"
category: "{category}"
category_name: "{category_name}"
category_url: "/{category}"
folder: "{folder_name}"
tags: {extract_tags(content)}
wikipedia_zh: "{wiki_zh}"
wikipedia_en: "{wiki_en}"
edit_url: "https://github.com/wklken/souls/edit/master/{category}/{folder_name}/SOUL.md"
download_url: "/{category}/{folder_name}/SOUL.md"
---

{content}
"""
    
    # 保存到分类目录下作为索引页面
    page_file = folder_path.parent / f"{folder_name}.md"
    page_file.write_text(page_content, encoding='utf-8')
    print(f"  Created page: {page_file}")

def main():
    """主函数"""
    base_dir = Path(__file__).parent.parent
    
    print("=" * 60)
    print("Souls 数据迁移工具")
    print("=" * 60)
    
    stats = {'real_world': 0, 'virtual_world': 0, 'personas': 0}
    
    for category in CATEGORIES.keys():
        source_dir = base_dir / category
        if not source_dir.exists():
            print(f"\n跳过 {category}: 目录不存在")
            continue
        
        print(f"\n处理分类: {category} ({CATEGORIES[category]})")
        print("-" * 40)
        
        # 获取所有 md 文件
        md_files = list(source_dir.glob("*.md"))
        
        for md_file in md_files:
            print(f"\n迁移: {md_file.name}")
            try:
                migrate_soul(md_file, category, source_dir)
                stats[category] += 1
            except Exception as e:
                print(f"  Error: {e}")
        
        # 为每个文件夹创建 Jekyll 页面
        print(f"\n创建 Jekyll 页面...")
        for folder in source_dir.iterdir():
            if folder.is_dir() and not folder.name.startswith('.'):
                try:
                    create_soul_page(folder, category, CATEGORIES[category])
                except Exception as e:
                    print(f"  Error creating page for {folder.name}: {e}")
    
    print("\n" + "=" * 60)
    print("迁移完成!")
    print(f"  真实世界: {stats['real_world']} 个人物")
    print(f"  非真实世界: {stats['virtual_world']} 个人物")
    print(f"  专家角色: {stats['personas']} 个人物")
    print(f"  总计: {sum(stats.values())} 个人物")
    print("=" * 60)

if __name__ == '__main__':
    main()
