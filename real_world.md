---
layout: default
title: "历史人物AI灵魂库 | 孔子、苏格拉底、诸葛亮Prompt"
title_en: "Real World"
title_zh: "真实世界"
seo_title_zh: "历史人物AI灵魂库 | 孔子、苏格拉底、诸葛亮Prompt"
seo_title_en: "Historical Figure AI Soul Library"
description: "历史人物AI灵魂库，收录200+历史人物AI灵魂设定：诸葛亮、苏格拉底、孔子、曹操等。下载SOUL.md，让AI以历史伟人的思维方式与你对话。"
description_zh: "历史人物AI灵魂库，收录200+历史人物AI灵魂设定：诸葛亮、苏格拉底、孔子、曹操等。下载SOUL.md，让AI以历史伟人的思维方式与你对话。"
description_en: "Explore 200+ historical figure AI soul prompts, including Zhuge Liang, Socrates, Confucius, and Cao Cao. Download SOUL.md files and chat with the logic of historical thinkers."
image: "https://robohash.org/agent-souls-real-world.png?size=1200x630&set=set4&bgset=bg1"
category: real_world
permalink: /real_world/
---

<div class="soul-list">
  <h1 data-i18n="nav.real_world">真实世界</h1>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title' %}
  {% include category_search.html %}
  
  <div class="soul-grid" id="soul-grid">
    {% if souls.size > 0 %}
    {% for soul in souls %}
      {% assign soul_name_zh = soul.title_zh | default: soul.title %}
      {% assign soul_name_en = soul.english_name | default: soul.title_en | default: soul.title %}
      {% assign soul_tags_zh = soul.tags_zh | default: soul.tags %}
      {% assign soul_tags_en = soul.tags_en | default: soul.tags %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div
          class="soul-name"
          data-localized-zh="{{ soul_name_zh | escape }}"
          data-localized-en="{{ soul_name_en | escape }}"
        >{{ soul_name_zh }}</div>
        {% if soul_tags_zh or soul_tags_en %}
        <div
          class="soul-tags"
          data-localized-zh="{{ soul_tags_zh | join: ', ' | escape }}"
          data-localized-en="{{ soul_tags_en | join: ', ' | escape }}"
        >{{ soul_tags_zh | join: ', ' }}</div>
        {% endif %}
      </a>
    {% endfor %}
    {% else %}
    <p class="list-empty">暂无人物数据</p>
    {% endif %}
  </div>
</div>
