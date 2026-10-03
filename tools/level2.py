"""The second submenu: the pages of the level the reader is in, in a bar on the left.

The site has three menu levels and never more (the author's rule, 2026-10-02): the
main menu, the section's path under it, and this bar. A page that sits one level
below a page of the path shows here the pages beside it -- the 28 areas, the 28
guides, the narrations run as pages, the classes of one area, the letters of the
method index -- so the reader can go back and forth in that level. A method entry
is a page of its class, not a fourth level: it shows its class's bar, with the
class marked as where the reader is.

On a wide screen the bar is a column on the left that stays in view; on a narrow
one it becomes a row above the page that scrolls sideways, as the path does.
"""
import html

def esc(s): return html.escape(str(s), quote=True)

def nav(label, groups):
    """groups: [(heading or "", [(href, text, state)])], state "page" for this page,
    "location" for the page this one belongs to, "" otherwise"""
    parts = []
    for heading, items in groups:
        lis = "".join(f'<li><a href="{esc(h)}"{f" aria-current={state}" if state else ""}>{esc(t)}</a></li>'
                      for h, t, state in items)
        head = f'<p class="l2-h">{esc(heading)}</p>' if heading else ""
        parts.append(f'<div class="l2-group">{head}<ul>{lis}</ul></div>')
    return f'<nav class="level2" aria-label="{esc(label)}"><div class="l2-in">{"".join(parts)}</div></nav>'

def wrap(page, nav_html):
    """put the bar beside the page's <main>"""
    assert page.count('<main id="main"') == 1 and page.count("</main>") == 1, "one main per page"
    page = page.replace('<main id="main"', '<div class="l2wrap">\n' + nav_html + '\n<main id="main"', 1)
    page = page.replace("</main>", "</main>\n</div>", 1)
    return page.replace('<body class="page ', '<body class="page has-l2 ', 1)

LABELS = {
    "areas":      {"fr": "Les domaines", "en": "The areas"},
    "guides":     {"fr": "Les guides des domaines", "en": "The area guides"},
    "narrations": {"fr": "Les narrations exécutées", "en": "The narrations run"},
    "classes":    {"fr": "Les classes du domaine", "en": "The area's classes"},
    "letters":    {"fr": "Les méthodes de A à Z", "en": "Methods from A to Z"},
    "chapters":   {"fr": "Les chapitres du livre", "en": "The chapters of the book"},
}

def area_groups(idx, lang, current, href=lambda slug: f"{slug}.html"):
    """the 28 areas under their six bands, in the Atlas's order"""
    out = []
    for b in idx["bands"]:
        items = [(href(g["slug"]), g[lang], "page" if g["slug"] == current else "")
                 for g in idx["groups"] if g["band"] == b["id"]]
        if items: out.append((b[lang], items))
    return out
