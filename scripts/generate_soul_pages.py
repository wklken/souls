#!/usr/bin/env python3
"""
Generate Jekyll soul pages from folder-based SOUL.md files.

This keeps source content files clean while producing layout:soul pages
that category listings and search can index.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = {
    "real_world": "真实世界",
    "virtual_world": "非真实世界",
    "personas": "专家角色",
}


def q(value: str | None) -> str:
    if not value:
        return ""
    return value.replace("\\", "\\\\").replace('"', '\\"').strip()


def extract_heading(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def extract_tags(markdown_text: str) -> list[str]:
    tag_section = re.search(r"##\s*标签(.*?)(?:\n##\s+|\Z)", markdown_text, re.S)
    if not tag_section:
        return []
    tags_match = re.search(r"tags:\s*(.+)", tag_section.group(1))
    if not tags_match:
        return []
    parts = re.split(r"[，,]", tags_match.group(1))
    return [p.strip() for p in parts if p.strip()]


def extract_readme_metadata(readme_text: str) -> tuple[str, str, str]:
    name_en = ""
    wiki_zh = ""
    wiki_en = ""

    name_en_match = re.search(r"\*\*英文名\*\*:\s*(.+)", readme_text)
    if name_en_match:
        name_en = name_en_match.group(1).strip()

    wiki_zh_match = re.search(r"\*\*中文\*\*:\s*(https?://\S+)", readme_text)
    if wiki_zh_match:
        wiki_zh = wiki_zh_match.group(1).strip()

    wiki_en_match = re.search(r"\*\*英文\*\*:\s*(https?://\S+)", readme_text)
    if wiki_en_match:
        wiki_en = wiki_en_match.group(1).strip()

    return name_en, wiki_zh, wiki_en


def generate_for_category(category: str, category_name: str) -> int:
    category_dir = ROOT / category
    created = 0

    for folder in sorted(category_dir.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue

        soul_md = folder / "SOUL.md"
        if not soul_md.exists():
            continue

        soul_content = soul_md.read_text(encoding="utf-8")
        title = extract_heading(soul_content) or folder.name.replace("_", " ").title()
        tags = extract_tags(soul_content)
        soul_en = folder / "SOUL.en.md"
        en_source = "SOUL.en.md" if soul_en.exists() else "SOUL.md"

        name_en = ""
        wiki_zh = ""
        wiki_en = ""

        readme = folder / "README.md"
        if readme.exists():
            readme_text = readme.read_text(encoding="utf-8")
            name_en, wiki_zh, wiki_en = extract_readme_metadata(readme_text)

        if not name_en and soul_en.exists():
            name_en = extract_heading(soul_en.read_text(encoding="utf-8"))

        page_path = category_dir / f"{folder.name}.md"

        fm = [
            "---",
            "layout: soul",
            f'title: "{q(title)}"',
            f'english_name: "{q(name_en)}"',
            f'category: "{category}"',
            f'category_name: "{category_name}"',
            f'category_url: "/{category}"',
            f'folder: "{folder.name}"',
            f'permalink: "/{category}/{folder.name}/"',
            f'wikipedia_zh: "{q(wiki_zh)}"',
            f'wikipedia_en: "{q(wiki_en)}"',
            f'edit_url: "https://github.com/wklken/souls/edit/master/{category}/{folder.name}/SOUL.md"',
            f'edit_url_zh: "https://github.com/wklken/souls/edit/master/{category}/{folder.name}/SOUL.md"',
            f'edit_url_en: "https://github.com/wklken/souls/edit/master/{category}/{folder.name}/{en_source}"',
            f'download_url: "/{category}/{folder.name}/SOUL.md"',
            f'download_url_zh: "/{category}/{folder.name}/SOUL.md"',
            f'download_url_en: "/{category}/{folder.name}/{en_source}"',
        ]

        if tags:
            fm.append("tags:")
            for tag in tags:
                fm.append(f'  - "{q(tag)}"')
        else:
            fm.append("tags: []")

        body = [
            f"{{% capture soul_content_zh %}}{{% include_relative {folder.name}/SOUL.md %}}{{% endcapture %}}",
            f"{{% capture soul_content_en %}}{{% include_relative {folder.name}/{en_source} %}}{{% endcapture %}}",
            '<div class="soul-lang-content soul-lang-zh">{{ soul_content_zh | markdownify }}</div>',
            '<div class="soul-lang-content soul-lang-en">{{ soul_content_en | markdownify }}</div>',
        ]

        fm.extend(["---", ""] + body + [""])
        page_path.write_text("\n".join(fm), encoding="utf-8")
        created += 1

    return created


def main() -> None:
    total = 0
    for category, category_name in CATEGORIES.items():
        created = generate_for_category(category, category_name)
        total += created
        print(f"{category}: {created}")
    print(f"total: {total}")


if __name__ == "__main__":
    main()
