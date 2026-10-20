"""The story page of an area (Platform > The areas > <area>), composed from what the library and the Compass wrote.

The author, 2026-10-19: an area page must show the depth, the beauty, the innovation and the practicality of how the
area was designed, from the Compass pages, the narrations and the design documents. So the page is a sequence of
movements, each fed by a source that exists and is named:

  1. where it stands        the Compass: the rating bar, the thesis, the one-sentence position, the honesty line
  2. the picture            the render the platform drew for the area
  3. rethought              the heritage: the principle, what was kept, what was rethought (data/heritage.json)
  4. run                    the showcase: the Softanza way, run inside the library (data/showcase.json)
  5. the lanes              the Compass grid: each lane against its category leader, what ships, what is owed
  6. what is owed           the Compass tiers, ordered by return, with value and effort
  7. the design             the library's design documents of the area (data/designdocs.json, abstracts by hand)
  8. the articles           the narrations of the area, with their abstracts
  9. the classes            the classes of the area, each a door to the reference

Every sentence from the Compass is shown in English, as the Compass wrote it, and the page says so.
"""
import json, re, html, pathlib
import rowex

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
GH_BLOB = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"

def esc(s): return html.escape(str(s), quote=True)

def _load(name, default):
    f = DATA / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default

COMPASS = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted((DATA / "atlas-compass").glob("*.json"))} if (DATA / "atlas-compass").exists() else {}
DESIGN = _load("designdocs.json", {"docs": {}, "areas": {}})
ABSTRACTS = _load("designdocs-abstracts.json", {})
NARR_META = _load("narrations-meta.json", {"articles": {}})
NARR_RUN = _load("narrations-run.json", {})
REFERENCE = _load("reference.json", {"classes": []})
AREA_INTROS = _load("area-intros.json", {})      # the essay of each area, written by hand from the sources (the author, 2026-10-19)
INTRO_RUN = _load("intro-run.json", {})            # the samples inside the introductions, run in the library (tools/intro_run.py)
CLASS_INTROS = _load("class-intros.json", {})    # the introduction of a class and its most expressive uses, written by hand

RATING_CLASS = {"Strong": "strong", "Solid": "solid", "Partial": "partial", "Emerging": "emerging"}
RATINGS = ["Strong", "Solid", "Partial", "Emerging"]

