#!/usr/bin/env python3
"""stzsite build -- one script turns content/<lang>/*.md into the static site.

Every page has a French and an English edition. Output is written next to the
sources (index.html, fr/*.html, en/*.html, deck-check.html) so that a clone of
the repository opens from file:// with no build step and GitHub Pages serves it
as it is. Run:  python tools/build.py
"""
import json, re, sys, html, datetime, pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
LANGS = ("fr", "en")

# ----------------------------------------------------------------------------
# strings the layout needs, per language
UI = {
  "fr": {
    "nav": [("why","Pourquoi"),("platform","Plateforme"),("learn","Apprendre"),("govern","Gouverner"),
            ("makers","Makers"),("products","Produits"),("africa","Afrique"),("start","Commencer"),("tour","Présenter")],
    "slogan": "La plateforme des makers à l'ère agentique",
    "second": "Née en Afrique. Utile au monde !",
    "skip": "Aller au contenu",
    "other_lang": "English", "other_code": "en",
    "theme": "Thème", "theme_light": "clair", "theme_dark": "sombre", "theme_auto": "auto",
    "proof_law": "Chaque affirmation de ce site renvoie au fichier, au garde ou au rendu qui la prouve. Chaque bloc de code a été exécuté le soir de la publication ; sa sortie est à côté.",
    "repos": "Dépôts",
    "prev": "Page précédente", "next": "Page suivante",
    "fonts": "Polices Fraunces, IBM Plex Sans et IBM Plex Mono, sous licence SIL OFL 1.1, hébergées sur ce site.",
    "built": "Site généré le",
  },
  "en": {
    "nav": [("why","Why"),("platform","Platform"),("learn","Learn"),("govern","Govern"),
            ("makers","Makers"),("products","Products"),("africa","Africa"),("start","Start"),("tour","Tour")],
    "slogan": "The Makers Platform of the Agentic Age",
    "second": "Born in Africa. Useful to the World!",
    "skip": "Skip to content",
    "other_lang": "Français", "other_code": "fr",
    "theme": "Theme", "theme_light": "light", "theme_dark": "dark", "theme_auto": "auto",
    "proof_law": "Every claim on this site links to the file, the guard or the render that proves it. Every code block was run on the night of publication; its output sits beside it.",
    "repos": "Repositories",
    "prev": "Previous page", "next": "Next page",
    "fonts": "Fraunces, IBM Plex Sans and IBM Plex Mono, under the SIL Open Font License 1.1, self-hosted on this site.",
    "built": "Site generated on",
  },
}

MD = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "md_in_html", "toc"],
                       extension_configs={"toc": {"permalink": False}})

def front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        block, text = text[3:end].strip(), text[end+4:]
        for line in block.splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    return meta, text

def md(text):
    MD.reset()
    return MD.convert(text)

THEME_SCRIPT = """<script>(function(){try{var q=new URLSearchParams(location.search).get('theme');var t=q||localStorage.getItem('stz-theme');if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();</script>"""

PAGE_PING = """<script>if(window.parent!==window){try{window.parent.postMessage({stzsite:'page',href:location.href},'*')}catch(e){}}</script>"""

def head(lang, title, description, rel, extra=""):
    return f"""<!doctype html>
<html lang="{lang}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" type="image/png" sizes="32x32" href="{rel}assets/img/mark-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{rel}assets/img/mark-64.png">
<link rel="apple-touch-icon" href="{rel}assets/img/mark-180.png">
<link rel="stylesheet" href="{rel}assets/css/fonts.css">
<link rel="stylesheet" href="{rel}assets/css/family.css">
<link rel="stylesheet" href="{rel}assets/css/site.css">
{extra}{THEME_SCRIPT}
</head>"""

def header(lang, slug, rel):
    ui = UI[lang]
    links = "".join(
        f'<a href="{s}.html"{" aria-current=page" if s == slug else ""}>{html.escape(l)}</a>'
        for s, l in ui["nav"])
    other = ui["other_code"]
    other_href = f"../{other}/{slug}.html"
    return f"""<a class="skip" href="#main">{ui["skip"]}</a>
<header class="site-head"><div class="wrap head-row">
  <a class="brand" href="{rel}index.html" aria-label="Softanza"><img src="{rel}assets/img/mark.png" alt="" width="34" height="29"><span>Softanza</span></a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span><span></span><span></span></button>
  <nav id="site-nav" class="site-nav">{links}</nav>
  <div class="head-tools">
    <a class="lang" href="{other_href}" lang="{other}" hreflang="{other}">{ui["other_lang"]}</a>
    <button class="theme-btn" type="button" data-theme-toggle aria-label="{ui["theme"]}" title="{ui["theme"]}: {ui["theme_light"]} / {ui["theme_dark"]} / {ui["theme_auto"]}"><span class="sun">&#9728;</span><span class="moon">&#9790;</span></button>
  </div>
</div></header>"""

