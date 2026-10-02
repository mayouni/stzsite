#!/usr/bin/env python3
"""stzsite build -- one script turns content/<lang>/*.md and data/ into the static site.

Every page has a French and an English edition. Output is written next to the
sources (index.html, fr/*.html, en/*.html, fr/atlas/*.html, ...) so that a clone
of the repository opens from file:// with no build step and GitHub Pages serves
it as it is.   Run:  python tools/build.py

The structure is the Zui constitution's (v3.11): a main menu of six sections
(Rule 27), and under it the PATH of the current section, every page of it shown,
the current one marked (Rules 108, 115, 116). Both stay on screen while the page
scrolls (Rule 13). Inside a page there is no menu of anchors: a page is read top
to bottom (Rule 12), and it carries no links that pull the reader elsewhere
except the ones that belong to what they are reading.
"""
import json, re, sys, html, datetime, pathlib
import markdown
from PIL import Image
from build_reference import build_reference
from build_guides import build_guides

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DATA = ROOT / "data"
LANGS = ("fr", "en")
GH = "https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/"

# ----------------------------------------------------------------------------
# the tree: six sections, each with its pages; the first page is the landing
SECTIONS = [
  ("platform", {"fr": "Plateforme", "en": "Platform"}, [
     ("platform", {"fr": "Plateforme", "en": "Platform"}),
     ("platforms", {"fr": "Plateforme de plateformes", "en": "Platform of platforms"}),
     ("areas", {"fr": "Les domaines", "en": "The areas"}),
     ("atlas", {"fr": "L'Atlas", "en": "The Atlas"}),
     ("code", {"fr": "Le code", "en": "The code"}),
     ("compare", {"fr": "Comparée", "en": "Compared"})]),
  ("vision", {"fr": "Vision", "en": "Vision"}, [
     ("vision", {"fr": "L'étoile polaire", "en": "The north star"}),
     ("principles", {"fr": "Douze principes", "en": "Twelve principles"}),
     ("estate", {"fr": "Le domaine", "en": "The estate"}),
     ("history", {"fr": "Depuis les principes", "en": "From first principles"}),
     ("sovereignty", {"fr": "Souveraineté", "en": "Sovereignty"}),
     ("africa", {"fr": "Née en Afrique", "en": "Born in Africa"})]),
  ("agentic", {"fr": "Agentique", "en": "Agentic"}, [
     ("agentic", {"fr": "Agentique", "en": "Agentic"}),
     ("wise", {"fr": "Wise coding", "en": "Wise coding"}),
     ("languages", {"fr": "Langue des langues", "en": "Language of languages"}),
     ("zui", {"fr": "Zui", "en": "Zui"}),
     ("refinement", {"fr": "Raffinement", "en": "Refinement"}),
     ("agents", {"fr": "Pour les agents", "en": "For agents"}),
     ("coding-agents", {"fr": "Agents qui codent", "en": "Coding agents"}),
     ("security", {"fr": "Sécurité", "en": "Security"})]),
  ("learn", {"fr": "Apprendre", "en": "Learn"}, [
     ("learn", {"fr": "Apprendre", "en": "Learn"}),
     ("book", {"fr": "Le livre", "en": "The book"}),
     ("docs", {"fr": "Documentation", "en": "Documentation"}),
     ("reference", {"fr": "Référence", "en": "Reference"}),
     ("narrations", {"fr": "Narrations", "en": "Narrations"}),
     ("teaching", {"fr": "Enseigner", "en": "Teaching"}),
     ("pedagogy", {"fr": "Pédagogie", "en": "Pedagogy"})]),
  ("offering", {"fr": "Offre", "en": "Offering"}, [
     ("offering", {"fr": "Audiences", "en": "Audiences"}),
     ("editions", {"fr": "Éditions", "en": "Editions"}),
     ("customers", {"fr": "Clients", "en": "Customers"})]),
  ("start", {"fr": "Démarrer", "en": "Start"}, [
     ("start", {"fr": "Démarrer", "en": "Start"})]),
]
GENERATED = {"atlas", "reference", "narrations"}   # built by code, not from a .md
OWNER = {}                                          # page -> its section
for sec, _, pages in SECTIONS:
    for slug, _ in pages: OWNER[slug] = sec
OWNER["atlas-group"] = "platform"                   # an area's own page sits under The areas
OWNER["guide"] = "learn"                            # a guide page sits under Documentation

