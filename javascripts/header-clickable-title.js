function makeHeaderTitleClickable() {
  var title = document.querySelector('.md-header__title');
  if (!title) return;

  title.style.cursor = 'pointer';
  title.setAttribute('role', 'link');
  title.setAttribute('aria-label', 'Go to home page');

  if (title.dataset.clickableBound === '1') return;
  title.dataset.clickableBound = '1';

  title.addEventListener('click', function (event) {
    // Ignore clicks on the logo icon/link itself.
    if (event.target && event.target.closest('.md-header__button.md-logo')) return;
    window.location.href = '/';
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', makeHeaderTitleClickable);
} else {
  makeHeaderTitleClickable();
}

// Material for MkDocs instant loading hook.
if (typeof document$ !== 'undefined' && document$.subscribe) {
  document$.subscribe(function () {
    makeHeaderTitleClickable();
  });
}
