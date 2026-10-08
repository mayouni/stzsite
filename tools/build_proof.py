"""From a cell of the book to its proof, in one gesture.

Pedagogy proposed it as a "pro bridge": one gesture from any cell of the
book to the guard that proves it. The reader is the library's page and stores no
output, by the course's own law, so the proof is a run, and a page of this site
records one: tools/proof_run.py ran every chapter in its four editions, each in
one fresh process, compared every promise with what its cell printed, compared
the promises across editions, and had every exercise prove itself on its wrong
and right answers. From that run this module writes

  - fr|en/book/<chapter>.html : the proof of one chapter, cell by cell, with the
    guard that proves it and how to run it alone;
  - the list of the 15 chapters on the book page (placeholder <!--PROOF-->);
  - the bridge inside the reader (reader.html): under each chapter title, a line
    with the chapter's verdict; on each cell, a link to its place on its proof
    page; on each exercise, a line saying it proves itself. They sit between
    <!--stz-proof--> markers in the site's copy of the reader, so a rebuild
    replaces them rather than stacking them. Arabic and Hausa get only the
    library's own names and numbers, never a sentence written by the site.
"""
import json, re, html, sys
import level2

def esc(s): return html.escape(str(s), quote=True)
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from haro import FORMER as WORD      # the former name, standing alone; a name the library owns (```ring, learn.ring, Ring++) is not it
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"
GUARD = GH + "base/test/education/course_narrated.ring"
NATIVE = {"en": "English", "fr": "Français", "ar": "العربية", "ha": "Hausa"}