T = {
  "fr": {"compass_h": "Où il en est", "compass_p": "La lecture du Compas Softanza : chaque couloir du domaine noté face au meilleur de sa catégorie, d'après ce que les gardes prouvent ({d}). Les phrases du Compas sont en anglais, telles qu'il les a écrites.",
         "lanes_h": "{n} couloirs, chacun face au meilleur de sa catégorie", "lanes_p": "Pour chaque couloir : ce qui tourne dans le moteur aujourd'hui, les outils contre lesquels il est juste de le mesurer, et ce qui reste dû.",
         "engine": "Dans le moteur", "against": "Mesuré contre", "owed": "Reste à faire",
         "tiers_h": "Ce qui est dû, dans l'ordre du rendement", "tiers_p": "Les manques, classés par ce qu'ils rapportent et non par leur taille ; la valeur est l'effet sur la portée de la bibliothèque, l'effort une lecture d'ingénieur.",
         "value": "Valeur", "effort": "Effort",
         "design_h": "La conception, telle que la bibliothèque l'a écrite", "design_p": "Les documents de conception de ce domaine, lus dans le dépôt au commit {c} : ce que chacun est, son plan, et le lien vers le texte entier.",
         "doc_meta": "{lines} lignes · {sections} sections · écrit le {first}{last}", "doc_last": ", revu le {d}", "outline": "Le plan", "read": "lire le document", "more_outline": "et {n} autres sections",
         "articles_h": "Les articles de ce domaine", "articles_p": "Les narrations que la bibliothèque a écrites sur ce domaine, chacune exécutée bloc par bloc avant d'être publiée ici.",
         "classes_h": "Les classes de ce domaine", "classes_p": "Chaque classe mène à sa page de référence : ses méthodes, chacune avec un exemple exécuté.", "methods": "méthodes", "more_classes": "et {n} autres classes dans la référence",
         "ref_door": "La référence de ce domaine, pour les programmeurs et les agents", "compass_src": "Compas Softanza : {d}.",
         "no_compass": "Le Compas n'a pas encore de page détaillée pour ce domaine ; les couloirs ci-dessous sont ceux de la carte de l'Atlas."},
  "en": {"compass_h": "Where it stands", "compass_p": "The Softanza Compass's reading: every lane of the area rated against the best of its category, by what the guards prove. {d}. The Compass's sentences are in English, as it wrote them.",
         "lanes_h": "{n} lanes, each against the best of its category", "lanes_p": "For every lane: what runs in the engine today, the tools it is fair to measure it against, and what is still owed.",
         "engine": "In the engine", "against": "Measured against", "owed": "Still owed",
         "tiers_h": "What is owed, in the order of return", "tiers_p": "The gaps, ordered by what they bring and not by their size; value is the effect on the library's reach, effort an engineer's reading.",
         "value": "Value", "effort": "Effort",
         "design_h": "The design, as the library wrote it", "design_p": "The design documents of this area, read in the repository at commit {c}: what each one is, its outline, and the link to the whole text.",
         "doc_meta": "{lines} lines · {sections} sections · written on {first}{last}", "doc_last": ", revised on {d}", "outline": "The outline", "read": "read the document", "more_outline": "and {n} more sections",
         "articles_h": "The articles of this area", "articles_p": "The narrations the library wrote about this area, each run block by block before it was published here.",
         "classes_h": "The classes of this area", "classes_p": "Each class leads to its reference page: its methods, each with an example run.", "methods": "methods", "more_classes": "and {n} more classes in the reference",
         "ref_door": "This area's reference, for programmers and agents", "compass_src": "The Softanza Compass: {d}.",
         "no_compass": "The Compass has no detailed page for this area yet; the lanes below are those of the Atlas card."},
}
VE = {"fr": {"High": "élevée", "Medium": "moyenne", "Low": "faible", "Strategic": "stratégique"}, "en": {"High": "high", "Medium": "medium", "Low": "low", "Strategic": "strategic"}}
VE_EFFORT = {"fr": {"High": "élevé", "Medium": "moyen", "Low": "faible"}, "en": {"High": "high", "Medium": "medium", "Low": "low"}}

RING = re.compile(r"\b(?:Ring|RING)\b")
def prose(s):
    """the site never names the platform's former language: the same rule as tools/build_guides.py"""
    return RING.sub(lambda m: "HARO" if m.group(0).isupper() else "Haro", str(s)).replace("Ring++", "Haro")

def mono(s):
    """`code` in the Compass's text becomes a code span"""
    return re.sub(r"`([^`]+)`", lambda m: f'<code>{esc(m.group(1))}</code>', esc(prose(s))).replace("&#x60;", "`")

def rating_bar(counts, lang):
    total = sum(counts.values()) or 1
    segs = "".join(f'<span style="flex:{counts[r]};background:var(--{RATING_CLASS[r]})"></span>' for r in RATINGS if counts[r])
    legend = " ".join(f'<span class="rk"><span class="dot" style="background:var(--{RATING_CLASS[r]})"></span>{counts[r]} {r}</span>' for r in RATINGS if counts[r])
    label = ", ".join(f"{counts[r]} {r}" for r in RATINGS if counts[r])
    return f'<div class="rate"><div class="ratebar" role="img" aria-label="{esc(label)}">{segs}</div><div class="rlegend">{legend}</div></div>'

def compass_head(lang, slug, d):
    """the Compass's thesis and its closing notes: the position sentence, the honesty line"""
    t = T[lang]; c = COMPASS.get(slug) or {}
    thesis = c.get("thesis") or d.get("thesis") or ""
    parts = [f'<h2>{t["compass_h"]}</h2><p class="proof">{t["compass_p"].format(d=esc(d.get("dated", "")))}</p>']
    if thesis: parts.append(f'<blockquote><p>{mono(thesis)}</p></blockquote>')
    for n in c.get("notes") or []:
        if n.get("lead") or n.get("text"):
            lead = f'<b>{mono(n["lead"])}</b> ' if n.get("lead") else ""
            parts.append(f'<div class="note"><p>{lead}{mono(n.get("text", ""))}</p></div>')
    return "".join(parts)