def footer(lang, slug, rel, order):
    ui = UI[lang]
    slugs = [s for s, _ in order]
    i = slugs.index(slug) if slug in slugs else -1
    prev_html = next_html = ""
    if i > 0:
        s, l = order[i-1]; prev_html = f'<a class="pager prev" href="{s}.html"><small>{ui["prev"]}</small><b>{html.escape(l)}</b></a>'
    if 0 <= i < len(order) - 1:
        s, l = order[i+1]; next_html = f'<a class="pager next" href="{s}.html"><small>{ui["next"]}</small><b>{html.escape(l)}</b></a>'
    today = datetime.date.today().isoformat()
    return f"""<footer class="site-foot"><div class="wrap">
  <div class="pagers">{prev_html}{next_html}</div>
  <div class="foot-grid">
    <div><img src="{rel}assets/img/logo.png" alt="Softanza" class="foot-logo" width="200" height="137"><p class="foot-slogan">{html.escape(ui["slogan"])}<br>{html.escape(ui["second"])}</p></div>
    <div class="foot"><p>{html.escape(ui["proof_law"])}</p>
      <p class="mono small">{ui["repos"]}: <a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a> · <a href="https://codeberg.org/MAyouni/stzlib">codeberg.org/MAyouni/stzlib</a> · <a href="https://github.com/mayouni/harobanda">github.com/mayouni/harobanda</a> · <a href="https://github.com/mayouni/stzsite">github.com/mayouni/stzsite</a></p>
      <p class="small">{html.escape(ui["fonts"])} {ui["built"]} {today}.</p></div>
  </div>
</div></footer>
<script src="{rel}assets/js/site.js"></script>{PAGE_PING}
</body></html>"""

def build_page(lang, slug, order):
    src = CONTENT / lang / f"{slug}.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    title = meta.get("title", slug)
    rel = "../"
    body_html = md(body)
    page = head(lang, f'{title} · Softanza', meta.get("description", ""), rel)
    page += f'\n<body class="page page-{slug}">\n' + header(lang, slug, rel)
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{html.escape(meta.get("kicker", ""))}</div>
    <h1>{meta.get("title_html", html.escape(title))}</h1>
    <p class="thesis">{meta.get("lede", "")}</p>
  </div></section>
  <div class="wrap page-body">
{body_html}
  </div>
</main>
"""
    page += footer(lang, slug, rel, order)
    out = ROOT / lang / f"{slug}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

# ----------------------------------------------------------------------------
# the tour: scenes separated by <<< scene ... >>> lines, notes in ```notes fences
SCENE_RX = re.compile(r'^<<<\s*scene\s+(.*?)\s*>>>\s*$', re.M)
ATTR_RX = re.compile(r'(\w+)="([^"]*)"')
NOTES_RX = re.compile(r'```notes\n(.*?)\n```', re.S)

def build_tour(lang, order):
    src = CONTENT / lang / "tour.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    parts = SCENE_RX.split(body)
    scenes = []
    for i in range(1, len(parts), 2):
        attrs = dict(ATTR_RX.findall(parts[i])); text = parts[i+1]
        m = NOTES_RX.search(text); notes = m.group(1).strip() if m else ""
        text = NOTES_RX.sub("", text)
        scenes.append((attrs, md(text), md(notes) if notes else ""))
    ui = UI[lang]
    rel = "../"
    n = len(scenes)
    secs = []
    for k, (attrs, body_html, notes_html) in enumerate(scenes, 1):
        cls = attrs.get("class", "")
        page = attrs.get("page", "")
        page_link = f'<a class="scene-page" href="{page}">{html.escape(attrs.get("label", page))}</a>' if page else ""
        notes_block = f'<aside class="notes"><div class="notes-inner"><div class="eyebrow">Notes</div>{notes_html}</div></aside>' if notes_html else ''
        secs.append(f"""<section class="scene {cls}" id="s{k}" data-index="{k}" aria-label="{k}/{n}">
  <div class="scene-inner">{body_html}</div>
  {notes_block}
  <div class="scene-foot">{page_link}<span class="scene-count mono">{k} / {n}</span></div>
</section>""")
    title = meta.get("title", "Tour")
    page_html = head(lang, f'{title} · Softanza', meta.get("description", ""), rel)
    page_html += '\n<body class="page page-tour tour-mode">\n' + header(lang, "tour", rel)
    page_html += f"""