T = {
  "fr": {"kicker": "Le livre · Chapitre {n}", "title_suffix": "La preuve",
         "ok": "Ce chapitre a {c} cellules et écrit {p} promesses. Dans chacune de ses quatre éditions, ses cellules ont été exécutées dans un processus neuf le {d} : {eds}. Les quatre éditions font les mêmes promesses, cellule pour cellule. Aucune édition ne stocke de sortie.",
         "ed": "{lang}, {c} cellules exécutées, {p} promesses tenues",
         "notok": "Ce chapitre n'a pas tout prouvé le {d}. {why}",
         "g_h": "Le garde", "g_p": "Le garde du cours est <a href=\"{u}\">course_narrated.ring</a> : il exécute chaque chapitre dans les quatre langues, compare les promesses d'une édition à l'autre, et fait prouver chaque exercice sur ses mauvaises et ses bonnes réponses. Cette page a posé les mêmes questions aux mêmes objets, dans un seul processus à l'intérieur de la bibliothèque, au commit 0e72e2e2c. Pour prouver ce chapitre seul, depuis votre copie du dépôt :",
         "g_cmd": "# exécutez course_narrated avec le moteur d'exécution du dépôt, pour ce chapitre :",
         "g_law": "Le lecteur ne stocke aucune sortie, par la loi du cours ; cette page est le compte rendu d'une exécution, faite pour elle.",
         "ran": "exécuté le {d} dans la bibliothèque au commit {c}, en {s} s pour tout le livre",
         "haro": "Le code est montré au nom de Haro : là où le chapitre a été écrit avant que la langue prenne son nom actuel, le nom a été changé et rien d'autre, et le chapitre a été exécuté de nouveau ainsi. Le lien vers la source mène au texte tel qu'il a été écrit.",
         "cells_h": "Les cellules, exécutées", "cell": "Cellule", "out": "Sortie de cette exécution",
         "hidden": "Le code de cette cellule montre l'ancien nom du langage de la plateforme, que ce site ne montre pas. Elle a été exécutée ; son verdict est ci-dessous, et sa place dans le chapitre est liée.",
         "kept": "exécutée : la promesse est tenue", "kept_all": "dans les quatre éditions", "nopromise": "exécutée : cette cellule n'écrit aucune promesse",
         "broken": "exécutée : a affiché autre chose que sa promesse", "raised": "n'a pas tourné",
         "where": "Cette cellule dans le chapitre", "ex_h": "Les exercices",
         "ex_p": "Chaque exercice s'éprouve lui-même : ses mauvaises réponses sont refusées et ses bonnes acceptées.",
         "ex_ok": "{wr} mauvaises réponses refusées sur {w}, {ra} bonnes acceptées sur {r}", "refused": "refusée", "accepted": "acceptée",
         "folder": "Le dossier de l'exercice", "files": "Les quatre éditions du chapitre",
         "book": "Le livre", "list_h": "La preuve de chaque chapitre",
         "list_p": "Chaque cellule du livre mène à sa preuve : une page par chapitre dit ce que le garde du cours a trouvé en exécutant ce chapitre dans ses quatre éditions, cellule par cellule, et comment le refaire.",
         "list_row": "{c} cellules, {k} promesses tenues · {x} exercices qui s'éprouvent", "lang_note": "Le code des cellules est celui de l'édition anglaise ; les titres viennent de l'édition française. Les quatre éditions font les mêmes promesses, cellule pour cellule.",
         "r_ch": "Preuve · {c} cellules exécutées, {k} promesses tenues, dans chacune des quatre éditions · <a href=\"{u}\">la preuve de ce chapitre</a>",
         "r_cell": "Preuve de cette cellule", "r_ex": "Cet exercice s'éprouve lui-même : {wr} mauvaises réponses refusées sur {w}, {ra} bonnes acceptées sur {r} · <a href=\"{u}\">la preuve</a>"},
  "en": {"kicker": "The book · Chapter {n}", "title_suffix": "The proof",
         "ok": "This chapter has {c} cells and writes {p} promises. In each of its four editions its cells were run in one fresh process on {d}: {eds}. The four editions make the same promises, cell for cell. No edition stores any output.",
         "ed": "{lang}, {c} cells ran, {p} promises kept",
         "notok": "This chapter did not prove everything on {d}. {why}",
         "g_h": "The guard", "g_p": "The course's guard is <a href=\"{u}\">course_narrated.ring</a>: it runs every chapter in all four languages, compares the promises from one edition to the next, and has every exercise prove itself on its wrong and right answers. This page asked the same questions of the same objects, in one process inside the library, at commit 0e72e2e2c. To prove this chapter alone, from your copy of the repository:",
         "g_cmd": "# run course_narrated with the repository's runtime, for this chapter:",
         "g_law": "The reader stores no output, by the course's own law; this page is the record of a run, made for it.",
         "ran": "run on {d} inside the library at commit {c}, in {s} s for the whole book",
         "haro": "The code is shown in Haro's name: where the chapter was written before the language took its present name, the name was changed and nothing else, and the chapter was run again that way. The source link leads to the text as it was written.",
         "cells_h": "The cells, run", "cell": "Cell", "out": "Output of this run",
         "hidden": "This cell's code shows the former name of the platform's language, which this site does not show. It was run; its verdict is below, and its place in the chapter is linked.",
         "kept": "ran: the promise is kept", "kept_all": "in all four editions", "nopromise": "ran: this cell writes no promise",
         "broken": "ran: printed something other than its promise", "raised": "did not run",
         "where": "This cell in the chapter", "ex_h": "The exercises",
         "ex_p": "Every exercise proves itself: its wrong answers are refused and its right answers accepted.",
         "ex_ok": "{wr} of {w} wrong answers refused, {ra} of {r} right answers accepted", "refused": "refused", "accepted": "accepted",
         "folder": "The exercise's folder", "files": "The four editions of the chapter",
         "book": "The book", "list_h": "The proof of each chapter",
         "list_p": "Every cell of the book leads to its proof: one page per chapter says what the course's guard found when it ran that chapter in its four editions, cell by cell, and how to do it again.",
         "list_row": "{c} cells, {k} promises kept · {x} exercises that prove themselves", "lang_note": "",
         "r_ch": "Proof · {c} cells ran, {k} promises kept, in each of the four editions · <a href=\"{u}\">the proof of this chapter</a>",
         "r_cell": "Proof of this cell", "r_ex": "This exercise proves itself: {wr} of {w} wrong answers refused, {ra} of {r} right answers accepted · <a href=\"{u}\">the proof</a>"},
}

def load(ROOT):
    f = ROOT / "data" / "proof-run.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None

