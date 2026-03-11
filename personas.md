---
layout: default
title: "专家角色AI人格设定 | 产品总监、CTO、投资人"
title_en: "Personas"
title_zh: "专家角色"
seo_title_zh: "专家角色AI人格设定 | 产品总监、CTO、投资人"
seo_title_en: "Expert Persona AI Prompt Library"
description: "专家角色AI人格设定，覆盖产品总监、硅谷CTO、投资人、管理顾问等场景。获取可直接下载的SOUL.md，提升专业判断与决策质量。"
description_zh: "专家角色AI人格设定，覆盖产品总监、硅谷CTO、投资人、管理顾问等场景。获取可直接下载的SOUL.md，提升专业判断与决策质量。"
description_en: "Explore expert persona AI prompts for product directors, Silicon Valley CTOs, investors, consultants, and more. Download SOUL.md files for sharper professional decision-making."
image: "https://robohash.org/agent-souls-personas.png?size=1200x630&set=set4&bgset=bg1"
category: personas
permalink: /personas/
---

<div class="soul-list">
  <h1 data-i18n="nav.personas">专家角色</h1>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'personas' | sort: 'title' %}
  {% include category_search.html %}
  
  <div class="soul-grid" id="soul-grid">
    {% if souls.size > 0 %}
    {% for soul in souls %}
      {% assign soul_name_zh = soul.title_zh | default: soul.title %}
      {% assign soul_name_zh_display = soul_name_zh | split: '（' | first | split: '(' | first | strip %}
      {% assign soul_name_en = soul.english_name | default: soul.title_en | default: soul.title %}
      {% assign soul_tags_zh = soul.tags_zh | default: soul.tags %}
      {% assign soul_tags_en = soul.tags_en | default: soul.tags %}
      {% assign soul_tags_zh_preview = soul_tags_zh | slice: 0, 6 %}
      {% assign soul_tags_en_preview = soul_tags_en | slice: 0, 6 %}
      {% assign soul_tags_zh_text = soul_tags_zh_preview | join: ' · ' %}
      {% assign soul_tags_en_text = soul_tags_en_preview | join: ' · ' %}
      {% if soul_tags_zh.size > 6 %}
        {% assign soul_tags_zh_text = soul_tags_zh_text | append: ' · ...' %}
      {% endif %}
      {% if soul_tags_en.size > 6 %}
        {% assign soul_tags_en_text = soul_tags_en_text | append: ' · ...' %}
      {% endif %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div
          class="soul-name"
          data-localized-zh="{{ soul_name_zh_display | escape }}"
          data-localized-en="{{ soul_name_en | escape }}"
        >{{ soul_name_zh_display }}</div>
        {% if soul_tags_zh or soul_tags_en %}
        <div
          class="soul-tags"
          data-localized-zh="{{ soul_tags_zh_text | escape }}"
          data-localized-en="{{ soul_tags_en_text | escape }}"
        >{{ soul_tags_zh_text }}</div>
        {% endif %}
      </a>
    {% endfor %}
    {% else %}
    <p class="list-empty">暂无人物数据</p>
    {% endif %}
  </div>
</div>
