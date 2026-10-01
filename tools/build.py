#!/usr/bin/env python3
"""stzsite build -- one script turns content/<lang>/*.md and data/ into the static site.

Every page has a French and an English edition. Output is written next to the
sources (index.html, fr/*.html, en/*.html, fr/atlas/*.html, en/atlas/*.html,
deck-check.html) so that a clone of the repository opens from file:// with no
build step and GitHub Pages serves it as it is.   Run:  python tools/build.py
"""
import json, re, sys, html, datetime, pathlib
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DATA = ROOT / "data"
LANGS = ("fr", "en")
GH = "https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/"

# ----------------------------------------------------------------------------
# strings the layout needs, per language
UI = {
  "fr": {
    "nav": [("why","Pourquoi"),("platform","Plateforme"),("atlas","Atlas"),("learn","Apprendre"),("govern","Gouverner"),
            ("makers","Makers"),("products","Produits"),("africa","Afrique"),("start","Démarrer"),("tour","Présenter")],
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
    "atlas_kicker": "L'Atlas Softanza", "atlas_title": "Où se tient <i>toute la plateforme</i>",
    "atlas_lede": "Vingt-huit groupes, 334 couloirs, chacun noté contre les meilleurs de sa catégorie. Le pari de Softanza est la cohérence de nombreux couloirs sous un seul moteur gouverné : aucun concurrent ne les couvre tous. Les notes sont gagnées par ce que les gardes prouvent, lues sur la branche principale, et les lacunes sont montrées.",
    "atlas_desc": "L'Atlas Softanza : 28 groupes de modules et 334 couloirs notés Strong, Solid, Partial ou Emerging contre les meilleurs de chaque catégorie.",
    "lanes": "couloirs", "strong": "Strong", "solid": "Solid", "partial": "Partial", "emerging": "Emerging",
    "measured": "Mesuré contre", "folders": "Dossiers", "standouts": "Ce qui se distingue", "gaps": "Ce qui est dû",
    "lanes_h": "Les couloirs, un par un", "lanes_note": "Les couloirs et leurs notes sont cités dans la langue de l'Atlas, l'anglais, tels qu'ils ont été lus à la source.",
    "example": "Un exemple, exécuté", "no_example": "Aucun exemple exécuté sur cette page",
    "atlas_page": "La page d'origine de l'Atlas", "all_groups": "Tous les groupes",
    "read_on": "lu à la source le", "legend": "Légende",
    "legend_text": "Strong : au niveau ou au-dessus du meilleur de la catégorie · Solid : complet et prouvé, un cran derrière · Partial : présent, incomplet · Emerging : prévu ou tout juste commencé.",
    "tally_label": "Les 334 couloirs", "groups_word": "groupes",
  },
  "en": {
    "nav": [("why","Why"),("platform","Platform"),("atlas","Atlas"),("learn","Learn"),("govern","Govern"),
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
    "atlas_kicker": "The Softanza Atlas", "atlas_title": "Where <i>the whole platform</i> stands",
    "atlas_lede": "Twenty-eight groups, 334 lanes, each rated against the leaders of its category. The bet Softanza makes everywhere is coherence across many lanes under one governed engine: no single competitor spans them all. Ratings are earned by what the guards prove, read from the main branch, and the gaps are shown.",
    "atlas_desc": "The Softanza Atlas: 28 module groups and 334 lanes rated Strong, Solid, Partial or Emerging against the leaders of each category.",
    "lanes": "lanes", "strong": "Strong", "solid": "Solid", "partial": "Partial", "emerging": "Emerging",
    "measured": "Measured against", "folders": "Folders", "standouts": "What stands out", "gaps": "What is owed",
    "lanes_h": "The lanes, one by one", "lanes_note": "Lanes and their notes are quoted as they were read at the source.",
    "example": "One example, run", "no_example": "No example run on this page",
    "atlas_page": "The original Atlas page", "all_groups": "All groups",
    "read_on": "read from the source on", "legend": "Legend",
    "legend_text": "Strong: at or above the category leader · Solid: complete and proven, a step behind · Partial: present, incomplete · Emerging: planned or barely begun.",
    "tally_label": "All 334 lanes", "groups_word": "groups",
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

def esc(s): return html.escape(str(s), quote=True)

THEME_SCRIPT = """<script>(function(){try{var q=new URLSearchParams(location.search).get('theme');var t=q||localStorage.getItem('stz-theme');if(t==='light'||t==='dark'){document.documentElement.setAttribute('data-theme',t);}}catch(e){}})();</script>"""

PAGE_PING = """<script>if(window.parent!==window){try{window.parent.postMessage({stzsite:'page',href:location.href},'*')}catch(e){}}</script>"""

def head(lang, title, description, rel, extra=""):
    return f"""<!doctype html>
<html lang="{lang}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" type="image/png" sizes="32x32" href="{rel}assets/img/mark-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{rel}assets/img/mark-64.png">
<link rel="apple-touch-icon" href="{rel}assets/img/mark-180.png">
<link rel="stylesheet" href="{rel}assets/css/fonts.css">
<link rel="stylesheet" href="{rel}assets/css/family.css">
<link rel="stylesheet" href="{rel}assets/css/site.css">
{extra}{THEME_SCRIPT}
</head>"""

def header(lang, slug, rel, other_href=None, nav_rel=""):
    ui = UI[lang]
    links = "".join(
        f'<a href="{nav_rel}{s}.html"{" aria-current=page" if s == slug else ""}>{esc(l)}</a>'
        for s, l in ui["nav"])
    other = ui["other_code"]
    if other_href is None: other_href = f"../{other}/{slug}.html"
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

def footer(lang, rel, pagers_html=""):
    ui = UI[lang]
    today = datetime.date.today().isoformat()
    return f"""<footer class="site-foot"><div class="wrap">
  <div class="pagers">{pagers_html}</div>
  <div class="foot-grid">
    <div><img src="{rel}assets/img/logo.png" alt="Softanza" class="foot-logo" width="200" height="137"><p class="foot-slogan">{esc(ui["slogan"])}<br>{esc(ui["second"])}</p></div>
    <div class="foot"><p>{esc(ui["proof_law"])}</p>
      <p class="mono small">{ui["repos"]}: <a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a> · <a href="https://codeberg.org/MAyouni/stzlib">codeberg.org/MAyouni/stzlib</a> · <a href="https://github.com/mayouni/harobanda">github.com/mayouni/harobanda</a> · <a href="https://github.com/mayouni/stzsite">github.com/mayouni/stzsite</a></p>
      <p class="small">{esc(ui["fonts"])} {ui["built"]} {today}.</p></div>
  </div>
</div></footer>
<script src="{rel}assets/js/site.js"></script>{PAGE_PING}
</body></html>"""

def pagers(lang, slug, order):
    ui = UI[lang]
    slugs = [s for s, _ in order]
    i = slugs.index(slug) if slug in slugs else -1
    prev_html = next_html = ""
    if i > 0:
        s, l = order[i-1]; prev_html = f'<a class="pager prev" href="{s}.html"><small>{ui["prev"]}</small><b>{esc(l)}</b></a>'
    if 0 <= i < len(order) - 1:
        s, l = order[i+1]; next_html = f'<a class="pager next" href="{s}.html"><small>{ui["next"]}</small><b>{esc(l)}</b></a>'
    return prev_html + next_html

# ----------------------------------------------------------------------------
# the Atlas data
def load_atlas():
    idx = json.loads((DATA / "atlas-index.json").read_text(encoding="utf-8"))
    runs_file = DATA / "atlas-runs.json"
    runs = json.loads(runs_file.read_text(encoding="utf-8")) if runs_file.exists() else {}
    groups = []
    for g in idx["groups"]:
        f = DATA / "atlas" / f"{g['slug']}.json"
        d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
        # the extractors wrote a replacement character where the pages had a dash
        for l in d.get("lanes", []):
            for k in ("lane", "note", "proof"): l[k] = l.get(k, "").replace("�", "-")
        d["thesis"] = d.get("thesis", "").replace("�", "-")
        d["standouts"] = [s.replace("�", "-") for s in d.get("standouts", [])]
        d["gaps"] = [s.replace("�", "-") for s in d.get("gaps", [])]
        groups.append({**g, "detail": d, "run": runs.get(g["slug"])})
    return idx, groups

def bar(s, so, p, e, cls="cardbar"):
    parts = []
    for n, var in ((s, "strong"), (so, "solid"), (p, "partial"), (e, "emerging")):
        if n: parts.append(f'<span style="flex:{n};background:var(--{var})"></span>')
    return f'<div class="{cls}" role="img" aria-label="{s} strong, {so} solid, {p} partial, {e} emerging">{"".join(parts)}</div>'

def counts(s, so, p, e):
    out = []
    for n, var, ab in ((s, "strong", "S"), (so, "solid", "So"), (p, "partial", "P"), (e, "emerging", "E")):
        if n: out.append(f'<span class="st-{var}"><b>{n}</b> {ab}</span>')
    return f'<div class="counts">{"".join(out)}</div>'

def tally_html(lang, idx):
    t = idx["tally"]; ui = UI[lang]
    return (f'<div class="tally" aria-label="{ui["tally_label"]}">{bar(t["strong"], t["solid"], t["partial"], t["emerging"], "tallybar")}'
            f'<div class="legend"><span class="k"><span class="dot" style="background:var(--strong)"></span>{t["strong"]} {ui["strong"]}</span>'
            f'<span class="k"><span class="dot" style="background:var(--solid)"></span>{t["solid"]} {ui["solid"]}</span>'
            f'<span class="k"><span class="dot" style="background:var(--partial)"></span>{t["partial"]} {ui["partial"]}</span>'
            f'<span class="k"><span class="dot" style="background:var(--emerging)"></span>{t["emerging"]} {ui["emerging"]}</span></div></div>')

def compact_html(lang, idx, groups, rel_atlas):
    """name + bar per group, banded; links into the group pages"""
    out = []
    for b in idx["bands"]:
        gs = [g for g in groups if g["band"] == b["id"]]
        items = "".join(
            f'<a class="abar" href="{rel_atlas}{g["slug"]}.html"><div class="n"><span>{esc(g[lang])}</span><small>{g["s"]+g["so"]+g["p"]+g["e"]}</small></div>{bar(g["s"], g["so"], g["p"], g["e"])}</a>'
            for g in gs)
        out.append(f'<div class="band-compact"><div class="band-h">{esc(b[lang])}</div><div class="atlas-compact">{items}</div></div>')
    return "".join(out)

def cards_html(lang, idx, groups, rel_atlas):
    out = []
    for b in idx["bands"]:
        gs = [g for g in groups if g["band"] == b["id"]]
        items = "".join(
            f'<a class="acard" href="{rel_atlas}{g["slug"]}.html"><div class="t"><span>{esc(g[lang])}</span><span class="arrow">&#8599;</span></div>'
            f'<p>{esc(g["line_" + lang])}</p>{bar(g["s"], g["so"], g["p"], g["e"])}{counts(g["s"], g["so"], g["p"], g["e"])}'
            f'<div class="dirs">{esc(g["dirs"])} · vs {esc(g["peers"])}</div></a>'
            for g in gs)
        out.append(f'<div class="band"><div class="band-h">{esc(b[lang])}</div><div class="atlas-grid">{items}</div></div>')
    return "".join(out)

def build_atlas_index(lang, idx, groups, order):
    ui = UI[lang]; rel = "../"
    page = head(lang, 'Atlas · Softanza', ui["atlas_desc"], rel)
    page += '\n<body class="page page-atlas">\n' + header(lang, "atlas", rel)
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{ui["atlas_kicker"]}</div>
    <h1>{ui["atlas_title"]}</h1>
    <p class="thesis">{esc(ui["atlas_lede"])}</p>
    {tally_html(lang, idx)}
    <p class="proof">{idx["tally"]["groups"]} {ui["groups_word"]} · {idx["tally"]["lanes"]} {ui["lanes"]} · Atlas v{idx["version"]} · {ui["read_on"]} {idx["read_at"]}, <a href="https://github.com/mayouni/stzlib/commit/{idx["commit"]}">{idx["commit"]}</a> · <a href="{idx["index_url"]}">{ui["atlas_page"]}</a></p>
  </div></section>
  <div class="wrap page-body">
    {cards_html(lang, idx, groups, "atlas/")}
    <div class="note"><p><b>{ui["legend"]}.</b> {esc(ui["legend_text"])}</p></div>
  </div>
</main>
"""
    page += footer(lang, rel, pagers(lang, "atlas", order))
    (ROOT / lang / "atlas.html").write_text(page, encoding="utf-8")

RATING_CLASS = {"Strong": "strong", "Solid": "solid", "Partial": "partial", "Emerging": "emerging"}

def build_group_page(lang, idx, groups, i):
    g = groups[i]; d = g["detail"]; ui = UI[lang]; rel = "../../"
    band = next(b for b in idx["bands"] if b["id"] == g["band"])
    lanes = "".join(
        f'<div class="lane"><div class="ln">{esc(l["lane"])}</div><div class="lr"><span class="chip {RATING_CLASS.get(l["rating"], "solid")}">{esc(l["rating"])}</span></div>'
        f'<div class="lt">{esc(l["note"])}{("<small>" + esc(l["proof"]) + "</small>") if l.get("proof") else ""}</div></div>'
        for l in d.get("lanes", []))
    folders = " · ".join(f'<a href="{GH}base/{f.strip()}">base/{esc(f.strip())}</a>' for f in g["dirs"].split(","))
    sg = ""
    if d.get("standouts") or d.get("gaps"):
        sg = (f'<div class="sg"><div class="good"><h4>{ui["standouts"]}</h4><ul>{"".join(f"<li>{esc(s)}</li>" for s in d.get("standouts", []))}</ul></div>'
              f'<div class="owed"><h4>{ui["gaps"]}</h4><ul>{"".join(f"<li>{esc(s)}</li>" for s in d.get("gaps", []))}</ul></div></div>')
    # the example run
    run = g.get("run") or {}
    out_lbl = "Sortie" if lang == "fr" else "Output"
    if run.get("code"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p>'
                   f'<div class="run"><div><div class="lbl">Ring</div><pre>{esc(run["code"])}</pre></div><div class="out"><div class="lbl">{out_lbl}</div><pre>{esc(run["out"])}</pre></div></div>'
                   f'<p class="ran">{esc(run.get("ran_" + lang, ""))}</p>')
    elif run.get("image"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p>'
                   f'<figure><img src="{rel}assets/img/{run["image"]}" alt="{esc(run.get("alt_" + lang, ""))}"><figcaption>{esc(run.get("ran_" + lang, ""))}</figcaption></figure>')
    elif run.get("text"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p><pre>{esc(run["text"])}</pre>'
                   f'<p class="ran">{esc(run.get("ran_" + lang, ""))}</p>')
    else:
        example = f'<div class="note warn"><p><b>{ui["no_example"]}.</b> {esc(run.get("why_" + lang, ""))}</p></div>'
    # the two readings, when the group page and the Atlas card disagree
    c = {"Strong": 0, "Solid": 0, "Partial": 0, "Emerging": 0}
    for l in d.get("lanes", []): c[l["rating"]] = c.get(l["rating"], 0) + 1
    note = ""
    if d.get("lanes") and (c["Strong"], c["Solid"], c["Partial"], c["Emerging"]) != (g["s"], g["so"], g["p"], g["e"]):
        if lang == "fr":
            note = (f'<div class="note warn"><p><b>Deux lectures.</b> La carte de l\'Atlas (v{idx["version"]}, {idx["read_at"]}) donne {g["s"]} Strong / {g["so"]} Solid / {g["p"]} Partial / {g["e"]} Emerging ; '
                    f'la page du groupe, lue le {esc(d.get("dated", ""))}, note ses couloirs {c["Strong"]} / {c["Solid"]} / {c["Partial"]} / {c["Emerging"]}. Les couloirs ci-dessous sont ceux de la page du groupe ; la carte est la lecture la plus récente.</p></div>')
        else:
            note = (f'<div class="note warn"><p><b>Two readings.</b> The Atlas card (v{idx["version"]}, {idx["read_at"]}) says {g["s"]} Strong / {g["so"]} Solid / {g["p"]} Partial / {g["e"]} Emerging; '
                    f'the group page, read {esc(d.get("dated", ""))}, rates its lanes {c["Strong"]} / {c["Solid"]} / {c["Partial"]} / {c["Emerging"]}. The lanes below are the group page\'s; the card is the more recent reading.</p></div>')
    prev_g = groups[i-1] if i > 0 else None
    next_g = groups[i+1] if i < len(groups) - 1 else None
    prev_a = f'<a href="{prev_g["slug"]}.html">&larr; {esc(prev_g[lang])}</a>' if prev_g else "<span></span>"
    next_a = f'<a href="{next_g["slug"]}.html">{esc(next_g[lang])} &rarr;</a>' if next_g else "<span></span>"
    nav = f'<div class="group-nav">{prev_a}<a href="../atlas.html">{ui["all_groups"]}</a>{next_a}</div>'
    title = g[lang]
    page = head(lang, f'{title} · Atlas · Softanza', g["line_" + lang], rel)
    page += '\n<body class="page page-atlas-group">\n' + header(lang, "atlas", rel, other_href=f"../../{ui['other_code']}/atlas/{g['slug']}.html", nav_rel="../")
    thesis = f'<blockquote><p>{esc(d["thesis"])}</p></blockquote>' if d.get("thesis") else ""
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{ui["atlas_kicker"]} · {esc(band[lang])}</div>
    <h1>{esc(title)}</h1>
    <p class="thesis">{esc(g["line_" + lang])}</p>
    <div class="tally">{bar(g["s"], g["so"], g["p"], g["e"], "tallybar")}{counts(g["s"], g["so"], g["p"], g["e"])}</div>
    <p class="proof">{ui["measured"]}: {esc(g["peers"])} · {ui["folders"]}: {folders} · <a href="{g["url"]}">{ui["atlas_page"]}</a></p>
  </div></section>
  <div class="wrap page-body">
    {thesis}
    {sg}
    {example}
    <h2>{ui["lanes_h"]}</h2>
    <p class="proof">{ui["lanes_note"]} {ui["read_on"]} {esc(d.get("dated", ""))}.</p>
    {note}
    <div class="lanes">{lanes}</div>
    {nav}
  </div>
</main>
"""
    page += footer(lang, rel, "")
    out = ROOT / lang / "atlas" / f"{g['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

def inject_atlas(body_html, lang, idx, groups, rel_atlas):
    body_html = body_html.replace("<!--ATLAS-TALLY-->", tally_html(lang, idx))
    body_html = body_html.replace("<!--ATLAS-COMPACT-->", compact_html(lang, idx, groups, rel_atlas))
    return body_html

# ----------------------------------------------------------------------------
def build_page(lang, slug, order, idx, groups):
    src = CONTENT / lang / f"{slug}.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    title = meta.get("title", slug)
    rel = "../"
    body_html = inject_atlas(md(body), lang, idx, groups, "atlas/")
    page = head(lang, f'{title} · Softanza', meta.get("description", ""), rel)
    page += f'\n<body class="page page-{slug}">\n' + header(lang, slug, rel)
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(meta.get("kicker", ""))}</div>
    <h1>{meta.get("title_html", esc(title))}</h1>
    <p class="thesis">{meta.get("lede", "")}</p>
  </div></section>
  <div class="wrap page-body">
{body_html}
  </div>
</main>
"""
    page += footer(lang, rel, pagers(lang, slug, order))
    out = ROOT / lang / f"{slug}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

# ----------------------------------------------------------------------------
# the tour: scenes separated by <<< scene ... >>> lines, notes in ```notes fences
SCENE_RX = re.compile(r'^<<<\s*scene\s+(.*?)\s*>>>\s*$', re.M)
ATTR_RX = re.compile(r'(\w+)="([^"]*)"')
NOTES_RX = re.compile(r'```notes\n(.*?)\n```', re.S)

def build_tour(lang, order, idx, groups):
    src = CONTENT / lang / "tour.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    parts = SCENE_RX.split(body)
    scenes = []
    for i in range(1, len(parts), 2):
        attrs = dict(ATTR_RX.findall(parts[i])); text = parts[i+1]
        m = NOTES_RX.search(text); notes = m.group(1).strip() if m else ""
        text = NOTES_RX.sub("", text)
        scenes.append((attrs, inject_atlas(md(text), lang, idx, groups, "atlas/"), md(notes) if notes else ""))
    rel = "../"
    n = len(scenes)
    secs = []
    for k, (attrs, body_html, notes_html) in enumerate(scenes, 1):
        cls = attrs.get("class", "")
        page = attrs.get("page", "")
        page_link = f'<a class="scene-page" href="{page}">{esc(attrs.get("label", page))}</a>' if page else ""
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
def build_home(idx, groups):
    """The onboarding scene: one page, both languages inside, JS picks."""
    body = (CONTENT / "home.html").read_text(encoding="utf-8")
    for lang in LANGS:
        body = body.replace(f"<!--ATLAS-TALLY-{lang.upper()}-->", tally_html(lang, idx))
        body = body.replace(f"<!--ATLAS-COMPACT-{lang.upper()}-->", compact_html(lang, idx, groups, f"{lang}/atlas/"))
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
    idx, groups = load_atlas()
    order = {lang: UI[lang]["nav"] for lang in LANGS}
    outs = []
    for lang in LANGS:
        for slug, _ in order[lang]:
            if slug in ("tour", "atlas"): continue
            outs.append(build_page(lang, slug, order[lang], idx, groups))
        build_atlas_index(lang, idx, groups, order[lang])
        for i in range(len(groups)):
            build_group_page(lang, idx, groups, i)
    scenes = {}
    for lang in LANGS:
        out, sc = build_tour(lang, order[lang], idx, groups); outs.append(out); scenes[lang] = sc
    build_home(idx, groups)
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
    nrun = sum(1 for g in groups if g.get("run") and (g["run"].get("code") or g["run"].get("image") or g["run"].get("text")))
    print(f"built {len(outs)} pages + {2*len(groups)} group pages + 2 atlas indexes + index.html + deck-check.html; "
          f"tour scenes fr={len(scenes['fr'])} en={len(scenes['en'])}; groups with a run example: {nrun}/{len(groups)}")
    print("contrast:")
    if not check_contrast():
        print("CONTRAST BELOW TARGET"); sys.exit(1)

if __name__ == "__main__":
    main()
