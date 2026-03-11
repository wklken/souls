---
layout: default
title: "经典虚拟角色AI人格设定 | 孙悟空、福尔摩斯、哈姆雷特"
title_en: "Virtual World"
title_zh: "非真实世界"
seo_title_zh: "经典虚拟角色AI人格设定 | 孙悟空、福尔摩斯、哈姆雷特"
seo_title_en: "Classic Character AI Persona Library"
description: "经典虚拟角色AI人格设定：孙悟空、福尔摩斯、哈姆雷特、堂吉诃德。让AI以文学角色的方式与你互动。"
description_zh: "经典虚拟角色AI人格设定：孙悟空、福尔摩斯、哈姆雷特、堂吉诃德。让AI以文学角色的方式与你互动。"
description_en: "Explore classic character AI personas, including Sun Wukong, Sherlock Holmes, Hamlet, and Don Quixote, and interact with literary voices in a more vivid way."
image: "https://robohash.org/agent-souls-virtual-world.png?size=1200x630&set=set4&bgset=bg1"
category: virtual_world
permalink: /virtual_world/
---

<div class="soul-list">
  <h1 data-i18n="nav.virtual_world">非真实世界</h1>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'virtual_world' | sort: 'title' %}
  {% include category_search.html %}
  
  <div class="soul-grid" id="soul-grid">
    {% if souls.size > 0 %}
    {% for soul in souls %}
      {% assign soul_name_zh = soul.title_zh | default: soul.title %}
      {% assign soul_name_zh_display = soul_name_zh | split: '（' | first | split: '(' | first | strip %}
      {% assign soul_name_en = soul.english_name | default: soul.title_en | default: soul.title %}
      {% assign soul_tags_zh = soul.tags_zh | default: soul.tags %}
      {% assign soul_tags_en = soul.tags_en | default: soul.tags %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div
          class="soul-name"
          data-localized-zh="{{ soul_name_zh_display | escape }}"
          data-localized-en="{{ soul_name_en | escape }}"
        >{{ soul_name_zh_display }}</div>
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
