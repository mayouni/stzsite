"""External links: a small mark, and a new tab.

The author, 2026-10-03: a link that points to another site (GitHub, for example) carries a small symbol so the
reader knows it leaves the site, and opens in a new tab, never in the tab of the site.

Run after every page is written. It touches each <a href="http(s)://..."> of the pages of the site:

  - target="_blank" and rel="noopener noreferrer" on every one (an icon link too);
  - a link made of words gets, after them, an arrow that draws itself in the link's own colour (a mask, no image, no
    glyph the font may lack) and, for a reader who cannot see it, the words "(opens in a new tab)" in the page's language;
  - a link that wraps a card, an image or a heading gets the new tab and no arrow: the arrow belongs to words;
  - a link to the site itself is left alone, and a link already marked is not marked twice (the pass is idempotent).
"""
import re, pathlib

A = re.compile(r'<a\b([^>]*?\bhref="(https?://[^"]*)"[^>]*)>(.*?)</a>', re.S)
BLOCK = re.compile(r"<(?:div|p|h[1-6]|img|svg|figure|ul|ol|pre|table)\b")
LANG = re.compile(r'<html[^>]*\blang="(\w+)"')
NOTE = {"en": "(opens in a new tab)", "fr": "(s'ouvre dans un nouvel onglet)"}
SELF = "mayouni.github.io/stzsite"

def mark(page):
    m = LANG.search(page)
    lang = m.group(1) if m else "en"
    note = NOTE.get(lang, NOTE["en"])
    def one(m):
        attrs, url, inner = m.group(1), m.group(2), m.group(3)
        if SELF in url or "target=" in attrs: return m.group(0)
        attrs = attrs + ' target="_blank" rel="noopener noreferrer"'
        if BLOCK.search(inner): return f"<a{attrs}>{inner}</a>"
        return f'<a{attrs}>{inner}<span class="ext" aria-hidden="true"></span><span class="sr">{note}</span></a>'
    return A.sub(one, page)

STATS = {"pages": 0, "links": 0}

def install(root):
    """Mark every page of the site as the build writes it, so no page is read a second time (reading the 4,000 pages of the site
    again cost four minutes where the whole build costs fifteen seconds). Path.write_text is wrapped for the html files of en/, fr/ and
    the home page; reader.html, which is a program, and everything else are written as they are."""
    root = pathlib.Path(root).resolve()
    original = pathlib.Path.write_text
    def write_text(self, data, *args, **kw):
        if self.suffix == ".html" and isinstance(data, str):
            try: rel = self.resolve().relative_to(root).parts
            except ValueError: rel = ()
            if rel and (rel[0] in ("en", "fr") or rel == ("index.html",)):
                marked = mark(data)
                if marked != data:
                    STATS["pages"] += 1; STATS["links"] += marked.count('target="_blank"') - data.count('target="_blank"')
                data = marked
        return original(self, data, *args, **kw)
    pathlib.Path.write_text = write_text
    return STATS
