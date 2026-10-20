#!/usr/bin/env python3
"""Code is never wrapped, never scrolled: it is laid out to fit its box (the author, StzZui, 2026-10-20).

Two rules of the author meet here and neither gives way: a line of code is never split (the closing bracket of a list does not
fall to a line of its own by accident), and a code box never carries a horizontal bar. So a line too long for its box is not left
to the browser: a list literal in it is broken at its commas, structurally, the way @@NL shows a list, each item on a line of its
own, nested lists indented. What this cannot lay out (a long string, a long comment) is left to wrap, never to scroll.

  fit(text, width)    the text with every line over `width` laid out; a promise line (#--> ...) keeps its prefix
  fit_site(root)      the same over every <pre> of every built page that holds only text, by the width of its box:
                      56 characters in a row of a class table, 64 elsewhere (the sample of an introduction is written to 72)
  no_scroll(css)      the stylesheet must not give code a scroll bar: returns the offending rules
"""
import re, html, pathlib

QUOTES = "\"'"

def _walk(s, start, stop_at_close=False):
    """index of the first '[' outside quotes from `start` (-1 if none); with stop_at_close, the index of the ']' that closes the
    group opened at `start` (-1 if the group never closes)"""
    q, d = None, 0
    for i in range(start, len(s)):
        ch = s[i]
        if q:
            if ch == q: q = None
            continue
        if ch in QUOTES: q = ch; continue
        if not stop_at_close:
            if ch == "[": return i
        else:
            if ch == "[": d += 1
            elif ch == "]":
                d -= 1
                if d == 0: return i
    return -1

def _items(inner):
    out, cur, d, q = [], "", 0, None
    for ch in inner:
        if q:
            cur += ch
            if ch == q: q = None
            continue
        if ch in QUOTES: q = ch; cur += ch; continue
        if ch == "[": d += 1
        elif ch == "]": d -= 1
        if ch == "," and d == 0: out.append(cur.strip()); cur = ""
        else: cur += ch
    if cur.strip(): out.append(cur.strip())
    return out

def pp(line, width):
    """one line, laid out in several when it is over `width` and holds a list literal"""
    if len(line) <= width or line.lstrip().startswith("#"): return [line]
    a = _walk(line, 0)
    if a < 0: return [line]
    b = _walk(line, a, True)
    if b < 0: return [line]
    inner = line[a + 1:b].strip()
    if not inner: return [line]
    base = line[:len(line) - len(line.lstrip())]
    pad = base + "    "
    items = _items(inner)
    if len(items) < 2 and "[" not in inner: return [line]
    out = [line[:a + 1]]
    for k, it in enumerate(items):
        out += pp(pad + it + ("," if k < len(items) - 1 else ""), width)
    out.append(base + line[b:])
    return out

def fit(text, width):
    out = []
    for line in text.split("\n"):
        if len(line) <= width: out.append(line); continue
        if line.startswith("#--> "):
            out += ["#--> " + x for x in pp(line[5:], width - 5)]
        else:
            out += pp(line, width)
    return "\n".join(out)

PRE = re.compile(r"<pre((?: [^>]*)?)>([^<]*)</pre>")

def fit_site(root):
    """lays out the long lines of every text-only <pre> of the built pages; returns (blocks changed, lines laid out)"""
    root = pathlib.Path(root)
    files = list((root / "en").rglob("*.html")) + list((root / "fr").rglob("*.html")) + list(root.glob("*.html"))
    blocks = lines = 0
    for f in files:
        s = f.read_text(encoding="utf-8", errors="replace")
        if "<pre" not in s: continue
        def one(m):
            nonlocal blocks, lines
            attrs, body = m.group(1), m.group(2)
            if 'class="sample"' in attrs: return m.group(0)
            width = 56 if 'class="rx"' in attrs else 64
            text = html.unescape(body)
            if all(len(l) <= width for l in text.split("\n")): return m.group(0)
            new = fit(text, width)
            if new == text: return m.group(0)
            blocks += 1; lines += new.count("\n") - text.count("\n")
            return f"<pre{attrs}>{html.escape(new, quote=False)}</pre>"
        t = PRE.sub(one, s)
        if t != s: f.write_text(t, encoding="utf-8")
    return blocks, lines

def no_scroll(css_text):
    """the rules of a stylesheet that give a code box a scroll bar"""
    bad = []
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css_text):
        sel, body = m.group(1), m.group(2)
        if re.search(r"\b(pre|code)\b", sel) and re.search(r"overflow(-x)?\s*:\s*(auto|scroll)", body):
            bad.append(sel.strip()[:80])
    return bad

if __name__ == "__main__":
    import sys
    r = pathlib.Path(__file__).resolve().parent.parent
    print("scroll rules on code:", no_scroll((r / "assets" / "css" / "site.css").read_text(encoding="utf-8")))
    print("laid out:", fit_site(r))