def lanes_html(lang, slug, d):
    t = T[lang]; c = COMPASS.get(slug) or {}
    lanes = c.get("lanes") or []
    if not lanes:
        rows = "".join(
            f'<div class="lane"><div class="ln">{esc(l["lane"])}</div><div class="lr"><span class="chip {RATING_CLASS.get(l["rating"], "solid")}">{esc(l["rating"])}</span></div>'
            f'<div class="lt">{esc(l["note"])}{("<small>" + esc(l["proof"]) + "</small>") if l.get("proof") else ""}</div></div>' for l in d.get("lanes", []))
        return (f'<h2>{t["lanes_h"].format(n=len(d.get("lanes", [])))}</h2><p>{t["no_compass"]}</p><div class="lanes">{rows}</div>') if rows else ""
    cards = []
    for l in lanes:
        peers = "".join(f'<span class="peer">{esc(p)}</span>' for p in (l.get("against") or []))
        cards.append(
            f'<article class="lc"><div class="lc-h"><span class="lc-n mono">{esc(l.get("n", ""))}</span><span class="lc-t">{esc(l["lane"])}</span>'
            f'<span class="chip {RATING_CLASS.get(l["rating"], "solid")}">{esc(l["rating"])}</span></div>'
            f'<div class="lc-b"><div><h4>{esc(l.get("engine_h") or t["engine"])}</h4><p>{mono(l.get("engine", ""))}</p>'
            + (f'<h4>{esc(l.get("against_h") or t["against"])}</h4><div class="peers">{peers}</div>' if peers else "") +
            f'</div><div class="owed"><h4>{esc(l.get("owed_h") or t["owed"])}</h4><p>{mono(l.get("owed", ""))}</p></div></div></article>')
    return f'<h2>{t["lanes_h"].format(n=len(lanes))}</h2><p>{t["lanes_p"]}</p><div class="lcs">{"".join(cards)}</div>'

def tiers_html(lang, slug):
    t = T[lang]; c = COMPASS.get(slug) or {}
    tiers = [x for x in (c.get("tiers") or []) if x.get("items")]
    if not tiers: return ""
    out = [f'<h2>{t["tiers_h"]}</h2><p>{t["tiers_p"]}</p>']
    for x in tiers:
        cards = []
        for it in x["items"]:
            tags = ""
            if it.get("value") or it.get("effort"):
                v = it.get("value"); e = it.get("effort")
                tags = '<div class="ve">' + (f'<span class="tag v">{t["value"]} · {esc(VE[lang].get(v, v))}</span>' if v else "") + (f'<span class="tag e">{t["effort"]} · {esc(VE_EFFORT[lang].get(e, e))}</span>' if e else "") + "</div>"
            cards.append(f'<article class="gap"><div class="gap-t">{mono(it.get("title", ""))}</div><p>{mono(it.get("text", ""))}</p>{tags}</article>')
        out.append(f'<div class="tier t{esc(x.get("tier", "A"))}"><h3>{mono(x.get("title", ""))}</h3><div class="gaps">{"".join(cards)}</div></div>')
    return "".join(out)

def design_html(lang, slug):
    t = T[lang]
    paths = DESIGN.get("areas", {}).get(slug) or []
    docs = [(p, DESIGN["docs"][p]) for p in paths if p in DESIGN.get("docs", {})]
    if not docs: return ""
    cards = []
    for p, x in docs:
        ab = ABSTRACTS.get(p, {}).get(lang, "")
        last = t["doc_last"].format(d=x["last"]) if x.get("last") and x.get("last") != x.get("first") else ""
        meta = t["doc_meta"].format(lines=f'{x["lines"]:,}'.replace(",", " " if lang == "fr" else ","), sections=x["sections"], first=x.get("first") or "?", last=last)
        outline = [prose(h) for h in (x.get("outline") or [])]
        shown = outline[:8]
        ol = "".join(f'<li>{esc(h)}</li>' for h in shown)
        more = f'<li class="more">{t["more_outline"].format(n=len(outline) - len(shown))}</li>' if len(outline) > len(shown) else ""
        cards.append(f'<article class="doc"><h3>{esc(prose(x["title"]))}</h3><p class="mono dmeta">{esc(meta)}</p>'
                     + (f'<p>{esc(ab)}</p>' if ab else "") +
                     (f'<p class="olabel">{t["outline"]}</p><ul class="outline">{ol}{more}</ul>' if ol else "") +
                     f'<p class="proof"><a href="{GH_BLOB}{esc(p)}">{t["read"]}</a> · <span class="mono">{esc(p)}</span></p></article>')
    return f'<h2>{t["design_h"]} <span class="mono">({len(docs)})</span></h2><p>{t["design_p"].format(c=esc(DESIGN.get("read_at", "")))}</p><div class="docs">{"".join(cards)}</div>'

