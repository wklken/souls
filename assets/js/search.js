// 搜索功能
(function() {
  let soulsData = [];
  let latestQuery = '';
  const baseUrl = document.documentElement.dataset.baseurl || '';
  const normalizedBaseUrl = baseUrl && baseUrl !== '/' ? baseUrl.replace(/\/$/, '') : '';
  const searchDataUrl = document.querySelector('meta[name="souls-search-url"]')?.content
    || `${normalizedBaseUrl}/search.json`;

  function getCurrentLanguage() {
    if (window.getLanguage) {
      return window.getLanguage();
    }
    return document.documentElement.lang || 'zh';
  }

  function escapeHtml(value) {
    return String(value || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function toArray(value) {
    if (Array.isArray(value)) return value;
    if (typeof value === 'string' && value.trim()) return [value.trim()];
    return [];
  }

  function getLocalizedName(soul, lang) {
    if (lang === 'en') {
      return soul.name_en || soul.name_zh || soul.name || '';
    }
    return soul.name_zh || soul.name || soul.name_en || '';
  }

  function getSecondaryName(soul, lang) {
    const primary = getLocalizedName(soul, lang);
    const secondary = lang === 'en'
      ? (soul.name_zh || soul.name || '')
      : (soul.name_en || '');
    if (!secondary || secondary === primary) return '';
    return secondary;
  }

  function getLocalizedCategory(soul, lang) {
    if (lang === 'en') {
      return soul.category_en || soul.category_zh || soul.category || '';
    }
    return soul.category_zh || soul.category || soul.category_en || '';
  }

  function getLocalizedTags(soul, lang) {
    if (lang === 'en') {
      return toArray(soul.tags_en).length > 0 ? toArray(soul.tags_en) : toArray(soul.tags);
    }
    return toArray(soul.tags_zh).length > 0 ? toArray(soul.tags_zh) : toArray(soul.tags);
  }

  function getSearchableFields(soul) {
    return [
      soul.name,
      soul.name_zh,
      soul.name_en,
      soul.category,
      soul.category_zh,
      soul.category_en,
      ...toArray(soul.tags),
      ...toArray(soul.tags_zh),
      ...toArray(soul.tags_en)
    ]
      .filter(Boolean)
      .map(value => String(value).toLowerCase());
  }
  
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
      const fields = getSearchableFields(soul);
      return fields.some(field => field.includes(lowerQuery));
    }).slice(0, 10); // 最多显示10个结果
  }
  
  // 渲染搜索结果
  function renderResults(results, container) {
    const lang = getCurrentLanguage();

    if (results.length === 0) {
      const noResultsText = window.translations?.[lang]?.['search.no_results']
        || 'No matching souls found';
      container.innerHTML = `<div class="no-results">${escapeHtml(noResultsText)}</div>`;
      return;
    }

    container.innerHTML = results.map(soul => {
      const primaryName = getLocalizedName(soul, lang);
      const secondaryName = getSecondaryName(soul, lang);
      const category = getLocalizedCategory(soul, lang);
      const tags = getLocalizedTags(soul, lang);

      return `
      <div class="search-result-item" onclick="window.location.href='${soul.url}'">
        <div class="result-name">
          ${escapeHtml(primaryName)}
          ${secondaryName ? ` / ${escapeHtml(secondaryName)}` : ''}
        </div>
        <div class="result-category">
          ${escapeHtml(category)}
          ${tags.length ? ` · ${escapeHtml(tags.join(', '))}` : ''}
        </div>
      </div>
    `;
    }).join('');
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
        latestQuery = query;
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

    document.addEventListener('souls:language-changed', () => {
      if (!latestQuery || latestQuery.length === 0) return;
      const results = search(latestQuery);
      renderResults(results, searchResults);
      if (results.length > 0) {
        searchResults.classList.add('active');
      }
    });
  });
})();
