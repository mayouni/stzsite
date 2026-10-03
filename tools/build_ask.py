"""The agents' door: how a program asks the library, measured, and the files an agent reads.

Every Softanza object answers Ask, HowTo and ExplainMethod from the doc-comments of
its class, with no model loaded. This page shows each call run, then measures the
door honestly: the 28 recipes the site publishes each state an intent and name the
methods that do it, and tools/ask_run.py asked each intent back of the recipe's
class. Every answer is shown as it came, graded the same method, the same verb in
another form, or another method. Decided in doc/DOCUMENTATION-DESIGN.md (D5).

It also writes what an agent reading this site wants instead of pages:
    llms.txt                  the site in one text file, every page that matters linked
    agents/index.json         every class and method with its explanation, every recipe
                              with its code and output, every narration run, as data
"""
import json, re, html
from build_howto import intent as howto_intent, page_name as howto_page, published as howto_published, KINDS, fold_methods
import qforms, build_proof, rowex

def esc(s): return html.escape(str(s), quote=True)
RING = re.compile(r"\b(?:Ring|RING)\b")
WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)
def prose(s): return RING.sub(lambda m: "HARO" if m.group(0).isupper() else "Haro", str(s)).replace("Ring++", "Haro")
SITE = "https://mayouni.github.io/stzsite/"
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"

SHOW_CODE = {
  ("Ask", "stzList"): 'aR = StzSelfDocQ("stzList").Ask("remove duplicates")\nfor k = 1 to len(aR)\n    ? aR[k][1] + "  " + aR[k][2] + "  " + aR[k][3]\nnext',
  ("HowTo", "stzString"): '? StzSelfDocQ("stzString").HowTo("replace one word with another")',
  ("ExplainMethod", "stzList"): '? StzSelfDocQ("stzList").ExplainMethod("RemoveDuplicates")',
  ("Ask", "stzText"): 'aR = StzSelfDocQ("stzText").Ask("what is the mood of this text")\nfor k = 1 to len(aR)\n    ? aR[k][1] + "  " + aR[k][2] + "  " + aR[k][3]\nnext',
}