def title_of(ch, lang): return ch["title"].get(lang) or ch["title"].get("en") or ch["id"]
def proven(ch):
    eds = ch["editions"].values()
    return (not ch.get("error") and not ch.get("mismatch") and not ch["drift"] and len(ch["editions"]) == 4
            and all(e["all_ran"] and e["all_kept"] and not e["stored_output"] for e in eds)
            and all(x["wrong_refused"] == x["wrong"] and x["right_accepted"] == x["right"] and x["wrong"] and x["right"] for x in ch["exercises"]))
def n_promises(ch): return ch["editions"]["en"]["promises"]
def page_url(ch, lang, rel=""):
    pl = lang if lang in ("en", "fr") else "en"
    return f"{rel}{pl}/book/{ch['id']}.html"

def why_not(ch, t):
    out = []
    if ch.get("error"): out.append(ch["error"])
    for k, e in ch["editions"].items():
        if not e["all_ran"] or not e["all_kept"]: out.append(f"{NATIVE[k]}: a cell diverged")
        if e["stored_output"]: out.append(f"{NATIVE[k]}: stored output")
    out += ch["drift"] + (ch.get("mismatch") or [])
    out += [f"{x['id']}: refused {x['wrong_refused']}/{x['wrong']}, accepted {x['right_accepted']}/{x['right']}" for x in ch["exercises"] if x["wrong_refused"] != x["wrong"] or x["right_accepted"] != x["right"]]
    return "; ".join(out)

def cell_label(c, t):
    if not c["ran"]: return "raised", t["raised"]
    if c["kept"] == -1: return "ran", t["nopromise"]
    if c["kept"] == 1:
        every = all(v in (1, -1) for v in c["kept_in"].values()) and len(c["kept_in"]) == 4
        return "kept", t["kept"] + (f' · {t["kept_all"]}' if every else "")
    return "differs", t["broken"]

