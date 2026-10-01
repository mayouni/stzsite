"""Guide pages: one per area of the platform, under Learn > Documentation.

Learned from the Wolfram documentation's guide pages: a guide answers "what can
I do in this area, and with which functions?" It opens with one sentence on the
area, groups the functions by what they DO under plain headings, gives each one
a line of explanation, and points to the reference entry, the tutorials and the
related areas. Here the explanations are the library's own (data/reference.json,
harvested from the doc-comments), the groups come from the verb that leads each
function's name, and the tutorials are the narrations that run.
"""
import json, re, html, collections, pathlib

def esc(s): return html.escape(str(s), quote=True)
RING = re.compile(r"\bRing\b")
def prose(s): return esc(RING.sub("Haro", str(s)).replace("Ring++", "Haro"))

# the families a function belongs to, by the verb that leads its name
FAMILIES = [
  (("Is", "Has", "Contains", "Check", "Are", "Can"), "Testing and checking", "Tester et vérifier"),
  (("Find", "Search", "Position", "Positions", "Nth", "First", "Last", "Where", "Which"), "Finding", "Trouver"),
  (("Number", "Count", "Size", "Len", "How", "Sum", "Mean", "Average", "Min", "Max"), "Counting and measuring", "Compter et mesurer"),
  (("Replace", "Update", "Set", "Change"), "Replacing and setting", "Remplacer et modifier"),
  (("Remove", "Delete", "Trim", "Without", "Clear", "Strip"), "Removing", "Retirer"),
  (("Add", "Insert", "Append", "Extend", "Push"), "Adding", "Ajouter"),
  (("Split", "Splits", "Section", "Sections", "Sub", "Part", "Parts", "Slice", "Extract", "Chunk"), "Splitting and extracting", "Découper et extraire"),
  (("Sort", "Reverse", "Move", "Swap", "Shuffle", "Rotate", "Order"), "Ordering and moving", "Ordonner et déplacer"),
  (("To", "From", "Convert", "As", "Parse"), "Converting", "Convertir"),
  (("Show", "Boxed", "Box", "Print", "Format", "Pad", "Align", "Render", "Draw", "Plot"), "Showing, drawing and formatting", "Afficher, dessiner et mettre en forme"),
  (("Save", "Write", "Read", "Load", "Open", "Export", "Import"), "Reading and writing", "Lire et écrire"),
  (("Walk", "Each", "Map", "Filter", "Yield", "Apply", "Perform", "Run", "Execute"), "Walking and applying", "Parcourir et appliquer"),
]
SUFFIX = re.compile(r"(?:CS|Q|XT|XTT|Z|ZZ|W|WXT|IB|B|Q[RM])+$")

KEYWORDS = {
  "string": ["string", "text", "char", "unicode"], "regex": ["regex", "pattern"], "collections": ["list", "hashlist", "object", "set", "collection"],
  "numeric": ["number", "numeric", "math", "decimal", "exact"], "tables": ["table", "dataset", "data"], "i18n": ["locale", "language", "culture", "date", "time", "calendar"],
  "nlp": ["natural", "linguistic", "lemma", "nlp", "adverb", "words"], "neural": ["neural", "model"], "agents": ["agent", "conversation", "wise"],
  "graphics": ["graphic", "canvas", "color", "colour", "draw", "font"], "geo": ["geo", "map", "carto"], "diagramming": ["diagram", "graph", "drakon"],
  "gpu": ["gpu"], "gui": ["gui", "reactive", "interface"], "stats": ["stat", "chart", "plot", "histogram"], "system": ["system", "process", "file system"],
  "concurrency": ["concurren", "cluster", "distribut", "parallel", "multicore"], "web": ["server", "http", "web", "service"], "performance": ["perf", "profil"],
  "meta": ["meta", "rule", "reflect"], "files": ["file", "csv", "json", "xml", "html", "format"], "binary": ["binary", "byte"], "security": ["secur", "secret", "crypt"],
  "extensibility": ["extern", "plugin", "foreign", "python", "javascript"], "sound": ["sound", "music", "audio"], "testing": ["test", "guard", "promise", "assert"],
  "documentation": ["narration", "doc", "explain", "self"], "governance": ["govern", "safe", "court", "commit"],
}

T = {
  "fr": {"kicker": "Guide", "classes": "Les classes de ce domaine", "methods": "méthodes", "fn": "Les fonctions, par ce qu'elles font",
         "more": "et {n} autres dans la référence", "tut": "Les narrations sur ce domaine", "tut_none": "Aucune narration n'est encore rattachée à ce domaine.",
         "see": "Voir aussi", "atlas": "La page du domaine dans l'Atlas : ce qu'un maker en fait, un exemple exécuté, et ses couloirs notés",
         "same": "Les autres domaines de ce thème", "src": "Les explications sont celles que la bibliothèque donne d'elle-même, en anglais, lues dans ses commentaires de documentation le",
         "in": "dans"},
  "en": {"kicker": "Guide", "classes": "The classes of this area", "methods": "methods", "fn": "The functions, by what they do",
         "more": "and {n} more in the reference", "tut": "Narrations about this area", "tut_none": "No narration is attached to this area yet.",
         "see": "See also", "atlas": "The area's page in the Atlas: what a maker does with it, an example run, and its rated lanes",
         "same": "The other areas of this theme", "src": "The explanations are the ones the library gives of itself, read from its documentation comments on",
         "in": "in"},
}

