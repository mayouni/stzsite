"""The reference, generated from the library's own explanations.

data/reference.json is harvested by the library's stzSelfDoc (base/meta) over every
class source: each method's name, its doc-comment and its aliases, with the class
that defines it. This module turns it into fr|en/reference.html (the index by
area), fr|en/reference/<class>.html (one page per class) and
fr|en/reference/methods-<letter>.html (the alphabetical index). Called by build.py
with its helpers, so the chrome stays one."""
import json, re, html, collections
import level2, qforms, extshow, rowex
PIN_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})\.</p>")
def pin(page): return PIN_DATE.sub("2026-10-01.</p>", page)

GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/"

T = {
  "fr": {"title": "Référence", "kicker": "La bibliothèque se documente elle-même",
         "lede": "Chaque méthode de chaque classe, avec l'explication que la bibliothèque porte dans sa propre source, récoltée par son module d'auto-documentation. Rien ici n'a été écrit pour le site : c'est ce que la bibliothèque répond quand on l'interroge.",
         "desc": "La référence Softanza, générée depuis les explications que la bibliothèque porte dans sa source : {nc} classes, {n} méthodes propres.",
         "examples": "exemples exécutés", "with_ex": "méthodes avec des exemples exécutés", "rowex": "méthodes avec un exemple sur leur ligne", "classes": "classes", "own": "méthodes propres", "entries": "entrées de surface, héritage compris", "described": "décrites depuis la source",
         "by_area": "Par domaine", "class_h": "Classe", "own_h": "Méthodes", "inherited_h": "Héritées", "area_h": "Domaine",
         "methods_az": "Toutes les méthodes, de A à Z", "letter": "Lettre", "filter": "Filtrer les méthodes…", "filter_classes": "Filtrer les classes…",
         "source": "la source", "inherits": "Hérite aussi de", "method": "Méthode", "explanation": "Explication, telle que la source la porte", "aka": "aussi nommée", "written": "aussi écrite", "forms": "aussi acceptée", "name_of": "autre nom de", "other_name_of": "{a} est un autre nom de {r}",
         "chip_q": "chaînable", "chip_cs": "sensible à la casse", "chip_xt": "étendue", "no_desc": "(sans commentaire dans la source : le nom se lit comme une phrase)", "section": "dans la section",
         "note": "Les explications sont citées dans la langue de la source, l'anglais. Récolte : {harvested}. Un commentaire absent est signalé plutôt qu'inventé.",
         "area_edu": "Le Système d'apprentissage", "area_other": "Autres", "back": "Toutes les classes", "guide": "Le guide", "count_in": "méthodes propres dans", "page_title": "Référence"},
  "en": {"title": "Reference", "kicker": "The library documents itself",
         "lede": "Every method of every class, with the explanation the library carries in its own source, harvested by its self-documentation module. Nothing here was written for the site: it is what the library answers when asked.",
         "desc": "The Softanza reference, generated from the explanations the library carries in its source: {nc} classes, {n} own methods.",
         "examples": "examples run", "with_ex": "methods with examples run", "rowex": "methods with an example on their row", "classes": "classes", "own": "own methods", "entries": "surface entries, inheritance included", "described": "described from the source",
         "by_area": "By area", "class_h": "Class", "own_h": "Methods", "inherited_h": "Inherited", "area_h": "Area",
         "methods_az": "Every method, A to Z", "letter": "Letter", "filter": "Filter the methods…", "filter_classes": "Filter the classes…",
         "source": "the source", "inherits": "Also inherits from", "method": "Method", "explanation": "Explanation, as the source carries it", "aka": "also named", "written": "also written", "forms": "also accepted", "name_of": "another name of", "other_name_of": "{a} is another name of {r}",
         "chip_q": "chainable", "chip_cs": "case-sensitive", "chip_xt": "extended", "no_desc": "(no comment in the source: the name reads as a sentence)", "section": "in the section",
         "note": "Explanations are quoted in the language of the source, English. Harvest: {harvested}. A missing comment is reported rather than invented.",
         "area_edu": "The Learning System", "area_other": "Other", "back": "All classes", "guide": "The guide", "count_in": "own methods in", "page_title": "Reference"},
}