<main id="main" class="deck" data-count="{n}">
{chr(10).join(secs)}
</main>
<div class="progress" aria-hidden="true"><div class="bar"></div></div>
<div class="deck-help mono">{meta.get("help", "")}</div>
<script src="{rel}assets/js/site.js"></script>
<script src="{rel}assets/js/tour.js"></script>{PAGE_PING}
</body></html>"""
    out = ROOT / lang / "tour.html"
    out.write_text(page_html, encoding="utf-8")
    return out, [a for a, _, _ in scenes]

# ----------------------------------------------------------------------------
def build_home():
    """The onboarding scene: one page, both languages inside, JS picks."""
    body = (CONTENT / "home.html").read_text(encoding="utf-8")
    page = head("fr", "Softanza · La plateforme des makers à l'ère agentique · The Makers Platform of the Agentic Age",
                "Softanza: declare a language for your world, run it on one engine, let agents speak it safely. Born in Africa. Useful to the World.", "")
    page = page.replace('<html lang="fr" data-lang="fr">', '<html lang="fr" data-lang="fr" class="home">')
    page += "\n<body class=\"home-body\">\n" + body + f"""
<script src="assets/js/site.js"></script>{PAGE_PING}
</body></html>"""
    (ROOT / "index.html").write_text(page, encoding="utf-8")

def build_deck_check(assets):
    items = json.dumps(assets, ensure_ascii=False, indent=1)
    src = (CONTENT / "deck-check.html").read_text(encoding="utf-8")
    (ROOT / "deck-check.html").write_text(src.replace("/*ASSETS*/[]", items), encoding="utf-8")

# ----------------------------------------------------------------------------
def hex_to_lum(h):
    h = h.lstrip("#"); r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4))
    f = lambda c: c/12.92 if c <= 0.03928 else ((c+0.055)/1.055) ** 2.4
    return 0.2126*f(r) + 0.7152*f(g) + 0.0722*f(b)

def contrast(a, b):
    la, lb = hex_to_lum(a), hex_to_lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

def check_contrast():
    """Measured, not eyeballed: the token pairs the site paints text with,
    declared in site.css as  /* contrast: fg | bg | minimum | label */ ."""
    css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
    pairs = re.findall(r'/\*\s*contrast:\s*([^*]+?)\s*\*/', css)
    ok = True
    for spec in pairs:
        fg, bg, need, label = [s.strip() for s in spec.split("|")]
        c = contrast(fg, bg)
        flag = "ok " if c >= float(need) else "LOW"
        if c < float(need): ok = False
        print(f"  contrast {flag} {c:5.2f} >= {need}  {label} ({fg} on {bg})")
    return ok

def main():
    order = {lang: UI[lang]["nav"] for lang in LANGS}
    outs = []
    for lang in LANGS:
        for slug, _ in order[lang]:
            if slug == "tour": continue
            outs.append(build_page(lang, slug, order[lang]))
    scenes = {}
    for lang in LANGS:
        out, sc = build_tour(lang, order[lang]); outs.append(out); scenes[lang] = sc
    build_home()
    # every asset the tour needs, for deck-check.html
    assets = []
    for f in sorted((ROOT / "assets/fonts").glob("*.woff2")):
        assets.append({"kind": "font", "path": f"assets/fonts/{f.name}"})
    for f in sorted((ROOT / "assets/img").glob("*")):
        if f.suffix.lower() in (".png", ".webp", ".jpg", ".svg"):
            assets.append({"kind": "image", "path": f"assets/img/{f.name}"})
    for f in ("fonts.css", "family.css", "site.css"):
        assets.append({"kind": "css", "path": f"assets/css/{f}"})
    for f in ("site.js", "tour.js"):
        assets.append({"kind": "script", "path": f"assets/js/{f}"})
    assets.append({"kind": "page", "path": "index.html"})
    for lang in LANGS:
        for slug, _ in order[lang]:
            assets.append({"kind": "page", "path": f"{lang}/{slug}.html"})
    reader = ROOT / "reader.html"
    if reader.exists():
        # the reader is built by the library's build_reader.ring; the one line the
        # offline check listens for is appended to this copy, never to the tool
        r = reader.read_text(encoding="utf-8")
        if "stzsite:'page'" not in r:
            reader.write_text(r.replace("</body>", PAGE_PING + "</body>", 1), encoding="utf-8")
        assets.append({"kind": "page", "path": "reader.html"})
    build_deck_check(assets)
    print(f"built {len(outs)} pages + index.html + deck-check.html; tour scenes fr={len(scenes['fr'])} en={len(scenes['en'])}")
    print("contrast:")
    if not check_contrast():
        print("CONTRAST BELOW TARGET"); sys.exit(1)

if __name__ == "__main__":
    main()
