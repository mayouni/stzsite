#!/usr/bin/env node
/* The floor, measured on the paint: every text a reader can see is at least 16 px, and its colour against the background behind it
   meets 4.5:1 (3:1 for large text), in the light theme and in the dark one. Rules 105 and 107 of the interface law, which the site's
   stylesheet keeps and which the two pages it publishes without styling them, the course reader and the deck check, broke: the
   external assessment measured about 2,730 text nodes under the floor in the reader and 417 in the deck check (2026-10-07).
   A text over a picture or a gradient is reported as UNMEASURED, never as a ratio: the instrument cannot see an image.
       node tools/floor_check.mjs reader.html deck-check.html en/index.html ...
   Exit 1 when a page has a text under the floor or under the contrast it needs. */
import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const CHROME = ['C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
const pages = process.argv.slice(2);
const port = 9334;
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--allow-file-access-from-files',
  `--remote-debugging-port=${port}`, '--window-size=1280,900', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function json(path, method = 'GET') {
  for (let i = 0; i < 50; i++) { try { const r = await fetch(`http://127.0.0.1:${port}${path}`, { method }); return await r.json(); } catch (e) { await sleep(200); } }
  throw new Error('chrome did not answer');
}
class CDP {
  constructor(ws) { this.ws = ws; this.id = 0; this.waits = new Map(); this.events = []; ws.onmessage = e => this.on(JSON.parse(e.data)); }
  on(m) { if (m.id && this.waits.has(m.id)) { this.waits.get(m.id)(m); this.waits.delete(m.id); } else if (m.method) this.events.push(m); }
  send(method, params = {}) { const id = ++this.id; this.ws.send(JSON.stringify({ id, method, params })); return new Promise(r => this.waits.set(id, r)); }
  async until(method, ms) { const t0 = Date.now(); while (Date.now() - t0 < ms) { const i = this.events.findIndex(e => e.method === method); if (i >= 0) { this.events.splice(0, i + 1); return true; } await sleep(50); } return false; }
}
/* runs inside the page: every visible text node, its size, its colour, the background behind it */
const PROBE = `(() => {
  const rgb = s => { const m = s.match(/rgba?\\(([^)]+)\\)/); if (!m) return null; const p = m[1].split(',').map(x => parseFloat(x)); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  function behind(el) {
    for (let e = el; e; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.backgroundImage && s.backgroundImage !== 'none') return 'image';
      const c = rgb(s.backgroundColor); if (c && c.a > 0.5) return c;
    }
    return { r: 255, g: 255, b: 255, a: 1 };
  }
  const out = { nodes: 0, small: 0, low: 0, unmeasured: 0, sizes: {}, examples: [] };
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = walk.nextNode(); n; n = walk.nextNode()) {
    const t = n.textContent.trim(); if (!t) continue;
    const el = n.parentElement; if (!el) continue;
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden' || el.closest('[hidden],script,style,noscript')) continue;
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    out.nodes++;
    const px = parseFloat(s.fontSize); out.sizes[px] = (out.sizes[px] || 0) + 1;
    const bg = behind(el), fg = rgb(s.color);
    let bad = '';
    if (px < 16) { out.small++; bad = px + 'px'; }
    if (bg === 'image') out.unmeasured++;
    else if (fg) {
      const large = px >= 24 || (px >= 18.66 && parseInt(s.fontWeight) >= 700);
      const c = ratio(fg, bg); if (c < (large ? 3 : 4.5)) { out.low++; bad += (bad ? ', ' : '') + c.toFixed(2) + ':1'; }
    }
    if (bad && out.examples.length < 6) out.examples.push(bad + '  <' + el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : '') + '>  ' + t.slice(0, 50));
  }
  return out;
})()`;
async function main() {
  const target = await json('/json/new?about:blank', 'PUT');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  const c = new CDP(ws);
  await c.send('Page.enable'); await c.send('Runtime.enable');
  let failed = 0;
  for (const page of pages) {
    for (const theme of ['light', 'dark']) {
      await c.send('Emulation.setDeviceMetricsOverride', { width: 1280, height: 900, deviceScaleFactor: 1, mobile: false });
      await c.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: theme }, { name: 'prefers-reduced-motion', value: 'reduce' }] });
      const base = page.split(/[?#]/)[0];
      await c.send('Page.navigate', { url: 'about:blank' }); await sleep(50);
      await c.send('Page.navigate', { url: pathToFileURL(resolve(ROOT, base)).href + page.slice(base.length) });
      await c.until('Page.loadEventFired', 20000); await sleep(1500);
      const r = await c.send('Runtime.evaluate', { expression: PROBE, returnByValue: true });
      const o = r.result.result.value;
      const ok = o.small === 0 && o.low === 0;
      if (!ok) failed++;
      const sizes = Object.entries(o.sizes).sort((a, b) => a[0] - b[0]).map(([k, v]) => `${k}px:${v}`).join(' ');
      console.log(`${ok ? 'ok  ' : 'FAIL'} ${page} ${theme}: ${o.nodes} texts, ${o.small} under 16 px, ${o.low} under contrast, ${o.unmeasured} over an image (unmeasured) | ${sizes}`);
      for (const e of o.examples) console.log('       ' + e);
    }
  }
  ws.close(); chrome.kill();
  process.exit(failed ? 1 : 0);
}
main().catch(e => { console.error(e); chrome.kill(); process.exit(2); });