def family_of(name):
    for verbs, en, fr in FAMILIES:
        for v in verbs:
            if name.startswith(v) and (len(name) == len(v) or name[len(v)].isupper()):
                return (en, fr)
    return None

def build_guides(ctx):
    ROOT, head, header, footer, idx, groups, heritage = (ctx[k] for k in ("ROOT", "head", "header", "footer", "idx", "groups", "heritage"))
    GH = "https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations/"
    ref = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
    narr = json.loads((ROOT / "data" / "narrations.json").read_text(encoding="utf-8"))
    classes = ref["classes"]; harvested = ref.get("harvested", "2026-10-01")
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]
        out_dir = ROOT / lang / "guide"; out_dir.mkdir(parents=True, exist_ok=True)
        for g in groups:
            slug = g["slug"]
            band = next(b for b in idx["bands"] if b["id"] == g["band"])
            cs = sorted([c for c in classes if c["area"] == slug], key=lambda c: -len(c["own"]))
            # the classes
            cls_rows = "".join(f'<li><a href="../reference/{c["name"].lower()}.html">{esc(c["name"])}</a> · {len(c["own"])} {t["methods"]}</li>' for c in cs[:24])
            # the functions, folded over their suffix forms, grouped by family
            fam = collections.OrderedDict((fr if lang == "fr" else en, []) for _, en, fr in FAMILIES)
            seen = set()
            for rank, c in enumerate(cs):
                names = {m[0] for m in c["own"]}
                for name, aka, desc in c["own"]:
                    base = SUFFIX.sub("", name) or name
                    if base != name and base in names: continue          # a suffix form of a function already listed
                    key = base.lower()
                    if key in seen or not desc or desc.lower().startswith("same as"): continue
                    f = family_of(name)
                    if not f: continue
                    seen.add(key)
                    fam[f[0] if lang == "en" else f[1]].append((name, desc, c["name"], rank))
            fam_html = []
            for label, items in fam.items():
                if not items: continue
                shown = sorted(items, key=lambda x: (x[3], len(x[0]), x[0]))[:12]
                lis = "".join(f'<li><a class="mono" href="../reference/{cl.lower()}.html#{esc(n.lower())}">{esc(n)}</a> {prose(d)} <span class="in">{t["in"]} {esc(cl)}</span></li>' for n, d, cl, _ in shown)
                more = f'<p class="proof">{t["more"].format(n=len(items) - len(shown))}</p>' if len(items) > len(shown) else ""
                fam_html.append(f'<h3>{esc(label)}</h3><ul class="fnlist">{lis}</ul>{more}')
            # the narrations
            kws = KEYWORDS.get(slug, [slug])
            rel_n = [n for n in narr if any(k in (n["file"] + " " + n["title"]).lower() for k in kws)][:12]
            tut = ("<ul>" + "".join(f'<li><a href="{GH}{esc(n["file"])}">{prose(n["title"])}</a></li>' for n in rel_n) + "</ul>") if rel_n else f'<p>{t["tut_none"]}</p>'
            same = " · ".join(f'<a href="{o["slug"]}.html">{esc(o[lang])}</a>' for o in groups if o["band"] == g["band"] and o["slug"] != slug)
            h = heritage.get(slug)
            lede = esc(h["principle_" + lang]) if h else esc(g["line_" + lang])
            body = (f'<h2>{t["fn"]}</h2>' + "".join(fam_html)
                    + f'<p class="proof">{t["src"]} {esc(harvested)}.</p>'
                    + f'<h2>{t["classes"]}</h2><ul>{cls_rows}</ul>'
                    + f'<h2>{t["tut"]}</h2>{tut}'
                    + f'<h2>{t["see"]}</h2><ul><li><a href="../atlas/{slug}.html">{t["atlas"]}</a></li>'
                    + (f'<li>{t["same"]} : {same}</li>' if lang == "fr" and same else (f'<li>{t["same"]}: {same}</li>' if same else "")) + '</ul>')
            title = g[lang]
            page = head(lang, f'{title} · {t["kicker"]} · Softanza', g["line_" + lang], "../../")
            page += '\n<body class="page page-guide">\n' + header(lang, "docs", "../../", other_href=f"../../{'en' if lang == 'fr' else 'fr'}/guide/{slug}.html", nav_rel="../", page_key="guide")
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{t["kicker"]} · {esc(band[lang])}</div>
    <h1>{esc(title)}</h1>
    <p class="lede">{lede}</p>
  </div></section>
  <div class="wrap page-body">
{body}
  </div>
</main>
"""
            page += footer(lang, "../../")
            (out_dir / f"{slug}.html").write_text(page, encoding="utf-8"); pages += 1
    return pages
