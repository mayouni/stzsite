"""How-to pages: one page per recipe of the library, its code run before it is shown.

A recipe (base/doc/quickers/recipes) answers one "how do I...?" with one block of
code: the page carries its intent as the title, its code as written, what the
run printed, the methods it uses with their entries, the words a reader would
search with, and the recipes it leads to. tools/howto_run.py ran them inside the
library; a recipe the run did not keep, or did not run, stays on GitHub and the
list says why. Learned from the Wolfram documentation's workflow pages and
decided in doc/DOCUMENTATION-DESIGN.md (D4).

    fr|en/howto.html             the list, by kind
    fr|en/howto/<kind>-<slug>.html   one recipe
"""
import json, re, html
import level2

def esc(s): return html.escape(str(s), quote=True)
RING = re.compile(r"\b(?:Ring|RING)\b")
def prose(s): return RING.sub(lambda m: "HARO" if m.group(0).isupper() else "Haro", str(s)).replace("Ring++", "Haro")
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/quickers/recipes/"

KINDS = {"list": {"fr": "Listes", "en": "Lists"}, "number": {"fr": "Nombres", "en": "Numbers"},
         "string": {"fr": "Chaînes", "en": "Strings"}, "text": {"fr": "Textes", "en": "Text"}}

# short labels for the bar, and the intents in French (the library writes them in English)
FR = {
  "list/average": ("Moyenne", "Calculer la moyenne d'une liste de nombres"),
  "list/contains": ("Contient", "Vérifier qu'une liste contient un élément"),
  "list/filter": ("Filtrer", "Ne garder que les éléments d'une liste qui remplissent une condition"),
  "list/find": ("Trouver", "Trouver la position d'un élément dans une liste"),
  "list/first-last": ("Premier et dernier", "Obtenir le premier ou le dernier élément d'une liste"),
  "list/max-min": ("Plus grand et plus petit", "Obtenir la plus grande ou la plus petite valeur d'une liste"),
  "list/remove-duplicates": ("Retirer les doublons", "Retirer les doublons d'une liste (garder les éléments uniques)"),
  "list/reverse": ("Inverser", "Inverser l'ordre des éléments d'une liste"),
  "list/sort": ("Trier", "Trier une liste par ordre croissant"),
  "list/sum": ("Somme", "Additionner tous les nombres d'une liste"),
  "number/even-odd": ("Pair ou impair", "Vérifier si un nombre est pair ou impair"),
  "number/factors": ("Diviseurs", "Obtenir tous les diviseurs d'un nombre"),
  "number/is-prime": ("Premier", "Vérifier si un nombre est premier"),
  "string/contains": ("Contient", "Vérifier qu'une chaîne contient une sous-chaîne"),
  "string/count-occurrences": ("Compter", "Compter combien de fois une sous-chaîne apparaît"),
  "string/find": ("Trouver", "Trouver où une sous-chaîne apparaît dans une chaîne"),
  "string/repeat": ("Répéter", "Répéter une chaîne plusieurs fois"),
  "string/replace": ("Remplacer", "Remplacer les occurrences d'une sous-chaîne par une autre"),
  "string/reverse": ("Inverser", "Inverser les caractères d'une chaîne"),
  "string/section": ("Extraire une portion", "Extraire la portion comprise entre deux positions"),
  "string/split": ("Découper", "Découper une chaîne en parties selon un séparateur"),
  "string/starts-ends-with": ("Commence ou finit par", "Vérifier si une chaîne commence ou finit par quelque chose"),
  "string/trim": ("Retirer les espaces", "Retirer les espaces au début et à la fin d'une chaîne"),
  "string/uppercase": ("Majuscules", "Mettre une chaîne en majuscules (ou en minuscules)"),
  "text/detect-language": ("Détecter la langue", "Détecter la langue naturelle dans laquelle un texte est écrit"),
  "text/entities": ("Entités", "Trouver les personnes, les lieux et les organisations cités dans un texte"),
  "text/normalize-words": ("Formes de base", "Ramener les mots à leur forme de base (lemmatiser, raciniser)"),
  "text/sentiment": ("Sentiment", "Détecter le ton d'un texte, positif ou négatif"),
  "text/summarize": ("Résumer", "Résumer un texte à ses phrases les plus importantes"),
  "text/topics": ("Sujets", "Trouver les sujets ou les expressions clés d'un texte"),
}
EN_SHORT = {"first-last": "First and last", "max-min": "Largest and smallest", "even-odd": "Even or odd", "is-prime": "Prime",
            "starts-ends-with": "Starts or ends with", "count-occurrences": "Count", "remove-duplicates": "Remove duplicates",
            "detect-language": "Detect the language", "normalize-words": "Base forms", "uppercase": "Upper case"}

