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
from build_methods import build_methods, load_entries
from build_narration_pages import build_narration_pages, slug as narration_slug
import level2
from build_howto import build_howto, load_howtos, howtos_by_method
from build_ask import build_ask
import build_ladder
import qforms
import build_proof
import external
import build_search
from haro import SHOWN

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
     ("architecture", {"fr": "Architecture", "en": "Architecture"}),
     ("craft", {"fr": "Le métier", "en": "The craft"}),
     ("areas", {"fr": "Les domaines", "en": "The areas"}),
     ("code", {"fr": "Le code", "en": "The code"})]),
  ("compare", {"fr": "Comparée", "en": "Compared"}, [
     ("compare", {"fr": "Comparée", "en": "Compared"})]),
  ("narrations", {"fr": "Narrations", "en": "Narrations"}, [
     ("narrations", {"fr": "Narrations", "en": "Narrations"}),
     ("narrations-performance", {"fr": "Série performance", "en": "Performance series"}),
     ("narrations-security", {"fr": "Série sécurité", "en": "Security series"}),
     ("narrations-delivery", {"fr": "Série livraison", "en": "Delivery series"})]),
  ("vision", {"fr": "Vision", "en": "Vision"}, [
     ("vision", {"fr": "L'étoile polaire", "en": "The north star"}),
     ("principles", {"fr": "Douze principes", "en": "Twelve principles"}),
     ("estate", {"fr": "Le domaine", "en": "The estate"}),
     ("history", {"fr": "Depuis les principes", "en": "From first principles"}),
     ("forged", {"fr": "Forgée en projets", "en": "Forged in projects"}),
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
     ("howto", {"fr": "Comment faire", "en": "How-to"}),
     ("reference", {"fr": "Référence", "en": "Reference"}),
     ("ask", {"fr": "Interroger", "en": "Ask the library"}),
     ("education", {"fr": "Éducation", "en": "Education"})]),
  ("offering", {"fr": "Offre", "en": "Offering"}, [
     ("offering", {"fr": "Audiences", "en": "Audiences"}),
     ("journeys", {"fr": "Parcours", "en": "Journeys"}),
     ("editions", {"fr": "Éditions", "en": "Editions"}),
     ("customers", {"fr": "Clients", "en": "Customers"})]),
  ("start", {"fr": "Démarrer", "en": "Start"}, [
     ("start", {"fr": "Démarrer", "en": "Start"})]),
]
# Education is one page with three doors (the author, 2026-10-03: learning, teaching and pedagogic design are one flow, not Teaching and
# Pedagogy): the doors are pages of the Learn section one level below it, shown in the left bar, never a third entry of the path
SUBPAGES = {"education-self": "education", "education-teach": "education", "education-programme": "education", "education-record": "education"}
EDU_BAR = {"fr": ("Éducation", [("education", "Les trois portes"), ("education-self", "J'apprends seul"), ("education-teach", "J'enseigne ou je conçois"), ("education-programme", "Je dirige un programme"), ("education-record", "Ce qui est prouvé")]),
           "en": ("Education", [("education", "The three doors"), ("education-self", "I learn by myself"), ("education-teach", "I teach or design"), ("education-programme", "I run a programme"), ("education-record", "What is proved")])}
# The Craft page is the style's page (12.12) and the paradigms that follow from it are its chapters, shown in the same left bar
SUBPAGES.update({p: "platforms" for p in ("conversations", "environment", "polyglot")})
SUBPAGES.update({p: "craft" for p in ("goals", "way", "natural", "byexample", "softanzuter", "innovations")})
CRAFT_BAR = {"fr": ("Comment Softanza s'écrit", [("craft", "Comment Softanza s'écrit"), ("goals", "Sept buts de conception"), ("way", "La manière Softanza"), ("natural", "Naturel, et exécutable"), ("byexample", "Par l'exemple"),
                                                    ("softanzuter", "Le Softanzuter"), ("innovations", "Les innovations")]),
             "en": ("How Softanza is written", [("craft", "How Softanza is written"), ("goals", "Seven design goals"), ("way", "The Softanza way"), ("natural", "Natural, and executable"), ("byexample", "By example"),
                                                ("softanzuter", "The Softanzuter"), ("innovations", "Innovations")])}
PLATFORMS_BAR = {"fr": ("Plateforme de plateformes", [("platforms", "Plateforme de plateformes"), ("conversations", "Conversations"), ("environment", "L'environnement"), ("polyglot", "Sept langues, une porte")]),
                 "en": ("Platform of platforms", [("platforms", "Platform of platforms"), ("conversations", "Conversations"), ("environment", "The environment"), ("polyglot", "Seven languages, one door")])}
BARS = {"education": EDU_BAR, "craft": CRAFT_BAR, "platforms": PLATFORMS_BAR}
OLD_PAGES = {"teaching": "education", "pedagogy": "education"}        # the old addresses lead to the new page
GENERATED = {"reference", "narrations", "howto", "ask", "journeys", "narrations-performance", "narrations-security", "narrations-delivery"}   # built by code, not from a .md
OWNER = {}                                          # page -> its section
for sec, _, pages in SECTIONS:
    for slug, _ in pages: OWNER[slug] = sec
for _sp in SUBPAGES: OWNER[_sp] = OWNER[SUBPAGES[_sp]]
OWNER["atlas-group"] = "platform"
OWNER["guide"] = "learn"                            # a guide page sits under Documentation
OWNER["book-proof"] = "learn"                       # the proof of a chapter sits under The book

