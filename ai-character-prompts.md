---
layout: default
title: "300+ AI Character Prompts - Historical Figures & Expert Personas"
title_zh: "AI角色Prompt库 - 历史人物与专家角色"
title_en: "AI Character Prompts - Historical Figures & Expert Personas"
description: "Free AI character prompts for ChatGPT, Claude, and other AI assistants. Download 300+ prompts for historical figures like Confucius, Socrates, Laozi, and expert personas like Product Directors, CTOs, Investors."
description_zh: "免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。下载 300+ 历史人物和专家角色的性格设定，包括孔子、苏格拉底、老子、产品总监、CTO、投资人等。"
description_en: "Free AI character prompts for ChatGPT, Claude, and other AI assistants. Download 300+ prompts for historical figures like Confucius, Socrates, Laozi, and expert personas like Product Directors, CTOs, Investors."
keywords: "AI character prompts, character prompts, ChatGPT prompts, Claude prompts, historical figure prompts, expert persona prompts, Confucius prompt, Socrates prompt, Laozi prompt"
permalink: /ai-character-prompts/
---

{% assign real_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title_en' %}
{% assign virtual_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'virtual_world' | sort: 'title_en' %}
{% assign personas_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'personas' | sort: 'title_en' %}

<div class="prompts-landing-page">
  <header class="prompts-hero">
    <h1>AI Character Prompts</h1>
    <p class="prompts-subtitle">让历史人物成为你的 AI 助手</p>
    <p class="prompts-description">
      下载 300+ 免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。
      与孔子探讨仁爱，向苏格拉底学习提问，让诸葛亮为你出谋划策。
    </p>
    <div class="prompts-stats">
      <span class="stat">200+ 历史人物</span>
      <span class="stat">4 位虚拟角色</span>
      <span class="stat">47 位专家角色</span>
    </div>
  </header>

  <section class="prompts-section">
    <h2>Popular Historical Figure Prompts</h2>
    <p class="section-desc">Most searched character prompts for AI assistants</p>
    <div class="prompts-grid">
      {% assign popular_figures = "confucius,socrates,laozi,zhuge_liang,sun_tzu,caocao,hamlet,sherlock_holmes,napoleon,aristotle" | split: "," %}
      {% for soul in real_world_souls %}
        {% assign soul_id = soul.folder | default: soul.url | split: '/' | last %}
        {% if popular_figures contains soul_id %}
          <a href="{{ soul.url | relative_url }}" class="prompt-card">
            <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
            <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
            <span class="prompt-tags">{{ soul.tags_en | default: soul.tags | slice: 0, 3 | join: ', ' }}</span>
          </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Philosopher Prompts</h2>
    <p class="section-desc">Ancient wisdom for modern AI conversations</p>
    <div class="prompts-grid">
      {% for soul in real_world_souls %}
        {% if soul.tags contains '哲学' or soul.tags contains '哲学家' or soul.tags_en contains 'philosopher' or soul.tags_en contains 'philosophy' %}
          <a href="{{ soul.url | relative_url }}" class="prompt-card">
            <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
            <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
          </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Military Strategist Prompts</h2>
    <p class="section-desc">Strategic thinking for business and life</p>
    <div class="prompts-grid">
      {% for soul in real_world_souls %}
        {% if soul.tags contains '军事' or soul.tags contains '兵法' or soul.tags_en contains 'military' or soul.tags_en contains 'strategy' %}
          <a href="{{ soul.url | relative_url }}" class="prompt-card">
            <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
            <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
          </a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Virtual Character Prompts</h2>
    <p class="section-desc">Literary and fictional characters for creative AI roleplay</p>
    <div class="prompts-grid">
      {% for soul in virtual_world_souls %}
        <a href="{{ soul.url | relative_url }}" class="prompt-card">
          <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
          <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
        </a>
      {% endfor %}
    </div>
  </section>

  <section class="prompts-section">
    <h2>Expert Persona Prompts</h2>
    <p class="section-desc">Professional AI assistants for work and learning</p>
    <div class="prompts-grid">
      {% for soul in personas_souls limit: 24 %}
        <a href="{{ soul.url | relative_url }}" class="prompt-card">
          <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
          <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
        </a>
      {% endfor %}
    </div>
    <a href="{{ '/personas/' | relative_url }}" class="view-more">View all 47 expert personas →</a>
  </section>

  <section class="prompts-guide">
    <h2>How to Use AI Character Prompts</h2>
    <div class="guide-steps">
      <div class="step">
        <span class="step-number">1</span>
        <h3>Choose a Character</h3>
        <p>Browse 300+ historical figures, virtual characters, and expert personas</p>
      </div>
      <div class="step">
        <span class="step-number">2</span>
        <h3>Download SOUL.md</h3>
        <p>Get the complete character prompt with personality, beliefs, and speaking style</p>
      </div>
      <div class="step">
        <span class="step-number">3</span>
        <h3>Use as System Prompt</h3>
        <p>Copy to ChatGPT, Claude, or any AI assistant as the system instruction</p>
      </div>
      <div class="step">
        <span class="step-number">4</span>
        <h3>Start Conversing</h3>
        <p>Ask questions, seek advice, or explore ideas in character</p>
      </div>
    </div>
  </section>

  <section class="prompts-faq-teaser">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item">
        <h4>What is an AI character prompt?</h4>
        <p>A detailed personality setting that allows AI assistants to respond as a specific character with their beliefs, knowledge, and speaking style.</p>
      </div>
      <div class="faq-item">
        <h4>Can I use these prompts for commercial projects?</h4>
        <p>Yes, all prompts are MIT licensed. You can use, modify, and distribute them freely.</p>
      </div>
      <div class="faq-item">
        <h4>How do I create my own character prompts?</h4>
        <p>Study the SOUL.md structure and use our <a href="https://github.com/wklken/souls/blob/master/scripts/soul-creator.sh">soul-creator tool</a> to generate new characters.</p>
      </div>
    </div>
    <a href="{{ '/faq/' | relative_url }}" class="view-more">View all FAQs →</a>
  </section>
</div>

<style>
.prompts-landing-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.prompts-hero {
  text-align: center;
  padding: 3rem 1rem;
  margin-bottom: 3rem;
}

.prompts-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.prompts-subtitle {
  font-size: 1.5rem;
  color: var(--text-secondary);
  margin-bottom: 1rem;
}

.prompts-description {
  max-width: 700px;
  margin: 0 auto 1.5rem;
  font-size: 1.1rem;
  line-height: 1.6;
}

.prompts-stats {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.prompts-stats .stat {
  padding: 0.5rem 1rem;
  background: var(--bg-secondary);
  border-radius: 20px;
  font-weight: 600;
}

.prompts-section {
  margin-bottom: 3rem;
}

.prompts-section h2 {
  margin-bottom: 0.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border-color);
}

.section-desc {
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
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

.prompt-name-en {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.prompt-name-zh {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.prompt-tags {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.view-more {
  display: inline-block;
  margin-top: 1rem;
  color: var(--primary);
  text-decoration: none;
}

.view-more:hover {
  text-decoration: underline;
}

.prompts-guide {
  background: var(--bg-secondary);
  padding: 2rem;
  border-radius: 12px;
  margin: 3rem 0;
}

.guide-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.step {
  text-align: center;
}

.step-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: var(--primary);
  color: white;
  border-radius: 50%;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.step h3 {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.step p {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.prompts-faq-teaser {
  margin-top: 3rem;
}

.faq-list {
  display: grid;
  gap: 1rem;
  margin: 1.5rem 0;
}

.faq-item {
  padding: 1rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
}

.faq-item h4 {
  margin-bottom: 0.5rem;
  color: var(--primary);
}

.faq-item p {
  color: var(--text-secondary);
  margin: 0;
}
</style>