def articles_html(lang, slug, narration_slug, title_of):
    t = T[lang]
    cards = NARR_META.get("articles", {})
    files = sorted((f for f, c in cards.items() if c.get("area") == slug and f in NARR_RUN and "text" in NARR_RUN[f]), key=lambda f: (cards[f].get("date") or "", f))
    if not files: return ""
    lis = []
    for f in files:
        c = cards[f]
        ab = prose(c.get("abstract") or "")
        lis.append(f'<li><a href="../narrations/{narration_slug(f)}.html">{esc(title_of(NARR_RUN[f]))}</a> <span class="mono">{esc(c.get("year") or "")}{(" · " + esc(c["genre"])) if c.get("genre") else ""}</span>'
                   + (f'<span class="abs">{esc(ab)}</span>' if ab else "") + "</li>")
    return f'<h2>{t["articles_h"]} <span class="mono">({len(files)})</span></h2><p>{t["articles_p"]}</p><ul class="narr arts">{"".join(lis)}</ul>'

def classes_html(lang, slug):
    t = T[lang]
    cs = sorted([c for c in REFERENCE.get("classes", []) if c.get("area") == slug], key=lambda c: -len(c["own"]))
    if not cs: return ""
    shown = cs[:24]
    rows = "".join(f'<div class="lane"><div class="ln mono"><a href="../reference/{c["name"].lower()}.html">{esc(c["name"])}</a></div><div class="lr mono">{len(c["own"])}</div><div class="lt">{esc(c["file"])}</div></div>' for c in shown)
    more = f'<p class="proof"><a href="../guide/{slug}.html">{t["more_classes"].format(n=len(cs) - len(shown))}</a></p>' if len(cs) > len(shown) else ""
    return (f'<h2>{t["classes_h"]} <span class="mono">({len(cs)})</span></h2><p>{t["classes_p"]}</p>'
            f'<div class="lanes"><div class="lane rhead"><div class="ln">Classe</div><div class="lr">{t["methods"]}</div><div class="lt">base/</div></div>{rows}</div>{more}'
            f'<p class="cta"><a href="../guide/{slug}.html">{t["ref_door"]}</a></p>').replace("<div class=\"ln\">Classe</div>", "<div class=\"ln\">Class</div>" if lang == "en" else "<div class=\"ln\">Classe</div>")

def lane_counts(slug, d, g):
    c = COMPASS.get(slug) or {}
    lanes = c.get("lanes") or d.get("lanes") or []
    counts = {r: 0 for r in RATINGS}
    for l in lanes:
        if l.get("rating") in counts: counts[l["rating"]] += 1
    if not any(counts.values()):
        counts = {"Strong": g["s"], "Solid": g["so"], "Partial": g["p"], "Emerging": g["e"]}
    return counts

# ---- a class's treasures, for its reference page -------------------------------------------------
CT = {
  "fr": {"h": "Ce que la bibliothèque a écrit sur cette classe", "area": "Le récit de son domaine", "ref": "La référence de son domaine",
         "docs": "Documents de conception qui la nomment", "mentions": "{n} mentions", "arts": "Narrations qui en parlent", "none": "Aucun document ni narration ne nomme cette classe ; sa page de domaine la situe."},
  "en": {"h": "What the library wrote about this class", "area": "The story of its area", "ref": "Its area's reference",
         "docs": "Design documents that name it", "mentions": "{n} mentions", "arts": "Narrations that speak of it", "none": "No document or narration names this class; its area page places it."},
}

