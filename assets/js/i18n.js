// 国际化功能
(function() {
  const STORAGE_KEY = 'souls-language';
  const DEFAULT_LANG = 'zh';
  
  const translations = {
    zh: {
      'site.title': 'Souls',
      'site.slogan': '与历史对话，让思想碰撞',
      'site.slogan_en': 'Dialogue with history, collide with minds',
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
      'action.download': '下载',
      'action.edit': '修正',
      'action.copied': '已复制!',
      'soul.wikipedia': '维基百科',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': '贡献指南',
      'search.placeholder': '搜索人物...',
      'search.no_results': '未找到匹配的人物'
    },
    en: {
      'site.title': 'Souls',
      'site.slogan': 'Dialogue with history, collide with minds',
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
      'action.download': 'Download',
      'action.edit': 'Edit',
      'action.copied': 'Copied!',
      'soul.wikipedia': 'Wikipedia',
      'footer.copyright': '© 2026 Souls Project',
      'footer.contribute': 'Contribute',
      'search.placeholder': 'Search souls...',
      'search.no_results': 'No matching souls found'
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
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.placeholder = translations[lang]['search.placeholder'];
    }
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
