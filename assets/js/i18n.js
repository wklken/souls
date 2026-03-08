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
      'disclaimer.home_notice_en': 'All content on this site is AI-generated for entertainment and educational purposes'
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
      'disclaimer.home_notice_en': 'All content on this site is AI-generated for entertainment and educational purposes'
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
    const siteTitle = root.dataset.siteTitle || 'Souls';
    const zhTitle = root.dataset.pageTitleZh || siteTitle;
    const enTitle = root.dataset.pageTitleEn || zhTitle || siteTitle;
    const activeTitle = lang === 'en' ? enTitle : zhTitle;

    if (!activeTitle || activeTitle === siteTitle) {
      document.title = siteTitle;
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
