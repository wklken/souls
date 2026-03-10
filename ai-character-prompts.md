---
layout: default
title: "250+ AI Character Prompts - Historical Figures & Expert Personas"
title_zh: "250+ AI角色Prompt库 - 历史人物与专家角色"
title_en: "250+ AI Character Prompts - Historical Figures & Expert Personas"
description: "Free AI character prompts for ChatGPT, Claude, and other AI assistants. Download 250+ prompts for historical figures like Confucius, Socrates, Laozi, and expert personas like Product Directors, CTOs, Investors."
description_zh: "免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。下载 250+ 历史人物和专家角色的性格设定，包括孔子、苏格拉底、老子、产品总监、CTO、投资人等。"
description_en: "Free AI character prompts for ChatGPT, Claude, and other AI assistants. Download 250+ prompts for historical figures like Confucius, Socrates, Laozi, and expert personas like Product Directors, CTOs, Investors."
keywords: "AI character prompts, character prompts, ChatGPT prompts, Claude prompts, historical figure prompts, expert persona prompts, Confucius prompt, Socrates prompt, Laozi prompt"
permalink: /ai-character-prompts/
---

{% assign real_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'real_world' | sort: 'title_en' %}
{% assign virtual_world_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'virtual_world' | sort: 'title_en' %}
{% assign personas_souls = site.pages | where: 'layout', 'soul' | where: 'category', 'personas' | sort: 'title_en' %}
{% assign real_world_count = real_world_souls | size %}
{% assign virtual_world_count = virtual_world_souls | size %}
{% assign personas_count = personas_souls | size %}
{% assign total_count = real_world_count | plus: virtual_world_count | plus: personas_count %}

<div class="prompts-landing-page">
  <header class="prompts-hero">
    <h1 data-i18n="prompts.title">AI Character Prompts</h1>
    <p class="prompts-subtitle" 
       data-i18n="prompts.subtitle">让历史人物成为你的 AI 助手</p>
    <p class="prompts-description"
       data-i18n="prompts.description"
       data-count="{{ total_count }}">
      下载 {{ total_count }} 个免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。
      与孔子探讨仁爱，向苏格拉底学习提问，让诸葛亮为你出谋划策。
    </p>
    <div class="prompts-stats">
      <span class="stat" data-i18n="prompts.stat_real" data-count="{{ real_world_count }}">{{ real_world_count }} 位历史人物</span>
      <span class="stat" data-i18n="prompts.stat_virtual" data-count="{{ virtual_world_count }}">{{ virtual_world_count }} 位虚拟角色</span>
      <span class="stat" data-i18n="prompts.stat_personas" data-count="{{ personas_count }}">{{ personas_count }} 位专家角色</span>
    </div>
  </header>

  <section class="prompts-section">
    <h2 data-i18n="prompts.popular_title">热门历史人物 Prompts</h2>
    <p class="section-desc" data-i18n="prompts.popular_desc">AI 助手最常用的角色设定</p>
    <div class="prompts-grid">
      {% assign popular_figures = "confucius,socrates,laozi,zhuge_liang,sun_tzu,cao_cao,aristotle,plato" | split: "," %}
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
    <h2 data-i18n="prompts.philosopher_title">哲学家 Prompts</h2>
    <p class="section-desc" data-i18n="prompts.philosopher_desc">古代智慧用于现代 AI 对话</p>
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
    <h2 data-i18n="prompts.military_title">军事家 Prompts</h2>
    <p class="section-desc" data-i18n="prompts.military_desc">商业和生活的战略思维</p>
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
    <h2 data-i18n="prompts.virtual_title">虚拟角色 Prompts</h2>
    <p class="section-desc" data-i18n="prompts.virtual_desc">文学和虚构角色用于创意 AI 角色扮演</p>
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
    <h2 data-i18n="prompts.expert_title">专家角色 Prompts</h2>
    <p class="section-desc" data-i18n="prompts.expert_desc">工作和学习的专业 AI 助手</p>
    <div class="prompts-grid">
      {% for soul in personas_souls limit: 24 %}
        <a href="{{ soul.url | relative_url }}" class="prompt-card">
          <span class="prompt-name-en">{{ soul.english_name | default: soul.title_en }}</span>
          <span class="prompt-name-zh">{{ soul.title_zh | default: soul.title }}</span>
        </a>
      {% endfor %}
    </div>
    <a href="{{ '/personas/' | relative_url }}" class="view-more" data-i18n="prompts.view_all" data-count="{{ personas_count }}">查看全部 {{ personas_count }} 位专家角色 →</a>
  </section>

  <section class="prompts-guide">
    <h2 data-i18n="prompts.guide_title">如何使用 AI Character Prompts</h2>
    <div class="guide-steps">
      <div class="step">
        <span class="step-number">1</span>
        <h3 data-i18n="prompts.step1_title">选择角色</h3>
        <p data-i18n="prompts.step1_desc" data-count="{{ total_count }}">浏览 {{ total_count }} 位历史人物、虚拟角色和专家角色</p>
      </div>
      <div class="step">
        <span class="step-number">2</span>
        <h3 data-i18n="prompts.step2_title">下载 SOUL.md</h3>
        <p data-i18n="prompts.step2_desc">获取包含性格、信念和说话风格的完整角色设定</p>
      </div>
      <div class="step">
        <span class="step-number">3</span>
        <h3 data-i18n="prompts.step3_title">用作系统提示词</h3>
        <p data-i18n="prompts.step3_desc">复制到 ChatGPT、Claude 或任何 AI 助手作为系统指令</p>
      </div>
      <div class="step">
        <span class="step-number">4</span>
        <h3 data-i18n="prompts.step4_title">开始对话</h3>
        <p data-i18n="prompts.step4_desc">以角色身份提问、寻求建议或探讨想法</p>
      </div>
    </div>
  </section>

  <section class="prompts-faq-teaser">
    <h2 data-i18n="prompts.faq_title">常见问题</h2>
    <div class="faq-list">
      <div class="faq-item">
        <h4 data-i18n="prompts.faq1_q">什么是 AI character prompt？</h4>
        <p data-i18n="prompts.faq1_a">详细的性格设定，让 AI 助手能够以特定角色的身份回应，包含其信念、知识和说话风格。</p>
      </div>
      <div class="faq-item">
        <h4 data-i18n="prompts.faq2_q">可以用于商业项目吗？</h4>
        <p data-i18n="prompts.faq2_a">可以，所有 Prompts 采用 MIT 许可证，你可以自由使用、修改和分发。</p>
      </div>
      <div class="faq-item">
        <h4 data-i18n="prompts.faq3_q">如何创建自己的角色 Prompts？</h4>
        <p data-i18n="prompts.faq3_a">学习 SOUL.md 结构，参考 GitHub 仓库里的贡献指南创建新角色。</p>
      </div>
    </div>
    <a href="{{ '/faq/' | relative_url }}" class="view-more" data-i18n="prompts.view_faq">查看全部常见问题 →</a>
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