def class_treasures(lang, cls, area, area_label, narration_slug, title_of):
    """for a class page: the design documents that name the class, the narrations that speak of it, and its two doors"""
    t = CT[lang]
    name = cls["name"]; low = name.lower()
    docs = sorted(((p, x["classes"][name]) for p, x in DESIGN.get("docs", {}).items() if x.get("classes", {}).get(name, 0) >= 3), key=lambda z: -z[1])[:6]
    cards = NARR_META.get("articles", {})
    arts = [f for f, c in cards.items() if f in NARR_RUN and "text" in NARR_RUN[f]
            and (low in f.lower() or low in (c.get("title") or "").lower() or low in (c.get("abstract") or "").lower())][:8]
    doors = ""
    if area:
        doors = f'<p class="proof"><a href="../atlas/{area}.html">{t["area"]}{": " if lang == "en" else " : "}{esc(area_label)}</a> · <a href="../guide/{area}.html">{t["ref"]}</a></p>'
    if not docs and not arts:
        return f'<div class="treasures">{doors}</div>' if doors else ""
    out = [f'<div class="treasures"><h2>{t["h"]}</h2>{doors}']
    if docs:
        lis = "".join(f'<li><a href="{GH_BLOB}{esc(p)}">{esc(prose(DESIGN["docs"][p]["title"]))}</a> <span class="mono">{t["mentions"].format(n=n)}</span>'
                      + (f'<span class="abs">{esc(ABSTRACTS.get(p, {}).get(lang, ""))}</span>' if ABSTRACTS.get(p, {}).get(lang) else "") + "</li>" for p, n in docs)
        out.append(f'<h3>{t["docs"]} <span class="mono">({len(docs)})</span></h3><ul class="narr arts">{lis}</ul>')
    if arts:
        lis = "".join(f'<li><a href="../narrations/{narration_slug(f)}.html">{esc(title_of(NARR_RUN[f]))}</a> <span class="mono">{esc(cards[f].get("year") or "")}</span>'
                      + (f'<span class="abs">{esc(prose(cards[f]["abstract"]))}</span>' if cards[f].get("abstract") else "") + "</li>" for f in arts)
        out.append(f'<h3>{t["arts"]} <span class="mono">({len(arts)})</span></h3><ul class="narr arts">{lis}</ul>')
    out.append("</div>")
    return "".join(out)


# ---- the essay of an area, and the introduction of a class ----------------------------------------
def essay_html(lang, slug):
    """the area told in a few paragraphs, written from the Compass, the design documents and the narrations"""
    e = AREA_INTROS.get(slug, {}).get(lang) or []
    if not e: return ""
    snippets = {x["id"]: x for x in INTRO_RUN.get("area:" + slug, [])}
    body = []
    for x in e:
        if x.startswith("@"):
            key = x[1:].strip()
            if "." in key:                                       # @stzTimeLine.blocked: the sample a class introduction runs
                cls, sid = key.split(".", 1)
                row = next((r for r in INTRO_RUN.get(cls, []) if r["id"] == sid), None)
                if row: body.append(sample_html(row, lang))
            elif key in snippets: body.append(sample_html(snippets[key], lang))   # a sample that did not run is left out
        else:
            body.append(f"<p>{para_html(x)}</p>")
    return '<div class="essay">' + "".join(body) + "</div>"

def para_html(x):
    """a paragraph written in the data: **bold** and `code` only"""
    h = esc(x)
    h = re.sub(r"\*\*(.+?)\*\*", lambda m: "<b>" + m.group(1) + "</b>", h)
    h = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", h)
    return h

USES_T = {"fr": {"h": "Les usages les plus parlants", "p": "{n} méthodes qui montrent ce que la classe sait faire ; chaque exemple a été exécuté dans la bibliothèque.", "one": "Une méthode qui montre ce que la classe sait faire ; son exemple a été exécuté dans la bibliothèque.", "all": "Toutes les méthodes, par section, plus bas."},
          "en": {"h": "The most expressive uses", "p": "{n} methods that show what the class is for; every example was run inside the library.", "one": "One method that shows what the class is for; its example was run inside the library.", "all": "Every method, by section, further down."}}
