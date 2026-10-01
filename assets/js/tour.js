/* stzsite -- presentation mode. Scenes are full-screen sections; arrow keys,
   space, page keys and a click advance; `n` toggles the presenter's notes;
   `h` shows the site header; Escape opens the scene as a page. The scene
   number lives in the URL hash so every scene is also an address. Scene
   changes are instant: a presenter wants the next picture, not a glide. */
(function () {
  var scenes = Array.prototype.slice.call(document.querySelectorAll('.scene'));
  if (!scenes.length) return;
  var n = scenes.length, body = document.body, bar = document.querySelector('.progress .bar');
  var current = 0, lockUntil = 0;
  document.documentElement.style.scrollBehavior = 'auto';

  function fromHash() {
    var m = /^#s?(\d+)$/.exec(location.hash || '');
    var k = m ? parseInt(m[1], 10) : 1;
    return Math.min(Math.max(k, 1), n) - 1;
  }
  function paint() {
    for (var k = 0; k < n; k++) scenes[k].classList.toggle('current', k === current);
    if (bar) bar.style.width = ((current + 1) / n * 100) + '%';
  }
  function show(i) {
    current = Math.min(Math.max(i, 0), n - 1);
    lockUntil = Date.now() + 400;
    paint();
    window.scrollTo(0, scenes[current].offsetTop);
    try { if (location.hash !== '#s' + (current + 1)) history.replaceState(null, '', '#s' + (current + 1)); } catch (e) {}
  }
  function next() { show(current + 1); }
  function prev() { show(current - 1); }

  document.addEventListener('keydown', function (e) {
    if (e.target && /input|textarea|select/i.test(e.target.tagName)) return;
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case 'PageDown': case ' ': case 'Enter': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace': e.preventDefault(); prev(); break;
      case 'Home': e.preventDefault(); show(0); break;
      case 'End': e.preventDefault(); show(n - 1); break;
      case 'n': case 'N': body.classList.toggle('show-notes'); break;
      case 'h': case 'H': body.classList.toggle('show-chrome'); break;
      case 'Escape': var a = scenes[current].querySelector('.scene-page'); if (a) location.href = a.getAttribute('href'); break;
    }
  });
  /* a click on empty scene space advances; links, buttons and frames keep their job */
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.closest('a, button, iframe, .notes, .site-head, pre, input, select, textarea')) return;
    var sc = t.closest('.scene'); if (!sc) return;
    if (e.clientX < window.innerWidth * 0.2) prev(); else next();
  });
  /* keep the counter honest when the visitor scrolls by hand */
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking || Date.now() < lockUntil) return; ticking = true;
    requestAnimationFrame(function () {
      if (Math.abs(scenes[current].offsetTop - window.scrollY) < 4) { ticking = false; return; }
      var y = window.scrollY + window.innerHeight / 2, best = 0;
      for (var k = 0; k < n; k++) if (scenes[k].offsetTop <= y) best = k;
      if (best !== current) { current = best; paint(); try { history.replaceState(null, '', '#s' + (current + 1)); } catch (e) {} }
      ticking = false;
    });
  });
  window.addEventListener('hashchange', function () { var k = fromHash(); if (k !== current) show(k); });
  window.addEventListener('load', function () { show(fromHash()); });
  show(fromHash());
})();
