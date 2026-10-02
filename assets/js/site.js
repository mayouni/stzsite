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
  /* the second submenu: a column on a wide screen, a row on a narrow one; open it on this page's entry */
  var l2 = document.querySelector('.level2'), l2cur = l2 && l2.querySelector('a[aria-current]');
  if (l2cur) {
    var a = l2cur.getBoundingClientRect(), b = l2.getBoundingClientRect();
    if (l2.scrollHeight > l2.clientHeight) l2.scrollTop += (a.top - b.top) - (l2.clientHeight - a.height) / 2;
    if (l2.scrollWidth > l2.clientWidth) l2.scrollLeft += (a.left - b.left) - (l2.clientWidth - a.width) / 2;
  }
  /* the height of the pinned menus, so a table's header row can stick just below them */
  function pin() {
    var tops = document.querySelectorAll('header.top'), h = 0;
    for (var k = 0; k < tops.length; k++) if (tops[k].getClientRects().length) h = tops[k].getBoundingClientRect().height;
    root.style.setProperty('--pin', Math.round(h) + 'px');
  }
  pin(); window.addEventListener('resize', pin);
  /* the home page: the photograph starts at the top of the browser, under the menu;
     the menu floats over it as text until the reader has scrolled past it */
  var body = document.body, hero = document.querySelector('.home-body .hero'), img = document.querySelector('.home-body .hero-img');
  if (hero && img) {
    var shown = function (sel) { var out = []; var es = document.querySelectorAll(sel); for (var k = 0; k < es.length; k++) if (es[k].getClientRects().length) out.push(es[k]); return out; };
    var state = function () {
      var t = shown('header.top')[0]; if (!t) return;
      body.classList.toggle('over-hero', img.getBoundingClientRect().bottom > t.getBoundingClientRect().bottom + 8);
    };
    var place = function () {
      var h = 0, es = shown('.brandrow, header.top');
      for (var k = 0; k < es.length; k++) h += es[k].getBoundingClientRect().height;
      hero.style.marginTop = (-Math.round(h)) + 'px';
      state();
    };
    place();
    window.addEventListener('resize', place);
    window.addEventListener('load', place);
    window.addEventListener('scroll', state, { passive: true });
  }
})();