COUNT_WORDS = {"en": ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"], "fr": ["", "Une", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit"]}


SAMPLE_T = {"en": "run in the library on {d}", "fr": "exécuté dans la bibliothèque le {d}"}

def sample_html(sn, lang):
    """a sample the introduction shows in its own block, with the promise written under the line that printed it"""
    body = esc(rowex.promise_body(sn["code"], sn["out"]))
    return f'<div class="sample"><pre class="rx">{body}</pre><span class="rx-src">{SAMPLE_T[lang].format(d=esc(sn["ran"][:10]))}</span></div>'

def pick_example_html(cls, name, exs, rdata, lang):
    """the library example a captioned pick shows: the shortest one that CALLS the method, under a budget wide enough
    for an expressive example -- the row budget (five lines) is sized for a table cell, and a pick is not a cell"""
    call = re.compile(r"\b" + re.escape(name) + r"\s*\(", re.I)
    best = None
    for e in exs or []:
        code = e["code"].strip("\n")
        if code.count("\n") > 24 or len(code) > 900 or e["out"].count("\n") > 14 or len(e["out"]) > 700: continue
        if not call.search(code): continue
        key = (code.count("\n"), len(code))
        if best is None or key < best[0]: best = (key, e)
    if not best: return ""
    e = best[1]
    code = e["code"].strip("\n")
    body = esc(rowex.promise_body(code, e["out"]))
    src = {"en": "library test", "fr": "test de la bibliothèque"}[lang]
    return f'<pre class="rx">{body}</pre><span class="rx-src">{src}</span>'

def class_intro_html(lang, c, entries, rdata, example_html):
    """a class page opens on what the class is and what it is for, then on its most expressive uses, run"""
    ci = CLASS_INTROS.get(c["name"]) or {}
    paras = ci.get(lang) or []
    if not paras: return ""
    t = USES_T[lang]
    snippets = {x["id"]: x for x in INTRO_RUN.get(c["name"], [])}
    body = []
    for x in paras:
        if x.startswith("@") and x[1:].strip() in snippets:        # a sample of its own, between two paragraphs: never code inside a sentence
            body.append(sample_html(snippets[x[1:].strip()], lang))
        elif x.startswith("@"):
            continue                                                # a sample that did not run is left out, and the build says so
        else:
            body.append(f"<p>{para_html(x)}</p>")
    out = ['<div class="essay">' + "".join(body) + "</div>"]
    uses = []
    picks = ci.get("picks") or {}
    if isinstance(picks, list): picks = {m: {} for m in picks}
    keys = {k[1].lower(): k[1] for k in entries if k[0] == c["name"]}          # the method's registered spelling
    for m, cap in picks.items():
        name = keys.get(m.lower()) or next((o[0] for o in c.get("own", []) if o[0].lower() == m.lower()), None)   # a method with only a row example
        if not name: continue
        exs = entries.get((c["name"], name))
        ex = pick_example_html(c["name"], name, exs, rdata, lang) or example_html(c["name"], name, exs, rdata, lang)
        if not ex: continue
        if ex.startswith("<details"):                                        # a composed example, chosen and captioned on purpose: shown open
            ex = re.sub(r"^<details[^>]*><summary>[^<]*</summary>", "", ex).replace("</details>", "")
            if len(ex) > 700: continue                                       # unless its setup is a wall (a GeoJSON string is not an example)
        caption = cap.get(lang) if isinstance(cap, dict) else ""
        uses.append(f'<div class="use"><h3 class="mono">{esc(name)}</h3>' + (f"<p>{para_html(caption)}</p>" if caption else "") + ex + "</div>")
    if uses:
        n = len(uses)
        lead = t["one"] if n == 1 else t["p"].format(n=COUNT_WORDS[lang][n] if n < len(COUNT_WORDS[lang]) else str(n))
        out.append(f'<h2>{t["h"]}</h2><p>{lead}</p><div class="uses">{"".join(uses)}</div><p class="proof">{t["all"]}</p>')
    return "".join(out)