T = {
  "fr": {
    "title": "Interroger la bibliothèque", "title_html": "Interroger la <i>bibliothèque</i>", "kicker": "Pour un programme, et pour un agent",
    "lede": "Un programme ne lit pas ce site : il interroge la bibliothèque. Chaque objet Softanza répond à trois questions à partir des explications écrites dans sa propre source, le même texte que la référence montre, sans modèle chargé et avec la même réponse à chaque fois.",
    "desc": "Comment un programme interroge Softanza : Ask, HowTo et ExplainMethod, exécutés et mesurés sur les recettes de la bibliothèque, et les fichiers qu'un agent lit.",
    "h_three": "Trois questions",
    "three": "<code>Ask(question)</code> rend les trois méthodes dont le sens répond le mieux à la question, avec un score et leur explication. <code>HowTo(intention)</code> rend un appel prêt à écrire : la grammaire des noms compose d'abord un nom de méthode et le vérifie contre la classe, sinon la recherche par le sens le trouve. <code>ExplainMethod(nom)</code> rend l'explication d'une méthode, sa forme et un exemple tiré des tests. Tout objet répond de même : <code>Q([1, 2, 2]).Ask(\"…\")</code> pose la question à sa propre classe.",
    "c_ask": "Ask : les méthodes qui répondent à une question", "c_howto": "HowTo : un appel pour une intention", "c_explain": "ExplainMethod : ce que fait une méthode", "c_ask2": "Ask, sur un texte",
    "out": "Sortie", "ran": "exécuté le {d} dans la bibliothèque au commit 0e72e2e2c, sans modèle neuronal chargé",
    "h_measured": "Mesuré : les recettes de la bibliothèque, posées en retour",
    "measured": "Les {n} recettes publiées sur ce site disent chacune une intention et nomment les méthodes qui la réalisent. Chaque intention a été posée telle quelle, mot pour mot, à la classe de sa recette. <code>HowTo</code> a proposé la méthode de la recette pour {hs} questions et une autre forme du même verbe pour {hv} ; <code>Ask</code> en avait une parmi ses trois premières réponses pour {ag}. Les {ho} autres réponses de <code>HowTo</code> sont montrées telles qu'elles sont venues : c'est le travail de la bibliothèque, et il lui est transmis.",
    "measured_note": "Exécuté le {d} dans la bibliothèque au commit 0e72e2e2c, en un seul processus ({s} s), sans modèle neuronal chargé, comme un agent l'obtient par défaut. Une réponse compte comme « même méthode » si elle nomme une méthode que la recette utilise, « même verbe » si elle en nomme une autre forme (Reverse pour Reversed). Un nom qui se termine par Q dans une réponse est la même méthode, qui rend l'objet pour que l'appel puisse s'enchaîner.",
    "uses": "La recette utilise", "proposes": "HowTo propose", "asks": "Ask répond",
    "g_same": "même méthode", "g_verb": "même verbe, autre forme", "g_other": "une autre méthode",
    "h_outside": "Depuis l'extérieur d'un programme",
    "outside": "Un agent qui dispose d'un terminal peut déjà exécuter un court programme qui pose ces questions. Les commandes <code>stz ask</code>, <code>stz explain</code> et <code>stz howto</code>, qui répondront sous forme de données avec un code de sortie fiable, sont décidées et pas encore construites ; la page <a href=\"coding-agents.html\">Agents qui codent</a> dit lesquelles et dans quel ordre.",
    "h_files": "Pour un agent qui lit ce site",
    "files": "Un agent n'a pas besoin des pages : deux fichiers lui donnent le site sous forme de données, générés avec lui à chaque publication.",
    "f_llms": "le site en un fichier texte : ce qu'est Softanza, et les pages qui comptent, chacune liée et décrite en une ligne",
    "f_index": "chaque classe et chaque méthode avec son explication, chaque recette avec son code et sa sortie, chaque narration exécutée, et l'adresse de chaque page",
    "files_note": "Les deux fichiers sont en anglais, la langue de la bibliothèque. Ils suivent les règles du site : rien qui n'ait été exécuté n'y est montré comme exécuté.",
  },
  "en": {
    "title": "Ask the library", "title_html": "Ask the <i>library</i>", "kicker": "For a program, and for an agent",
    "lede": "A program does not read this site: it asks the library. Every Softanza object answers three questions from the explanations written in its own source, the same text the reference shows, with no model loaded and the same answer every time.",
    "desc": "How a program asks Softanza: Ask, HowTo and ExplainMethod, run and measured against the library's own recipes, and the files an agent reads.",
    "h_three": "Three questions",
    "three": "<code>Ask(question)</code> returns the three methods whose meaning best answers the question, with a score and their explanation. <code>HowTo(intent)</code> returns a call ready to write: the grammar of names first composes a method name and checks it against the class, and otherwise a search by meaning finds one. <code>ExplainMethod(name)</code> returns a method's explanation, its form and an example taken from the tests. Every object answers the same way: <code>Q([1, 2, 2]).Ask(\"…\")</code> asks its own class.",
    "c_ask": "Ask: the methods that answer a question", "c_howto": "HowTo: a call for an intent", "c_explain": "ExplainMethod: what a method does", "c_ask2": "Ask, about a text",
    "out": "Output", "ran": "run on {d} inside the library at commit 0e72e2e2c, with no neural model loaded",
    "h_measured": "Measured: the library's recipes, asked back",
    "measured": "The {n} recipes published on this site each state an intent and name the methods that do it. Each intent was asked as it stands, word for word, of its recipe's class. <code>HowTo</code> proposed the recipe's method for {hs} questions and another form of the same verb for {hv}; <code>Ask</code> had one of them among its first three answers for {ag}. The {ho} other <code>HowTo</code> answers are shown as they came: they are the library's work, and they are routed to it.",
    "measured_note": "Run on {d} inside the library at commit 0e72e2e2c, in one process ({s} s), with no neural model loaded, as an agent gets it by default. An answer counts as \"same method\" when it names a method the recipe uses, and \"same verb\" when it names another form of one (Reverse for Reversed). A name ending in Q in an answer is the same method, returning the object so that a call can be chained.",
    "uses": "The recipe uses", "proposes": "HowTo proposes", "asks": "Ask answers",
    "g_same": "same method", "g_verb": "same verb, another form", "g_other": "another method",
    "h_outside": "From outside a program",
    "outside": "An agent with a shell can already run a short program that asks these questions. The commands <code>stz ask</code>, <code>stz explain</code> and <code>stz howto</code>, which will answer as data with an exit code a hook can trust, are decided and not built yet; the <a href=\"coding-agents.html\">Coding agents</a> page says which and in what order.",
    "h_files": "For an agent reading this site",
    "files": "An agent does not need the pages: two files give it the site as data, generated with it at every publication.",
    "f_llms": "the site in one text file: what Softanza is, and the pages that matter, each linked and described in one line",
    "f_index": "every class and method with its explanation, every recipe with its code and output, every narration run, and the address of every page",
    "files_note": "Both files are in English, the library's language. They follow the site's rules: nothing that did not run is shown as run.",
  },
}

