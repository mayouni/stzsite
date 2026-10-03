/* The matching of the site's search: no page, no DOM, so a browser and node run the same code.
   tools/search_check.mjs measures it against the questions a reader asks.

   An index is prepared once from the two files tools/build_search.py writes (names, then, on request, texts).
   A query becomes tokens; a method is found by its name, its other names, the forms written with extensions (FindW, ContainsCS),
   its class and its area, and, when the texts are loaded, by its description and its example. The results are structured as
   category (area) > class > method, always, whatever was typed. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.StzSearchCore = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';
  var STOP = { a: 1, an: 1, the: 1, of: 1, to: 1, in: 1, on: 1, for: 1, from: 1, with: 1, and: 1, or: 1, how: 1, do: 1, i: 1, is: 1, it: 1, my: 1, by: 1, can: 1,
    un: 1, une: 1, le: 1, la: 1, les: 1, de: 1, des: 1, du: 1, par: 1, pour: 1, avec: 1, et: 1, ou: 1, dans: 1, sur: 1, comment: 1, je: 1, mon: 1, ma: 1, mes: 1, au: 1, aux: 1, en: 1 };

  function words(name) {
    return name.replace(/([a-z0-9])([A-Z])/g, '$1 $2').replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2').toLowerCase().split(/[^a-z0-9@]+/).filter(Boolean);
  }
  function csv(s) { return s ? s.split(',') : []; }

  function prepare(names, texts) {
    var idx = { names: names, areas: [], classes: [], methods: [], pages: [], texts: null };
    names.areas.forEach(function (a) { idx.areas.push({ slug: a[0], en: a[1], fr: a[2], l: (a[1] + ' ' + a[2]).toLowerCase() }); });
    names.classes.forEach(function (c, i) {
      var also = csv(c[2]);
      idx.classes.push({ name: c[0], area: c[1], also: also, n: c[3], l: c[0].toLowerCase(), al: also.map(function (x) { return x.toLowerCase(); }), w: words(c[0]),
        anc: csv(c[4]).map(Number), desc: [] });
    });
    idx.classes.forEach(function (c, i) { c.anc.forEach(function (a) { if (idx.classes[a]) idx.classes[a].desc.push(i); }); });   // a class's methods are also its descendants'

    names.methods.forEach(function (m, i) {
      var also = csv(m[3]), forms = csv(m[5]);
      idx.methods.push({ name: m[0], ci: m[1], entry: m[2], also: also, ex: m[4], forms: forms, l: m[0].toLowerCase(), w: words(m[0]),
        al: also.map(function (x) { return x.toLowerCase(); }), fl: forms.map(function (x) { return x.toLowerCase(); }) });
    });
    names.pages.forEach(function (p) { idx.pages.push({ kind: p[0], en: p[1], fr: p[2], url: p[3], l: (p[1] + ' ' + p[2] + ' ' + (p[4] || '')).toLowerCase() }); });
    if (texts) attachTexts(idx, texts);
    return idx;
  }
  function attachTexts(idx, texts) {
    idx.texts = new Array(idx.methods.length);
    texts.m.forEach(function (t) { idx.texts[t[0]] = { desc: t[1], code: t[2], out: t[3], dl: (t[1] || '').toLowerCase(), cl: ((t[2] || '') + ' ' + (t[3] || '')).toLowerCase() }; });
  }

  function tokens(q) {
    var all = q.toLowerCase().split(/[\s.()\[\],:;"'=]+/).filter(Boolean);
    var kept = all.filter(function (t) { return !STOP[t]; });
    return (kept.length ? kept : all).slice(0, 6);
  }

  // how well one token matches one name: 100 exact, 80 starts with it, 60 starts a word of it, 40 inside it
  function scoreName(tok, l, w) {
    if (l === tok) return 100;
    if (l.indexOf(tok) === 0) return 80;
    for (var i = 0; i < w.length; i++) if (w[i].indexOf(tok) === 0) return 60;
    return l.indexOf(tok) >= 0 ? 40 : 0;
  }
  function best(tok, list) { var b = 0; for (var i = 0; i < list.length; i++) { var s = scoreName(tok, list[i], [list[i]]); if (s > b) b = s; } return b; }

  function search(idx, query, opt) {
    opt = opt || {};
    var q = query.trim();
    var toks = tokens(q);
    var res = { tokens: toks, areas: [], classes: [], groups: [], pages: [], total: 0, texts: !!idx.texts, qualified: null };
    if (!toks.length || (toks.length === 1 && toks[0].length < 2)) return res;
    // Class.Method, or a class named in a sentence: the class is where to look, the rest is what to look for
    var named = null, dot = /^([A-Za-z0-9_@]+)\.([A-Za-z0-9_@]*)/.exec(q);
    var exact = function (seg) {
      var out = [];
      idx.classes.forEach(function (c, i) { if (c.l === seg || c.al.indexOf(seg) >= 0) out.push(i); });
      return out;
    };
    if (dot) {
      var seg = dot[1].toLowerCase(), hit = exact(seg);
      if (!hit.length) idx.classes.forEach(function (c, i) { if (c.l.indexOf(seg) === 0) hit.push(i); });
      if (hit.length) { named = { classes: hit, seg: seg }; toks = tokens(q.slice(dot[1].length + 1)); }
    } else if (toks.length > 1) {
      for (var k0 = 0; k0 < toks.length && !named; k0++) {
        var hh = exact(toks[k0]);
        if (hh.length) { named = { classes: hh, seg: toks[k0] }; toks = toks.filter(function (_, i) { return i !== k0; }); }
      }
    }
    res.tokens = toks; res.qualified = named && named.seg;
    var allowed = null;                                         // the classes whose methods are looked at: the named ones and what they inherit
    if (named) {
      allowed = {};
      named.classes.forEach(function (ci) { allowed[ci] = 1; idx.classes[ci].anc.forEach(function (a) { allowed[a] = 1; }); });
    }
    // areas and classes found by name
    if (!named) idx.areas.forEach(function (a, i) {
      if (toks.every(function (t) { return a.l.indexOf(t) >= 0; })) res.areas.push({ ai: i, score: 50 });
    });
    var classScore = new Array(idx.classes.length), cv = new Array(idx.classes.length);
    idx.classes.forEach(function (c, i) {
      var s = 0, hit = 0, area = idx.areas[c.area], per = [];
      toks.forEach(function (t) {
        var v = Math.max(scoreName(t, c.l, c.w), best(t, c.al), area && area.l.indexOf(t) >= 0 ? 30 : 0), own = v;
        for (var d = 0; d < c.desc.length && v < 80; d++) { var dc = idx.classes[c.desc[d]]; v = Math.max(v, 0.8 * scoreName(t, dc.l, dc.w)); }   // hash list: stzList's methods are stzHashList's
        per.push(v);
        if (own) { hit++; s += own; }
      });
      cv[i] = per;
      classScore[i] = { hit: hit, s: s };
      if (!named && toks.length && hit === toks.length) res.classes.push({ ci: i, score: s });
      if (named && named.classes.indexOf(i) >= 0 && !toks.length) res.classes.push({ ci: i, score: 100 });
    });
    // how telling each token is: a word that few methods carry (sort) says more than one that thousands do (list)
    var N = idx.methods.length, df = toks.map(function () { return 1; });
    for (var m0 = 0; m0 < N; m0++) {
      var mm = idx.methods[m0];
      if (allowed && !allowed[mm.ci]) continue;
      for (var k1 = 0; k1 < toks.length; k1++) if (scoreName(toks[k1], mm.l, mm.w) || cv[mm.ci][k1]) df[k1]++;
    }
    var idf = df.map(function (d, k) { return Math.log(1 + N / d) / (1 + 0.15 * k); }),     // and the first word of a sentence is its verb: it weighs most
         total = idf.reduce(function (a, b) { return a + b; }, 0);
    var maxCover = 0, cand = [];
    for (var mi = 0; mi < N; mi++) {
      var m = idx.methods[mi];
      if (allowed && !allowed[m.ci]) continue;
      var tx = idx.texts && idx.texts[mi];
      var cover = 0, score = 0, where = '', via = '';
      for (var k = 0; k < toks.length; k++) {
        var t = toks[k], v = scoreName(t, m.l, m.w), w = 'name';
        var a = best(t, m.al); if (a * 0.9 > v) { v = a * 0.9; w = 'also'; via = via || t; }
        var f = best(t, m.fl); if (f * 0.8 > v) { v = f * 0.8; w = 'form'; via = via || t; }
        if (!v && cv[m.ci][k]) { v = cv[m.ci][k] * 0.25; w = 'class'; }
        if (!v && tx) {
          if (tx.dl.indexOf(t) >= 0) { v = 22; w = 'description'; }
          else if (tx.cl.indexOf(t) >= 0) { v = 18; w = 'example'; }
        }
        if (v) { cover += idf[k]; score += v * idf[k]; if (w !== 'class' && (!where || where === 'class' || (where === 'description' && w === 'name'))) where = w; }
      }
      if (named && !toks.length) { cover = 1; score = 100 - Math.min(99, mi % 1000) / 100; where = 'name'; }
      if (!cover) continue;
      if (m.ex) score += 2;
      score = cover * 1000 + score - m.name.length / 100;
      if (cover > maxCover) maxCover = cover;
      cand.push({ mi: mi, cover: cover, score: score, where: where || 'class', via: via });
    }
    // the methods that cover most of what was typed (a sentence keeps its best cover, not every word)
    var kept = cand.filter(function (x) { return x.cover >= 0.7 * maxCover; });
    if (toks.length && maxCover < 0.5 * total) kept = [];
    res.total = kept.length;
    // group: area > class > method
    var byClass = {};
    kept.forEach(function (x) {
      var m = idx.methods[x.mi];
      (byClass[m.ci] = byClass[m.ci] || { ci: m.ci, max: 0, methods: [] }).methods.push(x);
      if (x.score > byClass[m.ci].max) byClass[m.ci].max = x.score;
    });
    var byArea = {};
    Object.keys(byClass).forEach(function (ci) {
      var g = byClass[ci], c = idx.classes[ci];
      g.methods.sort(function (a, b) { return b.score - a.score; });
      (byArea[c.area] = byArea[c.area] || { ai: c.area, max: 0, classes: [] }).classes.push(g);
      if (g.max > byArea[c.area].max) byArea[c.area].max = g.max;
    });
    res.groups = Object.keys(byArea).map(function (k) { return byArea[k]; }).sort(function (a, b) { return b.max - a.max; });
    res.groups.forEach(function (g) { g.classes.sort(function (a, b) { return b.max - a.max; }); });
    res.classes.sort(function (a, b) { return b.score - a.score; });
    // pages: guides, how-to recipes, narrations, book chapters
    if (!named) idx.pages.forEach(function (p, i) {
      if (toks.every(function (t) { return p.l.indexOf(t) >= 0; })) res.pages.push({ pi: i, score: 40 });
    });
    return res;
  }

  // the pieces of a text, cut where a token matches: [[text, true|false], ...]: the page escapes and wraps them
  function segments(text, toks) {
    var l = text.toLowerCase(), mark = new Array(text.length + 1).fill(false), any = false;
    toks.forEach(function (t) {
      var at = l.indexOf(t);
      while (at >= 0) { any = true; for (var i = at; i < at + t.length; i++) mark[i] = true; at = l.indexOf(t, at + t.length); }
    });
    if (!any) return [[text, false]];
    var out = [], cur = '', on = mark[0];
    for (var i = 0; i < text.length; i++) {
      if (mark[i] !== on) { out.push([cur, on]); cur = ''; on = mark[i]; }
      cur += text[i];
    }
    out.push([cur, on]);
    return out;
  }
  // around the first match of a token in a longer text: a window of about `n` characters
  function snippet(text, toks, n) {
    n = n || 100;
    if (text.length <= n) return text;
    var l = text.toLowerCase(), at = -1;
    for (var i = 0; i < toks.length && at < 0; i++) at = l.indexOf(toks[i]);
    if (at < 0) at = 0;
    var from = Math.max(0, at - 30), to = Math.min(text.length, from + n);
    return (from > 0 ? '…' : '') + text.slice(from, to) + (to < text.length ? '…' : '');
  }
  return { prepare: prepare, attachTexts: attachTexts, search: search, tokens: tokens, segments: segments, snippet: snippet, words: words };
});