FILTER_JS = """<script>(function(){var i=document.getElementById('flt');if(!i)return;var rows=document.querySelectorAll('[data-k]');i.addEventListener('input',function(){var q=i.value.toLowerCase();for(var r=0;r<rows.length;r++){rows[r].hidden=q&&rows[r].getAttribute('data-k').indexOf(q)<0;}});})();</script>"""

RING = re.compile(r"\bRing\b")
def esc(s): return html.escape(str(s), quote=True)

RING = re.compile(r"\b(?:Ring|RING)\b")
def prose(s):
    """A description is prose the site renders under the language's current name,
    Haro; an identifier is never touched, so a method really named Ring stays Ring."""
    return esc(RING.sub(lambda m: "HARO" if m.group(0).isupper() else "Haro", str(s)).replace("Ring++", "Haro"))

def split_camel(name):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    return s.lower()

def chips(name, t):
    out = []
    base = name
    if base.endswith("Q"): out.append(("q", t["chip_q"])); base = base[:-1]
    if base.endswith("CS"): out.append(("cs", t["chip_cs"])); base = base[:-2]
    if base.endswith("XTT") or base.endswith("XT"): out.append(("xt", t["chip_xt"]))
    return "".join(f'<span class="fchip {k}">{esc(l)}</span>' for k, l in out)

NAMES = {
  "en": {"h": "Names", "p": "A thing is listed once, under its main name. Softanza gives many things several names so that code reads like a sentence; the reference does not turn each of them into an entry.",
         "kind": "Kind", "what": "What it is", "ex": "Example", "here": "Here",
         "rows": [("Another name of a class", "a class with nothing in it but its parent", "stz2DList and stzList2D are stzListOfLists; stzBarChart, stzVBarChart and stzVBarPlot are stzBarPlot",
                   "{nc} names fold under {nr} classes: one page, \"also named\" on it, and the old address leads there"),
                  ("Another name of a method", "a method whose whole body forwards to another, with the same parameters", "Length is NumberOfChars; IsLarger and IsLargerThan are HasMoreCharsThan",
                   "{nm:,} names fold under their main name, one row each, \"also written\" under it; the name that reads as a sentence is the main one"),
                  ("An extension", "a word added at the end of a name: the same method, one more word", "FindCS, FindZZ, FilterQ", "the strip under each method, and the catalogue above"),
                  ("A detour", "a spelling the host language forces, because it already holds the natural name", "IsAString() where IsString() reads right",
                   "examples show the natural name and say what it ran as; Haro removes the detour: {det}")]},
  "fr": {"h": "Les noms", "p": "Une chose est listée une fois, sous son nom principal. Softanza donne plusieurs noms à beaucoup de choses pour que le code se lise comme une phrase ; la référence n'en fait pas une entrée chacun.",
         "kind": "Sorte", "what": "Ce que c'est", "ex": "Exemple", "here": "Ici",
         "rows": [("Un autre nom d'une classe", "une classe qui ne contient rien que son parent", "stz2DList et stzList2D sont stzListOfLists ; stzBarChart, stzVBarChart et stzVBarPlot sont stzBarPlot",
                   "{nc} noms se replient sous {nr} classes : une page, « aussi nommée » dessus, et l'ancienne adresse y mène"),
                  ("Un autre nom d'une méthode", "une méthode dont tout le corps renvoie à une autre, avec les mêmes paramètres", "Length est NumberOfChars ; IsLarger et IsLargerThan sont HasMoreCharsThan",
                   "{nm:,} noms se replient sous leur nom principal, une ligne chacun, « aussi écrite » dessous ; le nom qui se lit comme une phrase est le principal"),
                  ("Une extension", "un mot ajouté à la fin d'un nom : la même méthode, un mot de plus", "FindCS, FindZZ, FilterQ", "la bande sous chaque méthode, et le catalogue ci-dessus"),
                  ("Un détour", "une graphie que le langage hôte impose, parce qu'il tient déjà le nom naturel", "IsAString() là où IsString() se lit bien",
                   "les exemples montrent le nom naturel et disent sous quel nom ils ont tourné ; Haro supprime le détour : {det}")]},
}