def chapter_page(ch, lang, data, ctx):
    head, header, footer = ctx["head"], ctx["header"], ctx["footer"]
    t = T[lang]; other = "en" if lang == "fr" else "fr"
    title = title_of(ch, lang)
    eds = "; ".join(t["ed"].format(lang=f"<bdi>{NATIVE[k]}</bdi>", c=e["cells"], p=e["promises"]) for k, e in ch["editions"].items())   # bdi: Arabic inside a sentence keeps its place
    verdict = (t["ok"].format(c=len(ch["cells"]), p=n_promises(ch), d=esc(data["ran"]), eds=eds) if proven(ch)
               else t["notok"].format(d=esc(data["ran"]), why=esc(why_not(ch, t))))
    cells = []
    for c in ch["cells"]:
        shown = not (WORD.search(c["code"]) or WORD.search(c["out"]))          # library code is never rewritten: a cell that shows the former name is not shown
        v, label = cell_label(c, t)
        head_txt = c["heading"].get(lang) or c["heading"].get("en") or ""
        links = " · ".join(f'<a href="{GH}{esc(ch["file"][k])}#L{c["lines"][k][0]}-L{c["lines"][k][1]}">{NATIVE[k]}</a>' for k in ("en", "fr", "ar", "ha") if k in c["lines"] and k in ch["file"])
        err = f'<pre class="ran-out">{esc(c["error"])}</pre>' if c["error"] else ""
        run = (f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(c["code"])}</pre></div>'
               f'<div class="out"><div class="lbl">{t["out"]}</div><pre>{esc(c["out"])}</pre></div></div>') if shown else f'<p class="proof">{t["hidden"]}</p>'
        colon = ":" if lang == "en" else " :"
        cells.append(f'<div class="proofcell" id="cell-{c["n"]}"><p class="cell-h"><b>{t["cell"]} {c["n"]}</b> · {esc(head_txt)}</p>{run}'
                     f'<p class="ran nv-{v}">{label}</p>{err}<p class="proof">{t["where"]}{colon} {links}</p></div>')
    exs = []
    for x in ch["exercises"]:
        samples = " · ".join(f'<span class="mono">{esc(s["name"])}</span> <b class="g-{"same" if s["passed"] else "other"}">{t["accepted"] if s["passed"] else t["refused"]}</b>' for s in x["samples"])
        exs.append(f'<div class="proofcell" id="ex-{esc(x["id"])}"><p class="cell-h"><b class="mono">{esc(x["id"])}</b> · {esc(x["title"].get(lang) or x["title"].get("en") or "")}</p>'
                   f'<p class="ran nv-{"kept" if x["wrong_refused"] == x["wrong"] and x["right_accepted"] == x["right"] else "differs"}">{t["ex_ok"].format(wr=x["wrong_refused"], w=x["wrong"], ra=x["right_accepted"], r=x["right"])}</p>'
                   f'<p>{samples}</p><p class="proof"><a href="{GH}base/education/program/courses/{data["course"]}/exercises/{esc(x["id"])}">{t["folder"]}</a></p></div>')
    files = " · ".join(f'<a href="{GH}{esc(ch["file"][k])}">{NATIVE[k]}</a>' for k in ("en", "fr", "ar", "ha") if k in ch["file"])
    rel = "../../"
    colon = ":" if lang == "en" else " :"
    body = (f'<p class="lede-verdict">{verdict}</p><h2>{t["g_h"]}</h2><p>{t["g_p"].format(u=GUARD)}</p>'
            f'<pre>cd libraries/stzlib/base/test/education\n{t["g_cmd"]}\n#   course_narrated {esc(ch["id"])}</pre>'
            f'<p class="ran">{t["ran"].format(d=esc(data["ran"]), s=data["seconds"], c=esc(data.get("commit", "0e72e2e2c")))} · {t["files"]}{colon} {files}</p>'
            f'<p class="proof">{t["g_law"]} {t["lang_note"]}'
            + (f' {t["haro"]}' if data.get("names") == "haro" and any(re.search(r"\bharo\b", c["code"], re.I) for c in ch["cells"]) else "")
            + f'</p><h2>{t["cells_h"]}</h2>{"".join(cells)}'
            + (f'<h2>{t["ex_h"]}</h2><p>{t["ex_p"]}</p>' + "".join(exs) if exs else ""))
    bar = level2.nav(level2.LABELS["chapters"][lang],
                     [("", [(f'{c["id"]}.html', f'{c["n"]} · {title_of(c, lang)}', "page" if c is ch else "") for c in data["chapters"]])])
    page = head(lang, f'{title} · {t["title_suffix"]} · Softanza', f'{title}: {t["title_suffix"].lower()}', rel)
    page += '\n<body class="page page-book-proof">\n' + header(lang, "book", rel, other_href=f"../../{other}/book/{ch['id']}.html", nav_rel="../", page_key="book-proof", tail=[(title, None)])
    page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(t["kicker"].format(n=ch["n"]))} · <a href="../book.html#proof">{t["list_h"]}</a></div>
    <h1>{esc(title)}</h1>
  </div></section>
  <div class="wrap page-body proof-page">
{body}
  </div>
