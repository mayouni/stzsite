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
  pin(); window.__stzPin = pin; window.addEventListener('resize', pin);
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

/* level 2 is the bar fixed under the menu, level 3 the bar on the left (the author's four levels, 2026-10-16). On a screen
   narrower than the left bar and the page together, the left bar folds into one line under the menu that opens on request;
   on a phone the level-2 bar folds into the same line. Without this script nothing is lost: both stand above the page */
(function () {
  if (!window.matchMedia) return;
  var wide = window.matchMedia('(max-width:1100px)'), narrow = window.matchMedia('(max-width:760px)');
  var top = document.querySelector('header.top'); if (!top) return;
  var path0 = top.querySelector('nav.path'), rail0 = document.querySelector('nav.level2.rail');
  if (!path0 && !rail0) return;
  /* where each bar stood, so that a window widened after load gets its bars back (a fold decided at load only stayed folded) */
  var home = [path0, rail0].map(function (n) { return n ? [n, n.parentNode, n.nextSibling] : null; });
  var d = null;
  function unfold() {
    if (!d) return;
    home.forEach(function (h) { if (h) h[1].insertBefore(h[0], h[2]); });
    d.parentNode.removeChild(d); d = null;
  }
  function fold() {
    unfold();
    if (!wide.matches) { if (window.__stzPin) window.__stzPin(); return; }
    var path = narrow.matches ? path0 : null, rail = rail0;
    if (!path && !rail) { if (window.__stzPin) window.__stzPin(); return; }
    var fr = (document.documentElement.lang || '').indexOf('fr') === 0;
    var cur = (rail && (rail.querySelector('a[aria-current=page]') || rail.querySelector('a[aria-current=location]'))) ||
              (path && (path.querySelector('a[aria-current=page]') || path.querySelector('a[aria-current=location]')));
    var sec = document.querySelector('nav.nav a[aria-current]');
    var here = [sec ? sec.textContent.trim() : '', cur ? cur.textContent.replace(/\s+/g, ' ').trim() : ''].filter(function (x, k, a) { return x && a.indexOf(x) === k; }).join(' › ');
    d = document.createElement('details'); d.className = 'where';
    var s = document.createElement('summary');
    s.textContent = (fr ? 'Où vous êtes : ' : 'Where you are: ') + here;
    d.appendChild(s); if (path) d.appendChild(path); if (rail) d.appendChild(rail);
    top.parentNode.insertBefore(d, top.nextSibling);
    if (window.__stzPin) window.__stzPin();
  }
  fold();
  [wide, narrow].forEach(function (m) { if (m.addEventListener) m.addEventListener('change', fold); else if (m.addListener) m.addListener(fold); });
})();
