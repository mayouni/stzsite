#!/usr/bin/env node
/* Drive the search of a built page in headless Chrome, the way a reader does, and keep what it showed.
       node tools/search_ui.mjs <page under the site, e.g. en/reference/stzstring.html> "<what to type>" <out.webp> [phone|laptop] [dialog|field] [texts]
   It opens the page from disk, opens the search (the magnifier, or the page's own field), types, waits for the results, prints the
   text of the results and writes a picture. `texts` presses the button that loads the descriptions and the examples first. */
import { spawn } from 'node:child_process';
import { existsSync, writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const [page, query, out, size = 'laptop', mode = 'dialog', texts] = process.argv.slice(2);
const CHROME = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
const [W, H, mobile] = size === 'phone' ? [390, 844, true] : [1366, 900, false];
const port = 9344;
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--allow-file-access-from-files', `--remote-debugging-port=${port}`, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function json(path, method = 'GET') { for (let i = 0; i < 50; i++) { try { return await (await fetch(`http://127.0.0.1:${port}${path}`, { method })).json(); } catch (e) { await sleep(200); } } throw new Error('no chrome'); }
const target = await json('/json/new?about:blank', 'PUT');
const ws = new WebSocket(target.webSocketDebuggerUrl); await new Promise(r => ws.onopen = r);
let id = 0; const waits = new Map(); const events = [];
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && waits.has(m.id)) { waits.get(m.id)(m); waits.delete(m.id); } else if (m.method) events.push(m); };
const send = (method, params = {}) => new Promise(r => { const i = ++id; waits.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const evalJs = async (expr) => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile });
await send('Page.navigate', { url: pathToFileURL(resolve(ROOT, page)).href });
await sleep(1800);
if (mode === 'dialog') await evalJs(`document.querySelector('.sbtn').click()`);
const inputSel = mode === 'dialog' ? '.sdlg .sin' : '#flt';
await evalJs(`(function(){var i=document.querySelector('${inputSel}'); i.focus(); i.value=${JSON.stringify(query)}; i.dispatchEvent(new Event('input',{bubbles:true}));})()`);
await sleep(1500);
if (texts) { await evalJs(`(document.querySelector('.st2')||{click(){}}).click()`); await sleep(2500); }
const text = await evalJs(`(function(){var p=document.querySelector(${JSON.stringify(mode === 'dialog' ? '.sdlg .sp' : '.srch .sp')}); return p? p.innerText : 'NO PANEL';})()`);
console.log(text);
const shot = await send('Page.captureScreenshot', { format: 'png' });
writeFileSync(resolve(ROOT, out.replace(/\.webp$/, '.png')), Buffer.from(shot.result.data, 'base64'));
console.log('->', out.replace(/\.webp$/, '.png'));
ws.close(); chrome.kill();
process.exit(0);