</main>
"""
    page += footer(lang, rel)
    return level2.wrap(page, bar)

def build_proof(ctx):
    ROOT = ctx["ROOT"]
    data = load(ROOT)
    if not data: return 0, 0
    n = 0
    for lang in ("fr", "en"):
        d = ROOT / lang / "book"
        if d.exists():
            for p in d.glob("*.html"): p.unlink()
        d.mkdir(parents=True, exist_ok=True)
        for ch in data["chapters"]:
            (d / f"{ch['id']}.html").write_text(chapter_page(ch, lang, data, ctx), encoding="utf-8"); n += 1
    return n, sum(1 for c in data["chapters"] if proven(c))

def proof_list_html(lang, data):
    t = T[lang]
    rows = "".join(f'<li><a href="book/{c["id"]}.html">{c["n"]} · {esc(title_of(c, lang))}</a> <span class="ran">{t["list_row"].format(c=len(c["cells"]), k=n_promises(c), x=len(c["exercises"]))}'
                   f'{"" if proven(c) else " · " + esc(why_not(c, t))}</span></li>' for c in data["chapters"])
    return f'<p>{t["list_p"]}</p><ol class="howto-list">{rows}</ol><p class="ran">{t["ran"].format(d=esc(data["ran"]), s=data["seconds"], c=esc(data.get("commit", "0e72e2e2c")))}</p>'

PROOF_CSS = ("<style>/*stz-proof*/figure.cell figcaption a.stz-proof-link{margin-inline-start:14px;font-weight:700;color:inherit;text-decoration:underline}"
             "p.stz-proof-ex{font-size:15px}</style>")

def inject_reader(text, data):
    """the bridge, inside the site's copy of the reader: the chapter's verdict, a link on each cell, a line on each exercise"""
    text = re.sub(r"<!--stz-proof-->.*?<!--/stz-proof-->", "", text, flags=re.S)
    text = re.sub(r"<style>/\*stz-proof\*/.*?</style>", "", text, flags=re.S)         # by marker, so an edited style never stacks
    text = text.replace("</head>", PROOF_CSS + "</head>", 1)
    chapters = {c["n"]: c for c in data["chapters"]}
    skipped = []
    def article(m):
        lang, n, whole = m.group(1), int(m.group(2)), m.group(0)
        ch = chapters.get(n)
        if not ch or lang not in ch["editions"]: return whole
        ed = ch["editions"][lang]
        t = T.get(lang)
        url = page_url(ch, lang)
        kept = sum(1 for c in ch["cells"] if c["kept"] == 1)
        # the chapter line, after the ladder line when there is one, else after the title
        if t:
            line = t["r_ch"].format(c=len(ch["cells"]), k=n_promises(ch), u=url)
        else:
            line = f'<bdi>course_narrated</bdi> · {kept}/{len(ch["cells"])} · <a href="{url}">↗</a>'
        mark = f'<!--stz-proof--><p class="stz-ladder">{line}</p><!--/stz-proof-->'
        if "<!--/stz-ladder-->" in whole: whole = whole.replace("<!--/stz-ladder-->", "<!--/stz-ladder-->" + mark, 1)
        else: whole = whole.replace("</h1>", "</h1>" + mark, 1)
        # a link on each cell: only when the article has exactly the chapter's cells, never a guess
        figs = list(re.finditer(r'(<figure class="cell"[^>]*><figcaption>)(.*?)(</figcaption>)', whole, re.S))
        if len(figs) == len(ch["cells"]):
            out, pos = [], 0
            for k, f in enumerate(figs, 1):
                label = t["r_cell"] if t else f"↗ {k}/{len(figs)}"
                link = f'<!--stz-proof--><a class="stz-proof-link" href="{page_url(ch, lang)}#cell-{k}">{label}</a><!--/stz-proof-->'
                out.append(whole[pos:f.end(2)]); out.append(link); pos = f.end(2)
            out.append(whole[pos:]); whole = "".join(out)
        else:
            skipped.append(f"{lang}-{n}: {len(figs)} cells in the reader, {len(ch['cells'])} in the proof")
        asides = list(re.finditer(r"</aside>", whole))
        exs = ch["exercises"]
        if len(asides) == len(exs):
            out, pos = [], 0
            for x, a in zip(exs, asides):
                u = f'{page_url(ch, lang)}#ex-{x["id"]}'
                if t: txt = t["r_ex"].format(wr=x["wrong_refused"], w=x["wrong"], ra=x["right_accepted"], r=x["right"], u=u)
                else: txt = f'{x["wrong_refused"]}/{x["wrong"]} · {x["right_accepted"]}/{x["right"]} · <a href="{u}">↗ <bdi>{x["id"]}</bdi></a>'
                out.append(whole[pos:a.start()]); out.append(f'<!--stz-proof--><p class="note stz-proof-ex">{txt}</p><!--/stz-proof-->'); pos = a.start()
            out.append(whole[pos:]); whole = "".join(out)
        else:
            skipped.append(f"{lang}-{n}: {len(asides)} exercises in the reader, {len(exs)} in the proof")
        return whole
    out = re.sub(r'<article id="(en|fr|ar|ha)-(\d+)"[^>]*>.*?</article>', article, text, flags=re.S)
    inject_reader.skipped = skipped
    return out
