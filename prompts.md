---
layout: default
title: "AI Character Prompts"
description: "Free AI character prompts for historical figures, philosophers, and virtual characters. Download 300+ AI souls for ChatGPT, Claude, and other AI assistants."
---

{% assign real_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title' %}
{% assign virtual_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'virtual_world' | sort: 'title' %}
{% assign personas_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'personas' | sort: 'title' %}

<div class="prompts-page">
  <nav class="breadcrumb">
    <a href="{{ '/' | relative_url }}" data-i18n="nav.home">首页</a>
    <span>/</span>
    <span>AI Prompts</span>
  </nav>

  <header class="prompts-header">
    <h1>AI Character Prompts</h1>
    <p class="prompts-subtitle">Free prompts for historical figures, philosophers & virtual characters</p>
    <p class="prompts-description">
      Download 300+ AI character prompts to bring historical figures to life in ChatGPT, Claude, and other AI assistants.
      Search prompts for Laozi, Confucius, Socrates, Zhuge Liang, Sun Tzu, and more.
    </p>
  </header>

  <section class="prompts-section">
    <h2>Popular Historical Figure Prompts</h2>
    <div class="prompts-grid">
      {% assign popular_figures = "confucius,laozi,socrates,zhuge_liang,sun_tzu,caocao,hamlet,sherlock_holmes" | split: "," %}
      {% for soul in real_world_souls %}
        {% assign soul_id = soul.url | split: '/' | last %}
        {% if popular_figures contains soul_id %}
          <a href="{{ soul.url | relative_url }}" class="prompt-card">
            <span class="prompt-name">{{ soul.english_name | default: soul.title }}</span>
            <span class="prompt-tags">{{ soul.tags | slice: 0, 3 | join: ', ' }}</span>
          </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Philosopher Prompts</h2>
    <div class="prompts-grid">
      {% for soul in real_world_souls %}
        {% if soul.tags contains '哲学' or soul.tags contains '哲学家' or soul.tags_en contains 'philosopher' %}
          <a href="{{ soul.url | relative_url }}" class="prompt-card">
            <span class="prompt-name">{{ soul.english_name | default: soul.title }}</span>
            <span class="prompt-tags">{{ soul.tags | slice: 0, 3 | join: ', ' }}</span>
          </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Virtual Character Prompts</h2>
    <div class="prompts-grid">
      {% for soul in virtual_world_souls limit: 8 %}
        <a href="{{ soul.url | relative_url }}" class="prompt-card">
          <span class="prompt-name">{{ soul.english_name | default: soul.title }}</span>
          <span class="prompt-tags">{{ soul.tags | slice: 0, 3 | join: ', ' }}</span>
        </a>
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Expert Persona Prompts</h2>
    <div class="prompts-grid">
      {% for soul in personas_souls %}
        <a href="{{ soul.url | relative_url }}" class="prompt-card">
          <span class="prompt-name">{{ soul.english_name | default: soul.title }}</span>
          <span class="prompt-tags">{{ soul.tags | slice: 0, 3 | join: ', ' }}</span>
        </a>
      {% endfor %}
    </div>
  </section>

  <section class="prompts-cta">
    <h2>How to Use These Prompts</h2>
    <ol>
      <li>Click on any character above</li>
      <li>Download the SOUL.md file or copy the content</li>
      <li>Use as system prompt in ChatGPT, Claude, or your favorite AI assistant</li>
      <li>Start a conversation with historical figures!</li>
    </ol>
  </section>
</div>

<style>
.prompts-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.prompts-header {
  text-align: center;
  margin-bottom: 3rem;
}

.prompts-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.prompts-subtitle {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: 1rem;
}

.prompts-description {
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

.prompts-section {
  margin-bottom: 3rem;
}

.prompts-section h2 {
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border-color);
}

.prompts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.prompt-card {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
}

.prompt-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.prompt-name {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.prompt-tags {
  font-size: 0.875rem;
  color: var(--text-secondary);
}

.prompts-cta {
  background: var(--bg-secondary);
  padding: 2rem;
  border-radius: 8px;
  margin-top: 3rem;
}

.prompts-cta ol {
  margin: 1rem 0;
  padding-left: 1.5rem;
}

.prompts-cta li {
  margin: 0.5rem 0;
}
</style>
