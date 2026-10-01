/* stzsite -- theme toggle, mobile nav, language pick on the onboarding page.
   No network, no framework. Works from file://. */
(function () {
  var root = document.documentElement;
  function store(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  /* theme: auto -> dark -> light -> auto */
  var btn = document.querySelector('[data-theme-toggle]');
  if (btn) {
    btn.addEventListener('click', function () {
      var cur = root.getAttribute('data-theme') || 'auto';
      var next = cur === 'auto' ? 'dark' : cur === 'dark' ? 'light' : 'auto';
      if (next === 'auto') { root.removeAttribute('data-theme'); store('stz-theme', ''); }
      else { root.setAttribute('data-theme', next); store('stz-theme', next); }
    });
  }

  /* mobile navigation */
  var tog = document.querySelector('.nav-toggle'), nav = document.getElementById('site-nav');
  if (tog && nav) {
    tog.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      tog.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* the onboarding page carries both languages; pick one */
  if (root.classList.contains('home')) {
    var q = new URLSearchParams(location.search);
    var lang = q.get('lang') || read('stz-lang');
    if (!lang) {
      var nl = (navigator.language || navigator.userLanguage || 'fr').toLowerCase();
      lang = nl.indexOf('fr') === 0 ? 'fr' : 'en';
    }
    setLang(lang);
    if (q.get('panel') === 'right') root.classList.add('panel-right');
    var bs = document.querySelectorAll('.hero-lang button');
    for (var i = 0; i < bs.length; i++) {
      bs[i].addEventListener('click', function () { setLang(this.getAttribute('data-set-lang')); store('stz-lang', this.getAttribute('data-set-lang')); });
    }
  }
  function setLang(l) {
    root.setAttribute('data-lang', l); root.setAttribute('lang', l);
    var bs = document.querySelectorAll('.hero-lang button');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-set-lang') === l ? 'true' : 'false');
  }
  /* remember the language of any inner page the visitor reads */
  var pl = root.getAttribute('lang');
  if (!root.classList.contains('home') && (pl === 'fr' || pl === 'en')) store('stz-lang', pl);
})();