def build_ask(ctx):
    ROOT, head, header, footer, entries, groups = (ctx[k] for k in ("ROOT", "head", "header", "footer", "entries", "groups"))
    from build_methods import slug as mslug
    Q = qforms.get(ROOT)
    ask = json.loads((ROOT / "data" / "ask-run.json").read_text(encoding="utf-8"))
    howto = json.loads((ROOT / "data" / "howto-run.json").read_text(encoding="utf-8"))
    by_file = {r["file"]: r for r in howto.values()}
    qs = [q for q in ask["questions"] if not q.get("error")]
    c = lambda k, g: sum(1 for q in qs if q[k] == g)
    hs, hv, ho = c("howto_grade", "same"), c("howto_grade", "verb"), c("howto_grade", "other")
    ag = sum(1 for q in qs if q["ask_grade"] in ("same", "verb"))
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]
        shows = []
        for s, key in zip(ask["shown"], ("c_ask", "c_howto", "c_explain", "c_ask2")):
            code = SHOW_CODE[(s["call"], s["class"])]
            assert not (WORD.search(code) or WORD.search(s["out"])), "a shown answer names the word"
            shows.append(f'<h3>{t[key]}</h3><div class="run"><div><div class="lbl">Softanza</div><pre>{esc(code)}</pre></div>'
                         f'<div class="out"><div class="lbl">{t["out"]}</div><pre>{esc(s["out"])}</pre></div></div>')
        rows = []
        for q in qs:
            r = by_file[q["file"]]
            cls = q["class"]
            def mref(m):
                if (cls, m) in entries: return f'<a class="mono" href="reference/{cls.lower()}/{mslug(m)}.html">{esc(m)}</a>'
                return f'<span class="mono">{esc(m)}</span>'
            g = lambda k: f'<b class="g-{q[k]}">{t["g_" + q[k]]}</b>'
            rows.append(f'<div class="ask-row"><p class="ask-q"><a href="howto/{howto_page(r)}.html">{esc(howto_intent(r, lang))}</a> <span class="mono">{esc(cls)}</span></p>'
                        f'<p>{t["uses"]} : {" · ".join(mref(m) for m in dict.fromkeys(Q.fold(cls, x) for x in q["methods"]))}</p>'.replace(" : ", ": " if lang == "en" else " : ")
                        + f'<p>{t["proposes"]} : <span class="mono">{esc(q["howto_method"])}</span> · {g("howto_grade")}</p>'.replace(" : ", ": " if lang == "en" else " : ")
                        + f'<p>{t["asks"]} : <span class="mono">{esc(", ".join(q["ask"]))}</span> · {g("ask_grade")}</p></div>'.replace(" : ", ": " if lang == "en" else " : "))
        body = f"""
<h2>{t["h_three"]}</h2>
<p>{t["three"]}</p>
{"".join(shows)}
<p class="ran">{t["ran"].format(d=esc(ask["ran"]))} · <a href="{GH}base/meta/stzSelfDoc.ring">stzSelfDoc.ring</a> · <a href="{GH}base/object/stzObject.ring">stzObject.ring</a></p>
<h2>{t["h_measured"]}</h2>
<p>{t["measured"].format(n=len(qs), hs=hs, hv=hv, ag=ag, ho=ho)}</p>
<p class="proof">{esc(t["measured_note"].format(d=ask["ran"], s=ask["seconds"]))}</p>
<div class="ask-rows">{"".join(rows)}</div>
<h2>{t["h_outside"]}</h2>
<p>{t["outside"]}</p>
<h2>{t["h_files"]}</h2>
<p>{t["files"]}</p>
<ul><li><a class="mono" href="../llms.txt">llms.txt</a> · {t["f_llms"]}</li><li><a class="mono" href="../agents/index.json">agents/index.json</a> · {t["f_index"]}</li></ul>
<p class="proof">{t["files_note"]}</p>"""
        page = ctx["page_shell"](lang, "ask", t["title"], t["desc"], esc(t["kicker"]), t["title_html"], esc(t["lede"]), body)
        (ROOT / lang / "ask.html").write_text(page, encoding="utf-8"); pages += 1
    write_machine_files(ROOT, entries, groups, howto, ask)
    return pages, (hs, hv, ho, ag, len(qs))

