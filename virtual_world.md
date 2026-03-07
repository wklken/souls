---
layout: default
title: 非真实世界
category: virtual_world
---

<div class="soul-list">
  <h1 data-i18n="nav.virtual_world">非真实世界</h1>
  
  <div class="soul-grid" id="soul-grid">
    {% for soul in site.pages %}
      {% if soul.layout == 'soul' and soul.category == 'virtual_world' %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div class="soul-name">{{ soul.title }}</div>
        {% if soul.tags %}
        <div class="soul-tags">{{ soul.tags | join: ', ' }}</div>
        {% endif %}
      </a>
      {% endif %}
    {% endfor %}
  </div>
</div>