def names_section(lang, ref, nm):
    """the four kinds of name, said once on the reference index"""
    n = NAMES[lang]
    classes = ref["classes"]
    fills = {"nc": len(ref.get("class_aliases", {})), "nr": len({r for r in ref.get("class_aliases", {}).values()}),
             "nm": sum(len(v) for c in classes for v in c["also_written"].values()), "det": ", ".join(f"{a}() → {b}()" for a, b in nm.get("detours", {}).items())}
    rows = "".join(f'<div class="lane lane4"><div class="ln">{esc(k)}</div><div class="lt">{esc(w)}</div><div class="lt">{esc(e)}</div><div class="lt">{esc(h.format(**fills))}</div></div>' for k, w, e, h in n["rows"])
    head_ = f'<div class="lane lane4 rhead"><div class="ln">{n["kind"]}</div><div class="lt">{n["what"]}</div><div class="lt">{n["ex"]}</div><div class="lt">{n["here"]}</div></div>'
    return f'<h2 id="names">{n["h"]}</h2><p>{n["p"]}</p><div class="lanes rtable">{head_}{rows}</div>'

def also_html(names, t, key="aka"):
    """the other names of a class or a method, as one small line: the thing is listed once, under its root"""
    return f'<small>{t[key]}: <span class="mono">{esc(" · ".join(names))}</span></small>' if names else ""

def area_name(a, lang, area_title):
    if a in area_title: return area_title[a][lang]
    return T[lang]["area_edu"] if a == "education" else T[lang]["area_other"]

def class_bar(lang, area, names, current, state, prefix=""):
    """the second submenu of a class page, and of its method entries: the classes of its area"""
    items = [(f"{prefix}{n.lower()}.html", n, state if n == current else "") for n in sorted(names, key=str.lower)]
    return level2.nav(level2.LABELS["classes"][lang], [(area, items)])

def jump_html(lang, c):
    """a class page can hold two thousand methods: a way to the letter, and to each section the source names"""
    first, secs = {}, {}
    for name, aka, desc in c["own"]:
        first.setdefault(name[:1].upper() if name[:1].isalpha() else "#", name.lower())
        sec = c["sections"].get(name.lower())
        if sec: secs.setdefault(sec, name.lower())
    if len(first) < 4: return ""
    word = {"fr": ("Aller à", "Sections"), "en": ("Jump to", "Sections")}[lang]
    out = f'<nav class="jump" aria-label="{word[0]}"><p><b>{word[0]}</b> ' + " ".join(f'<a href="#{esc(i)}">{esc(L)}</a>' for L, i in sorted(first.items())) + "</p>"
    if len(secs) >= 3:
        out += f'<p><b>{word[1]}</b> ' + " · ".join(f'<a href="#{esc(i)}">{esc(" ".join(t.split())[:60])}</a>' for t, i in secs.items()) + "</p>"
    return out + "</nav>"