UI = {
  "fr": {
    "slogan": "La plateforme des artisans du logiciel à l'ère de l'IA", "second": "Née en Afrique. Utile au monde !",
    "skip": "Aller au contenu", "other_lang": "English", "other_code": "en",
    "present": "Présenter le site en diaporama", "github": "Le dépôt Softanza sur GitHub", "menu": "Menu principal", "path": "Pages de la section", "here": "Vous êtes ici", "moved": "Cette page est devenue Éducation",
    "proof_law": "Chaque affirmation de ce site renvoie au fichier, au garde ou au rendu qui la prouve. Chaque bloc de code qui s'exécute a été exécuté le soir de la publication et sa sortie est à côté ; les autres le disent.",
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
    "measured": "Mesuré contre", "folders": "Dossiers", "standouts": "Ce qu'un artisan en fait, et ce qui se distingue", "gaps": "Ce qui est dû",
    "lanes_h": "Les couloirs, un par un", "lanes_note": "Les couloirs et leurs notes sont cités tels qu'ils ont été lus à la source, le",
    "example": "Un exemple, exécuté", "no_example": "Aucun exemple exécuté sur cette page", "output": "Sortie",
    "source": "la source", "nopic": "Pas encore d'image", "guide": "Le guide des fonctions de ce domaine",
    "narr_title": "Narrations", "narr_title_html": "Les <i>narrations</i>", "narr_kicker": "Recherche",
    "narr_lede": "Les articles du projet : cent trente-cinq essais où les idées de Softanza ont d\'abord été argumentées, avec leur code de la main de l\'auteur.",
    "narr_desc": "Les 135 articles de Softanza, chacun une page : résumé, genre, domaine, année, et le code exécuté au nom de Haro.",
    "narr_note": "Liste lue dans le dossier doc/narrations du dépôt au commit 0e72e2e2c. Le 2026-10-02, chaque narration qui pouvait s'exécuter a été exécutée dans la bibliothèque, bloc après bloc dans un seul processus. Celles dont au moins trois blocs sur quatre tiennent leur promesse sont des pages de ce site, avec le verdict de chaque bloc ; les autres s'ouvrent sur GitHub, et la liste dit pourquoi.",
    "narr_groups": {"page": "Exécutées, pages de ce site", "run": "Exécutées, ne tenant pas encore leurs promesses : sur GitHub", "effects": "Non exécutées, elles touchent aux fichiers, au réseau, à la saisie, à l'horloge ou au hasard : sur GitHub", "names": "Non exécutées, leur code nomme l'ancien langage de la plateforme : sur GitHub", "compile": "Non exécutées, elles ne compilent pas telles qu'écrites : sur GitHub", "nocode": "Sans code à exécuter : sur GitHub"},
    "narr_kept": "{k} blocs sur {n} tiennent leur promesse",
    "narr_ex_ran": "un exemple de cette narration, exécuté le {d} dans la bibliothèque", "narr_ex_written": "un exemple tel que la narration l'écrit, non exécuté pour cette page", "narr_ex_none": "une narration qui raisonne, sans code à montrer",
    "cov_row": "Domaine", "cov_present": "Présent", "cov_deep": "Deep", "cov_solid": "Solid", "cov_partial": "Partial", "cov_none": "Absent",
  },
  "en": {
    "slogan": "The Software Crafters Platform of the AI Age", "second": "Born in Africa. Useful to the World!",
    "skip": "Skip to content", "other_lang": "Français", "other_code": "fr",
    "present": "Present the site as a slideshow", "github": "The Softanza repository on GitHub", "menu": "Main menu", "path": "Pages of the section", "here": "You are here", "moved": "This page became Education",
    "proof_law": "Every claim on this site links to the file, the guard or the render that proves it. Every code block that runs was run on the night of publication and its output sits beside it; the others say so.",
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
    "measured": "Measured against", "folders": "Folders", "standouts": "What a crafter does with it, and what stands out", "gaps": "What is owed",
    "lanes_h": "The lanes, one by one", "lanes_note": "Lanes and their notes are quoted as they were read at the source, on",
    "example": "One example, run", "no_example": "No example run on this page", "output": "Output",
    "source": "the source", "nopic": "No picture yet", "guide": "The guide to this area's functions",
    "narr_title": "Narrations", "narr_title_html": "The <i>narrations</i>", "narr_kicker": "Research",
    "narr_lede": "The articles of the project: one hundred and thirty-five essays in which the ideas of Softanza were first argued, with their code in the author's hand.",
    "narr_desc": "Softanza's 135 articles, each a page: abstract, genre, area, year, and the code run in Haro's name.",
    "narr_note": "List read in the repository's doc/narrations folder at commit 0e72e2e2c. On 2026-10-02 every narration that could run was run inside the library, block after block in one process. Those where at least three blocks in four keep their promise are pages of this site, with each block's verdict; the others open on GitHub, and the list says why.",
    "narr_groups": {"page": "Run, pages of this site", "run": "Run, not yet keeping their promises: on GitHub", "effects": "Not run, they touch files, the network, input, the clock or chance: on GitHub", "names": "Not run, their code names the platform's former language: on GitHub", "compile": "Not run, they do not compile as written: on GitHub", "nocode": "No code to run: on GitHub"},
    "narr_kept": "{k} of {n} blocks keep their promise",
    "narr_ex_ran": "an example of this narration, run on {d} inside the library", "narr_ex_written": "an example as the narration writes it, not run for this page", "narr_ex_none": "a narration that reasons, with no code to show",
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
READER_FLOOR = ("<style>/*stz-floor*/figure.cell figcaption,.out,nav.chapters,.note,p.draft,p.reviewed,p.stz-proof-ex"
                "{font-size:16px!important}a{color:var(--accent)}</style>")      # important: the reader styles some of these more specifically
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
<link rel="stylesheet" href="{rel}assets/css/search.css">
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

def header(lang, slug, rel, other_href=None, nav_rel=None, page_key=None, data_lang="", tail=None):
    """the main menu, and under it the path of the current section. A page deeper than the section's own pages passes its
    `tail`, [(label, href or None)], and the header pins where the reader is: Learn > Reference > String > stzString"""
    ui = UI[lang]
    if nav_rel is None: nav_rel = nav_prefix(rel, lang)
    key = page_key or slug
    sec = OWNER.get(key)
    current_page = {"atlas-group": "areas", "guide": "docs", "book-proof": "book", **SUBPAGES}.get(key, key)
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
    crumbs = ""
    if tail and sec:
        first = next(p for s_, _, p in SECTIONS if s_ == sec)
        items = [(next(lab for s_, lab, _ in SECTIONS if s_ == sec)[lang], f"{nav_rel}{first[0][0]}.html")]
        if current_page != first[0][0]: items.append((next(lab for p_, lab in first if p_ == current_page)[lang], f"{nav_rel}{current_page}.html"))
        items += list(tail)
        lis = "".join((f'<li><a href="{h}">{esc(l)}</a></li>' if h and k < len(items) - 1 else f'<li aria-current="page">{esc(l)}</li>') for k, (l, h) in enumerate(items))
        crumbs = f'\n  <nav class="crumbs" aria-label="{esc(ui["here"])}"><ol class="crumbs-in">{lis}</ol></nav>'
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
  </div>{path}{crumbs}
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
        out += f'\n<script src="{rel}assets/js/site.js"></script><script src="{rel}assets/js/search-core.js"></script><script src="{rel}assets/js/search.js"></script>{PAGE_PING}\n</body></html>'
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

COUNTS = {}                                         # figures read from the data, filled in main() before any page is built

def inject(body_html, lang, idx, groups, rel="../"):
    body_html = body_html.replace("<!--RUNTIME-->", RUNTIME[lang])
    fmt = (lambda n: f"{n:,}") if lang == "en" else (lambda n: f"{n:,}".replace(",", " "))
    body_html = body_html.replace("<!--METHODS-->", fmt(COUNTS["methods"])).replace("<!--CLASSES-->", fmt(COUNTS["classes"])).replace("<!--ENTRIES-->", fmt(COUNTS["entries"]))
    body_html = body_html.replace("<!--AREAS-->", fmap_html(lang, idx, groups, "atlas/") + tiles_html(lang, idx, groups, "atlas/", rel))
    body_html = body_html.replace("<!--ATLAS-WALL-->", tiles_html(lang, idx, groups, "atlas/", rel, themed=False))
    for tag, fn in (("LEADS", leads_html), ("RULES", rules_html), ("STEPS", steps_html), ("INNOVATIONS", innovations_html), ("GOALS", goals_html)):
        if f"<!--{tag}-->" in body_html: body_html = body_html.replace(f"<!--{tag}-->", fn(lang))
    body_html = body_html.replace("<!--COVERAGE-->", coverage_html(lang))
    body_html = body_html.replace("<!--DOCS-SCOPE-->", scope_html(lang, idx, groups))
    for tag, data_file in (("EDU", "edu-run.json"), ("FORGED", "forged-run.json"), ("EDUREC", "edu-record-run.json")):      # code the library ran for the page, beside what it printed
        if f"<!--{tag}:" in body_html or f"<!--{tag}-RAN-->" in body_html:
            run = json.loads((DATA / data_file).read_text(encoding="utf-8")) if (DATA / data_file).exists() else None
            if not run: raise SystemExit(f"<!--{tag}:...--> needs data/{data_file}: run its tool (tools/{ {'EDU': 'edu_run', 'FORGED': 'forged_run', 'EDUREC': 'edu_record_run'}[tag] }.py)")
            def run_block(m, run=run):
                seg = next(s for s in run["segments"] if s["name"] == m.group(1))
                ran = {"fr": "exécuté le {d} dans la bibliothèque au commit {c}", "en": "run on {d} inside the library at commit {c}"}[lang].format(d=run["ran"], c=run["commit"])
                lbl = {"fr": "Sortie", "en": "Output"}[lang]
                lcode = {"EDUREC": {"fr": "En ligne de commande", "en": "At the command line"}}.get(tag, {}).get(lang, "Softanza")
                return (f'<div class="run"><div><div class="lbl">{lcode}</div><pre>{esc(seg["code"])}</pre></div>'
                        f'<div class="out"><div class="lbl">{lbl}</div><pre>{esc(seg["out"])}</pre></div></div><p class="ran">{ran}</p>')
            body_html = re.sub(r"<!--" + tag + r":(\w+)-->", run_block, body_html).replace(f"<!--{tag}-RAN-->", run["ran"])
    if "<!--PROOF-->" in body_html:
        proof = build_proof.load(ROOT)
        if not proof: raise SystemExit("<!--PROOF--> needs data/proof-run.json: run tools/proof_run.py")
        body_html = body_html.replace("<!--PROOF-->", build_proof.proof_list_html(lang, proof))
    if "<!--LADDER-->" in body_html:
        ladder = build_ladder.load(ROOT)
        if not ladder: raise SystemExit("<!--LADDER--> needs data/ladder-run.json: run tools/ladder_run.py")
        body_html = body_html.replace("<!--LADDER-->", build_ladder.ladder_html(ladder, lang))
    # <!--SHOWCASE:slug-->: the runs of data/showcase.json inside a content page, under the page's own heading
    # <!--SHOWCASE:slug:2,3--> places chosen runs beside the idea they show (positions in the source list, from 1)
    body_html = re.sub(r"<!--SHOWCASE:([a-z0-9-]+)(?::([0-9,]+))?-->",
                       lambda m: showcase_html(lang, m.group(1), heading=False,
                                               only=[int(x) for x in m.group(2).split(",")] if m.group(2) else None), body_html)
    return diagram_imgs(body_html, rel)

LONG = []
def check_reading_arc(slug, lang, body_html):
    """Rule 123: a paragraph past about 800 characters has become a wall"""
    for p in re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>", body_html, re.S):
        t = re.sub(r"<[^>]+>", "", p)
        if len(t) > 800: LONG.append(f"{lang}/{slug}: {len(t)} chars: {t[:60]}...")

WAY_RX = re.compile(r'<p class="way"><span>(The Softanza way|La manière Softanza)</span>')
def page_shell(lang, slug, title, description, kicker, title_html, lede, body_html, rel="../", page_key=None, other_href=None, body_class=None, tail=None):
    if slug != "way":
        body_html = WAY_RX.sub(lambda m: f'<p class="way"><span><a href="{nav_prefix(rel, lang)}way.html">{m.group(1)}</a></span>', body_html)
    page = head(lang, f'{title} · Softanza', description, rel)
    page += f'\n<body class="{body_class or "page page-" + slug}">\n' + header(lang, slug, rel, other_href=other_href, page_key=page_key, tail=tail)
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
    parent = slug if slug in BARS else SUBPAGES.get(slug)
    if parent:
        label, items = BARS[parent][lang]
        page = level2.wrap(page, level2.nav(label, [("", [(f"{s}.html", n, "page" if s == slug else "") for s, n in items])]))
    out = ROOT / lang / f"{slug}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

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
SHOW_UI = {"fr": {"h": "La manière Softanza, exécutée", "ran": "exécuté le {d} dans la bibliothèque au commit {c} ; tiré de",
                  "intro": "Ce que Softanza fait autrement dans ce domaine, montré par du code tiré de ses narrations et de ses gardes, et exécuté pour cette page."},
           "en": {"h": "The Softanza way, run", "ran": "run on {d} inside the library at commit {c}; taken from",
                  "intro": "What Softanza does differently in this area, shown by code taken from its narrations and guards, and run for this page."}}
def load_showcase():
    f = DATA / "showcase.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
SHOWCASE = load_showcase()

def showcase_html(lang, slug, heading=True, only=None):
    items = SHOWCASE.get(slug)
    if not items:
        if not heading: raise SystemExit(f"no run in data/showcase.json for the placeholder SHOWCASE:{slug}")
        return ""
    # the site never names the platform's former language, and library code is never rewritten:
    # a run that shows the word in its code or output is left out (a .ring file name does not count)
    WORD = SHOWN   # the former name in code shown as the library wrote it (tools/haro.py)
    if any(WORD.search(it["code"]) or WORD.search(it["out"]) for it in items):
        if only:
            raise SystemExit(f"SHOWCASE:{slug}: a selected run shows the word; choose another run")
        items = [it for it in items if not (WORD.search(it["code"]) or WORD.search(it["out"]))]
    # a ...Q() call whose result nothing uses is not right (the plain form does the job): left out as well
    plain = qforms.get(ROOT).plain_anywhere
    if any(qforms.unchained(it["code"], plain) for it in items):
        if only:
            raise SystemExit(f"SHOWCASE:{slug}: a selected run calls a Q form and uses nothing of its result; choose another run")
        items = [it for it in items if not qforms.unchained(it["code"], plain)]
    if only:
        # a selection by position is only safe when every snippet of the source list kept its run
        src = json.loads((DATA / "showcase-src.json").read_text(encoding="utf-8")).get(slug, [])
        if len(src) != len(items):
            raise SystemExit(f"SHOWCASE:{slug}: {len(items)} runs kept of {len(src)} snippets; a selection by position would shift")
        items = [items[i - 1] for i in only]
    ui = SHOW_UI[lang]; out_lbl = "Sortie" if lang == "fr" else "Output"
    parts = [f'<h2>{ui["h"]}</h2><p>{ui["intro"]}</p>'] if heading else []
    for it in items:
        parts.append(f'<p style="margin-top:32px"><b>{esc(it["what_" + lang])}</b></p>'
                     f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(it["code"])}</pre></div>'
                     f'<div class="out"><div class="lbl">{out_lbl}</div><pre>{esc(it["out"])}</pre></div></div>'
                     f'<p class="ran">{ui["ran"].format(d=esc(it["ran"]), c=esc(it.get("commit", "0e72e2e2c")))} <a href="{esc(src_link(it["source"]))}">{esc(it["source"].split(" ")[0])}</a></p>')
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
    {area_articles(lang, g["slug"])}
    <h2>{ui["lanes_h"]}</h2>
    <p class="proof">{ui["lanes_note"]} {esc(d.get("dated", ""))}.</p>
    {note}
    <div class="lanes">{lanes}</div>"""
    page = page_shell(lang, "atlas", g[lang], g["line_" + lang], esc(band[lang]), esc(g[lang]), esc(g["line_" + lang]), body,
                      rel=rel, page_key="atlas-group", other_href=f"../../{ui['other_code']}/atlas/{g['slug']}.html", body_class="page page-atlas-group", tail=[(g[lang], None)])
    page = level2.wrap(page, level2.nav(level2.LABELS["areas"][lang], level2.area_groups(idx, lang, g["slug"])))
    out = ROOT / lang / "atlas" / f"{g['slug']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

RING_WORD = re.compile(r"\bRing\b")
NARR_UI = {
  "fr": {"note": "Lus dans le dossier doc/narrations du dépôt au commit {c}. Chaque article est une page. Le {d}, chacun a été exécuté au nom de Haro dans la bibliothèque, bloc après bloc ; un bloc qui a tenu sa promesse le dit, les autres sont des illustrations. Le code des articles est du code Haro : là où un article a été écrit avant que la langue prenne son nom actuel, le nom a été changé et rien d'autre. Genre, domaine et série sont lus dans le nom du fichier et l'année dans le premier commit : dérivés, jusqu'à ce que chaque article porte son propre en-tête.",
         "genre": "Genre", "area": "Domaine", "year": "Année", "family": "Famille", "family_off": "conçu, pas encore construit", "all": "tous",
         "shown": "{n} sur {t} affichés", "series_h": "Les séries", "series_p": "Une série se lit dans l'ordre.", "list_h": "Tous les articles",
         "kept": "{k} bloc(s) sur {n} ont tenu leur promesse", "noarea": "plusieurs domaines",
         "not": {"effects": "non exécuté : touche aux fichiers, au réseau, à l'horloge ou au hasard", "does not compile": "non exécuté : ne se charge pas tel qu'écrit", "no code": "sans code", "": "non exécuté"},
         "series": {"performance": ("Série performance", "La série performance", "Onze articles de 2026 sur la mesure : la charge, le profil, la trace, le jugement, le moniteur."),
                    "security": ("Série sécurité", "La série sécurité", "Quatorze articles de 2026 sur la sécurité : la porte d'entrée, les secrets, le registre, la détection, la réponse."),
                    "delivery": ("Série livraison", "La série livraison", "Cinq articles de 2026 sur la livraison : planifier, émuler, déployer, la virtualisation des services.")}},
  "en": {"note": "Read in the repository's doc/narrations folder at commit {c}. Every article is a page. On {d} each was run in Haro's name inside the library, block after block; a block that kept its promise says so, the others are illustrations. The code of the articles is Haro code: where an article was written before the language took its present name, the name was changed and nothing else. Genre, area and series are read from the file's name and the year from its first commit: derived, until each article carries its own header.",
         "genre": "Genre", "area": "Area", "year": "Year", "family": "Family", "family_off": "designed, not yet built", "all": "all",
         "shown": "{n} of {t} shown", "series_h": "The series", "series_p": "A series is read in order.", "list_h": "Every article",
         "kept": "{k} of {n} blocks kept their promise", "noarea": "several areas",
         "not": {"effects": "not run: touches files, the network, the clock or chance", "does not compile": "not run: does not load as written", "no code": "no code", "": "not run"},
         "series": {"performance": ("Performance series", "The performance series", "Eleven articles of 2026 on measuring: the load, the profile, the trace, the judgment, the monitor."),
                    "security": ("Security series", "The security series", "Fourteen articles of 2026 on security: the front door, the secrets, the ledger, detection, response."),
                    "delivery": ("Delivery series", "The delivery series", "Five articles of 2026 on delivery: planning, emulating, deploying, service virtualization.")}},
}
GENRE_ORDER = ["paradigm essay", "design essay", "feature essay", "comparison", "tutorial", "use case", "series"]
NARR_FILTER_JS = """<script>(function(){var l=document.getElementById('nlist');if(!l)return;var s=[].slice.call(document.querySelectorAll('.nfilters select[data-f]')),c=document.getElementById('ncount');
function go(){var n=0,t=0;[].forEach.call(l.children,function(li){var ok=s.every(function(x){return!x.value||li.getAttribute('data-'+x.getAttribute('data-f'))===x.value});li.hidden=!ok;t++;if(ok)n++});
if(c)c.textContent=c.getAttribute('data-t').replace('{n}',n).replace('{t}',t)}s.forEach(function(x){x.addEventListener('change',go)});go()})();</script>"""

def narration_items(lang, files, runs, cards, groups, rel=""):
    from build_narration_pages import GENRE as NGENRE, title_of
    nu = NARR_UI[lang]; names = {g["slug"]: g[lang] for g in groups}
    lis = []
    for f in files:
        r, c = runs[f], cards[f]
        if r.get("status") == "run" and r.get("blocks"):
            note = nu["kept"].format(k=sum(1 for b in r["blocks"] if b["verdict"] == "kept"), n=len(r["blocks"]))
        else:
            note = nu["not"].get(r.get("reason") or ("no code" if r.get("status") == "no code" else ""), nu["not"][""])
        area = names.get(c["area"], nu["noarea"]) if c["area"] else nu["noarea"]
        meta = " · ".join(x for x in (NGENRE[lang][c["genre"]], area, c["year"], c["author"], note) if x)
        lis.append(f'<li data-genre="{esc(c["genre"])}" data-area="{esc(c["area"] or "")}" data-year="{esc(c["year"])}">'
                   f'<a href="{rel}narrations/{narration_slug(f)}.html"><b>{esc(title_of(r))}</b></a>'
                   f'<p>{esc(c["abstract"])}</p><span class="rx-src">{esc(meta)}</span></li>')
    return "".join(lis)

def build_narrations(lang, published):
    ui, nu = UI[lang], NARR_UI[lang]
    runs = json.loads((DATA / "narrations-run.json").read_text(encoding="utf-8"))
    meta = json.loads((DATA / "narrations-meta.json").read_text(encoding="utf-8"))
    cards = meta["articles"]
    files = [f for f in published if f in cards]
    _, groups = load_atlas()
    from build_narration_pages import GENRE as NGENRE
    ran = max((runs[f].get("ran", "") for f in files), default="")[:10]
    files.sort(key=lambda f: (GENRE_ORDER.index(cards[f]["genre"]), cards[f]["date"], f))
    def options(key, values, label):
        opts = "".join(f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in values)
        return f'<label>{label} <select data-f="{key}"><option value="">{nu["all"]}</option>{opts}</select></label>'
    names = {g["slug"]: g[lang] for g in groups}
    areas = sorted({cards[f]["area"] for f in files if cards[f]["area"]}, key=lambda a: names.get(a, a))
    years = sorted({cards[f]["year"] for f in files if cards[f]["year"]})
    genres = [g for g in GENRE_ORDER if any(cards[f]["genre"] == g for f in files)]
    filters = (f'<div class="nfilters">{options("genre", [(g, NGENRE[lang][g]) for g in genres], nu["genre"])}'
               f'{options("area", [(a, names.get(a, a)) for a in areas], nu["area"])}{options("year", [(y, y) for y in years], nu["year"])}'
               f'<label>{nu["family"]} <select disabled><option>{nu["family_off"]}</option></select></label>'
               f'<span class="mono" id="ncount" data-t="{esc(nu["shown"])}"></span></div>')
    series = "".join(f'<li><a href="narrations-{k}.html"><b>{esc(v[1])}</b></a> <span class="mono">({sum(1 for f in files if cards[f]["series"] == k)})</span><p>{esc(v[2])}</p></li>'
                     for k, v in nu["series"].items())
    body = (f'<p class="proof">{esc(nu["note"].format(c=meta["commit"], d=ran))}</p>'
            f'<h2>{nu["series_h"]}</h2><p>{nu["series_p"]}</p><ul class="narr">{series}</ul>'
            f'<h2>{nu["list_h"]} <span class="mono">({len(files)})</span></h2>{filters}'
            f'<ol class="narr research" id="nlist">{narration_items(lang, files, runs, cards, groups)}</ol>{NARR_FILTER_JS}')
    page = page_shell(lang, "narrations", ui["narr_title"], ui["narr_desc"], esc(ui["narr_kicker"]), ui["narr_title_html"], esc(ui["narr_lede"]), body)
    (ROOT / lang / "narrations.html").write_text(page, encoding="utf-8")
    for k, v in nu["series"].items():
        sf = sorted((f for f in files if cards[f]["series"] == k), key=lambda f: (cards[f]["date"], f))
        body = (f'<p class="proof">{esc(nu["note"].format(c=meta["commit"], d=ran))}</p><p>{nu["series_p"]}</p>'
                f'<ol class="narr research">{narration_items(lang, sf, runs, cards, groups)}</ol>')
        page = page_shell(lang, f"narrations-{k}", v[0], v[2], esc(ui["narr_kicker"]), esc(v[1]), esc(v[2]), body)
        (ROOT / lang / f"narrations-{k}.html").write_text(page, encoding="utf-8")

def area_articles(lang, slug):
    """the articles of an Atlas area, listed on its page (12.16: each area lists its articles)"""
    f_meta, f_run = DATA / "narrations-meta.json", DATA / "narrations-run.json"
    if not (f_meta.exists() and f_run.exists()): return ""
    cards = json.loads(f_meta.read_text(encoding="utf-8"))["articles"]
    runs = json.loads(f_run.read_text(encoding="utf-8"))
    files = sorted((f for f, c in cards.items() if c["area"] == slug and f in runs and "text" in runs[f]), key=lambda f: (cards[f]["date"], f))
    if not files: return ""
    from build_narration_pages import title_of
    head_txt = {"fr": "Les articles de ce domaine", "en": "The articles of this area"}[lang]
    lis = "".join(f'<li><a href="../narrations/{narration_slug(f)}.html">{esc(title_of(runs[f]))}</a> <span class="mono">{esc(cards[f]["year"])}</span></li>' for f in files)
    return f'<h2>{head_txt} <span class="mono">({len(files)})</span></h2><ul class="narr">{lis}</ul>'

# ----------------------------------------------------------------------------
# the discipline, declared once (data/discipline.json), and the register of innovations (data/innovations.json)
def load_json(name): return json.loads((DATA / name).read_text(encoding="utf-8"))

def rules_html(lang):
    d = load_json("discipline.json")
    lis = "".join(f'<li id="rule-{r["n"]}" value="{r["n"]}">{esc(r[lang])} <code>{esc(r["ex"])}</code></li>' for r in d["rules"])
    return f'<ol class="rules">{lis}</ol>'

def steps_html(lang):
    d = load_json("discipline.json")
    lab = {"fr": "règles", "en": "rules"}[lang]
    lis = []
    for st in d["steps"]:
        rl = ", ".join(f'<a href="craft.html#rule-{n}">{n}</a>' for n in st["rules"])
        lis.append(f'<li value="{st["n"]}"><b>{esc(st[lang])}</b> <span class="rx-src">{lab} {rl}</span><code>{esc(st["sample"])}</code></li>')
    return f'<ol class="steps">{"".join(lis)}</ol>'

EVIDENCE_FR = [(r"a design of ([\d,]+) lines", r"une conception de \1 lignes"), (r"an analysis of ([\d,]+) lines", r"une analyse de \1 lignes"),
               (r"1 article of ([\d,]+) lines", r"1 article de \1 lignes"), (r"a design", "une conception"), (r"designs", "conceptions"), (r"a registry", "un registre"),
               (r"code files", "fichiers de code"), (r"code file", "fichier de code"), (r"test files", "fichiers de test"), (r"test blocks", "blocs de test"),
               (r"no test", "aucun test"), (r"engine modules", "modules du moteur"), (r"an engine module", "un module du moteur"), (r"engine module", "module du moteur"),
               (r"guards ([\d/]+) and ([\d/]+)", r"gardes \1 et \2"), (r"a guard of ([\d/]+)", r"garde : \1"), (r"guards", "gardes"),
               (r"the structured-output contract", "le contrat de sortie structurée"), (r"two engines", "deux moteurs"), (r"four instances", "quatre instances"),
               (r"promised examples", "exemples promis"), (r"the agent declared and reserved", "l'agent est déclaré et réservé"), (r"assertions", "assertions"),
               (r"articles", "articles"), (r"tags", "balises"), (r"files", "fichiers"), (r"lines", "lignes"), (r"and", "et")]
def evidence(lang, e):
    if lang == "en": return e
    for a, b in EVIDENCE_FR: e = re.sub(a, b, e)
    return e

PAGE_NAMES = {"conversations": {"fr": "Conversations", "en": "Conversations"}, "environment": {"fr": "L'environnement", "en": "The environment"}, "polyglot": {"fr": "Sept langues, une porte", "en": "Seven languages, one door"}, "goals": {"fr": "Sept buts de conception", "en": "Seven design goals"}, "softanzuter": {"fr": "Le Softanzuter", "en": "The Softanzuter"}, "natural": {"fr": "Naturel, et exécutable", "en": "Natural, and executable"},
              "byexample": {"fr": "Par l'exemple", "en": "By example"}, "craft": {"fr": "Comment Softanza s'écrit", "en": "How Softanza is written"},
              "refinement": {"fr": "Raffinement", "en": "Refinement"}, "wise": {"fr": "Wise coding", "en": "Wise coding"}, "agentic": {"fr": "Agentique", "en": "Agentic"},
              "languages": {"fr": "Langue des langues", "en": "Language of languages"}, "ask": {"fr": "Interroger la bibliothèque", "en": "Ask the library"},
              "narrations-delivery": {"fr": "Série livraison", "en": "Delivery series"}, "narrations-performance": {"fr": "Série performance", "en": "Performance series"},
              "narrations-security": {"fr": "Série sécurité", "en": "Security series"}}

def innovations_html(lang):
    from build_narration_pages import title_of
    reg = load_json("innovations.json")
    runs = load_json("narrations-run.json")
    told = {"fr": "Raconté ici", "en": "Told on this site"}[lang]
    ev = {"fr": "Preuves", "en": "Evidence"}[lang]
    out = [f'<p class="proof"><b>{ {"fr": "conçu", "en": "designed"}[lang] }</b> {esc(reg["read" if lang == "en" else "read_fr"])}</p>']
    for fam, (en, fr) in reg["families"].items():
        rows = [r for r in reg["rows"] if r[0] == fam]
        lis = []
        for _, n, nen, nfr, oen, ofr, evid, files, page in rows:
            links = []
            if page: links.append(f'<a href="{page}.html">{esc(PAGE_NAMES[page][lang])}</a>')
            for f in files:
                if f not in runs or "text" not in runs[f]: raise SystemExit(f"innovations.json row {n}: no article {f}")
                links.append(f'<a href="narrations/{narration_slug(f)}.html">{esc(title_of(runs[f]))}</a>')
            tl = " · ".join(links) if links else {"fr": "pas encore raconté sur ce site", "en": "not yet told on this site"}[lang]
            lis.append(f'<li><a id="i{n}"></a><b>{n} · {esc(nen if lang == "en" else nfr)}</b><p>{esc(oen if lang == "en" else ofr)}</p>'
                       f'<span class="rx-src">{ev} : {esc(evidence(lang, evid))}</span><br><span class="rx-src">{told} : </span>{tl}</li>')
        out.append(f'<h2>{esc(en if lang == "en" else fr)}</h2><ul class="narr research">{"".join(lis)}</ul>')
    return "".join(out)

# ----------------------------------------------------------------------------
# the journeys (data/journeys.json): who you are and what you are doing, with the anatomy underneath each step
STAGE_FR = {"built": "construit", "in construction": "en construction", "designed": "conçu", "specification": "spécification", "named": "nommé"}
STAGE_EN = {k: k for k in STAGE_FR}
JOURNEY_UI = {
  "fr": {"kicker": "Parcours", "hub_title": "Les parcours", "hub_title_html": "Les <i>parcours</i>",
         "hub_lede": "Une bibliothèque se présente d'ordinaire par son anatomie. Softanza se présente aussi par ce que vous êtes et ce que vous faites : un parcours par personne, ses étapes dans l'ordre où elle les prend, et sous chaque étape la partie de Softanza qui la sert, son étape de construction et une page qui la montre.",
         "hub_desc": "Neuf parcours, du programmeur à l'architecte de plateforme : pour chacun, des étapes dans l'ordre, la partie de Softanza qui sert chaque étape et son état.",
         "stage_intro": "Chaque étape porte son état, avec les mots de la page Domaine : construit, en construction, spécification, conçu, nommé. Un parcours peut paraître avec des étapes qui ne sont pas construites ; il le dit à chaque pas.",
         "focus_h": "Un focus, sans restriction", "focus": "Softanza sert n'importe quel besoin algorithmique, et l'Atlas en est la preuve d'étendue. Elle est mieux faite pour les domaines où ses couloirs sont forts, et ce focus est une mesure qui bouge avec la bibliothèque : les parcours s'appuient sur ces domaines, et l'Atlas garde les autres atteignables.",
         "steps_h": "Les étapes", "start_h": "Par où commencer", "pos_h": "La phrase de positionnement", "back": "Tous les parcours", "see": "voir",
         "doors_h": "Neuf parcours", "n_steps": "{n} étapes : {t}", "hub_p": "Les six portes de la page Audiences disent ce que chaque lecteur déclare et obtient ; les parcours disent comment il y va.",
         "arch_h": "Le neuvième", "arch": "Le parcours de l'architecte de plateforme est celui qui traverse toute la verticale, de la machine à l'organisation. C'est celui dont dépend l'offre commerciale : le directeur technique achète auprès d'un architecte."},
  "en": {"kicker": "Journey", "hub_title": "The journeys", "hub_title_html": "The <i>journeys</i>",
         "hub_lede": "A library is usually presented by its anatomy. Softanza is also presented by who you are and what you are doing: one journey per person, the steps in the order they take them, and under each step the part of Softanza that serves it, its stage of construction and a page that shows it.",
         "hub_desc": "Nine journeys, from the programmer to the platform architect: for each, the steps in order, the part of Softanza that serves each step, and its stage.",
         "stage_intro": "Every step carries its stage, in the words of the Estate page: built, in construction, specification, designed, named. A journey may be published with steps that are not built; it says so at every one.",
         "focus_h": "Focus without restriction", "focus": "Softanza serves any algorithmic need, and the Atlas is the proof of breadth. It is best made for the domains where its lanes are strong, and that focus is a measurement that moves with the library: the journeys stand on those domains and the Atlas keeps the rest reachable.",
         "steps_h": "The steps", "start_h": "Where to start", "pos_h": "The positioning sentence", "back": "All the journeys", "see": "see",
         "doors_h": "Nine journeys", "n_steps": "{n} steps: {t}", "hub_p": "The six doors of the Audiences page say what each reader declares and gets; the journeys say how they get there.",
         "arch_h": "The ninth", "arch": "The platform architect's journey is the one that crosses the whole vertical, from the machine up to the organisation. It is the journey the commercial offer depends on: the technical leader buys from an architect."},
}
def page_label(lang, page):
    """the name of a page of this site, as a reader meets it: the menu's word, the Atlas area's name, the article's title"""
    if page.startswith("narrations/"):
        from build_narration_pages import title_of
        runs = load_json("narrations-run.json")
        for f, r in runs.items():
            if "text" in r and narration_slug(f) == page[len("narrations/"):-5]: return title_of(r)
    elif page.startswith("atlas/") or page.startswith("guide/"):
        slug = page.split("/")[1][:-5]
        for g in load_atlas()[1]:
            if g["slug"] == slug: return g[lang] if page.startswith("atlas/") else {"fr": "Guide : ", "en": "Guide: "}[lang] + g[lang]
    else:
        slug = page[:-5]
        for j in load_json("journeys.json")["journeys"]:
            if slug == "journey-" + j["id"]: return j["name"][lang]
        for _, _, pages in SECTIONS:
            for sl, lab in pages:
                if sl == slug: return lab[lang]
        if slug in PAGE_NAMES: return PAGE_NAMES[slug][lang]
        if slug in ("education-record", "education-teach", "natural", "wise", "estate", "education", "start", "agents", "zui"): return {"education-record": {"fr": "Ce qui est prouvé", "en": "What is proved"}, "education-teach": {"fr": "J'enseigne ou je conçois", "en": "I teach or design"}}.get(slug, {}).get(lang, slug)
    return page

def journey_bar(lang, current):
    jd = load_json("journeys.json")
    ui = JOURNEY_UI[lang]
    items = [("journeys.html", ui["hub_title"], "page" if current == "journeys" else "")]
    items += [(f"journey-{j['id']}.html", j["name"][lang], "page" if current == "journey-" + j["id"] else "") for j in jd["journeys"]]
    return level2.nav(ui["hub_title"], [("", items)])

def stage_tally(lang, steps):
    names = STAGE_FR if lang == "fr" else STAGE_EN
    order = ["built", "in construction", "specification", "designed", "named"]
    return ", ".join(f"{sum(1 for st in steps if st['stage'] == k)} {names[k]}" for k in order if any(st["stage"] == k for st in steps))

def build_journeys(lang, idx, groups):
    jd = load_json("journeys.json")
    ui = JOURNEY_UI[lang]; names = STAGE_FR if lang == "fr" else STAGE_EN
    cards = "".join(f'<div class="card"><h3><a href="journey-{j["id"]}.html">{esc(j["name"][lang])}</a></h3><p>{esc(j["promise"][lang])}</p>'
                    f'<p class="rx-src">{esc(ui["n_steps"].format(n=len(j["steps"]), t=stage_tally(lang, j["steps"])))}</p></div>' for j in jd["journeys"])
    body = (f'<p>{ui["hub_p"]}</p><p>{ui["stage_intro"]}</p><h2>{ui["doors_h"]}</h2><div class="cards">{cards}</div>'
            f'<h2>{ui["focus_h"]}</h2><p>{ui["focus"]}</p>')
    page = page_shell(lang, "journeys", ui["hub_title"], ui["hub_desc"], esc(ui["kicker"]), ui["hub_title_html"], esc(ui["hub_lede"]), body, page_key="journeys")
    (ROOT / lang / "journeys.html").write_text(level2.wrap(page, journey_bar(lang, "journeys")), encoding="utf-8")
    for j in jd["journeys"]:
        lis = []
        for n, st in enumerate(j["steps"], 1):
            lis.append(f'<li value="{n}"><b>{esc(st[lang])}</b> <span class="rx-src">{names[st["stage"]]} · {ui["see"]}: <a href="{st["page"]}">{esc(page_label(lang, st["page"]))}</a></span></li>')
        pos = f'<h2>{ui["pos_h"]}</h2><p>{esc(j["positioning"][lang])}</p>' if j.get("positioning") else ""
        extra = f'<h2>{ui["arch_h"]}</h2><p>{ui["arch"]} <a href="journey-architect.html">{esc(jd["journeys"][-1]["name"][lang])}</a>.</p>' if j["id"] == "leader" else ""
        body = (f'<p class="rx-src">{esc(j["who"][lang])}</p><h2>{ui["steps_h"]}</h2><ol class="steps">{"".join(lis)}</ol>'
                f'<h2>{ui["start_h"]}</h2><p>{esc(j["start"][lang])}: <a href="{j["start"]["page"]}">{esc(page_label(lang, j["start"]["page"]))}</a>.</p>'
                f'{pos}{extra}<p><a href="journeys.html">{ui["back"]}</a></p>')
        page = page_shell(lang, f"journey-{j['id']}", j["name"][lang], j["promise"][lang], esc(ui["kicker"]), esc(j["name"][lang]), esc(j["promise"][lang]), body, page_key="journeys")
        (ROOT / lang / f"journey-{j['id']}.html").write_text(level2.wrap(page, journey_bar(lang, "journey-" + j["id"])), encoding="utf-8")

GOAL_UI = {"fr": {"tally": "Sur {n} fonctions : {t}.", "see": "ce que la fonction devient aujourd'hui", "ran": "Une exécution"},
           "en": {"tally": "Of {n} features: {t}.", "see": "what the feature is today", "ran": "A run"}}
def goals_html(lang):
    d = load_json("goals.json"); i = 0 if lang == "en" else 1
    ui = GOAL_UI[lang]
    counts = {}
    for g in d["goals"]:
        for f in g["features"]: counts[f[2]] = counts.get(f[2], 0) + 1
    n = sum(counts.values())
    order = ["built", "transformed", "changed", "partial", "archived", "name"]
    tally = ", ".join(f"{counts[k]} {d['states'][k][i]}" for k in order if k in counts)
    out = [f'<p class="proof">{esc(ui["tally"].format(n=n, t=tally))}</p>']
    for k, g in enumerate(d["goals"], 1):
        lis = "".join(f'<li><b>{esc(f[i])}</b> <span class="rx-src">{esc(d["states"][f[2]][i])} · {esc(f[4] if lang == "fr" else f[3])}</span></li>' for f in g["features"])
        out.append(f'<h2 id="{g["id"]}">{k} · {esc(g["name"][i])}</h2><p>{esc(g["why"][i])}</p><ul class="narr">{lis}</ul>'
                   + showcase_html(lang, "goals", heading=False, only=[k]))
    return "".join(out)

def leads_html(lang):
    cov = json.loads((DATA / "coverage.json").read_text(encoding="utf-8"))
    word = {"deep": {"fr": "de premier rang", "en": "deep"}, "solid": {"fr": "solide", "en": "solid"}, "partial": {"fr": "partiel", "en": "partial"}, "none": {"fr": "absent", "en": "absent"}}
    lis = []
    for g in cov["groups"]:
        for r in g["rows"]:
            if r["r"][0] not in ("partial", "none"): continue
            lead = [f'{cov["platforms"][k][1]}' for k in range(1, len(cov["platforms"])) if r["r"][k] == "deep"]
            who = ", ".join(lead) if lead else {"fr": "aucune des quatre n'est de premier rang", "en": "none of the four is deep"}[lang]
            link = (' <a href="polyglot.html">' + {"fr": "Et quand il faut Python lui-même", "en": "And when you need Python itself"}[lang] + "</a>.") if r["en"].startswith("Interop") else ""
            col = " :" if lang == "fr" else ":"
            lis.append(f'<li><b>{esc(r[lang])}</b> <span class="rx-src">Softanza{col} {word[r["r"][0]][lang]}</span> {({"fr": "Ils mènent", "en": "Where they lead"}[lang])}{col} {esc(who)}.{link}</li>')
    return f'<ul class="narr">{"".join(lis)}</ul>'

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
    page = head("fr", "Softanza · La plateforme des artisans du logiciel à l'ère de l'IA · The Software Crafters Platform of the AI Age",
                "Softanza: declare a language for your world, run it on one engine, let agents speak it safely. Born in Africa. Useful to the World.", "")
    page = page.replace('<html lang="fr" data-lang="fr">', '<html lang="fr" data-lang="fr" class="home">')
    heads = "".join(header(l, "index", "", other_href=f"index.html?lang={o}", nav_rel=f"{l}/", data_lang=l) for l, o in (("fr", "en"), ("en", "fr")))
    feet = "".join(footer(l, "", nav_rel=f"{l}/", scripts=False, data_lang=l) for l in LANGS)
    page += "\n<body class=\"home-body over-hero\">\n" + heads + '\n<main id="main">\n' + body + '\n</main>\n' + feet + f"""
<script src="assets/js/site.js"></script><script src="assets/js/search-core.js"></script><script src="assets/js/search.js"></script>{PAGE_PING}
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

BANNED = [(re.compile(r"\bZin\b"), "Zin: its innovations are Softanza's now, and the site never names it (the author, 2026-10-03)")]

# The runtime, said plainly (ruled by the author 2026-10-07, 12.6 of the external assessment): the one sentence in which the site's
# prose names the former language and its bridge. It is written HERE, once, and a page says <!--RUNTIME--> where it stands; the
# rule below refuses the name anywhere else in the prose, so the exception stays one sentence (and, when it is written, the page
# that tells why Softanza leaves it, 12.7, named in RING_PAGES).
RUNTIME = {"en": "Softanza runs today on its Ring face, kept so that the code already written keeps working. Ring++ is the bridge, "
                 "in construction. Haro is the destination.",
           "fr": "Softanza tourne aujourd'hui sur sa face Ring, gardée pour que le code déjà écrit continue de fonctionner. Ring++ est "
                 "le pont, en construction. Haro est la destination."}
RING_PAGES = set()
PROSE_RING = re.compile(r"(?<![\w./`-])Ring(?![\w.])")

def check_names():
    """the names the site does not say, looked for at the SOURCE (the markdown, the data, the diagrams), where a mention starts;
    reading the 4,000 built pages for it would cost minutes. Returns the list of (file, rule)."""
    bad = []
    for f in list((ROOT / "content").rglob("*.md")) + list((ROOT / "data").glob("*.json")) + list((ROOT / "tools" / "diagrams").glob("*.py")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for rx, why in BANNED:
            if rx.search(text): bad.append((f.relative_to(ROOT).as_posix(), why))
        if f.suffix == ".md" and f.parent.parent.name == "content" and f.stem not in RING_PAGES and PROSE_RING.search(text):
            bad.append((f.relative_to(ROOT).as_posix(), "names the former language: the prose says it only in the runtime's sentence (<!--RUNTIME-->)"))
    return bad

def main():
    external.install(ROOT)                 # every page is marked as it is written
    idx, groups = load_atlas()
    ENTRIES = load_entries(ROOT)
    COUNTS["methods"] = sum(len(c["own"]) for c in qforms.reference(ROOT)["classes"])    # a method is listed once: its extensions and its other names are folded into it
    COUNTS["classes"] = len(qforms.reference(ROOT)["classes"])        # one class under all its names
    COUNTS["entries"] = len(ENTRIES)
    npages, PUBLISHED = build_narration_pages({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "md": md, "groups": groups})
    _runs = json.loads((DATA / "narrations-run.json").read_text(encoding="utf-8"))
    print(f"narrations: {npages} pages, {len(PUBLISHED)} articles published, "
          f"{sum(1 for f in PUBLISHED if _runs[f].get('status') == 'run')} of them run in Haro's name (the run is a note, not a gate)")
    outs = []
    for lang in LANGS:
        for sec, _, pages in SECTIONS:
            for slug, _ in pages:
                if slug in GENERATED: continue
                outs.append(build_page(lang, slug, idx, groups))
        for slug in SUBPAGES:
            outs.append(build_page(lang, slug, idx, groups))
        for old, new in OLD_PAGES.items():                              # Teaching and Pedagogy became Education: the old address says so and goes there
            (ROOT / lang / f"{old}.html").write_text(
                f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{esc(UI[lang]["moved"])} · Softanza</title><meta name="robots" content="noindex">'
                f'<meta http-equiv="refresh" content="0;url={new}.html"><link rel="canonical" href="{new}.html"></head>'
                f'<body><p><a href="{new}.html">{esc(UI[lang]["moved"])}</a></p></body></html>', encoding="utf-8")
        build_narrations(lang, PUBLISHED)
        build_journeys(lang, idx, groups)
        for i in range(len(groups)):
            build_group_page(lang, idx, groups, i)
        for old in ("why", "govern", "makers", "products"):
            f = ROOT / lang / f"{old}.html"
            if f.exists(): f.unlink()
    scenes = {lang: build_tour(lang, idx, groups) for lang in LANGS}
    build_home(idx, groups)
    nref, ncls, nown = build_reference({"ROOT": ROOT, "LANGS": LANGS, "head": head, "header": header, "footer": footer, "idx": idx, "groups": groups, "entries": ENTRIES})
    HOWTOS = howtos_by_method(load_howtos(ROOT), qforms.get(ROOT))
    nmeth = build_methods({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "entries": ENTRIES, "howtos": HOWTOS})
    nhow, npub = build_howto({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "md": md, "entries": ENTRIES})
    print(f"how-to: {nhow} pages, {npub} recipes run and published")
    nproof, nproven = build_proof.build_proof({"ROOT": ROOT, "head": head, "header": header, "footer": footer})
    print(f"book proof: {nproof} pages, {nproven} chapters proven")
    nask, (hs, hv, ho, ag, nq) = build_ask({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "entries": ENTRIES,
                                            "groups": json.loads((DATA / "atlas-index.json").read_text(encoding="utf-8"))["groups"], "page_shell": page_shell})
    print(f"ask: {nask} pages; of {nq} recipe intents, HowTo same method {hs}, same verb {hv}, other {ho}; Ask top three {ag}; llms.txt and agents/index.json")
    print(f"method entries: {nmeth} pages, {len(ENTRIES)} methods with examples run")
    nguide = build_guides({"ROOT": ROOT, "head": head, "header": header, "footer": footer, "idx": idx, "groups": groups, "heritage": HERITAGE, "entries": ENTRIES})
    print(f"guides: {nguide} pages")
    assets = []
    for f in sorted((ROOT / "assets/fonts").glob("*.woff2")):
        assets.append({"kind": "font", "path": f"assets/fonts/{f.name}"})
    for sub in ("", "areas/", "diagrams/"):
        for f in sorted((ROOT / "assets/img" / sub).glob("*")):
            if f.is_file() and f.suffix.lower() in (".png", ".webp", ".jpg", ".svg"):
                assets.append({"kind": "image", "path": f"assets/img/{sub}{f.name}"})
    for f in ("fonts.css", "site.css", "search.css"):
        assets.append({"kind": "css", "path": f"assets/css/{f}"})
    for f in ("site.js", "tour.js", "search-core.js", "search.js"):
        assets.append({"kind": "script", "path": f"assets/js/{f}"})
    assets.append({"kind": "page", "path": "index.html"})
    for lang in LANGS:
        for sec, _, pages in SECTIONS:
            for slug, _ in pages:
                assets.append({"kind": "page", "path": f"{lang}/{slug}.html"})
        assets.append({"kind": "page", "path": f"{lang}/tour.html"})
    reader = ROOT / "reader.html"
    if reader.exists():
        r0 = reader.read_text(encoding="utf-8")
        r = r0 if "stzsite:'page'" in r0 else r0.replace("</body>", PAGE_PING + "</body>", 1)
        r = re.sub(r"<style>/[*]stz-floor[*]/.*?</style>", "", r, flags=re.S)       # the floor (Rules 105, 107): one stylesheet, by marker
        r = r.replace("</head>", READER_FLOOR + "</head>", 1)
        ladder = build_ladder.load(ROOT)
        if ladder: r = build_ladder.inject_reader(r, ladder)      # the rung of every chapter, under its title
        proof = build_proof.load(ROOT)
        if proof:                                                  # the bridge from each cell to its proof
            r = build_proof.inject_reader(r, proof)
            for w in build_proof.inject_reader.skipped: print("reader bridge skipped:", w)
        if r != r0: reader.write_text(r, encoding="utf-8")
        assets.append({"kind": "page", "path": "reader.html"})
    build_deck_check(assets)
    print(f"reference: {nref} pages, {ncls} classes, {nown} own methods")
    for f, why in check_names(): print(f"NAME CHECK FAILED  {f}: {why}")
    sc, sm, st, sp = build_search.build(ROOT, ENTRIES, groups)
    print(f"search index: {sc} classes, {sm:,} methods, {st:,} texts, {sp} pages")
    print(f"external links: {external.STATS['links']:,} marked, opening in a new tab, on {external.STATS['pages']:,} pages")
    print(f"built {len(outs)} pages + {2*len(groups)} area pages + atlas + narrations + index.html + deck-check.html; tour scenes fr={len(scenes['fr'])} en={len(scenes['en'])}")
    if LONG:
        print("reading arc (Rule 123), paragraphs past 800 characters:")
        for l in LONG: print("  ", l)
    print("contrast:")
    if not check_contrast():
        print("CONTRAST BELOW TARGET"); sys.exit(1)

if __name__ == "__main__":
    main()
