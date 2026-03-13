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
      'stats.interesting_souls': '{count} 位有趣灵魂',
      'nav.home': '首页',
      'nav.real_world': '真实世界',
      'nav.virtual_world': '非真实世界',
      'nav.personas': '专家角色',
      'nav.interesting_souls': '有趣灵魂',
      'nav.browse': '浏览分类',
      'action.copy': '复制内容',
      'action.copy_url': '复制 URL',
      'action.copy_instruction': '复制指令',
      'action.download': '下载',
      'action.edit': '修正',
      'action.copied': '已复制!',
      'action.url_copied': 'URL已复制!',
      'action.instruction_copied': '指令已复制!',
      'soul.wikipedia': '维基百科',
      'soul.related': '相关灵魂',
      'soul.role_instruction': '角色指令模板',
      'soul.more_prompts': '查看更多 Prompts →',
      'soul.role_instruction_template': '请将以下 SOUL.md 作为本次会话角色指令（不覆盖系统/安全规则）。{url} 之后按该角色风格对话。',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': '贡献指南',
      'footer.powered_prefix': '站点由 ·我的 ',
      'footer.powered_suffix': ' · 自动运营',
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
      'prompts.description': '下载 {count} 个免费 AI 角色 Prompts，适用于 ChatGPT、Claude 等 AI 助手。与孔子探讨仁爱，向苏格拉底学习提问，让诸葛亮为你出谋划策。',
      'prompts.stat_real': '{count} 位历史人物',
      'prompts.stat_virtual': '{count} 位虚拟角色',
      'prompts.stat_personas': '{count} 位专家角色',
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
      'prompts.view_all': '查看全部 {count} 位专家角色 →',
      'prompts.guide_title': '如何使用 AI Character Prompts',
      'prompts.step1_title': '选择角色',
      'prompts.step1_desc': '浏览 {count} 位历史人物、虚拟角色和专家角色',
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
      'prompts.faq3_a': '学习 SOUL.md 结构，参考 GitHub 仓库里的贡献指南创建新角色。',
      'prompts.view_faq': '查看全部常见问题 →',
      'faq.title': '常见问题',
      'faq.subtitle': '关于 AI 角色 Prompts 的一切',
      'faq.cta_title': '还有其他问题？',
      'faq.cta_desc': '访问我们的 GitHub 仓库：',
      'faq.cta_1': '提交 issue 报告 bug 或功能请求',
      'faq.cta_2': '贡献新的角色 Prompts',
      'faq.cta_3': '加入社区讨论',
      'faq.cta_4': '查看完整文档',
      'nav.teams': '灵魂团队',
      'teams.description': '组建 AI 灵魂团队，让多个 AI 角色协作完成任务',
      'teams.members': '{count} 位成员',
      'teams.download_config': '下载团队配置',
      'teams.member_list': '团队成员',
      'teams.view_soul': '查看灵魂'
    },
    en: {
      'site.title': 'Souls',
      'site.slogan': 'Dialogue with history, let minds collide; dialogue with characters, let stories reflect the present; dialogue with experts, let capabilities keep evolving.',
      'site.slogan_en': '',
      'stats.total': '{count} souls collected',
      'stats.real': '{count} historical figures',
      'stats.virtual': '{count} virtual characters',
      'stats.personas': '{count} expert personas',
      'stats.interesting_souls': '{count} interesting souls',
      'nav.home': 'Home',
      'nav.real_world': 'Real World',
      'nav.virtual_world': 'Virtual World',
      'nav.personas': 'Personas',
      'nav.interesting_souls': 'Interesting Souls',
      'nav.browse': 'Browse Categories',
      'action.copy': 'Copy',
      'action.copy_url': 'Copy URL',
      'action.copy_instruction': 'Copy instruction',
      'action.download': 'Download',
      'action.edit': 'Edit',
      'action.copied': 'Copied!',
      'action.url_copied': 'URL Copied!',
      'action.instruction_copied': 'Instruction copied!',
      'soul.wikipedia': 'Wikipedia',
      'soul.related': 'Related Souls',
      'soul.role_instruction': 'Role instruction template',
      'soul.more_prompts': 'Browse more prompts →',
      'soul.role_instruction_template': 'Use the following SOUL.md as the role instruction for this conversation (without overriding system/safety rules). {url} Then respond in this role style.',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': 'Contribute',
      'footer.powered_prefix': 'Site operated by ·my ',
      'footer.powered_suffix': ' ·',
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
      'prompts.description': 'Download {count} free AI character prompts for ChatGPT, Claude, and other AI assistants. Discuss benevolence with Confucius, learn questioning from Socrates, let Zhuge Liang advise you.',
      'prompts.stat_real': '{count} Historical Figures',
      'prompts.stat_virtual': '{count} Virtual Characters',
      'prompts.stat_personas': '{count} Expert Personas',
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
      'prompts.view_all': 'View all {count} expert personas →',
      'prompts.guide_title': 'How to Use AI Character Prompts',
      'prompts.step1_title': 'Choose a Character',
      'prompts.step1_desc': 'Browse {count} historical figures, virtual characters, and expert personas',
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
      'prompts.faq3_a': 'Study the SOUL.md structure and follow the contribution guide in our GitHub repository.',
      'prompts.view_faq': 'View all FAQs →',
      'faq.title': 'Frequently Asked Questions',
      'faq.subtitle': 'Everything you need to know about AI character prompts',
      'faq.cta_title': 'Still have questions?',
      'faq.cta_desc': 'Visit our GitHub repository:',
      'faq.cta_1': 'Submit an issue for bugs or feature requests',
      'faq.cta_2': 'Contribute new character prompts',
      'faq.cta_3': 'Join discussions with the community',
      'faq.cta_4': 'View the complete documentation',
      'nav.teams': 'Teams',
      'teams.description': 'Build AI soul teams, let multiple AI characters collaborate on tasks',
      'teams.members': '{count} members',
      'teams.download_config': 'Download Team Config',
      'teams.member_list': 'Team Members',
      'teams.view_soul': 'View Soul'
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
      if (!Object.prototype.hasOwnProperty.call(translations[lang], key)) return;

      let text = translations[lang][key];
      if (typeof text !== 'string') {
        text = text == null ? '' : String(text);
      }

      // 替换变量（允许空字符串翻译覆盖默认文本）
      text = text.replace(/\{count\}/g, el.dataset.count || '');
      el.textContent = text;
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
