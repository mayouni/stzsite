#!/usr/bin/env python3
"""Check every example the site shows under a row, a function or a narration (the <pre class="rx"> blocks).

The rules an example answers to, each one a ruling of the author or of the site:

  - it never names the platform's former language (the word, standing alone)
  - it never calls a ...Q() form as a statement whose value nothing uses (the Q rule of 2026-10-03)
  - it says what it printed: a `#-->` line, except a narration's example that the narration gives without output
  - it names its source on the line under it

    python tools/check_examples.py            prints the counts and every failure; exit 1 when there is one
"""
import re, sys, html, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qforms

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)
RX = re.compile(r'<pre class="rx">(.*?)</pre>(<span class="rx-src">(.*?)</span>)?', re.S)

def main():
    plain = qforms.get(ROOT).plain_anywhere
    count, bad, per = 0, [], collections.Counter()
    for lang in ("en", "fr"):
        for f in sorted((ROOT / lang).rglob("*.html")):
            kind = "narrations" if f.name == "narrations.html" else "guide" if "guide" in f.parts else "reference" if "reference" in f.parts else "other"
            text = f.read_text(encoding="utf-8", errors="replace")
            for m in RX.finditer(text):
                body = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
                code = "\n".join(l for l in body.split("\n") if not l.startswith("#-->"))
                out = [l for l in body.split("\n") if l.startswith("#-->")]
                count += 1; per[(lang, kind)] += 1
                rel = f.relative_to(ROOT).as_posix()
                if WORD.search(body): bad.append((rel, "names the former language", code.split("\n")[-1][:70]))
                if qforms.unchained(code, plain): bad.append((rel, "calls a Q form as a bare statement", code.split("\n")[-1][:70]))
                if not out and kind != "narrations": bad.append((rel, "prints nothing", code.split("\n")[-1][:70]))
                if not m.group(3): bad.append((rel, "names no source", code.split("\n")[-1][:70]))
    print(f"{count} examples checked")
    for (lang, kind), n in sorted(per.items()): print(f"  {lang} {kind:11} {n}")
    for b in bad[:40]: print("FAIL", *b)
    print(f"{len(bad)} failures")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
