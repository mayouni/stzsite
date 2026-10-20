#!/usr/bin/env python3
"""Which pages of the site tell without showing (the author, 2026-10-20: a paragraph that makes a claim about behaviour is
illustrated with code, not left abstract).

For every English page that has prose, count the words of its paragraphs, the code blocks it shows, and the words of prose per
code block. A page is listed when it has at least `--min` words of prose (default 220) and either no code block at all or more
than `--per` words of prose for each block (default 450). Pages that are indexes or pure reference are skipped: the method
and class pages (reference/), the narrations (they are code), the glossary and the roots.

    python tools/prose_audit.py [--min N] [--per N]       prints the pages, worst first, and the count
"""
import re, sys, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIR = {"reference", "narrations", "guide", "howto", "recipes"}
SKIP_NAME = {"glossary.html", "roots.html", "404.html", "search.html", "index.html"}

def words(s): return len(re.findall(r"\w+", html.unescape(re.sub(r"<[^>]+>", " ", s))))

def audit(min_words=220, per=450):
    out = []
    for f in sorted((ROOT / "en").rglob("*.html")):
        rel = f.relative_to(ROOT / "en")
        if rel.parts[0] in SKIP_DIR or f.name in SKIP_NAME: continue
        s = f.read_text(encoding="utf-8", errors="replace")
        body = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>", " ", s, flags=re.S)
        prose = sum(words(m) for m in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", body, flags=re.S))
        code = len(re.findall(r"<pre\b", body))
        if prose >= min_words and (code == 0 or prose / code > per):
            out.append((prose / max(code, 1), prose, code, rel.as_posix()))
    return sorted(out, reverse=True)

if __name__ == "__main__":
    a = sys.argv[1:]
    mn = int(a[a.index("--min") + 1]) if "--min" in a else 220
    pr = int(a[a.index("--per") + 1]) if "--per" in a else 450
    rows = audit(mn, pr)
    for ratio, prose, code, rel in rows: print(f"{prose:5d} words  {code:3d} code blocks  {rel}")
    print(f"{len(rows)} pages tell more than they show")
