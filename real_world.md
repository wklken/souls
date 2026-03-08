---
layout: default
title: 真实世界
title_en: Real World
category: real_world
---

<div class="soul-list">
  <h1 data-i18n="nav.real_world">真实世界</h1>

  <div class="search-section">
    {% include search.html %}
  </div>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title' %}
  {% include category_search.html %}
  
  <div class="soul-grid" id="soul-grid">
    {% if souls.size > 0 %}
    {% for soul in souls %}
      {% assign soul_name_zh = soul.title_zh | default: soul.title %}
      {% assign soul_name_en = soul.title_en | default: soul.english_name | default: soul.title %}
      {% assign soul_tags_zh = soul.tags_zh | default: soul.tags %}
      {% assign soul_tags_en = soul.tags_en | default: soul.tags %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div
          class="soul-name"
          data-localized-zh="{{ soul_name_zh | escape }}"
          data-localized-en="{{ soul_name_en | escape }}"
        >{{ soul_name_zh }}</div>
        {% if soul_name_en and soul_name_en != soul_name_zh %}
        <div
          class="soul-english"
          data-localized-zh="{{ soul_name_en | escape }}"
          data-localized-en="{{ soul_name_zh | escape }}"
        >{{ soul_name_en }}</div>
        {% endif %}
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