UI = {
  "fr": {
    "slogan": "La plateforme des makers à l'ère agentique", "second": "Née en Afrique. Utile au monde !",
    "skip": "Aller au contenu", "other_lang": "English", "other_code": "en",
    "present": "Présenter le site en diaporama", "github": "Le dépôt Softanza sur GitHub", "menu": "Menu principal", "path": "Pages de la section",
    "proof_law": "Chaque affirmation de ce site renvoie au fichier, au garde ou au rendu qui la prouve. Chaque bloc de code a été exécuté le soir de la publication ; sa sortie est à côté.",
    "fonts": "Polices Fraunces, IBM Plex Sans et IBM Plex Mono, sous licence SIL OFL 1.1, hébergées sur ce site ; le site s'ouvre sans réseau.",
    "made": "Les textes de ce site ont été rédigés avec un assistant d'IA, Claude, sous la direction de l'auteur ; le code, les exécutions et les chiffres viennent des dépôts. (Règle 99 de la constitution Zui : ce qui est fait par une machine le dit.)",
    "built": "Site généré le", "elsewhere": "Softanza", "repo": "Le dépôt sur GitHub", "tour": "Mode présentation", "check": "Vérifier hors ligne",
    "theme_light": "Passer en clair", "theme_dark": "Passer en sombre", "theme_auto": "Suivre le système", "theme_h": "Affichage",
    "atlas_title": "L'Atlas", "atlas_title_html": "L'<i>Atlas</i>", "atlas_kicker": "Où se tient toute la plateforme",
    "atlas_lede": "Vingt-huit groupes et 334 couloirs, chacun noté contre les meilleurs de sa catégorie : Strong, au niveau ou au-dessus du meilleur ; Solid, complet et prouvé, un cran derrière ; Partial, présent mais incomplet ; Emerging, prévu ou tout juste commencé. Les notes sont gagnées par ce que les gardes prouvent, et les lacunes sont montrées à côté des forces.",
    "atlas_desc": "L'Atlas Softanza : 28 groupes et 334 couloirs notés Strong, Solid, Partial ou Emerging contre les meilleurs de chaque catégorie.",
    "group": "Groupe", "strong": "Strong", "solid": "Solid", "partial": "Partial", "emerging": "Emerging", "vs": "comparé à",
    "tally": "Les 334 couloirs : 101 Strong · 129 Solid · 68 Partial · 36 Emerging.",
    "atlas_note": "Atlas version 21, lu sur la branche principale le 2026-09-30 au commit",
    "measured": "Mesuré contre", "folders": "Dossiers", "standouts": "Ce qu'un maker en fait, et ce qui se distingue", "gaps": "Ce qui est dû",
    "lanes_h": "Les couloirs, un par un", "lanes_note": "Les couloirs et leurs notes sont cités tels qu'ils ont été lus à la source, le",
    "example": "Un exemple, exécuté", "no_example": "Aucun exemple exécuté sur cette page", "output": "Sortie",
    "source": "la source", "nopic": "Pas encore d'image", "guide": "Le guide des fonctions de ce domaine",
    "narr_title": "Narrations", "narr_title_html": "Les <i>narrations</i>", "narr_kicker": "La documentation qui s'exécute",
    "narr_lede": "Cent trente-quatre documents où chaque bloc de code s'exécute quand on le lit et où aucune sortie n'est stockée. Chacun est un fichier du dépôt ; le titre est celui du fichier.",
    "narr_desc": "Les 134 narrations de Softanza, listées avec leur fichier dans le dépôt.",
    "narr_note": "Liste lue dans le dossier doc/narrations du dépôt au commit 0e72e2e2c, le 2026-10-01. Une narration s'ouvre sur GitHub ; sa version exécutée comme page de ce site est le prochain pas de la publication.",
    "cov_row": "Domaine", "cov_present": "Présent", "cov_deep": "Deep", "cov_solid": "Solid", "cov_partial": "Partial", "cov_none": "Absent",
  },
  "en": {
    "slogan": "The Makers Platform of the Agentic Age", "second": "Born in Africa. Useful to the World!",
    "skip": "Skip to content", "other_lang": "Français", "other_code": "fr",
    "present": "Present the site as a slideshow", "github": "The Softanza repository on GitHub", "menu": "Main menu", "path": "Pages of the section",
    "proof_law": "Every claim on this site links to the file, the guard or the render that proves it. Every code block was run on the night of publication; its output sits beside it.",
    "fonts": "Fraunces, IBM Plex Sans and IBM Plex Mono, under the SIL Open Font License 1.1, hosted on this site; the site opens with no network.",
    "made": "The prose of this site was drafted with an AI assistant, Claude, under the author's direction; the code, the runs and the figures come from the repositories. (Rule 99 of the Zui constitution: what a machine made says so.)",
    "built": "Site generated on", "elsewhere": "Softanza", "repo": "The repository on GitHub", "tour": "Presentation mode", "check": "Check offline",
    "theme_light": "Use the light theme", "theme_dark": "Use the dark theme", "theme_auto": "Follow the system", "theme_h": "Display",
    "atlas_title": "The Atlas", "atlas_title_html": "The <i>Atlas</i>", "atlas_kicker": "Where the whole platform stands",
    "atlas_lede": "Twenty-eight groups and 334 lanes, each rated against the leaders of its category: Strong, at or above the leader; Solid, complete and proven, a step behind; Partial, present but incomplete; Emerging, planned or barely begun. Ratings are earned by what the guards prove, and the gaps are shown beside the strengths.",
    "atlas_desc": "The Softanza Atlas: 28 groups and 334 lanes rated Strong, Solid, Partial or Emerging against the leaders of each category.",
    "group": "Group", "strong": "Strong", "solid": "Solid", "partial": "Partial", "emerging": "Emerging", "vs": "measured against",
    "tally": "All 334 lanes: 101 Strong · 129 Solid · 68 Partial · 36 Emerging.",
    "atlas_note": "Atlas version 21, read on the main branch on 2026-09-30 at commit",
    "measured": "Measured against", "folders": "Folders", "standouts": "What a maker does with it, and what stands out", "gaps": "What is owed",
    "lanes_h": "The lanes, one by one", "lanes_note": "Lanes and their notes are quoted as they were read at the source, on",
    "example": "One example, run", "no_example": "No example run on this page", "output": "Output",
    "source": "the source", "nopic": "No picture yet", "guide": "The guide to this area's functions",
    "narr_title": "Narrations", "narr_title_html": "The <i>narrations</i>", "narr_kicker": "Documentation that runs",
    "narr_lede": "One hundred and thirty-four documents where every code block runs as it is read and no output is stored. Each is a file of the repository; the title is the file's own.",
    "narr_desc": "Softanza's 134 narrations, listed with their file in the repository.",
    "narr_note": "List read in the repository's doc/narrations folder at commit 0e72e2e2c, on 2026-10-01. A narration opens on GitHub; its run version as a page of this site is the next step of the publication.",
    "cov_row": "Domain", "cov_present": "Present", "cov_deep": "Deep", "cov_solid": "Solid", "cov_partial": "Partial", "cov_none": "Absent",
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
<link rel="stylesheet" href="{rel}assets/css/site.css">
{extra}{THEME_SCRIPT}
</head>"""

PRESENT_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="3.5" width="19" height="12.5" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 7.1v5.8l4.8-2.9z" fill="currentColor"/><path d="M12 16v3.2M8.2 21.2l3.8-2 3.8 2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')   # a screen on its stand, with a play mark: the slideshow
GITHUB_SVG = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>'

def nav_prefix(rel, lang):
    """from a page at depth `rel`, the prefix that reaches this language's folder"""
    return f"{lang}/" if rel == "" else rel[3:]

def wordmark(rel):
    return (f'<img class="wm-light" src="{rel}assets/img/wordmark.png" alt="Softanza" width="660" height="105">'
            f'<img class="wm-dark" src="{rel}assets/img/wordmark-dark.png" alt="" width="660" height="105">')

def header(lang, slug, rel, other_href=None, nav_rel=None, page_key=None, data_lang=""):
    """the main menu, and under it the path of the current section"""
    ui = UI[lang]
    if nav_rel is None: nav_rel = nav_prefix(rel, lang)
    key = page_key or slug
    sec = OWNER.get(key)
    current_page = {"atlas-group": "areas", "guide": "docs"}.get(key, key)
    links = "".join(f'<a href="{nav_rel}{pages[0][0]}.html"{" aria-current=page" if s == sec else ""}>{esc(lab[lang])}</a>'
                    for s, lab, pages in SECTIONS)
    other = ui["other_code"]
    if other_href is None: other_href = f"../{other}/{slug}.html"
    path = ""
    if sec:
        pages = next(p for s, _, p in SECTIONS if s == sec)
        if len(pages) > 1:
            path = ('\n  <nav class="path" aria-label="' + esc(ui["path"]) + '"><div class="path-in">'
                    + "".join(f'<a href="{nav_rel}{p}.html"{" aria-current=page" if p == current_page else ""}>{esc(lab[lang])}</a>' for p, lab in pages)
                    + '</div></nav>')
    dl = f' data-lang="{data_lang}"' if data_lang else ""
    home = f"{rel}index.html" + (f"?lang={lang}" if rel else "")
    tools = (f'<div class="tools"><a class="present" href="{nav_rel}tour.html" aria-label="{esc(ui["present"])}" title="{esc(ui["present"])}">{PRESENT_SVG}</a>'
             f'<a class="gh" href="https://github.com/mayouni/stzlib" aria-label="{esc(ui["github"])}" title="{esc(ui["github"])}">{GITHUB_SVG}</a>'
             f'<a class="lang" href="{other_href}" lang="{other}" hreflang="{other}">{ui["other_lang"]}</a></div>')
    brand = f'<a class="brand" href="{home}" aria-label="Softanza">{wordmark(rel)}</a>'
    # on a phone the brand row scrolls away and only the two menus stay pinned;
    # the row is the same links, shown in one place or the other, never both
    return f"""<a class="skip" href="#main"{dl}>{ui["skip"]}</a>
<div class="brandrow"{dl}>{brand}{tools}</div>
<header class="top"{dl}>
  <div class="topbar">
    {brand}
    <nav class="nav" aria-label="{esc(ui["menu"])}">{links}</nav>
    {tools}
  </div>{path}
</header>"""

def footer(lang, rel, pagers_html="", nav_rel=None, scripts=True, data_lang=""):
    """a site map: every section and every page, then the signature"""
    ui = UI[lang]
    if nav_rel is None: nav_rel = nav_prefix(rel, lang)
    today = datetime.date.today().isoformat()
    cols = "".join(f'<div><h3>{esc(lab[lang])}</h3><ul>' + "".join(f'<li><a href="{nav_rel}{p}.html">{esc(pl[lang])}</a></li>' for p, pl in pages) + '</ul></div>'
                   for s, lab, pages in SECTIONS)
    other = ui["other_code"]
    cols += (f'<div><h3>{esc(ui["elsewhere"])}</h3><ul>'
             f'<li><a href="https://github.com/mayouni/stzlib">{esc(ui["repo"])}</a></li>'
             f'<li><a href="{nav_rel}tour.html">{esc(ui["tour"])}</a></li>'
             f'<li><a href="{rel}deck-check.html">{esc(ui["check"])}</a></li>'
             f'<li><a href="{rel}index.html?lang={other}" lang="{other}">{esc(ui["other_lang"])}</a></li></ul></div>')
    themes = (f'<div class="themes" role="group" aria-label="{esc(ui["theme_h"])}">'
              f'<button type="button" data-set-theme="light">{esc(ui["theme_light"])}</button>'
              f'<button type="button" data-set-theme="dark">{esc(ui["theme_dark"])}</button>'
              f'<button type="button" data-set-theme="auto">{esc(ui["theme_auto"])}</button></div>')
    dl = f' data-lang="{data_lang}"' if data_lang else ""
    out = f"""<footer class="foot"{dl}><div class="wrap">
  <nav class="map" aria-label="Site">{cols}</nav>
  <div class="foot-bottom">
    <div><a class="foot-mark" href="{rel}index.html" aria-label="Softanza">{wordmark(rel)}</a>
      <p style="margin-top:12px">{esc(ui["slogan"])}. {esc(ui["second"])}</p>{themes}</div>
    <div><p>{esc(ui["proof_law"])}</p><p>{esc(ui["made"])}</p><p>{esc(ui["fonts"])} {ui["built"]} {today}.</p></div>
  </div>
</div></footer>"""
    if scripts:
        out += f'\n<script src="{rel}assets/js/site.js"></script>{PAGE_PING}\n</body></html>'
    return out

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
        for l in d.get("lanes", []):
            for k in ("lane", "note", "proof"): l[k] = l.get(k, "").replace("�", "-")
        d["thesis"] = d.get("thesis", "").replace("�", "-")
        d["standouts"] = [s.replace("�", "-") for s in d.get("standouts", [])]
        d["gaps"] = [s.replace("�", "-") for s in d.get("gaps", [])]
        groups.append({**g, "detail": d, "run": runs.get(g["slug"])})
    return idx, groups

def tiles_html(lang, idx, groups, rel_atlas, rel_assets, themed=True, hl="h2"):
    """every area as a picture with its name beneath it, grouped by theme"""
    def tile(g):
        r = g.get("render"); href = f"{rel_atlas}{g['slug']}.html"
        if r:
            pic = (f'<a class="pic" href="{href}" tabindex="-1" aria-hidden="true"><img src="{rel_assets}assets/img/areas/{r["thumb"]}" '
                   f'alt="" width="1100" height="660" loading="lazy"></a>')
            what = esc(r["cap_" + lang])
        else:
            pic = f'<div class="nopic">{esc(UI[lang]["nopic"])}</div>'
            what = esc(g.get("nopic_" + lang, ""))
        h = HERITAGE.get(g["slug"])
        if h: what = esc(h["principle_" + lang])
        return f'<div class="tile">{pic}<a class="name" href="{href}">{esc(g[lang])}</a><span class="what">{what}</span></div>'
    if not themed:
        return '<div class="tiles">' + "".join(tile(g) for g in groups if g.get("render")) + '</div>'
    out = []
    for b in idx["bands"]:
        gs = [g for g in groups if g["band"] == b["id"]]
        out.append(f'<section class="theme"><{hl} id="{b["id"]}">{esc(b[lang])}</{hl}><div class="tiles">{"".join(tile(g) for g in gs)}</div></section>')
    return "".join(out)

MAP_LABEL = {"fr": ("La carte des domaines", "Les vingt-huit domaines d'un coup d'oeil, chacun dans la couleur de son thème."),
             "en": ("The map of the areas", "All twenty-eight areas at a glance, each in the colour of its theme.")}

def fmap_html(lang, idx, groups, rel_atlas):
    """every area in one grid, coloured by its theme, before the families are shown one by one"""
    legend = "".join(f'<span class="fk" data-t="{b["id"]}">{esc(b[lang])}</span>' for b in idx["bands"])
    tiles = "".join(f'<a class="ft" data-t="{g["band"]}" href="{rel_atlas}{g["slug"]}.html">{esc(g[lang])}</a>'
                    for b in idx["bands"] for g in groups if g["band"] == b["id"])
    return f'<div class="fmap"><div class="fkeys" aria-label="{esc(MAP_LABEL[lang][0])}">{legend}</div><div class="fgrid">{tiles}</div></div>'

def scope_html(lang, idx, groups):
    """the documentation's whole scope, one door per area of the reference"""
    out = []
    for b in idx["bands"]:
        for g in [g for g in groups if g["band"] == b["id"]]:
            out.append(f'<a data-t="{b["id"]}" href="guide/{g["slug"]}.html"><span>{esc(g[lang])}<small>{esc(b[lang])}</small></span></a>')
    return '<div class="scope">' + "".join(out) + '</div>'

def coverage_html(lang):
    cov = json.loads((DATA / "coverage.json").read_text(encoding="utf-8"))
    ui = UI[lang]; n = len(cov["platforms"])
    heads = "".join(f'<th scope="col">{esc(p[1])}<small>{esc(p[2] if lang == "en" else p[3])}</small></th>' for p in cov["platforms"])
    rows = []
    for g in cov["groups"]:
        rows.append(f'<tr class="cg"><th colspan="{1 + n}" scope="colgroup">{esc(g[lang])}</th></tr>')
        for r in g["rows"]:
            note = r.get("note_" + lang)
            name = f'{esc(r[lang])}{("<small>" + esc(note) + "</small>") if note else ""}'
            cells = "".join(f'<td><span class="cv {v}">{esc(ui["cov_" + v])}</span></td>' for v in r["r"])
            rows.append(f'<tr class="dn" aria-hidden="true"><th colspan="{n}">{name}</th></tr><tr><th scope="row">{name}</th>{cells}</tr>')
    t = cov["tally"]; pr = cov["present"]
    tally = "".join(f'<td><b>{esc(pr[k])}</b><small>{t[k][0]} deep · {t[k][1]} solid · {t[k][2]} partial</small></td>' for k, _, _, _ in cov["platforms"])
    rows.append(f'<tr class="dn" aria-hidden="true"><th colspan="{n}">{esc(ui["cov_present"])}</th></tr><tr class="ct"><th scope="row">{esc(ui["cov_present"])}</th>{tally}</tr>')
    return f'<div class="covwrap"><table class="cov"><thead><tr><th scope="col">{esc(ui["cov_row"])}</th>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'

def diagram_imgs(body_html, rel):
    """every drawn diagram gets its phone drawing beside it; CSS shows the one that fits"""
    def rep(m):
        name, lang, alt = m.group(1), m.group(2), m.group(3)
        narrow = ROOT / "assets" / "img" / "diagrams" / f"{name}-narrow-{lang}.png"
        if not narrow.exists():
            return m.group(0)
        w, h = Image.open(narrow).size
        return (f'<img class="wide-only" src="{rel}assets/img/diagrams/{name}-{lang}.png" alt="{alt}" width="1376" height="768">'
                f'<img class="narrow-only" loading="lazy" src="{rel}assets/img/diagrams/{name}-narrow-{lang}.png" alt="{alt}" width="{w}" height="{h}">')
    return re.sub(r'<img src="(?:\.\./)+assets/img/diagrams/([a-z]+)-(fr|en)\.png" alt="([^"]*)"[^>]*>', rep, body_html)

def inject(body_html, lang, idx, groups, rel="../"):
    body_html = body_html.replace("<!--AREAS-->", fmap_html(lang, idx, groups, "atlas/") + tiles_html(lang, idx, groups, "atlas/", rel))
    body_html = body_html.replace("<!--ATLAS-WALL-->", tiles_html(lang, idx, groups, "atlas/", rel, themed=False))
    body_html = body_html.replace("<!--COVERAGE-->", coverage_html(lang))
    body_html = body_html.replace("<!--DOCS-SCOPE-->", scope_html(lang, idx, groups))
    # <!--SHOWCASE:slug-->: the runs of data/showcase.json inside a content page, under the page's own heading
    body_html = re.sub(r"<!--SHOWCASE:([a-z0-9-]+)-->", lambda m: showcase_html(lang, m.group(1), heading=False), body_html)
    return diagram_imgs(body_html, rel)

LONG = []
def check_reading_arc(slug, lang, body_html):
    """Rule 123: a paragraph past about 800 characters has become a wall"""
    for p in re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>", body_html, re.S):
        t = re.sub(r"<[^>]+>", "", p)
        if len(t) > 800: LONG.append(f"{lang}/{slug}: {len(t)} chars: {t[:60]}...")

def page_shell(lang, slug, title, description, kicker, title_html, lede, body_html, rel="../", page_key=None, other_href=None, body_class=None):
    page = head(lang, f'{title} · Softanza', description, rel)
    page += f'\n<body class="{body_class or "page page-" + slug}">\n' + header(lang, slug, rel, other_href=other_href, page_key=page_key)
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{kicker}</div>
    <h1>{title_html}</h1>
    {f'<p class="lede">{lede}</p>' if lede else ''}
  </div></section>
  <div class="wrap page-body">
{body_html}
  </div>
</main>
"""
    page += footer(lang, rel)
    return page

# ----------------------------------------------------------------------------
BOLD_RX = re.compile("[*][*](.+?)[*][*]")
def BOLD_TO(m): return "<b>" + m.group(1) + "</b>"

def build_page(lang, slug, idx, groups):
    src = CONTENT / lang / f"{slug}.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    title = meta.get("title", slug)
    body_html = inject(md(body), lang, idx, groups)
    check_reading_arc(slug, lang, body_html)
    page = page_shell(lang, slug, title, meta.get("description", ""), esc(meta.get("kicker", "")),
                      meta.get("title_html", esc(title)), BOLD_RX.sub(BOLD_TO, meta.get("lede", "")), body_html)
    out = ROOT / lang / f"{slug}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

def build_atlas_index(lang, idx, groups):
    ui = UI[lang]
    sections = []
    for b in idx["bands"]:
        rows = "".join(
            f'<tr><td><a href="atlas/{g["slug"]}.html">{esc(g[lang])}</a><span class="line">{esc(g["line_" + lang])}</span>'
            f'<span class="peers">{ui["vs"]} {esc(g["peers"])}</span></td>'
            f'<td class="n">{g["s"]}</td><td class="n">{g["so"]}</td><td class="n">{g["p"]}</td><td class="n">{g["e"]}</td></tr>'
            for g in groups if g["band"] == b["id"])
        cols = "".join(f'<th scope="col" class="n"><span class="full">{ui[k]}</span><span class="short" aria-hidden="true">{ui[k][:2] if k == "solid" else ui[k][0]}</span></th>'
                       for k in ("strong", "solid", "partial", "emerging"))
        sections.append(f'<h2 id="{b["id"]}">{esc(b[lang])}</h2><div class="tw"><table class="ratings"><thead><tr><th scope="col">{ui["group"]}</th>{cols}</tr></thead><tbody>{rows}</tbody></table></div>')
    body = (f'<p class="tally-line">{ui["tally"]}</p>'
            f'<p class="proof">{ui["atlas_note"]} <a href="https://github.com/mayouni/stzlib/commit/{idx["commit"]}">{idx["commit"]}</a>.</p>'
            + "".join(sections))
    page = page_shell(lang, "atlas", ui["atlas_title"], ui["atlas_desc"], esc(ui["atlas_kicker"]), ui["atlas_title_html"], esc(ui["atlas_lede"]), body)
    (ROOT / lang / "atlas.html").write_text(page, encoding="utf-8")

# ----------------------------------------------------------------------------
# the heritage: how each area was rethought from first principles (data/heritage.json)
HER_UI = {
  "fr": {"h": "Repensé depuis les premiers principes", "way": "La manière Softanza", "kept": "Gardé des meilleures pratiques",
         "re": "Repensé", "planned": "prévu", "src": "source",
         "intro": "Ce que Softanza a gardé de ce qui marche, et ce qu'elle a repensé, tel que la bibliothèque l'a écrit dans ses documents de conception et ses narrations."},
  "en": {"h": "Rethought from first principles", "way": "The Softanza way", "kept": "Kept from the best practice",
         "re": "Rethought", "planned": "planned", "src": "source",
         "intro": "What Softanza kept from what works, and what it rethought, as the library wrote it down in its design documents and narrations."},
}
def load_heritage():
    f = DATA / "heritage.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
HERITAGE = load_heritage()

def src_link(path):
    path = path.split(" (")[0].split(" §")[0].split(" #")[0].strip()
    url = "https://github.com/mayouni/stzlib/blob/main/CLAUDE.md" if path == "CLAUDE.md" else "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/" + path
    return url

def heritage_html(lang, slug):
    h = HERITAGE.get(slug)
    if not h: return ""
    ui = HER_UI[lang]
    def items(lst, staged):
        out = []
        for it in lst:
            mark = f' <b>({ui["planned"]})</b>' if staged and it.get("stage") == "planned" else ""
            src = f' <a class="src" href="{esc(src_link(it["source"]))}">{ui["src"]}</a>' if it.get("source") else ""
            out.append(f'<li>{esc(it[lang])}{mark}{src}</li>')
        return "".join(out)
    return (f'<h2>{ui["h"]}</h2><p>{ui["intro"]}</p>'
            f'<p class="way"><span>{ui["way"]}</span>{esc(h["principle_" + lang])}</p>'
            f'<div class="sg"><div><h4>{ui["kept"]}</h4><ul>{items(h.get("kept", []), False)}</ul></div>'
            f'<div><h4>{ui["re"]}</h4><ul>{items(h.get("rethought", []), True)}</ul></div></div>')

# the distinctive capability of each area, run inside the library (data/showcase.json)
SHOW_UI = {"fr": {"h": "La manière Softanza, exécutée", "ran": "exécuté le {d} dans la bibliothèque au commit 0e72e2e2c ; tiré de",
                  "intro": "Ce que Softanza fait autrement dans ce domaine, montré par du code tiré de ses narrations et de ses gardes, et exécuté pour cette page."},
           "en": {"h": "The Softanza way, run", "ran": "run on {d} inside the library at commit 0e72e2e2c; taken from",
                  "intro": "What Softanza does differently in this area, shown by code taken from its narrations and guards, and run for this page."}}
def load_showcase():
    f = DATA / "showcase.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
SHOWCASE = load_showcase()

def showcase_html(lang, slug, heading=True):
    items = SHOWCASE.get(slug)
    if not items:
        if not heading: raise SystemExit(f"no run in data/showcase.json for the placeholder SHOWCASE:{slug}")
        return ""
    ui = SHOW_UI[lang]; out_lbl = "Sortie" if lang == "fr" else "Output"
    parts = [f'<h2>{ui["h"]}</h2><p>{ui["intro"]}</p>'] if heading else []
    for it in items:
        parts.append(f'<p style="margin-top:32px"><b>{esc(it["what_" + lang])}</b></p>'
                     f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(it["code"])}</pre></div>'
                     f'<div class="out"><div class="lbl">{out_lbl}</div><pre>{esc(it["out"])}</pre></div></div>'
                     f'<p class="ran">{ui["ran"].format(d=esc(it["ran"]))} <a href="{esc(src_link(it["source"]))}">{esc(it["source"].split(" ")[0])}</a></p>')
    return "".join(parts)

RATING_CLASS = {"Strong": "strong", "Solid": "solid", "Partial": "partial", "Emerging": "emerging"}

def build_group_page(lang, idx, groups, i):
    g = groups[i]; d = g["detail"]; ui = UI[lang]; rel = "../../"
    band = next(b for b in idx["bands"] if b["id"] == g["band"])
    colon = " :" if lang == "fr" else ":"
    lanes = "".join(
        f'<div class="lane"><div class="ln">{esc(l["lane"])}</div><div class="lr"><span class="chip {RATING_CLASS.get(l["rating"], "solid")}">{esc(l["rating"])}</span></div>'
        f'<div class="lt">{esc(l["note"])}{("<small>" + esc(l["proof"]) + "</small>") if l.get("proof") else ""}</div></div>'
        for l in d.get("lanes", []))
    folders = " · ".join(f'<a href="{GH}base/{f.strip()}">base/{esc(f.strip())}</a>' for f in g["dirs"].split(","))
    sg = ""
    if d.get("standouts") or d.get("gaps"):
        sg = (f'<div class="sg"><div><h4>{ui["standouts"]}</h4><ul>{"".join(f"<li>{esc(s)}</li>" for s in d.get("standouts", []))}</ul></div>'
              f'<div><h4>{ui["gaps"]}</h4><ul>{"".join(f"<li>{esc(s)}</li>" for s in d.get("gaps", []))}</ul></div></div>')
    run = g.get("run") or {}
    if SHOWCASE.get(g["slug"]):
        example = showcase_html(lang, g["slug"])
    elif run.get("code"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p>'
                   f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(run["code"])}</pre></div><div class="out"><div class="lbl">{ui["output"]}</div><pre>{esc(run["out"])}</pre></div></div>'
                   f'<p class="ran">{esc(run.get("ran_" + lang, ""))}</p>')
    elif run.get("image"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p>'
                   f'<figure><img src="{rel}assets/img/{run["image"]}" alt="{esc(run.get("alt_" + lang, ""))}"><figcaption>{esc(run.get("ran_" + lang, ""))}</figcaption></figure>')
    elif run.get("text"):
        example = (f'<h2>{ui["example"]}</h2><p>{esc(run.get("intro_" + lang, ""))}</p><pre>{esc(run["text"])}</pre>'
                   f'<p class="ran">{esc(run.get("ran_" + lang, ""))}</p>')
    else:
        example = f'<div class="note"><p><b>{ui["no_example"]}.</b> {esc(run.get("why_" + lang, ""))}</p></div>'
    c = {"Strong": 0, "Solid": 0, "Partial": 0, "Emerging": 0}
    for l in d.get("lanes", []): c[l["rating"]] = c.get(l["rating"], 0) + 1
    note = ""
    if d.get("lanes") and (c["Strong"], c["Solid"], c["Partial"], c["Emerging"]) != (g["s"], g["so"], g["p"], g["e"]):
        if lang == "fr":
            note = (f'<div class="note"><p><b>Deux lectures.</b> La carte de l\'Atlas (v{idx["version"]}, {idx["read_at"]}) donne {g["s"]} Strong, {g["so"]} Solid, {g["p"]} Partial, {g["e"]} Emerging ; '
                    f'la page du groupe, lue le {esc(d.get("dated", ""))}, note ses couloirs {c["Strong"]}, {c["Solid"]}, {c["Partial"]}, {c["Emerging"]}. Les couloirs ci-dessous sont ceux de la page du groupe ; la carte est la lecture la plus récente.</p></div>')
        else:
            note = (f'<div class="note"><p><b>Two readings.</b> The Atlas card (v{idx["version"]}, {idx["read_at"]}) says {g["s"]} Strong, {g["so"]} Solid, {g["p"]} Partial, {g["e"]} Emerging; '
                    f'the group page, read {esc(d.get("dated", ""))}, rates its lanes {c["Strong"]}, {c["Solid"]}, {c["Partial"]}, {c["Emerging"]}. The lanes below are the group page\'s; the card is the more recent reading.</p></div>')
    r = g.get("render")
    if r:
        hero = (f'<figure class="area-hero"><img src="{rel}assets/img/areas/{r["file"]}" alt="{esc(r["cap_" + lang])}" width="1100" height="660">'
                f'<figcaption><b>{esc(r["cap_" + lang])}.</b> {esc(r["by_" + lang])} · <a href="{r["src"]}">{ui["source"]}</a></figcaption></figure>')
    else:
        hero = f'<div class="note"><p><b>{ui["nopic"]}.</b> {esc(g.get("nopic_" + lang, ""))}</p></div>'
    thesis = f'<blockquote><p>{esc(d["thesis"])}</p></blockquote>' if d.get("thesis") else ""
    body = f"""<p class="counts-line">{g["s"]} Strong · {g["so"]} Solid · {g["p"]} Partial · {g["e"]} Emerging</p>
    <p class="proof">{ui["measured"]}{colon} {esc(g["peers"])} · {ui["folders"]}{colon} {folders} · <a href="../guide/{g["slug"]}.html">{ui["guide"]}</a></p>
    {hero}
    {heritage_html(lang, g["slug"])}
    {thesis}
    {sg}
    {example}
    <h2>{ui["lanes_h"]}</h2>
    <p class="proof">{ui["lanes_note"]} {esc(d.get("dated", ""))}.</p>
    {note}
    <div class="lanes">{lanes}</div>"""
    page = page_shell(lang, "atlas", g[lang], g["line_" + lang], esc(band[lang]), esc(g[lang]), esc(g["line_" + lang]), body,
                      rel=rel, page_key="atlas-group", other_href=f"../../{ui['other_code']}/atlas/{g['slug']}.html", body_class="page page-atlas-group")
    out = ROOT / lang / "atlas" / f"{g['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

RING_WORD = re.compile(r"\bRing\b")
def build_narrations(lang):
    ui = UI[lang]
    items = json.loads((DATA / "narrations.json").read_text(encoding="utf-8"))
    lis = "".join(f'<li><a href="{GH}base/doc/narrations/{esc(n["file"])}">{esc(RING_WORD.sub("Haro", n["title"]).replace("Ring++", "Haro"))}</a></li>' for n in items)
    body = f'<p class="proof">{esc(ui["narr_note"])}</p><ol class="narr">{lis}</ol>'
    page = page_shell(lang, "narrations", ui["narr_title"], ui["narr_desc"], esc(ui["narr_kicker"]), ui["narr_title_html"], esc(ui["narr_lede"]), body)
    (ROOT / lang / "narrations.html").write_text(page, encoding="utf-8")

# ----------------------------------------------------------------------------
# the tour: scenes separated by <<< scene ... >>> lines, notes in ```notes fences
SCENE_RX = re.compile(r'^<<<\s*scene\s+(.*?)\s*>>>\s*$', re.M)
ATTR_RX = re.compile(r'(\w+)="([^"]*)"')
NOTES_RX = re.compile(r'```notes\n(.*?)\n```', re.S)

def build_tour(lang, idx, groups):
    src = CONTENT / lang / "tour.md"
    meta, body = front_matter(src.read_text(encoding="utf-8"))
    parts = SCENE_RX.split(body)
    scenes = []
    for i in range(1, len(parts), 2):
        attrs = dict(ATTR_RX.findall(parts[i])); text = parts[i+1]
        m = NOTES_RX.search(text); notes = m.group(1).strip() if m else ""
        text = NOTES_RX.sub("", text)
        scenes.append((attrs, inject(md(text), lang, idx, groups), md(notes) if notes else ""))
    rel = "../"; n = len(scenes); secs = []
    for k, (attrs, body_html, notes_html) in enumerate(scenes, 1):
        page = attrs.get("page", "")
        page_link = f'<a class="scene-page" href="{page}">{esc(attrs.get("label", page))}</a>' if page else ""
        notes_block = f'<aside class="notes"><div class="eyebrow">Notes</div>{notes_html}</aside>' if notes_html else ''
        secs.append(f"""<section class="scene {attrs.get("class", "")}" id="s{k}" data-index="{k}" aria-label="{k}/{n}">
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
    (ROOT / lang / "tour.html").write_text(page_html, encoding="utf-8")
    return [a for a, _, _ in scenes]

# ----------------------------------------------------------------------------
def build_home(idx, groups):
    """the landing page: both languages inside, the header's language link picks"""
    body = (CONTENT / "home.html").read_text(encoding="utf-8")
    for lang in LANGS:
        body = body.replace(f"<!--AREAS-{lang.upper()}-->", fmap_html(lang, idx, groups, f"{lang}/atlas/") + tiles_html(lang, idx, groups, f"{lang}/atlas/", "", hl="h3"))
    page = head("fr", "Softanza · La plateforme des makers à l'ère agentique · The Makers Platform of the Agentic Age",
                "Softanza: declare a language for your world, run it on one engine, let agents speak it safely. Born in Africa. Useful to the World.", "")
    page = page.replace('<html lang="fr" data-lang="fr">', '<html lang="fr" data-lang="fr" class="home">')
    heads = "".join(header(l, "index", "", other_href=f"index.html?lang={o}", nav_rel=f"{l}/", data_lang=l) for l, o in (("fr", "en"), ("en", "fr")))
    feet = "".join(footer(l, "", nav_rel=f"{l}/", scripts=False, data_lang=l) for l in LANGS)
    page += "\n<body class=\"home-body over-hero\">\n" + heads + '\n<main id="main">\n' + body + '\n</main>\n' + feet + f"""
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
    """Measured, not eyeballed: the pairs declared in site.css as /* contrast: fg | bg | min | label */"""
    css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
    ok = True
    for spec in re.findall(r'/\*\s*contrast:\s*([^*]+?)\s*\*/', css):
        fg, bg, need, label = [s.strip() for s in spec.split("|")]
        c = contrast(fg, bg)
        if c < float(need): ok = False
        print(f"  contrast {'ok ' if c >= float(need) else 'LOW'} {c:5.2f} >= {need}  {label} ({fg} on {bg})")
    return ok

def main():
    idx, groups = load_atlas()
    outs = []
    for lang in LANGS:
        for sec, _, pages in SECTIONS:
            for slug, _ in pages:
                if slug in GENERATED: continue
                outs.append(build_page(lang, slug, idx, groups))
        build_atlas_index(lang, idx, groups)
        build_narrations(lang)
        for i in range(len(groups)):
            build_group_page(lang, idx, groups, i)
        for old in ("why", "govern", "makers", "products"):
            f = ROOT / lang / f"{old}.html"
            if f.exists(): f.unlink()
    scenes = {lang: build_tour(lang, idx, groups) for lang in LANGS}
    build_home(idx, groups)
    nref, ncls, nown = build_reference({"ROOT": ROOT, "LANGS": LANGS, "head": head, "header": header, "footer": footer, "idx": idx, "groups": groups})
    nguide = build_guides({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "idx": idx, "groups": groups, "heritage": HERITAGE})
    print(f"guides: {nguide} pages")
    assets = []
    for f in sorted((ROOT / "assets/fonts").glob("*.woff2")):
        assets.append({"kind": "font", "path": f"assets/fonts/{f.name}"})
    for sub in ("", "areas/", "diagrams/"):
        for f in sorted((ROOT / "assets/img" / sub).glob("*")):
            if f.is_file() and f.suffix.lower() in (".png", ".webp", ".jpg", ".svg"):
                assets.append({"kind": "image", "path": f"assets/img/{sub}{f.name}"})
    for f in ("fonts.css", "site.css"):
        assets.append({"kind": "css", "path": f"assets/css/{f}"})
    for f in ("site.js", "tour.js"):
        assets.append({"kind": "script", "path": f"assets/js/{f}"})
    assets.append({"kind": "page", "path": "index.html"})
    for lang in LANGS:
        for sec, _, pages in SECTIONS:
            for slug, _ in pages:
                assets.append({"kind": "page", "path": f"{lang}/{slug}.html"})
        assets.append({"kind": "page", "path": f"{lang}/tour.html"})
    reader = ROOT / "reader.html"
    if reader.exists():
        r = reader.read_text(encoding="utf-8")
        if "stzsite:'page'" not in r:
            reader.write_text(r.replace("</body>", PAGE_PING + "</body>", 1), encoding="utf-8")
        assets.append({"kind": "page", "path": "reader.html"})
    build_deck_check(assets)
    print(f"reference: {nref} pages, {ncls} classes, {nown} own methods")
    print(f"built {len(outs)} pages + {2*len(groups)} area pages + atlas + narrations + index.html + deck-check.html; tour scenes fr={len(scenes['fr'])} en={len(scenes['en'])}")
    if LONG:
        print("reading arc (Rule 123), paragraphs past 800 characters:")
        for l in LONG: print("  ", l)
    print("contrast:")
    if not check_contrast():
        print("CONTRAST BELOW TARGET"); sys.exit(1)

if __name__ == "__main__":
    main()
