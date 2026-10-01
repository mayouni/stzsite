/* stzsite -- the theme buttons, the language of the home page, and the
   scroll rows of a narrow screen. No network, no framework, works from file://.
   Nothing here animates (Zui Rule 112): every change is instant. */
(function () {
  var root = document.documentElement;
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  /* the theme: three buttons in the footer, each saying what it does (Rule 106) */
  function paintTheme() {
    var cur = root.getAttribute('data-theme') || 'auto';
    var bs = document.querySelectorAll('[data-set-theme]');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-set-theme') === cur ? 'true' : 'false');
  }
  var tb = document.querySelectorAll('[data-set-theme]');
  for (var i = 0; i < tb.length; i++) {
    tb[i].addEventListener('click', function () {
      var t = this.getAttribute('data-set-theme');
      if (t === 'auto') { root.removeAttribute('data-theme'); store('stz-theme', ''); }
      else { root.setAttribute('data-theme', t); store('stz-theme', t); }
      paintTheme();
    });
  }
  paintTheme();

  /* the home page carries both languages; the header's language link chooses */
  function setLang(l) { root.setAttribute('data-lang', l); root.setAttribute('lang', l); }
  if (root.classList.contains('home')) {
    var q = new URLSearchParams(location.search);
    var lang = q.get('lang');
    if (lang === 'fr' || lang === 'en') store('stz-lang', lang); else lang = read('stz-lang');
    if (lang !== 'fr' && lang !== 'en') {
      var nl = (navigator.language || 'fr').toLowerCase();
      lang = nl.indexOf('fr') === 0 ? 'fr' : 'en';
    }
    setLang(lang);
  } else {
    var pl = root.getAttribute('lang');
    if (pl === 'fr' || pl === 'en') store('stz-lang', pl);
  }

  /* on a narrow screen the menu and the path are scrollable rows: open them on
     the current entry, instantly, so the reader sees where they are */
  var cur = document.querySelectorAll('.nav a[aria-current], .path a[aria-current]');
  for (var j = 0; j < cur.length; j++) {
    var row = cur[j].parentNode;
    if (row.scrollWidth > row.clientWidth) row.scrollLeft = (cur[j].offsetLeft - row.offsetLeft) - (row.clientWidth - cur[j].offsetWidth) / 2;
  }
  /* the height of the pinned menus, so a table's header row can stick just below them */
  function pin() {
    var tops = document.querySelectorAll('header.top'), h = 0;
    for (var k = 0; k < tops.length; k++) if (tops[k].getClientRects().length) h = tops[k].getBoundingClientRect().height;
    root.style.setProperty('--pin', Math.round(h) + 'px');
  }
  pin(); window.addEventListener('resize', pin);
})();
