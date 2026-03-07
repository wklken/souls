// 主题切换功能
(function() {
  const STORAGE_KEY = 'souls-theme';
  const DEFAULT_THEME = document.documentElement.getAttribute('data-theme') || 'light';
  
  function getTheme() {
    return localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME;
  }
  
  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
  }
  
  function toggleTheme() {
    const currentTheme = getTheme();
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
  }
  
  // 初始化
  setTheme(getTheme());
  
  // 暴露到全局
  window.toggleTheme = toggleTheme;
})();
