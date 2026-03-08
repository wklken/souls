// 分类页卡片搜索
(function() {
  function normalizeForSearch(value) {
    const text = String(value || '');
    const normalized = typeof text.normalize === 'function' ? text.normalize('NFKC') : text;
    return normalized
      .toLowerCase()
      .replace(/\s+/g, ' ')
      .trim();
  }

  function collectSearchParts(card) {
    const parts = [card.textContent || '', card.getAttribute('href') || ''];
    card.querySelectorAll('[data-localized-zh], [data-localized-en]').forEach(element => {
      parts.push(element.dataset.localizedZh || '');
      parts.push(element.dataset.localizedEn || '');
    });
    return parts;
  }

  function buildSearchText(card) {
    return collectSearchParts(card)
      .map(normalizeForSearch)
      .filter(Boolean)
      .join(' ');
  }

  document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('category-search-input');
    const soulGrid = document.getElementById('soul-grid');

    if (!searchInput || !soulGrid) return;

    const cards = Array.from(soulGrid.querySelectorAll('.soul-card'));
    if (cards.length === 0) return;

    const emptyState = document.getElementById('category-search-empty');
    const searchCache = new Map();

    function rebuildSearchCache() {
      cards.forEach(card => {
        searchCache.set(card, buildSearchText(card));
      });
    }

    function filterCards() {
      const query = normalizeForSearch(searchInput.value);
      let visibleCount = 0;

      cards.forEach(card => {
        const searchableText = searchCache.get(card) || '';
        const matches = !query || searchableText.includes(query);
        card.hidden = !matches;
        if (matches) visibleCount += 1;
      });

      if (emptyState) {
        emptyState.hidden = !query || visibleCount > 0;
      }
    }

    rebuildSearchCache();
    filterCards();

    searchInput.addEventListener('input', filterCards);
    searchInput.addEventListener('search', filterCards);
    searchInput.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        searchInput.value = '';
        filterCards();
      }
    });

    document.addEventListener('souls:language-changed', () => {
      rebuildSearchCache();
      filterCards();
    });
  });
})();
