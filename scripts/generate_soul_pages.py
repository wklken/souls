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
    "real_world": {"zh": "真实世界", "en": "Real World"},
    "virtual_world": {"zh": "非真实世界", "en": "Virtual World"},
    "personas": {"zh": "专家角色", "en": "Personas"},
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
    for line in markdown_text.splitlines():
        tags_match = re.search(r"\btags:\s*(.+)", line, re.I)
        if not tags_match:
            continue
        parts = re.split(r"[，,]", tags_match.group(1))
        return [p.strip() for p in parts if p.strip()]
    return []


def extract_readme_metadata(readme_text: str) -> tuple[str, str, str]:
    name_en = ""
    wiki_zh = ""
    wiki_en = ""

    name_en_match = re.search(r"\*\*英文名\*\*:\s*(.+)", readme_text)
    if name_en_match:
        name_en = name_en_match.group(1).strip()
        if name_en in {"待补充", "Pending", "(Pending manual verification)"}:
            name_en = ""

    wiki_zh_match = re.search(r"\*\*中文\*\*:\s*(https?://\S+)", readme_text)
    if wiki_zh_match:
        wiki_zh = wiki_zh_match.group(1).strip()

    wiki_en_match = re.search(r"\*\*英文\*\*:\s*(https?://\S+)", readme_text)
    if wiki_en_match:
        wiki_en = wiki_en_match.group(1).strip()

    return name_en, wiki_zh, wiki_en


def append_yaml_list(front_matter: list[str], key: str, values: list[str]) -> None:
    if values:
        front_matter.append(f"{key}:")
        for value in values:
            front_matter.append(f'  - "{q(value)}"')
        return

    front_matter.append(f"{key}: []")


def clear_generated_pages(category_dir: Path) -> None:
    """Remove stale generated entry pages before a fresh generation pass."""
    for page in category_dir.glob("*.md"):
        page.unlink()


def generate_for_category(category: str, category_name: str | dict[str, str]) -> int:
    category_dir = ROOT / category
    created = 0

    clear_generated_pages(category_dir)

    if isinstance(category_name, dict):
        category_name_zh = category_name.get("zh", "")
        category_name_en = category_name.get("en", "")
    else:
        category_name_zh = category_name
        category_name_en = CATEGORIES.get(category, {}).get("en", "")

    if not category_name_en:
        category_name_en = category.replace("_", " ").title()

    for folder in sorted(category_dir.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue

        soul_md = folder / "SOUL.md"
        if not soul_md.exists():
            continue

        soul_content = soul_md.read_text(encoding="utf-8")
        title_zh = extract_heading(soul_content) or folder.name.replace("_", " ").title()
        tags_zh = extract_tags(soul_content)
        soul_en = folder / "SOUL.en.md"
        soul_content_en = soul_content
        en_source = "SOUL.md"
        if soul_en.exists():
            en_source = "SOUL.en.md"
            soul_content_en = soul_en.read_text(encoding="utf-8")

        title_en = extract_heading(soul_content_en)
        tags_en = extract_tags(soul_content_en)

        name_en = ""
        wiki_zh = ""
        wiki_en = ""

        readme = folder / "README.md"
        if readme.exists():
            readme_text = readme.read_text(encoding="utf-8")
            name_en, wiki_zh, wiki_en = extract_readme_metadata(readme_text)

        if not title_en:
            title_en = name_en
        if not name_en:
            name_en = title_en
        if not title_en:
            title_en = title_zh
        if not tags_en:
            tags_en = tags_zh

        page_path = category_dir / f"{folder.name}.md"

        fm = [
            "---",
            "layout: soul",
            f'title: "{q(title_zh)}"',
            f'title_zh: "{q(title_zh)}"',
            f'title_en: "{q(title_en)}"',
            f'english_name: "{q(name_en)}"',
            f'category: "{category}"',
            f'category_name: "{q(category_name_zh)}"',
            f'category_name_zh: "{q(category_name_zh)}"',
            f'category_name_en: "{q(category_name_en)}"',
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

        append_yaml_list(fm, "tags", tags_zh)
        append_yaml_list(fm, "tags_zh", tags_zh)
        append_yaml_list(fm, "tags_en", tags_en)

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
