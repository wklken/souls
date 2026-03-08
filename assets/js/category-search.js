// 分类页卡片搜索
(function() {
  function buildSearchText(card) {
    const localizedText = Array.from(
      card.querySelectorAll('[data-localized-zh], [data-localized-en]')
    )
      .map(element => `${element.dataset.localizedZh || ''} ${element.dataset.localizedEn || ''}`)
      .join(' ');

    return `${card.textContent || ''} ${localizedText}`.toLowerCase();
  }

  document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('category-search-input');
    const soulGrid = document.getElementById('soul-grid');

    if (!searchInput || !soulGrid) return;

    const cards = Array.from(soulGrid.querySelectorAll('.soul-card'));
    const emptyState = document.getElementById('category-search-empty');
    const searchCache = new Map(cards.map(card => [card, buildSearchText(card)]));

    function filterCards() {
      const query = searchInput.value.trim().toLowerCase();
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

    searchInput.addEventListener('input', filterCards);
    searchInput.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        searchInput.value = '';
        filterCards();
      }
    });

    document.addEventListener('souls:language-changed', () => {
      cards.forEach(card => {
        searchCache.set(card, buildSearchText(card));
      });
      filterCards();
    });
  });
})();
