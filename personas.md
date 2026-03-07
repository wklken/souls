---
layout: default
title: 专家角色
category: personas
---

<div class="soul-list">
  <h1 data-i18n="nav.personas">专家角色</h1>
  {% assign souls = site.pages | where: 'layout', 'soul' | where: 'category', 'personas' | sort: 'title' %}
  
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