def build_reference(ctx):
    ROOT, LANGS, head, header, footer, idx, groups = (ctx[k] for k in ("ROOT", "LANGS", "head", "header", "footer", "idx", "groups"))
    entries = ctx.get("entries", {})
    from build_methods import slug as mslug
    data = qforms.reference(ROOT)       # a method is listed once: its ...Q() form is the same method that returns the object
    classes = data["classes"]
    aliases = data.get("class_aliases", {})        # other names of a class: one class, one page; the old address goes to it
    by_name = {c["name"].lower(): c for c in classes}
    n_own = sum(len(c["own"]) for c in classes)
    n_folded = sum(c["folded"] for c in classes)
    rdata = rowex.load(ROOT)                      # the example on each row: the library's own, or one composed and run for this site
    n_rowex = sum(sum(rowex.class_counts(c, entries, rdata)[:2]) for c in classes)
    n_entries = n_own + sum(sum(c["inherited"].values()) for c in classes)
    n_desc = sum(1 for c in classes for m in c["own"] if m[2])
    area_title = {g["slug"]: {l: g[l] for l in LANGS} for g in groups}
    area_order = [g["slug"] for g in groups] + ["education", ""]
    by_area = collections.defaultdict(list)
    for c in classes: by_area[c["area"]].append(c["name"])
    # the alphabetical index: method name -> [(class, has_desc)]
    az = collections.defaultdict(list)
    az_root = collections.defaultdict(set)         # another name -> the methods it is another name of
    for c in classes:
        for m in c["own"]:
            az[m[0]].append(c["name"])
            for other in c["also_written"].get(m[0].lower(), []):
                az[other].append(c["name"]); az_root[other].add(m[0])
    letters = sorted({(n[0].upper() if n[0].isalpha() else "#") for n in az})
    pages = 0
    for lang in LANGS:
        t = T[lang]; rel = "../"; rel2 = "../../"
        # ---- the index -------------------------------------------------------
        sections = []
        for a in area_order:
            cs = sorted([c for c in classes if c["area"] == a], key=lambda c: -len(c["own"]))
            if not cs: continue
            if a == "education": title = t["area_edu"]; link = f'<a href="learn.html">{esc(title)}</a>'
            elif a == "": title = t["area_other"]; link = esc(title)
            else: title = area_title[a][lang]; link = f'<a href="atlas/{a}.html">{esc(title)}</a>'
            rows = "".join(
                f'<div class="lane rrow" data-k="{esc(c["name"].lower())}"><div class="ln"><a href="reference/{c["name"].lower()}.html">{esc(c["name"])}</a></div>'
                f'<div class="lr mono">{len(c["own"])}</div><div class="lt">{esc(", ".join(f"{k} ({v})" for k, v in c["inherited"].items())) if c["inherited"] else "·"}'
                f'<small>{esc(c["file"])}</small>{also_html(c.get("also_named"), t)}{rowex.example_of_class(c, entries, rdata, lang)}</div></div>' for c in cs)
            sections.append(f'<h2 id="{a or "other"}">{link} <small class="mono">{sum(len(c["own"]) for c in cs)} {t["own"]} · {len(cs)} {t["classes"]}</small></h2>'
                            f'<div class="lanes rtable"><div class="lane rhead"><div class="ln">{t["class_h"]}</div><div class="lr">{t["own_h"]}</div><div class="lt">{t["inherited_h"]}</div></div>{rows}</div>')
        az_links = " ".join(f'<a class="chip solid" href="reference/methods-{L.lower() if L != "#" else "other"}.html">{L}</a>' for L in letters)
        page = head(lang, f'{t["title"]} · Softanza', t["desc"].format(nc=len(classes), n=f"{n_own:,}" if lang == "en" else f"{n_own:,}".replace(",", " ")), rel)
        page += '\n<body class="page page-reference">\n' + header(lang, "reference", rel)
        page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(t["kicker"])}</div>
    <h1>{esc(t["title"])}</h1>
    <p class="thesis">{esc(t["lede"])}</p>
    <div class="figures">
      <div class="figure"><b>{len(classes)}</b><span>{t["classes"]}</span></div>
      <div class="figure"><b>{n_own:,}</b><span>{t["own"]}</span></div>
      <div class="figure"><b>{n_entries:,}</b><span>{t["entries"]}</span></div>
      <div class="figure"><b>{n_folded:,}</b><span>{extshow.T[lang]["folded"]}</span></div>
      <div class="figure"><b>{n_rowex:,}</b><span>{t["rowex"]}</span></div>
      <div class="figure"><b>{len(entries):,}</b><span>{t["with_ex"]}</span></div>
      <div class="figure"><b>{round(100*n_desc/max(n_own,1))}%</b><span>{t["described"]}</span></div>
    </div>
    <p class="proof">{esc(t["note"].format(harvested=data["harvested"]))} · <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/meta/stzSelfDoc.ring">stzSelfDoc</a></p>
  </div></section>
  <div class="wrap page-body">
    {extshow.catalogue(lang, ROOT, n_folded)}
    {names_section(lang, data, qforms.names(ROOT))}
    <p class="azrow"><b>{t["methods_az"]}:</b> {az_links}</p>
    <input id="flt" class="flt" type="search" placeholder="{esc(t["filter_classes"])}" aria-label="{esc(t["filter_classes"])}">
    {"".join(sections)}
  </div>
