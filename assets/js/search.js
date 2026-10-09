/* The search of the site: one field, everywhere under the menu, structured as category > class > method.

   - a magnifier in the header (and the keys / and Ctrl+K) opens it over any page;
   - the filter field of the reference (id flt) gets the same results under it, and keeps filtering its own page;
   - the names are loaded when the field gets the focus (about 120 KB compressed); the descriptions and the examples only when
     the reader asks (about 330 KB), and the choice is remembered, so a reader on a metered connection decides once.
   The matching is search-core.js, measured by tools/search_check.mjs. No animation, no hover-only control, every row 44 px tall. */
(function () {
  'use strict';
  var me = document.currentScript, here = me ? me.src : '';
  var ROOT = here ? new URL('../../', here).href : '';
  var LANG = (document.documentElement.lang || 'en').slice(0, 2) === 'fr' ? 'fr' : 'en';
  var T = {
    en: { open: 'Search', ph: 'Search classes, methods, descriptions, code…', loading: 'Loading the index…', none: 'Nothing found.', areas: 'Areas', classes: 'Classes', methods: 'Methods',
          pages: 'Guides, how-to, narrations, book, education', more: 'Show more', in: 'in', example: 'example', also: 'also written', via: 'written', moreIn: 'more in',
          texts: 'Search the descriptions and the examples too', textsHow: 'about 330 KB, loaded once', textsOn: 'Looking in the descriptions and the examples too', close: 'Close',
          count: '{n} methods in {a} areas', qual: 'Looking inside', hint: 'Try a method (Find), a class (stzList), a sentence (sort a hash list), a piece of code (banana split)',
          kind: { guide: 'Guide', howto: 'How-to', narration: 'Narration', book: 'Book', education: 'Education', page: 'Page' }, ext: 'opens on GitHub' },
    fr: { open: 'Chercher', ph: 'Chercher une classe, une méthode, une description, du code…', loading: "Chargement de l'index…", none: 'Rien trouvé.', areas: 'Domaines', classes: 'Classes', methods: 'Méthodes',
          pages: 'Guides, comment faire, narrations, livre, éducation', more: 'Voir plus', in: 'dans', example: 'exemple', also: 'aussi écrite', via: 'écrite', moreIn: 'de plus dans',
          texts: 'Chercher aussi dans les descriptions et les exemples', textsHow: 'environ 330 Ko, chargés une fois', textsOn: 'Recherche aussi dans les descriptions et les exemples', close: 'Fermer',
          count: '{n} méthodes dans {a} domaines', qual: 'Dans', hint: 'Essayez une méthode (Find), une classe (stzList), une phrase (trier une liste de hachage), du code (banana split)',
          kind: { guide: 'Guide', howto: 'Comment faire', narration: 'Narration', book: 'Livre', education: 'Éducation', page: 'Page' }, ext: 'ouvre GitHub' }
  }[LANG];
  var state = { idx: null, names: null, texts: null, loading: null, wantTexts: false };
  try { state.wantTexts = localStorage.getItem('stz-search-text') === '1'; } catch (e) {}

  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function marked(parent, text, toks) {                     // a text with the matching pieces in <mark>: bold, accent, underlined
    StzSearchCore.segments(text, toks).forEach(function (s) { parent.appendChild(s[1] ? el('mark', 'sm', s[0]) : document.createTextNode(s[0])); });
  }
  function loadScript(src) {
    return new Promise(function (ok, fail) { var s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = fail; document.head.appendChild(s); });
  }
  function ensureNames() {
    if (state.idx) return Promise.resolve();
    if (!state.loading) state.loading = loadScript(ROOT + 'assets/search/names.js').then(function () {
      state.names = window.STZ_SEARCH_NAMES; state.idx = StzSearchCore.prepare(state.names);
      if (state.wantTexts) return ensureTexts();
    });
    return state.loading;
  }
  function ensureTexts() {
    if (state.texts) return Promise.resolve();
    return loadScript(ROOT + 'assets/search/text.js').then(function () { state.texts = window.STZ_SEARCH_TEXT; StzSearchCore.attachTexts(state.idx, state.texts); });
  }

  function methodUrl(m, cls) { return ROOT + LANG + '/reference/' + cls.name.toLowerCase() + (m.entry ? '/' + m.entry + '.html' : '.html#' + m.name.toLowerCase()); }
  function classUrl(c) { return ROOT + LANG + '/reference/' + c.name.toLowerCase() + '.html'; }
  function areaUrl(a) { return ROOT + LANG + (a.slug && a.slug !== 'education' ? '/guide/' + a.slug + '.html' : '/reference.html#' + (a.slug || 'other')); }
  function pageUrl(p) { return /^https?:/.test(p.url) ? p.url : ROOT + LANG + '/' + p.url; }
  function link(href, cls) {
    var a = el('a', cls); a.href = href; a.setAttribute('role', 'option');
    if (/^https?:/.test(href) && href.indexOf(ROOT) !== 0) { a.target = '_blank'; a.rel = 'noopener noreferrer'; }
    return a;
  }

  function render(panel, res, cap, input, status) {
    var idx = state.idx, toks = res.tokens;
    panel.textContent = '';
    var shown = 0;
    function head(txt, n) { var h = el('p', 'sh'); h.appendChild(document.createTextNode(txt)); if (n != null) h.appendChild(el('span', 'sn', ' · ' + n)); panel.appendChild(h); }
    if (res.qualified) panel.appendChild(el('p', 'sq', T.qual + ' ' + (idx.classes.filter(function (c) { return c.l === res.qualified; })[0] || { name: res.qualified }).name));
    if (res.areas.length) {
      head(T.areas);
      res.areas.slice(0, 3).forEach(function (r) {
        var a = idx.areas[r.ai], row = link(areaUrl(a), 'srow sa'); marked(row.appendChild(el('b', '')), LANG === 'fr' ? a.fr : a.en, toks); panel.appendChild(row); shown++;
      });
    }
    if (res.classes.length) {
      head(T.classes, res.classes.length);
      res.classes.slice(0, Math.min(cap, 6)).forEach(function (r) {
        var c = idx.classes[r.ci], a = idx.areas[c.area], row = link(classUrl(c), 'srow sc');
        var b = row.appendChild(el('b', 'mono')); marked(b, c.name, toks);
        if (c.also.length) row.appendChild(el('span', 'sd', ' · ' + c.also.slice(0, 3).join(' · ')));
        row.appendChild(el('span', 'spath', (LANG === 'fr' ? a.fr : a.en) + ' › ' + c.n + ' ' + T.methods.toLowerCase()));
        panel.appendChild(row); shown++;
      });
    }
    if (res.groups.length) {
      head(T.methods, res.total);
      var left = cap * 4;
      res.groups.slice(0, Math.max(2, Math.ceil(cap / 2))).forEach(function (g) {
        var a = idx.areas[g.ai]; panel.appendChild(el('p', 'sa-h', LANG === 'fr' ? a.fr : a.en));
        g.classes.slice(0, 3).forEach(function (cg) {
          var c = idx.classes[cg.ci], ch = el('p', 'sc-h'); ch.appendChild(el('span', 'spath', (LANG === 'fr' ? a.fr : a.en) + ' › ')); ch.appendChild(el('b', 'mono', c.name)); panel.appendChild(ch);
          cg.methods.slice(0, 4).forEach(function (x) {
            if (left-- <= 0) return;
            var m = idx.methods[x.mi], row = link(methodUrl(m, c), 'srow sm');
            marked(row.appendChild(el('b', 'mono')), m.name, toks);
            if (x.where === 'form' || x.where === 'also') {
              var shownAs = (x.where === 'form' ? m.forms : m.also).filter(function (n) { return toks.some(function (t) { return n.toLowerCase().indexOf(t) >= 0; }); })[0];
              if (shownAs) { var s = el('span', 'sd'); s.appendChild(document.createTextNode(' · ' + T.via + ' ')); marked(s.appendChild(el('span', 'mono')), shownAs, toks); row.appendChild(s); }
            }
            var tx = idx.texts && idx.texts[x.mi];
            if (tx && (x.where === 'example' || !tx.dl) && tx.code) { var cl = el('span', 'sl mono'); marked(cl, StzSearchCore.snippet(tx.code, toks, 110), toks); row.appendChild(cl); }
            else if (tx && tx.desc) { var dd = el('span', 'sl'); marked(dd, StzSearchCore.snippet(tx.desc, toks, 120), toks); row.appendChild(dd); }
            if (m.ex) row.appendChild(el('span', 'sb', T.example));
            panel.appendChild(row); shown++;
          });
          if (cg.methods.length > 4) panel.appendChild(el('p', 'sx', '+ ' + (cg.methods.length - 4) + ' ' + T.moreIn + ' ' + c.name));
        });
      });
    }
    if (res.pages.length) {
      head(T.pages, res.pages.length);
      res.pages.slice(0, Math.min(cap, 6)).forEach(function (r) {
        var p = idx.pages[r.pi], row = link(pageUrl(p), 'srow sg'), t = LANG === 'fr' && p.fr ? p.fr : p.en;
        row.appendChild(el('span', 'sb', T.kind[p.kind] || p.kind)); marked(row.appendChild(el('span', 'st')), t, toks); panel.appendChild(row); shown++;
      });
    }
    var more = res.groups.length > Math.max(2, Math.ceil(cap / 2)) || res.classes.length > 6 || res.total > cap * 4;
    if (more && cap < 12) { var b = el('button', 'sbtn2', T.more); b.type = 'button'; b.onclick = function () { run(input, panel, status, cap * 3); input.focus(); }; panel.appendChild(b); }
    if (!state.texts) {
      var t = el('button', 'sbtn2 st2', T.texts + ' (' + T.textsHow + ')'); t.type = 'button';
      t.onclick = function () { try { localStorage.setItem('stz-search-text', '1'); } catch (e) {} state.wantTexts = true; status.textContent = T.loading; ensureTexts().then(function () { run(input, panel, status, cap); input.focus(); }); };
      panel.appendChild(t);
    } else panel.appendChild(el('p', 'sx', T.textsOn));
    if (!shown) panel.insertBefore(el('p', 'sq', T.none), panel.firstChild);
    status.textContent = shown ? T.count.replace('{n}', res.total).replace('{a}', res.groups.length) : T.none;
  }

  function run(input, panel, status, cap) {
    var q = input.value;
    if (q.trim().length < 2) { panel.hidden = true; panel.textContent = ''; status.textContent = ''; return; }
    panel.hidden = false;
    if (!state.idx) { panel.textContent = T.loading; status.textContent = T.loading; ensureNames().then(function () { run(input, panel, status, cap); }); return; }
    render(panel, StzSearchCore.search(state.idx, q), cap || 4, input, status);
  }

  function keys(input, panel, close) {
    input.addEventListener('keydown', function (e) {
      var rows = Array.prototype.slice.call(panel.querySelectorAll('a.srow')), at = rows.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); (rows[at + 1] || rows[0]) && (rows[at + 1] || rows[0]).focus(); }
      else if (e.key === 'ArrowUp' && at > 0) { e.preventDefault(); rows[at - 1].focus(); }
      else if (e.key === 'Enter' && rows.length && at < 0) { e.preventDefault(); rows[0].click(); }
      else if (e.key === 'Escape') { close(); }
    });
    panel.addEventListener('keydown', function (e) {
      var rows = Array.prototype.slice.call(panel.querySelectorAll('a.srow')), at = rows.indexOf(document.activeElement);
      if (e.key === 'ArrowDown' && at >= 0) { e.preventDefault(); (rows[at + 1] || rows[at]).focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); if (at > 0) rows[at - 1].focus(); else input.focus(); }
      else if (e.key === 'Escape') { close(); input.focus(); }
    });
  }

  // the field of the page (the reference's filter): results under it; the page keeps filtering its own rows
  function attach(input) {
    var wrap = el('div', 'srch'), status = el('p', 'sr-only'), panel = el('div', 'sp'); panel.hidden = true;
    status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite'); panel.setAttribute('role', 'listbox');
    input.parentNode.insertBefore(wrap, input); wrap.appendChild(input); wrap.appendChild(status); wrap.appendChild(panel);
    input.setAttribute('autocomplete', 'off'); input.setAttribute('placeholder', T.ph); input.setAttribute('aria-label', T.ph);
    input.addEventListener('focus', function () { ensureNames(); });
    input.addEventListener('input', function () { run(input, panel, status, 4); if (!panel.hidden && input.getBoundingClientRect().top > 260) input.scrollIntoView({ block: 'start' }); });   // the results are under the field: bring them into view
    keys(input, panel, function () { panel.hidden = true; });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) panel.hidden = true; });
  }

  // the overlay: the same field over any page
  var dialog = null;
  function openDialog() {
    if (!dialog) {
      dialog = el('div', 'sdlg'); dialog.setAttribute('role', 'dialog'); dialog.setAttribute('aria-modal', 'true'); dialog.setAttribute('aria-label', T.open); dialog.hidden = true;
      var box = el('div', 'sbox'), bar = el('div', 'sbar'), input = el('input', 'sin'), x = el('button', 'sx2', T.close);
      input.type = 'search'; input.placeholder = T.ph; input.setAttribute('aria-label', T.ph); input.autocomplete = 'off';
      x.type = 'button'; x.onclick = closeDialog;
      var status = el('p', 'sr-only'); status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
      var panel = el('div', 'sp sp-d'); panel.setAttribute('role', 'listbox'); var hint = el('p', 'sq', T.hint);
      bar.appendChild(input); bar.appendChild(x); box.appendChild(bar); box.appendChild(status); box.appendChild(hint); box.appendChild(panel); dialog.appendChild(box); document.body.appendChild(dialog);
      dialog.addEventListener('click', function (e) { if (e.target === dialog) closeDialog(); });
      input.addEventListener('input', function () { hint.hidden = input.value.trim().length >= 2; run(input, panel, status, 4); });
      keys(input, panel, closeDialog);
      dialog._input = input;
    }
    dialog.hidden = false; document.body.classList.add('sopen'); ensureNames(); dialog._input.focus(); dialog._input.select();
  }
  function closeDialog() { if (dialog) { dialog.hidden = true; document.body.classList.remove('sopen'); if (dialog._from) dialog._from.focus(); } }

  function init() {
    if (typeof StzSearchCore === 'undefined') return;
    document.querySelectorAll('.tools').forEach(function (tools) {
      var a = el('a', 'sbtn'); a.href = '#search'; a.setAttribute('role', 'button'); a.setAttribute('aria-label', T.open); a.title = T.open + '  /';
      a.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="M15.5 15.5L21 21" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg><span class="sw">' + T.open + '</span>';
      a.addEventListener('click', function (e) { e.preventDefault(); openDialog(); dialog._from = a; });
      tools.insertBefore(a, tools.firstChild);
    });
    document.querySelectorAll('input#flt').forEach(attach);
    document.addEventListener('keydown', function (e) {
      var typing = /^(input|textarea|select)$/i.test((e.target.tagName || '')) || e.target.isContentEditable;
      if ((e.key === '/' && !typing && !e.ctrlKey && !e.metaKey) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k')) { e.preventDefault(); openDialog(); }
      else if (e.key === 'Escape' && dialog && !dialog.hidden) closeDialog();
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