T = {
  "fr": {"title": "Comment faire", "title_html": "<i>Comment</i> faire", "kicker": "Une tâche, son code, exécuté",
         "lede": "Les recettes de la bibliothèque : chacune répond à une question « comment faire… ? » par un bloc de code. Chaque recette a été exécutée dans la bibliothèque avant d'être publiée ; sa sortie est celle de cette exécution.",
         "desc": "Les recettes Softanza : une tâche, son code et sa sortie, exécutés dans la bibliothèque.",
         "note": "Recettes lues dans le dossier doc/quickers/recipes de la bibliothèque au commit 0e72e2e2c et exécutées le {d}, toutes dans un seul processus. Une expression qui porte une promesse sans l'afficher a été affichée pour l'exécution.",
         "github": "Sur GitHub", "names": "son code nomme l'ancien langage de la plateforme", "effects": "elle touche aux fichiers, au réseau, à l'horloge ou au hasard",
         "not_kept": "son exécution ne tient pas encore sa promesse", "compile": "elle ne compile pas telle qu'écrite",
         "out": "Sortie", "kept": "exécuté : a affiché ce que la recette promet", "differs": "exécuté : a affiché autre chose", "raised": "exécuté : a levé une erreur", "ran": "exécuté",
         "ran_note": "exécuté le {d} dans la bibliothèque au commit 0e72e2e2c",
         "printed": "l'expression qui porte la promesse a été affichée pour l'exécution",
         "methods": "Les méthodes", "words": "Les mots de cette tâche", "see": "Voir aussi", "source": "La recette sur GitHub",
         "lang_note": "La recette est écrite en anglais, comme la bibliothèque ; son intention est traduite ici.", "kind": "Comment faire"},
  "en": {"title": "How-to", "title_html": "<i>How</i> to", "kicker": "A task, its code, run",
         "lede": "The library's recipes: each answers one \"how do I…?\" with one block of code. Every recipe was run inside the library before it was published; its output is that run's.",
         "desc": "The Softanza recipes: a task, its code and its output, run inside the library.",
         "note": "Recipes read in the library's doc/quickers/recipes folder at commit 0e72e2e2c and run on {d}, all in one process. An expression that carries a promise without printing it was printed for the run.",
         "github": "On GitHub", "names": "its code names the platform's former language", "effects": "it touches files, the network, the clock or chance",
         "not_kept": "its run does not yet keep its promise", "compile": "it does not compile as written",
         "out": "Output", "kept": "ran: printed what the recipe promises", "differs": "ran: printed something else", "raised": "ran: raised an error", "ran": "ran",
         "ran_note": "run on {d} inside the library at commit 0e72e2e2c",
         "printed": "the expression carrying the promise was printed for the run",
         "methods": "The methods", "words": "Words for this task", "see": "See also", "source": "The recipe on GitHub",
         "lang_note": "", "kind": "How-to"},
}

def key(rec): return f'{rec["category"]}/{rec["slug"]}'
def page_name(rec): return f'{rec["category"]}-{rec["slug"]}'
def published(rec): return rec["status"] == "run" and all(p["verdict"] in ("kept", "ran") for p in rec["parts"])
def intent(rec, lang): return FR.get(key(rec), ("", rec["intent"]))[1] if lang == "fr" else rec["intent"]
def short(rec, lang):
    if lang == "fr": return FR.get(key(rec), (rec["slug"], ""))[0]
    return EN_SHORT.get(rec["slug"], rec["slug"].replace("-", " ").capitalize())

def load_howtos(ROOT):
    f = ROOT / "data" / "howto-run.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}

def howtos_by_method(runs):
    """(class, method) -> the published recipes that use it, for the method entries' See also"""
    out = {}
    for rec in runs.values():
        if not published(rec): continue
        for m in rec["methods"]:
            if "." in m:
                cls, meth = m.split(".", 1)
                out.setdefault((cls, meth), []).append(rec)
    return out

