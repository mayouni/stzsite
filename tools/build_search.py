"""The search index of the site: what the field of the header and of the reference looks through.

The author, 2026-10-03: the search field of the reference is impractical; whatever is entered, it should help find classes,
methods, even the descriptions inside texts and the code inside examples, quickly and visually, and always structured as
category > class > method.

Two files, both plain scripts (a script loads from the page opened on disk as well as from the web; a fetch of a json does not):

  assets/search/names.js   always loaded when the field gets the focus: the areas, the classes, every method's name with its
                           class, its other names and whether it has an example, and the titles of the guides, how-to
                           recipes, narrations and book chapters. About 130 KB compressed.
  assets/search/text.js    loaded only when the reader asks for it: every method's description and the first lines of its
                           example and what they printed. About a megabyte compressed, so it is never loaded unasked: a reader
                           on a metered connection chooses.

The matching itself is assets/js/search-core.js, which runs in the page and in node (tools/search_check.mjs measures it).
"""
import json, re, html, pathlib, datetime
import qforms, rowex

def esc(s): return html.escape(str(s), quote=True)
TITLE = re.compile(r"<title>(.*?)(?:\s*[·|]\s*[^<]*)?</title>", re.S)

def slug(name): return re.sub(r"[^a-z0-9@_-]", "_", name.lower())

def page_titles(ROOT, lang, sub, kind):
    out = []
    d = ROOT / lang / sub
    if not d.exists(): return out
    for f in sorted(d.glob("education*.html" if kind == "education" else "*.html")):
        m = TITLE.search(f.read_text(encoding="utf-8", errors="replace")[:4000])
        if m: out.append((kind, html.unescape(m.group(1)).strip(), f"{sub}/{f.name}" if sub else f.name))
    return out

def build(ROOT, entries, groups):
    ref = qforms.reference(ROOT)
    rdata = rowex.load(ROOT)
    detours = rdata.get("detours", {})
    areas = [[g["slug"], g["en"], g["fr"]] for g in groups] + [["education", "The Learning System", "Le Système d'apprentissage"], ["", "Other", "Autres"]]
    aidx = {a[0]: i for i, a in enumerate(areas)}
    classes, methods, text = [], [], []
    order = sorted(ref["classes"], key=lambda c: (aidx.get(c["area"], 99), c["name"].lower()))
    cidx = {c["name"]: i for i, c in enumerate(order)}
    for ci, c in enumerate(order):
        anc = ",".join(str(cidx[k]) for k in c["inherited"] if k in cidx)         # the classes it inherits from: their methods are its methods
        classes.append([c["name"], aidx.get(c["area"], len(areas) - 1), ",".join(c.get("also_named", [])), len(c["own"]), anc])
        for m in sorted(c["own"], key=lambda m: m[0].lower()):
            name, aka, desc = m
            exs = entries.get((c["name"], name))
            ex = rowex.pick(c["name"], name, exs, rdata)
            forms = sorted({v[0] for v in c["variants"].get(name.lower(), [])}, key=lambda n: (len(n), n))      # FindW, FindCS...: typed as written, found under the method
            methods.append([name, ci, slug(name) if exs else "", ",".join(c["also_written"].get(name.lower(), [])), 1 if ex else 0, ",".join(forms[:30])])
            mi = len(methods) - 1
            code = out = ""
            if ex:
                code, used = rowex.natural(ex[0], detours)
                code = " ".join(l.strip() for l in code.split("\n") if l.strip())[:170]
                out = " ".join(str(ex[1]).split())[:90]
            d = " ".join((desc or "").split())[:220]
            if d or code: text.append([mi, d, code, out])
    pages = []
    RING = re.compile(r"Ring")
    runs = json.loads((ROOT / "data" / "narrations-run.json").read_text(encoding="utf-8"))
    from build_narration_pages import slug as nslug
    GHN = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/"
    for f, r in sorted(runs.items()):                                  # every narration, run or not: the page when there is one, else its file
        title = RING.sub("Haro", r.get("title") or f).replace("Ring++", "Haro").replace("`", "")
        page = (ROOT / "en" / "narrations" / f"{nslug(f)}.html")
        pages.append(["narration", title, title, f"narrations/{nslug(f)}.html" if page.exists() else GHN + f, f[:-3] if f.endswith(".md") else f])
    for lang in ("en", "fr"):
        for kind, sub in (("guide", "guide"), ("howto", "howto"), ("book", "book"), ("education", "")):
            for k, title, url in page_titles(ROOT, lang, sub, kind):
                if lang == "en": pages.append([k, title, "", url, ""])
                else:
                    for p in pages:
                        if p[3] == url: p[2] = title
    names = {"v": 1, "built": datetime.date.today().isoformat(), "areas": areas, "classes": classes, "methods": methods, "pages": pages}
    d = ROOT / "assets" / "search"; d.mkdir(parents=True, exist_ok=True)
    dump = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    (d / "names.js").write_text("window.STZ_SEARCH_NAMES=" + dump(names) + ";", encoding="utf-8")
    (d / "text.js").write_text("window.STZ_SEARCH_TEXT=" + dump({"v": 1, "m": text}) + ";", encoding="utf-8")
    return len(classes), len(methods), len(text), len(pages)
