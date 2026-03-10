---
layout: default
title: "FAQ - AI Character Prompts Guide"
title_zh: "常见问题 - AI角色Prompt使用指南"
title_en: "FAQ - AI Character Prompts Guide"
description: "Learn what AI character prompts are, how to use them with ChatGPT and Claude, and how to create your own character prompts."
description_zh: "了解什么是 AI 角色 Prompts，如何在 ChatGPT 和 Claude 中使用，以及如何创建自己的角色 Prompts。"
description_en: "Learn what AI character prompts are, how to use them with ChatGPT and Claude, and how to create your own character prompts."
keywords: "AI character prompts FAQ, how to use character prompts, ChatGPT prompts guide, Claude prompts tutorial, SOUL.md guide"
permalink: /faq/
faq:
  - question: "What is an AI character prompt?"
    answer: "An AI character prompt (also called AI soul prompt) is a detailed personality setting that allows AI assistants like ChatGPT and Claude to respond as a specific character. It includes the character's core beliefs, speaking style, knowledge areas, and personality traits, enabling the AI to simulate meaningful conversations in character."
  
  - question: "How do I use character prompts in ChatGPT?"
    answer: "To use a character prompt in ChatGPT: 1) Download the SOUL.md file from our site, 2) Copy the entire content, 3) Start a new ChatGPT conversation, 4) Paste the content as your first message or use it as a custom instruction in settings, 5) Start conversing with the character. The AI will now respond in the character's voice and personality."
  
  - question: "How do I use character prompts in Claude?"
    answer: "For Claude: 1) Download the SOUL.md file, 2) Copy the complete character description, 3) Start a new conversation with Claude, 4) Paste the SOUL.md content as the first message to establish the character context, 5) Begin your conversation. Claude will maintain the character's persona throughout your chat."
  
  - question: "Can I use these prompts for commercial projects?"
    answer: "Yes! All character prompts on Agent Souls are released under the MIT License. This means you can use, modify, distribute, and even sell them commercially. We only ask that you include the original license and copyright notice."
  
  - question: "How do I create my own character prompts?"
    answer: "To create your own character: 1) Study our SOUL.md structure which includes Core Identity, Core Wisdom, Soul Portrait, Beliefs, Personality, and Speaking Style, 2) Research your character thoroughly, 3) Write in first person to capture their voice, 4) Include specific quotes and phrases they would use, 5) Use our soul-creator tool or follow the template in our GitHub repository."
  
  - question: "What's the difference between historical and virtual character prompts?"
    answer: "Historical character prompts are based on real historical figures like Confucius, Socrates, or Einstein, grounded in their actual writings, speeches, and documented beliefs. Virtual character prompts are based on fictional characters like Sherlock Holmes or Hamlet, drawing from literary works and established character traits. Both types help you explore different perspectives and modes of thinking."
  
  - question: "What are expert persona prompts?"
    answer: "Expert persona prompts are AI character settings designed for professional contexts. They include roles like Product Director, CTO, Investment Analyst, and UX Researcher. These prompts help you get expert-level advice, review your work from a professional perspective, or simulate stakeholder conversations for better decision-making."
  
  - question: "Can I combine multiple character prompts?"
    answer: "While you typically use one character at a time for clear persona consistency, you can create interesting scenarios by switching between characters or asking them to debate topics. Some advanced users also blend aspects of different characters to create unique composite personas for specific use cases."
  
  - question: "How accurate are these character representations?"
    answer: "Our character prompts are AI-generated based on extensive research of historical records, literary works, and established biographies. While we strive for accuracy, they are creative interpretations rather than perfect historical replicas. Think of them as 'inspired by' rather than 'exact replicas of' the original figures. Always verify important historical facts independently."
  
  - question: "Do the prompts work with other AI assistants besides ChatGPT and Claude?"
    answer: "Yes! Our SOUL.md format works with any AI assistant that supports system prompts or context settings, including Gemini, Llama, and custom AI implementations. The key is providing enough context about the character's personality and voice for the AI to simulate effectively."
  
  - question: "How can I contribute a new character?"
    answer: "We welcome contributions! To add a new character: 1) Fork our GitHub repository, 2) Create a new folder in the appropriate category (real_world, virtual_world, or personas), 3) Follow our SOUL.md template structure, 4) Include both Chinese and English versions if possible, 5) Submit a pull request. See our CONTRIBUTING.md for detailed guidelines."
  
  - question: "What's the best way to search for specific character types?"
    answer: "Use our search function to find characters by name, era, field of expertise, or tags. You can also browse by category: Real World for historical figures, Virtual World for fictional characters, and Personas for professional roles. Each character page includes related suggestions based on shared tags and categories."
---

<div class="faq-page">
  <header class="faq-header">
    <h1>Frequently Asked Questions</h1>
    <p class="faq-subtitle">Everything you need to know about AI character prompts</p>
  </header>

  <div class="faq-content">
    {% for item in page.faq %}
    <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
      <h3 class="faq-question" itemprop="name">{{ item.question }}</h3>
      <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <div itemprop="text">{{ item.answer }}</div>
      </div>
    </div>
    {% endfor %}
  </div>

  <section class="faq-cta">
    <h2>Still have questions?</h2>
    <p>Visit our <a href="https://github.com/wklken/souls">GitHub repository</a> to:</p>
    <ul>
      <li>Submit an issue for bugs or feature requests</li>
      <li>Contribute new character prompts</li>
      <li>Join discussions with the community</li>
      <li>View the complete documentation</li>
    </ul>
  </section>
</div>

<style>
.faq-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.faq-header {
  text-align: center;
  margin-bottom: 3rem;
}

.faq-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.faq-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary);
}

.faq-content {
  margin-bottom: 3rem;
}

.faq-item {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid var(--border-color);
}

.faq-item:last-child {
  border-bottom: none;
}

.faq-question {
  font-size: 1.25rem;
  color: var(--primary);
  margin-bottom: 0.75rem;
  cursor: pointer;
}

.faq-answer {
  line-height: 1.7;
  color: var(--text-secondary);
}

.faq-answer ol,
.faq-answer ul {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.faq-answer li {
  margin: 0.25rem 0;
}

.faq-cta {
  background: var(--bg-secondary);
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
}

.faq-cta h2 {
  margin-bottom: 1rem;
}

.faq-cta ul {
  text-align: left;
  display: inline-block;
  margin: 1rem 0;
}

.faq-cta li {
  margin: 0.5rem 0;
}
</style>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {% for item in page.faq %}
    {
      "@type": "Question",
      "name": {{ item.question | jsonify }},
      "acceptedAnswer": {
        "@type": "Answer",
        "text": {{ item.answer | jsonify }}
      }
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>