def build_howto(ctx):
    ROOT, head, header, footer, md, entries = (ctx[k] for k in ("ROOT", "head", "header", "footer", "md", "entries"))
    from build_methods import slug as mslug
    runs = load_howtos(ROOT)
    ref = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
    classes = {c["name"]: {m[0] for m in c["own"]} for c in ref["classes"]}
    pub = [r for r in runs.values() if published(r)]
    by_slug = {}
    for r in pub: by_slug.setdefault(r["slug"], []).append(r)
    ran = next((r["ran"] for r in runs.values() if r.get("ran")), "")
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]; other = "en" if lang == "fr" else "fr"
        out_dir = ROOT / lang / "howto"
        if out_dir.exists():
            for p in out_dir.glob("*.html"): p.unlink()
        out_dir.mkdir(parents=True, exist_ok=True)
        groups = [(KINDS[k][lang], [(f"{page_name(r)}.html", short(r, lang), r) for r in sorted(pub, key=lambda r: short(r, lang).lower()) if r["category"] == k])
                  for k in KINDS]
        for rec in pub:
            bar = level2.nav(t["title"], [(g, [(h, s, "page" if r is rec else "") for h, s, r in items]) for g, items in groups if items])
            blocks = []
            for block, part in zip(rec["blocks"], rec["parts"]):
                label = t[part["verdict"]]
                blocks.append(f'<div class="run"><div><div class="lbl">Softanza</div><pre>{esc(block)}</pre></div>'
                              f'<div class="out"><div class="lbl">{t["out"]}</div><pre>{esc(part["out"])}</pre></div></div>'
                              f'<p class="ran nv-{part["verdict"]}">{label}</p>')
            def mlink(m):
                if "." not in m: return f'<span class="mono">{esc(m)}</span>'
                cls, meth = m.split(".", 1)
                if (cls, meth) in entries: return f'<a class="mono" href="../reference/{cls.lower()}/{mslug(meth)}.html">{esc(m)}</a>'
                if cls in classes and meth in classes[cls]: return f'<a class="mono" href="../reference/{cls.lower()}.html#{esc(meth.lower())}">{esc(m)}</a>'
                if cls in classes: return f'<a class="mono" href="../reference/{cls.lower()}.html">{esc(m)}</a>'
                return f'<span class="mono">{esc(m)}</span>'
            def see(s):
                cands = by_slug.get(s, [])
                r = next((c for c in cands if c["category"] == rec["category"]), cands[0] if cands else None)
                return f'<a href="{page_name(r)}.html">{esc(intent(r, lang))}</a>' if r else None
            sees = [x for x in (see(s) for s in rec["see"]) if x]
            notes = f'<div class="howto-notes">{md(prose(rec["notes"]))}</div>' if rec["notes"] else ""
            run_line = t["ran_note"].format(d=esc(rec["ran"]))
            if any(p["printed"] for p in rec["parts"]): run_line += (" ; " if lang == "fr" else "; ") + t["printed"]
            body = (f'{"".join(blocks)}<p class="proof">{run_line} · <a href="{GH}{esc(rec["file"])}">{t["source"]}</a></p>'
                    f'{notes}'
                    f'<h2>{t["methods"]}</h2><p>{" · ".join(mlink(m) for m in rec["methods"])}</p>'
                    + (f'<h2>{t["see"]}</h2><ul>' + "".join(f"<li>{s}</li>" for s in sees) + "</ul>" if sees else "")
                    + (f'<p class="proof">{t["words"]} : {esc(", ".join(rec["tags"]))}</p>'.replace(" : ", ": " if lang == "en" else " : ") if rec["tags"] else "")
                    + (f'<p class="proof">{t["lang_note"]}</p>' if t["lang_note"] else ""))
            title = intent(rec, lang)
            page = head(lang, f'{title} · {t["title"]} · Softanza', title, "../../")
            page += '\n<body class="page page-howto-recipe">\n' + header(lang, "howto", "../../", other_href=f"../../{other}/howto/{page_name(rec)}.html", nav_rel="../")
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{t["kind"]} · {esc(KINDS[rec["category"]][lang])}</div>
    <h1>{esc(title)}</h1>
  </div></section>
  <div class="wrap page-body">
{body}
  </div>
</main>
"""
            page += footer(lang, "../../")
            (out_dir / f"{page_name(rec)}.html").write_text(level2.wrap(page, bar), encoding="utf-8"); pages += 1
        # ---- the list --------------------------------------------------------
        sections = []
        for k in KINDS:
            items = [r for r in pub if r["category"] == k]
            if items:
                sections.append(f'<h2>{esc(KINDS[k][lang])} <span class="mono">({len(items)})</span></h2><ul class="howto-list">'
                                + "".join(f'<li><a href="howto/{page_name(r)}.html">{esc(short(r, lang))}</a> · {esc(intent(r, lang))}</li>' for r in sorted(items, key=lambda r: short(r, lang).lower())) + "</ul>")
        rest = [r for r in runs.values() if not published(r)]
        if rest:
            def why(r):
                if r["reason"] in ("names", "names in output"): return t["names"]
                if r["reason"] == "effects": return t["effects"]
                if r["reason"] == "does not compile": return t["compile"]
                return t["not_kept"]
            sections.append(f'<h2>{t["github"]} <span class="mono">({len(rest)})</span></h2><ul class="howto-list">'
                            + "".join(f'<li><a href="{GH}{esc(r["file"])}">{esc(intent(r, lang))}</a> <span class="ran">{esc(why(r))}</span></li>' for r in rest) + "</ul>")
        page = head(lang, f'{t["title"]} · Softanza', t["desc"], "../")
        page += '\n<body class="page page-howto">\n' + header(lang, "howto", "../")
        page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{esc(t["kicker"])}</div>
    <h1>{t["title_html"]}</h1>
    <p class="lede">{esc(t["lede"])}</p>
  </div></section>
  <div class="wrap page-body">
    <p class="proof">{esc(t["note"].format(d=ran))}</p>
    {"".join(sections)}
  </div>
</main>
"""
        page += footer(lang, "../")
        (ROOT / lang / "howto.html").write_text(page, encoding="utf-8"); pages += 1
    return pages, len(pub)
