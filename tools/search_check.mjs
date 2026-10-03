#!/usr/bin/env node
/* The search measured against what a reader asks (the author's rule: a rethought search is judged on questions, not on looks).
   Each question names what must be found, and where it must stand: a class, a method of a class, a page, in the first five results
   of the kind it belongs to. The same file the page loads runs here: assets/js/search-core.js on assets/search/*.js.
       node tools/search_check.mjs     prints each question and the verdict; exit code 1 when one fails   */
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import vm from 'node:vm';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const core = createRequire(import.meta.url)(resolve(ROOT, 'assets/js/search-core.js'));
const load = (f, g) => { const w = {}; vm.runInNewContext(readFileSync(resolve(ROOT, 'assets/search', f), 'utf8'), { window: w }); return w[g]; };
const names = load('names.js', 'STZ_SEARCH_NAMES'), texts = load('text.js', 'STZ_SEARCH_TEXT');
const withNames = core.prepare(names), withTexts = core.prepare(names, texts);

// [what the reader types, "names" or "texts" (the index it needs), a predicate over the first five hits, what is expected, in words]
const flat = (idx, r) => r.groups.flatMap(a => a.classes.flatMap(c => c.methods.map(x => ({ cls: idx.classes[idx.methods[x.mi].ci].name, m: idx.methods[x.mi], via: x.via, where: x.where }))));
const QUESTIONS = [
  ['remove duplicates', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => /duplicat/i.test(h.m.name) && /remov/i.test(h.m.name)), 'a method that removes duplicates'],
  ['FindW', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => h.m.name === 'Find' && h.via), 'Find, through its form FindW'],
  ['ContainsCS', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => h.m.name === 'Contains'), 'Contains, through its form ContainsCS'],
  ['stzString.Find', 'names', (idx, r) => flat(idx, r).slice(0, 3).some(h => h.cls === 'stzString' && h.m.name === 'Find'), 'stzString, Find'],
  ['list of pairs', 'names', (idx, r) => r.classes.slice(0, 5).some(c => idx.classes[c.ci].name === 'stzListOfPairs'), 'the class stzListOfPairs'],
  ['palindrome', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => /palindrome/i.test(h.m.name)), 'a method about palindromes'],
  ['uppercase', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => h.cls === 'stzString' && /^uppercase/i.test(h.m.name)), 'stzString, Uppercase'],
  ['graph shortest path', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => /graph/i.test(h.cls) && /shortestpath/i.test(h.m.name)), 'a graph method for the shortest path'],
  ['sort hash list by value', 'names', (idx, r) => flat(idx, r).slice(0, 5).some(h => /^stz(hash)?list$/i.test(h.cls) && /^sort/i.test(h.m.name)), 'a sort method that applies to a hash list (stzList, which stzHashList inherits)'],
  ['banana split', 'texts', (idx, r) => r.total > 0 && flat(idx, r).slice(0, 5).every(h => h.where === 'example' || h.where === 'description' || h.where === 'name'), 'methods whose example shows "banana split"'],
  ['vowels in a word', 'texts', (idx, r) => flat(idx, r).slice(0, 5).some(h => /vowel/i.test(h.m.name)), 'a method about vowels'],
  ['string', 'names', (idx, r) => r.areas.length > 0 && r.classes.length > 0, 'the area String and its classes'],
  ['xml', 'names', (idx, r) => r.pages.some(p => /xml/i.test(idx.pages[p.pi].l)), 'a page about XML'],
];

let bad = 0;
for (const [q, need, ok, what] of QUESTIONS) {
  const idx = need === 'texts' ? withTexts : withNames;
  const t0 = performance.now(); const r = core.search(idx, q); const ms = (performance.now() - t0).toFixed(1);
  const first = flat(idx, r).slice(0, 3).map(h => `${h.cls}.${h.m.name}`).join(', ');
  const pass = ok(idx, r);
  if (!pass) bad++;
  console.log(`${pass ? 'ok  ' : 'FAIL'} ${q.padEnd(26)} ${ms.padStart(6)} ms  ${String(r.total).padStart(5)} methods in ${r.groups.length} areas  | ${what}${pass ? '' : ' -- NOT FOUND'}  | first: ${first}`);
}
console.log(`${QUESTIONS.length - bad} of ${QUESTIONS.length} questions answered; index: ${names.methods.length.toLocaleString()} methods, ${names.classes.length} classes`);
process.exit(bad ? 1 : 0);
