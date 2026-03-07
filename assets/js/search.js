// 搜索功能
(function() {
  let soulsData = [];
  const searchDataUrl = document.querySelector('meta[name="souls-search-url"]')?.content || '/search.json';
  
  // 加载搜索数据
  async function loadSearchData() {
    try {
      const response = await fetch(searchDataUrl);
      soulsData = await response.json();
    } catch (e) {
      console.error('Failed to load search data:', e);
    }
  }
  
  // 搜索函数
  function search(query) {
    if (!query || query.length < 1) return [];
    
    const lowerQuery = query.toLowerCase();
    return soulsData.filter(soul => {
      const nameMatch = soul.name.toLowerCase().includes(lowerQuery);
      const nameEnMatch = soul.name_en && soul.name_en.toLowerCase().includes(lowerQuery);
      const tagsMatch = soul.tags && soul.tags.some(tag => tag.toLowerCase().includes(lowerQuery));
      return nameMatch || nameEnMatch || tagsMatch;
    }).slice(0, 10); // 最多显示10个结果
  }
  
  // 渲染搜索结果
  function renderResults(results, container) {
    if (results.length === 0) {
      container.innerHTML = '<div class="no-results">未找到匹配的人物</div>';
      return;
    }
    
    const lang = window.getLanguage ? window.getLanguage() : 'zh';
    
    container.innerHTML = results.map(soul => `
      <div class="search-result-item" onclick="window.location.href='${soul.url}'">
        <div class="result-name">${soul.name}${soul.name_en ? ` / ${soul.name_en}` : ''}</div>
        <div class="result-category">${soul.category}</div>
      </div>
    `).join('');
  }
  
  // 初始化
  document.addEventListener('DOMContentLoaded', () => {
    loadSearchData();
    
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;
    
    let debounceTimer;
    
    searchInput.addEventListener('input', (e) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        const query = e.target.value.trim();
        if (query.length === 0) {
          searchResults.classList.remove('active');
          return;
        }
        
        const results = search(query);
        renderResults(results, searchResults);
        searchResults.classList.add('active');
      }, 200);
    });
    
    // 点击外部关闭搜索结果
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-container')) {
        searchResults.classList.remove('active');
      }
    });
    
    // 键盘导航
    let selectedIndex = -1;
    
    searchInput.addEventListener('keydown', (e) => {
      const items = searchResults.querySelectorAll('.search-result-item');
      
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
        updateSelection(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = Math.max(selectedIndex - 1, -1);
        updateSelection(items);
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (selectedIndex >= 0 && items[selectedIndex]) {
          items[selectedIndex].click();
        } else if (items.length > 0) {
          items[0].click();
        }
      }
    });
    
    function updateSelection(items) {
      items.forEach((item, index) => {
        item.style.backgroundColor = index === selectedIndex ? 'var(--bg-secondary)' : '';
      });
    }
  });
})();
