// 国际化功能
(function() {
  const STORAGE_KEY = 'souls-language';
  const DEFAULT_LANG = 'zh';
  
  const translations = {
    zh: {
      'site.title': 'Souls',
      'site.slogan': '与历史对话，让思想碰撞；与角色对话，让故事映照当下；与专家对话，让能力不断进化',
      'site.slogan_en': 'Dialogue with history, let minds collide; dialogue with characters, let stories reflect the present; dialogue with experts, let capabilities keep evolving.',
      'stats.total': '共收录 {count} 位人物',
      'stats.real': '{count} 位历史人物',
      'stats.virtual': '{count} 位虚构角色',
      'stats.personas': '{count} 位专家角色',
      'nav.home': '首页',
      'nav.real_world': '真实世界',
      'nav.virtual_world': '非真实世界',
      'nav.personas': '专家角色',
      'nav.browse': '浏览分类',
      'action.copy': '复制内容',
      'action.copy_url': '复制 URL',
      'action.download': '下载',
      'action.edit': '修正',
      'action.copied': '已复制!',
      'action.url_copied': 'URL已复制!',
      'soul.wikipedia': '维基百科',
      'soul.related': '相关灵魂',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': '贡献指南',
      'search.placeholder': '搜索人物...',
      'search.no_results': '未找到匹配的人物',
      'disclaimer.ai_generated': '本内容为 AI 生成，与真实人物无关',
      'disclaimer.ai_generated_en': 'This content is AI-generated and is not affiliated with real persons',
      'disclaimer.historical': '基于公开资料的 AI 模拟',
      'disclaimer.historical_en': 'AI simulation based on public information',
      'disclaimer.home_notice': '本网站所有内容均为 AI 生成，仅供娱乐和学习参考',
      'disclaimer.home_notice_en': 'All content on this site is AI-generated for entertainment and educational purposes',
      'prompts.title': 'AI Character Prompts',
      'prompts.subtitle': '让历史人物成为你的 AI 助手',
      'prompts.description': '下载 300+ 免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。与孔子探讨仁爱，向苏格拉底学习提问，让诸葛亮为你出谋划策。',
      'prompts.stat_real': '200+ 历史人物',
      'prompts.stat_virtual': '4 位虚拟角色',
      'prompts.stat_personas': '47 位专家角色',
      'prompts.popular_title': '热门历史人物 Prompts',
      'prompts.popular_desc': 'AI 助手最常用的角色设定',
      'prompts.philosopher_title': '哲学家 Prompts',
      'prompts.philosopher_desc': '古代智慧用于现代 AI 对话',
      'prompts.military_title': '军事家 Prompts',
      'prompts.military_desc': '商业和生活的战略思维',
      'prompts.virtual_title': '虚拟角色 Prompts',
      'prompts.virtual_desc': '文学和虚构角色用于创意 AI 角色扮演',
      'prompts.expert_title': '专家角色 Prompts',
      'prompts.expert_desc': '工作和学习的专业 AI 助手',
      'prompts.view_all': '查看全部 47 位专家角色 →',
      'prompts.guide_title': '如何使用 AI Character Prompts',
      'prompts.step1_title': '选择角色',
      'prompts.step1_desc': '浏览 300+ 历史人物、虚拟角色和专家角色',
      'prompts.step2_title': '下载 SOUL.md',
      'prompts.step2_desc': '获取包含性格、信念和说话风格的完整角色设定',
      'prompts.step3_title': '用作系统提示词',
      'prompts.step3_desc': '复制到 ChatGPT、Claude 或任何 AI 助手作为系统指令',
      'prompts.step4_title': '开始对话',
      'prompts.step4_desc': '以角色身份提问、寻求建议或探讨想法',
      'prompts.faq_title': '常见问题',
      'prompts.faq1_q': '什么是 AI character prompt？',
      'prompts.faq1_a': '详细的性格设定，让 AI 助手能够以特定角色的身份回应，包含其信念、知识和说话风格。',
      'prompts.faq2_q': '可以用于商业项目吗？',
      'prompts.faq2_a': '可以，所有 Prompts 采用 MIT 许可证，你可以自由使用、修改和分发。',
      'prompts.faq3_q': '如何创建自己的角色 Prompts？',
      'prompts.faq3_a': '学习 SOUL.md 结构，使用我们的 soul-creator 工具生成新角色。',
      'prompts.view_faq': '查看全部常见问题 →',
      'faq.title': '常见问题',
      'faq.subtitle': '关于 AI 角色 Prompts 的一切',
      'faq.cta_title': '还有其他问题？',
      'faq.cta_desc': '访问我们的 GitHub 仓库：',
      'faq.cta_1': '提交 issue 报告 bug 或功能请求',
      'faq.cta_2': '贡献新的角色 Prompts',
      'faq.cta_3': '加入社区讨论',
      'faq.cta_4': '查看完整文档'
    },
    en: {
      'site.title': 'Souls',
      'site.slogan': 'Dialogue with history, let minds collide; dialogue with characters, let stories reflect the present; dialogue with experts, let capabilities keep evolving.',
      'site.slogan_en': '',
      'stats.total': '{count} souls collected',
      'stats.real': '{count} historical figures',
      'stats.virtual': '{count} virtual characters',
      'stats.personas': '{count} expert personas',
      'nav.home': 'Home',
      'nav.real_world': 'Real World',
      'nav.virtual_world': 'Virtual World',
      'nav.personas': 'Personas',
      'nav.browse': 'Browse Categories',
      'action.copy': 'Copy',
      'action.copy_url': 'Copy URL',
      'action.download': 'Download',
      'action.edit': 'Edit',
      'action.copied': 'Copied!',
      'action.url_copied': 'URL Copied!',
      'soul.wikipedia': 'Wikipedia',
      'soul.related': 'Related Souls',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': 'Contribute',
      'search.placeholder': 'Search souls...',
      'search.no_results': 'No matching souls found',
      'disclaimer.ai_generated': '本内容为 AI 生成，与真实人物无关',
      'disclaimer.ai_generated_en': 'This content is AI-generated and is not affiliated with real persons',
      'disclaimer.historical': '基于公开资料的 AI 模拟',
      'disclaimer.historical_en': 'AI simulation based on public information',
      'disclaimer.home_notice': '本网站所有内容均为 AI 生成，仅供娱乐和学习参考',
      'disclaimer.home_notice_en': 'All content on this site is AI-generated for entertainment and educational purposes',
      'prompts.title': 'AI Character Prompts',
      'prompts.subtitle': 'Bring historical figures to life as your AI assistants',
      'prompts.description': 'Download 300+ free AI character prompts for ChatGPT, Claude, and other AI assistants. Discuss benevolence with Confucius, learn questioning from Socrates, let Zhuge Liang advise you.',
      'prompts.stat_real': '200+ Historical Figures',
      'prompts.stat_virtual': '4 Virtual Characters',
      'prompts.stat_personas': '47 Expert Personas',
      'prompts.popular_title': 'Popular Historical Figure Prompts',
      'prompts.popular_desc': 'Most searched character prompts for AI assistants',
      'prompts.philosopher_title': 'Philosopher Prompts',
      'prompts.philosopher_desc': 'Ancient wisdom for modern AI conversations',
      'prompts.military_title': 'Military Strategist Prompts',
      'prompts.military_desc': 'Strategic thinking for business and life',
      'prompts.virtual_title': 'Virtual Character Prompts',
      'prompts.virtual_desc': 'Literary and fictional characters for creative AI roleplay',
      'prompts.expert_title': 'Expert Persona Prompts',
      'prompts.expert_desc': 'Professional AI assistants for work and learning',
      'prompts.view_all': 'View all 47 expert personas →',
      'prompts.guide_title': 'How to Use AI Character Prompts',
      'prompts.step1_title': 'Choose a Character',
      'prompts.step1_desc': 'Browse 300+ historical figures, virtual characters, and expert personas',
      'prompts.step2_title': 'Download SOUL.md',
      'prompts.step2_desc': 'Get the complete character prompt with personality, beliefs, and speaking style',
      'prompts.step3_title': 'Use as System Prompt',
      'prompts.step3_desc': 'Copy to ChatGPT, Claude, or any AI assistant as the system instruction',
      'prompts.step4_title': 'Start Conversing',
      'prompts.step4_desc': 'Ask questions, seek advice, or explore ideas in character',
      'prompts.faq_title': 'Frequently Asked Questions',
      'prompts.faq1_q': 'What is an AI character prompt?',
      'prompts.faq1_a': 'A detailed personality setting that allows AI assistants to respond as a specific character with their beliefs, knowledge, and speaking style.',
      'prompts.faq2_q': 'Can I use these prompts for commercial projects?',
      'prompts.faq2_a': 'Yes, all prompts are MIT licensed. You can use, modify, and distribute them freely.',
      'prompts.faq3_q': 'How do I create my own character prompts?',
      'prompts.faq3_a': 'Study the SOUL.md structure and use our soul-creator tool to generate new characters.',
      'prompts.view_faq': 'View all FAQs →',
      'faq.title': 'Frequently Asked Questions',
      'faq.subtitle': 'Everything you need to know about AI character prompts',
      'faq.cta_title': 'Still have questions?',
      'faq.cta_desc': 'Visit our GitHub repository:',
      'faq.cta_1': 'Submit an issue for bugs or feature requests',
      'faq.cta_2': 'Contribute new character prompts',
      'faq.cta_3': 'Join discussions with the community',
      'faq.cta_4': 'View the complete documentation'
    }
  };
  
  function getLanguage() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    
    // 检测浏览器语言
    const browserLang = navigator.language || navigator.userLanguage;
    if (browserLang && browserLang.startsWith('zh')) {
      return 'zh';
    }
    return 'en';
  }

  function getLocalizedText(element, lang) {
    const zh = element.dataset.localizedZh;
    const en = element.dataset.localizedEn;
    if (lang === 'en') {
      return en || zh || '';
    }
    return zh || en || '';
  }

  function updateLocalizedElements(lang) {
    document.querySelectorAll('[data-localized-zh], [data-localized-en]').forEach(element => {
      const localizedText = getLocalizedText(element, lang);
      if (localizedText) {
        element.textContent = localizedText;
      }
    });
  }

  function updateDocumentTitle(lang) {
    const root = document.documentElement;
    const siteTitle = root.dataset.siteTitle || 'Agent Souls';
    const zhTitle = root.dataset.pageTitleZh || siteTitle;
    const enTitle = root.dataset.pageTitleEn || zhTitle || siteTitle;
    const activeTitle = lang === 'en' ? enTitle : zhTitle;

    if (!activeTitle || activeTitle === siteTitle) {
      document.title = siteTitle;
      return;
    }

    if (activeTitle.includes(siteTitle)) {
      document.title = activeTitle;
      return;
    }

    document.title = `${activeTitle} - ${siteTitle}`;
  }
  
  function setLanguage(lang) {
    if (!translations[lang]) return;
    
    localStorage.setItem(STORAGE_KEY, lang);
    document.documentElement.lang = lang;
    
    // 更新按钮状态
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
    
    // 更新所有带有 data-i18n 的元素
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      let text = translations[lang][key];
      
      if (text) {
        // 替换变量
        text = text.replace(/\{count\}/g, el.dataset.count || '');
        el.textContent = text;
      }
    });
    
    // 更新搜索框 placeholder
    document.querySelectorAll('[data-search-input]').forEach(searchInput => {
      searchInput.placeholder = translations[lang]['search.placeholder'];
    });

    updateLocalizedElements(lang);
    updateDocumentTitle(lang);

    document.dispatchEvent(new CustomEvent('souls:language-changed', {
      detail: { lang }
    }));
  }
  
  // 初始化
  document.addEventListener('DOMContentLoaded', () => {
    setLanguage(getLanguage());
  });
  
  // 暴露到全局
  window.setLanguage = setLanguage;
  window.getLanguage = getLanguage;
  window.translations = translations;
})();
