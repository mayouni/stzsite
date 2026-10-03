"""Method entries with graded examples: one page per method that has examples run.

Learned from the Wolfram reference page and decided in doc/DOCUMENTATION-DESIGN.md
(D3): an entry says what the method does, shows the family of forms its verb
belongs to, and gives examples graded by purpose, each heading carrying the
count of examples that ran. Here every example is a test file of the library,
run inside the library for the site (tools/examples_run.py); only those whose
output kept every promise their file wrote are shown.

    fr|en/reference/<class>/<method>.html
"""
import json, re, html, collections
import level2, qforms, extshow

def esc(s): return html.escape(str(s), quote=True)
RING = re.compile(r"\b(?:Ring|RING)\b")
RING_WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)   # the word, not a .ring file name
def prose(s): return esc(RING.sub(lambda m: "HARO" if m.group(0).isupper() else "Haro", str(s)).replace("Ring++", "Haro"))
ISSUE = re.compile(r"(?i)\b(error|raises?|refus\w*|cannot|can't|invalid|not allowed|incorrect|unsupported|not found)\b")

T = {
  "fr": {"kicker": "Référence", "forms": "Les formes de ce verbe", "basic": "Exemples de base", "scope": "Portée", "issues": "Points d'attention",
         "out": "Sortie", "ran": "exécuté le {d} dans la bibliothèque au commit 0e72e2e2c ; tiré de", "see": "Voir aussi",
         "class": "La classe", "guide": "Le guide du domaine", "also": "Les autres méthodes de ces exemples",
         "no_desc": "Pas encore d'explication dans la source :", "aka": "aussi", "howto": "Comment faire",
         "proof": "Chaque exemple est un fichier de test de la bibliothèque, exécuté dans la bibliothèque pour cette page ; seuls ceux dont la sortie a tenu toutes les promesses écrites par leur fichier sont montrés. Les explications, les titres et le code sont ceux de la bibliothèque, en anglais.",
         "more": "et {n} autres dans les tests"},
  "en": {"kicker": "Reference", "forms": "The forms of this verb", "basic": "Basic examples", "scope": "Scope", "issues": "Possible issues",
         "out": "Output", "ran": "run on {d} inside the library at commit 0e72e2e2c; taken from", "see": "See also",
         "class": "The class", "guide": "The area's guide", "also": "The other methods in these examples",
         "no_desc": "No explanation in the source yet:", "aka": "also", "howto": "How-to",
         "proof": "Every example is a test file of the library, run inside the library for this page; only those whose output kept every promise their file wrote are shown.",
         "more": "and {n} more in the tests"},
}
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"

def slug(name): return re.sub(r"[^a-z0-9@_-]", "_", name.lower())

def load_entries(ROOT):
    f = ROOT / "data" / "examples.json"
    entries = collections.defaultdict(list)
    Q = qforms.get(ROOT)
    if f.exists():
        for ex in json.loads(f.read_text(encoding="utf-8")):
            # the site never names the platform's former language; library code is never rewritten,
            # so an example that shows the word, in its code or its output, is left out
            if RING_WORD.search(ex["code"]) or RING_WORD.search(ex["out"]):
                continue
            # a ...Q() call whose result nothing uses is not right (the plain form does the job): left out too
            if qforms.unchained(ex["code"], Q.plain_anywhere):
                continue
            # a method is listed once: its ...Q() form is the same method, so an example of one is an example of the other
            for key in {(cls, Q.fold(cls, meth)) for cls, meth in ex["methods"]}:
                entries[key].append(ex)
    return entries

def entry_href(cls, meth, rel_to_reference):
    return f"{rel_to_reference}{cls.lower()}/{slug(meth)}.html"

def split_camel(name): return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name).lower()

def run_block(ex, t):
    return (f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(ex["code"])}</pre></div>'
            f'<div class="out"><div class="lbl">{t["out"]}</div><pre>{esc(ex["out"])}</pre></div></div>'
            f'<p class="ran">{t["ran"].format(d=esc(ex["ran"]))} <a href="{GH}{esc(ex["source"])}">{esc(ex["source"].split("/")[-1])}</a></p>')

