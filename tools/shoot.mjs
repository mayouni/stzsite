#!/usr/bin/env node
/* Render every page at phone, laptop and projector widths, light and dark,
   from file://, and keep the pictures in proofs/. Drives one headless Chrome
   through its DevTools protocol so the phone viewport is a real 390 CSS px
   (a plain --window-size cannot go below about 490 on Windows).
   No dependencies: Node 22's fetch and WebSocket.
       node tools/shoot.mjs [substring ...]   */
import { spawn } from 'node:child_process';
import { existsSync, writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CHROME = ['C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
if (!CHROME) { console.error('no Chrome or Edge found'); process.exit(1); }
const SIZES = { phone: [390, 844, true], laptop: [1366, 768, false], projector: [1920, 1080, false] };
const NEW = ['platform', 'platforms', 'architecture', 'craft', 'areas', 'atlas', 'code', 'compare', 'vision', 'principles', 'estate', 'history', 'sovereignty', 'africa',
  'agentic', 'wise', 'languages', 'zui', 'refinement', 'agents', 'coding-agents', 'security', 'learn', 'book', 'docs', 'reference',
  'narrations', 'teaching', 'pedagogy', 'offering', 'editions', 'customers', 'start', 'tour'];
const PAGES = ['index.html', ...NEW.map(p => `fr/${p}.html`), ...NEW.map(p => `en/${p}.html`), 'deck-check.html'];
const PLAN = [];
for (const p of PAGES) {
  PLAN.push([p, 'laptop', 'light']);
  if (p.startsWith('fr/') || p === 'index.html') PLAN.push([p, 'phone', 'light']);
  if (['index.html', 'fr/platform.html', 'fr/agentic.html', 'fr/areas.html', 'fr/tour.html'].includes(p)) PLAN.push([p, 'projector', 'light']);
  if (['index.html', 'fr/vision.html', 'fr/agentic.html', 'fr/compare.html', 'en/platform.html'].includes(p)) PLAN.push([p, 'laptop', 'dark']);
}
for (const g of ['string', 'geo', 'governance', 'security', 'tables', 'binary', 'gui']) PLAN.push([`fr/atlas/${g}.html`, 'laptop', 'light']);
PLAN.push(['fr/guide/string.html', 'laptop', 'light'], ['fr/guide/string.html', 'phone', 'light'], ['en/guide/geo.html', 'laptop', 'light']);
PLAN.push(['fr/atlas/geo.html', 'phone', 'light'], ['fr/reference/stzlist.html', 'laptop', 'light'], ['fr/reference/stzstring.html', 'phone', 'light'], ['en/reference/methods-a.html', 'laptop', 'light']);
for (const k of [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) PLAN.push([`fr/tour.html#s${k}`, 'projector', 'light']);
PLAN.push(['fr/tour.html#s4', 'phone', 'light']);
const FULL = ['index.html', 'fr/platform.html', 'fr/architecture.html', 'en/architecture.html', 'fr/craft.html', 'en/craft.html', 'fr/coding-agents.html', 'en/coding-agents.html', 'fr/platforms.html', 'en/platforms.html', 'fr/vision.html', 'en/vision.html', 'fr/areas.html', 'fr/agentic.html', 'fr/compare.html', 'fr/estate.html', 'fr/learn.html', 'fr/offering.html', 'fr/atlas.html', 'en/zui.html', 'en/docs.html'];

const only = process.argv.slice(2);
const port = 9333;
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
  '--allow-file-access-from-files', `--remote-debugging-port=${port}`, '--window-size=1920,1080', 'about:blank'],
  { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function json(path, method = 'GET') {
  for (let i = 0; i < 50; i++) {
    try { const r = await fetch(`http://127.0.0.1:${port}${path}`, { method }); return await r.json(); } catch (e) { await sleep(200); }
  }
  throw new Error('chrome did not answer on ' + port);
}
class CDP {
  constructor(ws) { this.ws = ws; this.id = 0; this.waits = new Map(); this.events = []; ws.onmessage = e => this.on(JSON.parse(e.data)); }
  on(m) { if (m.id && this.waits.has(m.id)) { this.waits.get(m.id)(m); this.waits.delete(m.id); } else if (m.method) this.events.push(m); }
  send(method, params = {}) { const id = ++this.id; this.ws.send(JSON.stringify({ id, method, params })); return new Promise(r => this.waits.set(id, r)); }
  async until(method, ms) { const t0 = Date.now(); while (Date.now() - t0 < ms) { const i = this.events.findIndex(e => e.method === method); if (i >= 0) { this.events.splice(0, i + 1); return true; } await sleep(30); } return false; }
}
function name(page, size, theme, full) {
  return page.replace(/\//g, '-').replace('.html', '').replace(/[?#=]/g, '-') + `--${size}-${theme}${full ? '-full' : ''}.webp`;
}
async function main() {
  mkdirSync(resolve(ROOT, 'proofs'), { recursive: true });
  const target = await json('/json/new?about:blank', 'PUT');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  const c = new CDP(ws);
  await c.send('Page.enable'); await c.send('Runtime.enable');
  const t0 = Date.now(); let n = 0;
  const jobs = PLAN.map(([p, s, t]) => [p, s, t, false]).concat(FULL.map(p => [p, 'laptop', 'light', true]));   // a selection filters these too
  for (const [page, size, theme, full] of jobs) {
    if (only.length && !only.some(o => page.includes(o))) continue;
    const [w, h, mobile] = SIZES[size];
    const base = page.split(/[?#]/)[0]; let q = page.slice(base.length);
    if (theme === 'dark') q = q.includes('#') ? q.replace('#', '?theme=dark#') : q + (q.includes('?') ? '&' : '?') + 'theme=dark';
    const url = pathToFileURL(resolve(ROOT, base)).href + q;
    await c.send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile });
    await c.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await c.send('Page.navigate', { url: 'about:blank' }); await sleep(50);
    await c.send('Page.navigate', { url });
    await c.until('Page.loadEventFired', 15000);
    await c.send('Runtime.evaluate', { expression: 'document.fonts ? document.fonts.ready.then(()=>1) : 1', awaitPromise: true });
    await sleep(page.includes('tour') || page.includes('deck-check') ? 9000 : 700);
    let opts = { format: 'webp', quality: 82, captureBeyondViewport: false };
    if (full) {
      /* a whole page at the real viewport size: the layout a reader gets, captured past the fold;
         lazy pictures are told to load first, since a capture never scrolls */
      await c.send('Runtime.evaluate', { expression: "document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager'); 1" });
      await sleep(1500);
      const hh = await c.send('Runtime.evaluate', { expression: 'Math.min(document.documentElement.scrollHeight, 16000)', returnByValue: true });
      opts = { format: 'webp', quality: 80, captureBeyondViewport: true, clip: { x: 0, y: 0, width: w, height: hh.result.result.value, scale: 1 } };
    }
    const shot = await c.send('Page.captureScreenshot', opts);
    const out = resolve(ROOT, 'proofs', name(page, size, theme, full));
    writeFileSync(out, Buffer.from(shot.result.data, 'base64'));
    console.log(`  ${name(page, size, theme, full)}  ${w}x${h}`); n++;
  }
  ws.close(); chrome.kill();
  console.log(`${n} renders in ${Math.round((Date.now() - t0) / 1000)}s -> proofs/`);
}
main().catch(e => { console.error(e); chrome.kill(); process.exit(1); });
