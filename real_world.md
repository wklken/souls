---
layout: default
title: 真实世界
category: real_world
---

<div class="soul-list">
  <h1 data-i18n="nav.real_world">真实世界</h1>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title' %}
  
  <div class="soul-grid" id="soul-grid">
    {% if souls.size > 0 %}
    {% for soul in souls %}
      <a href="{{ soul.url | relative_url }}" class="soul-card">
        <div class="soul-name">{{ soul.title }}</div>
        {% if soul.english_name %}
        <div class="soul-english">{{ soul.english_name }}</div>
        {% endif %}
        {% if soul.tags %}
        <div class="soul-tags">{{ soul.tags | join: ', ' }}</div>
        {% endif %}
      </a>
    {% endfor %}
    {% else %}
    <p class="list-empty">暂无人物数据</p>
    {% endif %}
  </div>
</div>