</main>
"""
        page += footer(lang, rel, "").replace("</body>", FILTER_JS + "</body>")
        (ROOT / lang / "reference.html").write_text(pin(page), encoding="utf-8"); pages += 1
        # ---- one page per class ---------------------------------------------
        out_dir = ROOT / lang / "reference"; out_dir.mkdir(parents=True, exist_ok=True)
        for c in classes:
            a = c["area"]
            area_link = (f'<a href="../atlas/{a}.html">{esc(area_title[a][lang])}</a>' if a in area_title else
                         (f'<a href="../learn.html">{esc(t["area_edu"])}</a>' if a == "education" else esc(t["area_other"])))
            inh = " · ".join((f'<a href="{k.lower()}.html">{esc(k)}</a> ({v})' if k.lower() in by_name else f'{esc(k)} ({v})') for k, v in c["inherited"].items())
            rows = []
            for m in c["own"]:
                name, aka, desc = m
                d = prose(desc) if desc else f'<i>{esc(t["no_desc"])}</i> <span class="mono">{esc(split_camel(name))}</span>'
                aka_html = f'<small>{t["aka"]}: {prose(aka)}</small>' if aka else ""
                sec = c["sections"].get(name.lower())          # the harvest read a section title as this method's comment: say it is the section
                sec_html = f'<small>{t["section"]} <b>{prose(sec)}</b></small>' if sec else ""
                written = c["also_written"].get(name.lower(), [])
                written_html = also_html(written, t, "written")
                forms = qforms.names(ROOT).get("forms", {}).get(c["name"], {}).get(name)
                if forms: written_html += f'<small>{t["forms"]}: <span class="mono">{esc(" · ".join(forms))}</span></small>'
                anchors = "".join(f'<span id="{esc(w.lower())}"></span>' for w in written)       # the other names stay addressable
                exs = entries.get((c["name"], name))
                if exs:
                    href = f'{c["name"].lower()}/{mslug(name)}.html'
                    nm = f'<a href="{href}">{esc(name)}</a>'
                    ex_html = f' <a class="ex" href="{href}">{len(exs)} {t["examples"]}</a>'
                else:
                    nm, ex_html = esc(name), ""
                strip = extshow.row_strip(c["variants"].get(name.lower(), []), lang)
                rx = rowex.example_html(c["name"], name, exs, rdata, lang)
                rows.append(f'<div class="lane lane2 rrow" id="{esc(name.lower())}" data-k="{esc((name + " " + " ".join(written) + " " + desc).lower())}">{anchors}<div class="ln mono">{nm}</div><div class="lt">{d}{ex_html}{aka_html}{written_html}{sec_html}{rx}<span class="ext-line">{strip}</span></div></div>')
            for name, aka, desc, owner in c["extra"]:      # a method of an ancestor to which this class gives extensions
                exs = entries.get((c["name"], name))
                nm = f'<a href="{c["name"].lower()}/{mslug(name)}.html">{esc(name)}</a>' if exs else esc(name)
                d = prose(desc) if desc else f'<i>{esc(t["no_desc"])}</i> <span class="mono">{esc(split_camel(name))}</span>'
                strip = extshow.row_strip(c["variants"].get(name.lower(), []), lang)
                rows.append(f'<div class="lane lane2 rrow" id="{esc(name.lower())}" data-k="{esc((name + " " + desc).lower())}"><div class="ln mono">{nm}</div><div class="lt">{d}<small>{extshow.T[lang]["inherited"].format(owner=esc(owner))}</small><span class="ext-line">{strip}</span></div></div>')
            title = c["name"]
            page = head(lang, f'{title} · {t["title"]} · Softanza', f'{title}: {len(c["own"])} {t["own"]}', rel2)
            page += '\n<body class="page page-reference-class">\n' + header(lang, "reference", rel2, other_href=f"../../{'en' if lang == 'fr' else 'fr'}/reference/{c['name'].lower()}.html", nav_rel="../",
                                                                                  tail=[(area_name(c["area"], lang, area_title), f"../reference.html#{c['area'] or 'other'}"), (c["name"], None)])
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(t["kicker"])} · {area_link}</div>
    <h1 class="mono-title">{esc(title)}</h1>
    <p class="thesis">{len(c["own"])} {t["own"]} · {c["folded"]} {extshow.T[lang]["folded"]}{(" · " + t["inherits"] + " " + inh) if inh else ""}</p>
    {also_html(c.get("also_named"), t).replace("<small>", '<p class="thesis">').replace("</small>", "</p>")}
    <p class="proof"><a href="{GH}{esc(c["file"])}">{t["source"]}: base/{esc(c["file"])}</a> · <a href="../reference.html">{t["back"]}</a>{(' · <a href="../guide/' + a + '.html">' + t["guide"] + ' ' + esc(area_title[a][lang]) + '</a>') if a in area_title else ''}</p>
  </div></section>
  <div class="wrap page-body">
    {extshow.legend(lang, "../")}
    {rowex.legend(c, entries, rdata, lang)}
    {jump_html(lang, c)}
    <input id="flt" class="flt" type="search" placeholder="{esc(t["filter"])}" aria-label="{esc(t["filter"])}">
    <div class="lanes rtable"><div class="lane lane2 rhead"><div class="ln">{t["method"]}</div><div class="lt">{t["explanation"]}</div></div>{"".join(rows)}</div>
  </div>
</main>
"""
            page += footer(lang, rel2, "").replace("</body>", FILTER_JS + "</body>")
            page = level2.wrap(page, class_bar(lang, area_name(c["area"], lang, area_title), by_area[c["area"]], c["name"], "page"))
            (out_dir / f"{c['name'].lower()}.html").write_text(pin(page), encoding="utf-8"); pages += 1
        for alias, root in aliases.items():
            href = f"{root.lower()}.html"
            note = t["other_name_of"].format(a=alias, r=root)
            (out_dir / f"{alias.lower()}.html").write_text(
                f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{esc(alias)} · Softanza</title>'
                f'<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={href}"><link rel="canonical" href="{href}"></head>'
                f'<body><p><a href="{href}">{esc(note)}</a></p></body></html>', encoding="utf-8")
        # ---- the alphabetical index, one page per letter ----------------------
        for L in letters:
            names = sorted([n for n in az if (n[0].upper() if n[0].isalpha() else "#") == L], key=str.lower)
            rows = []
            for n in names:
                links = " · ".join(f'<a href="{cl.lower()}.html#{esc(n.lower())}">{esc(cl)}</a>' for cl in sorted(az[n]))
                other = f'<small>{t["name_of"]} <span class="mono">{esc(" · ".join(sorted(az_root[n])))}</span></small>' if n in az_root else ""
                rows.append(f'<div class="lane rrow" data-k="{esc(n.lower())}"><div class="ln mono">{esc(n)}</div><div class="lr mono">{len(az[n])}</div><div class="lt">{links}{other}{"" if n in az_root else rowex.example_for_method(n, az[n], entries, rdata, lang)}</div></div>')
            rows = "".join(rows)
            page = head(lang, f'{t["methods_az"]} · {L} · Softanza', t["desc"].format(nc=len(classes), n=f"{n_own:,}" if lang == "en" else f"{n_own:,}".replace(",", " ")), rel2)
            page += '\n<body class="page page-reference-az">\n' + header(lang, "reference", rel2, other_href=f"../../{'en' if lang == 'fr' else 'fr'}/reference/methods-{L.lower() if L != '#' else 'other'}.html", nav_rel="../",
                                                                                  tail=[(t["methods_az"], "methods-a.html"), (f'{t["letter"]} {L}', None)])
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(t["methods_az"])}</div>
    <h1>{esc(t["letter"])} {esc(L)} <small class="mono">{len(names)}</small></h1>
    <p class="proof"><a href="../reference.html">{t["back"]}</a></p>
  </div></section>
  <div class="wrap page-body">
    <input id="flt" class="flt" type="search" placeholder="{esc(t["filter"])}" aria-label="{esc(t["filter"])}">
    <div class="lanes rtable">{rows}</div>
  </div>
</main>
"""
            page += footer(lang, rel2, "").replace("</body>", FILTER_JS + "</body>")
            letters_bar = level2.nav(level2.LABELS["letters"][lang], [("", [(f"methods-{X.lower() if X != '#' else 'other'}.html", X, "page" if X == L else "") for X in letters])])
            page = level2.wrap(page, letters_bar)
            (out_dir / f"methods-{L.lower() if L != '#' else 'other'}.html").write_text(pin(page), encoding="utf-8"); pages += 1
    return pages, len(classes), n_own