def write_machine_files(ROOT, entries, groups, howto, ask):
    from build_methods import slug as mslug
    from build_narration_pages import publishable, slug as nslug
    ref = qforms.reference(ROOT)
    Q = qforms.get(ROOT)
    narr = json.loads((ROOT / "data" / "narrations-run.json").read_text(encoding="utf-8"))
    classes = []
    rdata = rowex.load(ROOT)
    for c in ref["classes"]:
        ms = []
        for name, aka, desc in c["own"]:
            m = {"name": name, "description": prose(desc)}
            if aka: m["also"] = prose(aka)
            if (c["name"], name) in entries: m["entry"] = f'{SITE}en/reference/{c["name"].lower()}/{mslug(name)}.html'
            vs = c["variants"].get(name.lower(), [])
            have = qforms.extensions_of(vs)
            m["extensions"] = [e for e in qforms.CODES if e in have]          # which extensions exist for this method
            if vs: m["forms"] = sorted({v[0] for v in vs}, key=lambda n: (len(n), n))
            ex = rowex.pick(c["name"], name, entries.get((c["name"], name)), rdata)      # an example on every method that has one
            if ex: m["example"] = {"code": ex[0], "output": ex[1].strip(), "from": "library test" if ex[2] == "lib" else "composed from the signature, run in the library"}
            ms.append(m)
        classes.append({"name": c["name"], "area": c["area"], "page": f'{SITE}en/reference/{c["name"].lower()}.html',
                        "source": f'{GH}base/{c["file"]}', "inherits": c["inherited"], "methods": ms})
    recipes = []
    for r in howto.values():
        if not howto_published(r): continue
        recipes.append({"intent": r["intent"], "kind": r["category"], "page": f'{SITE}en/howto/{howto_page(r)}.html',
                        "code": r["blocks"], "output": [p["out"] for p in r["parts"]], "methods": fold_methods(Q, r["methods"]),
                        "words": r["tags"], "ran": r["ran"]})
    narrations = [{"title": prose(x["title"]).replace("`", ""), "page": f"{SITE}en/narrations/{nslug(f)}.html", "ran": x["ran"]}
                  for f, x in sorted(narr.items()) if publishable(x)]
    proof = build_proof.load(ROOT)
    book = [{"chapter": c["n"], "title": c["title"].get("en", c["id"]), "page": f'{SITE}en/book/{c["id"]}.html', "cells": len(c["cells"]),
             "promises": c["editions"]["en"]["promises"], "proven": build_proof.proven(c), "exercises": len(c["exercises"]), "ran": proof["ran"]}
            for c in proof["chapters"]] if proof else []
    areas = [{"slug": g["slug"], "title": g["en"], "page": f'{SITE}en/atlas/{g["slug"]}.html', "guide": f'{SITE}en/guide/{g["slug"]}.html'} for g in groups]
    index = {"site": SITE, "library": "https://github.com/mayouni/stzlib", "commit": "0e72e2e2c",
             "naming": "A method name that ends in an extension (Q, CS, XT, Z, ZZ, U, IB, W...) is not listed apart: it is the same method written with one more word. Each method lists the extensions that exist for it and the names of its forms.",
             "extensions": [{"code": e[0], "adds": e[1], "documented_in": GH + e[3]} for e in qforms.EXTENSIONS],
             "note": "Generated with the Softanza site from the library at commit 0e72e2e2c. Descriptions are the library's own doc-comments. Every recipe's output was produced by running it inside the library.",
             "ask": {"calls": ["Ask(question)", "HowTo(intent)", "ExplainMethod(name)"], "page": f"{SITE}en/ask.html",
                     "measured": {"questions": len(ask["questions"]), "ran": ask["ran"],
                                  "howto_same_method": sum(1 for q in ask["questions"] if q.get("howto_grade") == "same"),
                                  "howto_same_verb": sum(1 for q in ask["questions"] if q.get("howto_grade") == "verb"),
                                  "ask_top3_hit": sum(1 for q in ask["questions"] if q.get("ask_grade") in ("same", "verb"))}},
             "areas": areas, "recipes": recipes, "narrations": narrations, "book": book, "classes": classes}
    # prose is mapped as on the pages; identifiers and file names stay as the library spells them
    text = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    (ROOT / "agents").mkdir(exist_ok=True)
    (ROOT / "agents" / "index.json").write_text(text, encoding="utf-8")
    # llms.txt: the convention of a site written for language models (llmstxt.org)
    L = ["# Softanza", "",
         "> Softanza is a computational platform for makers: one engine, written in Zig, handles text, exact numbers, tables, graphs, maps, images, sound, neural networks, governed agents and the security around them. Its language, Haro, is in construction. Born in Africa, useful to the world.", "",
         "This site was generated from the library at commit 0e72e2e2c. Its method examples, recipes and narrations were run inside the library before publication, and each output shown is that run's; what did not run is not shown as run. The site is in English and French; this file links the English pages.", "",
         "## Ask the library", "",
         f"- [Ask the library]({SITE}en/ask.html): how a program asks Softanza (Ask, HowTo, ExplainMethod), every call run, measured against the library's own recipes",
         f"- [Machine index]({SITE}agents/index.json): every class and method with its explanation, every recipe with its code and output, every narration run, as JSON",
         f"- [Coding agents]({SITE}en/coding-agents.html): what an agent reaches today, and the stz command decided for it", "",
         "## Documentation", "",
         f"- [Documentation]({SITE}en/docs.html): the whole scope, area by area",
         f"- [Reference]({SITE}en/reference.html): {len(ref['classes'])} classes, each method with the explanation the library gives of itself; {len(entries):,} methods have an entry with examples run",
         f"- [How-to]({SITE}en/howto.html): {len(recipes)} recipes, each a task, its code and its output, run",
         f"- [Narrations]({SITE}en/narrations.html): the library's stories in code; {len(narrations)} run block by block as pages", 
         f"- [The book]({SITE}en/book.html): the Elementary Introduction, fifteen chapters in four languages; {len(book)} proof pages show each chapter's cells run, the guard that proves them, and its exercises proving themselves", "",
         "## How-to", ""]
    for k in KINDS:
        for r in sorted((x for x in recipes if x["kind"] == k), key=lambda x: x["intent"]):
            L.append(f"- [{r['intent']}]({r['page']}): {', '.join(r['methods'])}")
    L += ["", "## Areas", ""]
    for a in areas:
        L.append(f"- [{a['title']}]({a['page']}): what Softanza rethought in this area, its code run, and its guide at {a['guide']}")
    L += ["", "## Optional", "",
          f"- [The platform]({SITE}en/platform.html): the platform in plain words",
          f"- [Architecture]({SITE}en/architecture.html): layers, engine, conventions",
          f"- [French version]({SITE}fr/ask.html): the same site in French",
          "- [The library on GitHub](https://github.com/mayouni/stzlib): the source, under the MIT licence", ""]
    llms = "\n".join(L)
    assert not WORD.search(llms), "llms.txt names the word"
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
