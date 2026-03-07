---
layout: default
title: 专家角色
category: personas
---

<div class="soul-list">
  <h1 data-i18n="nav.personas">专家角色</h1>
  
  <div class="soul-grid" id="soul-grid">
    {% for soul in site.pages %}
      {% if soul.layout == 'soul' and soul.category == 'personas' %}
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