def build_methods(ctx):
    ROOT, head, header, footer, entries = (ctx[k] for k in ("ROOT", "head", "header", "footer", "entries"))
    howtos = ctx.get("howtos", {})
    from build_howto import intent as howto_intent, page_name as howto_page
    ref = qforms.reference(ROOT)
    Q = qforms.get(ROOT)
    by_class = {c["name"]: c for c in ref["classes"]}
    by_area = collections.defaultdict(list)
    for c in ref["classes"]: by_area[c["area"]].append(c["name"])
    from build_reference import class_bar, area_name
    area_title = {g["slug"]: g for g in json.loads((ROOT / "data" / "atlas-index.json").read_text(encoding="utf-8"))["groups"]}
    # the entry folders hold nothing but generated pages: clear them, so an entry that no longer qualifies leaves no page
    import shutil
    for lang in ("fr", "en"):
        for d in (ROOT / lang / "reference").glob("*"):
            if d.is_dir(): shutil.rmtree(d)
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]
        for (cls, meth), exs in sorted(entries.items()):
            c = by_class.get(cls)
            if not c: continue
            own = {m[0]: m for m in c["own"]}
            rec = Q.records(cls).get(meth.lower())            # the method may be defined in a class this one inherits from
            name, aka, desc = (rec[0], rec[1], rec[2]) if rec else (meth, "", "")
            # the voices of the verb: the active form and its passive twin (Remove, Removed). An extension is not a voice: it is
            # the same method, and the extensions table says which exist
            ml = meth.lower()
            fam = [n for n in own if n.lower() in (ml, ml + "d", ml + "ed") or (ml.endswith("ed") and n.lower() == ml[:-2]) or (ml.endswith("d") and n.lower() == ml[:-1])]
            fam = sorted(set(fam) | {meth}, key=lambda n: (len(n), n))[:18]
            fam_html = " · ".join((f'<b class="mono">{esc(n)}</b>' if n == meth else
                                   f'<a class="mono" href="{slug(n)}.html">{esc(n)}</a>' if (cls, n) in entries else
                                   f'<a class="mono" href="../{cls.lower()}.html#{esc(n.lower())}">{esc(n)}</a>') for n in fam)
            # grading: the issues, then the shortest as basic, the rest as scope
            issues = [e for e in exs if ISSUE.search(e["out"]) or ISSUE.search(e["expected"])]
            rest = sorted([e for e in exs if e not in issues], key=lambda e: (e["code"].count("\n"), len(e["code"])))
            basic, scope = rest[:2], rest[2:]
            more = max(0, len(scope) - 8); scope = scope[:8]
            sections = []
            for label, group in ((t["basic"], basic), (t["scope"], scope), (t["issues"], issues)):
                if not group: continue
                sections.append(f'<h2>{label} <span class="mono">({len(group)})</span></h2>' + "".join(run_block(e, t) for e in group))
            if more: sections.append(f'<p class="proof">{t["more"].format(n=more)}</p>')
            others = sorted({(c2, Q.fold(c2, m2)) for e in exs for c2, m2 in e["methods"] if (c2, Q.fold(c2, m2)) != (cls, meth)})
            other_html = " · ".join((f'<a class="mono" href="../{c2.lower()}/{slug(m2)}.html">{esc(c2)}.{esc(m2)}</a>' if (c2, m2) in entries
                                     else f'<span class="mono">{esc(c2)}.{esc(m2)}</span>') for c2, m2 in others[:12])
            a = c.get("area")
            guide = f'<li><a href="../../guide/{a}.html">{t["guide"]} : {esc(area_title[a][lang])}</a></li>'.replace(" : ", ": " if lang == "en" else " : ") if a in area_title else ""
            see = (f'<h2>{t["see"]}</h2><ul><li><a href="../{cls.lower()}.html#{esc(meth.lower())}">{t["class"]} {esc(cls)}</a></li>{guide}'
                   + (f'<li>{t["also"]} : {other_html}</li>'.replace(" : ", ": " if lang == "en" else " : ") if other_html else "")
                   + "".join(f'<li>{t["howto"]} : <a href="../../howto/{howto_page(r)}.html">{esc(howto_intent(r, lang))}</a></li>'.replace(" : ", ": " if lang == "en" else " : ")
                             for r in howtos.get((cls, meth), []))
                   + "</ul>")
            lede = prose(desc) if desc else f'{t["no_desc"]} <span class="mono">{esc(split_camel(meth))}</span>'
            aka_html = f'<p class="proof">{t["aka"]}: {prose(aka)}</p>' if aka else ""
            rel = "../../../"
            other = "en" if lang == "fr" else "fr"
            page = head(lang, f'{cls}.{meth} · {t["kicker"]} · Softanza', f'{cls}.{meth}: {desc or split_camel(meth)}'[:300], rel)
            page += '\n<body class="page page-reference-method">\n' + header(lang, "reference", rel, other_href=f"../../../{other}/reference/{cls.lower()}/{slug(meth)}.html", nav_rel="../../",
                                                                                 tail=([(area_title[a][lang], f"../../reference.html#{a}")] if a in area_title else []) + [(cls, f"../{cls.lower()}.html"), (f"{meth}()", None)])
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{t["kicker"]} · <a href="../{cls.lower()}.html">{esc(cls)}</a></div>
    <h1 class="mono-title">{esc(meth)}()</h1>
    <p class="lede">{lede}</p>
    {aka_html}
  </div></section>
  <div class="wrap page-body">
    {f'<h2>{t["forms"]}</h2><p>{fam_html}</p>' if len(fam) > 1 else ''}
    {"".join(sections)}
    {extshow.method_table(c["variants"].get(meth.lower(), []), lang)}
    <p class="proof">{t["proof"]}</p>
    {see}
  </div>
</main>
"""
            page += footer(lang, rel)
            a_names = {k: {l: v[l] for l in ("fr", "en")} for k, v in area_title.items()}
            page = level2.wrap(page, class_bar(lang, area_name(c["area"], lang, a_names), by_area[c["area"]], cls, "location", "../"))
            out = ROOT / lang / "reference" / cls.lower()
            out.mkdir(parents=True, exist_ok=True)
            (out / f"{slug(meth)}.html").write_text(page, encoding="utf-8"); pages += 1
    return pages
