"""Showing the extensions of a method: the strip on each row, the table of one method, the catalogue.

The ruling (2026-10-03): an extension (Q, CS, XT, Z, ZZ, U, IB, W...) is a syntax variation of the same
method, never another method. The reference lists a method once and each method says which extensions
exist for it and which do not (tools/qforms.py decides, and holds the catalogue with its sources).
"""
import html, json
import qforms

def esc(s): return html.escape(str(s), quote=True)
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"

SHORT = {   # the short word of each standard extension, for the legend
    "en": {"Q": "chains", "CS": "case sensitivity", "XT": "extended", "Z": "positions", "ZZ": "sections", "IB": "bounds", "W": "condition", "U": "unique"},
    "fr": {"Q": "enchaîne", "CS": "casse", "XT": "étendue", "Z": "positions", "ZZ": "sections", "IB": "bornes", "W": "condition", "U": "sans doublon"},
}
T = {
  "fr": {"example": "Exemple", "out": "Sortie", "generic": "Aucun nom de méthode ne la porte dans la référence : la bibliothèque la fournit pour toute méthode, et les tableaux par méthode l'omettent.",
         "ex_ran": "Chaque exemple a été exécuté le {d} dans la bibliothèque au commit 0e72e2e2c. Les appels sont composés à partir de l'usage que la bibliothèque documente (ses tests, ses narrations et ses descriptions), avec de vrais noms de méthodes ; la sortie est celle de l'exécution.",
         "label": "Extensions", "none": "aucune extension", "folded": "formes avec extensions, rangées sous leur méthode",
         "legend": "Une extension s'écrit à la fin du nom d'une méthode : c'est la même méthode, avec un mot de plus, jamais une autre méthode. Chaque méthode dit ci-dessous lesquelles existent : un nom en gras et coché existe pour elle, un nom barré n'existe pas.",
         "legend_link": "Les extensions et leur sens",
         "remind": "Sous chaque méthode, ses extensions (Q CS XT Z ZZ IB W U) : en gras et cochée, elle existe ; barrée, elle n'existe pas.",
         "h": "Les extensions", "p": "Un nom qui se termine par une extension est la même méthode écrite avec un mot de plus, jamais une autre méthode : la référence liste la méthode une seule fois, et dit pour chacune quelles extensions existent et lesquelles n'existent pas. Seules les extensions que la bibliothèque documente sont rangées ainsi : les {n} ci-dessous ; les formes passives (Removed à côté de Remove) ne sont pas des extensions, car elles ne font pas la même chose : Remove change l'objet, Removed rend une copie.",
         "code": "Extension", "adds": "Ce qu'elle ajoute", "source": "Documentée dans", "exists": "Existe", "yes": "oui", "no": "non", "names": "Les noms",
         "more": "et {n} autres", "for": "Les extensions de cette méthode", "forp": "Chaque extension, et si elle existe pour cette méthode ; une extension qui existe se compose avec les autres (FindSTCS).",
         "left_h": "Des terminaisons laissées telles quelles",
         "left_p": "Ces terminaisons ressemblent à des extensions mais la bibliothèque ne les documente pas comme telles : les noms qui les portent restent listés, chacun comme sa propre méthode. Si l'une d'elles est une extension, elle sera rangée à la prochaine génération du site. Entre parenthèses, le nombre de noms et un exemple.",
         "inherited": "définie dans {owner} ; ses extensions ici", "table_of": "extensions de"},
  "en": {"example": "Example", "out": "Output", "generic": "No method name carries it in the reference: the library provides it for any method, and the per-method tables leave it out.",
         "ex_ran": "Each example was run on {d} inside the library at commit 0e72e2e2c. The calls are composed from the usage the library documents (its tests, its narrations and its descriptions), with real method names; the output is the run's.",
         "label": "Extensions", "none": "no extension", "folded": "forms written with extensions, listed under their method",
         "legend": "An extension is written at the end of a method's name: it is the same method with one more word, never another method. Each method says below which exist: a bold, ticked name exists for it, a struck name does not.",
         "legend_link": "The extensions and what they mean",
         "remind": "Under each method, its extensions (Q CS XT Z ZZ IB W U): bold and ticked, it exists; struck, it does not.",
         "h": "The extensions", "p": "A name that ends in an extension is the same method written with one more word, never another method: the reference lists the method once, and says for each which extensions exist and which do not. Only the extensions the library documents are folded this way: the {n} below; passive forms (Removed beside Remove) are not extensions, since they do not do the same thing: Remove changes the object, Removed returns a copy.",
         "code": "Extension", "adds": "What it adds", "source": "Documented in", "exists": "Exists", "yes": "yes", "no": "no", "names": "The names",
         "more": "and {n} more", "for": "The extensions of this method", "forp": "Each extension, and whether it exists for this method; an extension that exists combines with the others (FindSTCS).",
         "left_h": "Endings left as they are",
         "left_p": "These endings look like extensions but the library does not document them as such, so the names that carry them stay listed, each as its own method. If one of them is an extension, it will be folded the next time the site is built. In brackets, the number of names and one example.",
         "inherited": "defined in {owner}; its extensions here", "table_of": "extensions of"},
}

def strip(variants, lang="en"):
    """the strip on one row: yes or no for the standard extensions, and any other that exists; 'none' when the method has none.
    Each letter carries its meaning as a title: the paragraph that used to open every page is one line now"""
    if not variants: return "none"
    have = qforms.extensions_of(variants)
    codes = qforms.STANDARD + [e for e in qforms.CODES if e in have and e not in qforms.STANDARD]
    def title(e):
        w = SHORT[lang].get(e) or next((x[1] if lang == "en" else x[2] for x in qforms.EXTENSIONS if x[0] == e), "")
        return f'{e}: {w}' + ("" if e in have else (" (does not exist for this method)" if lang == "en" else " (n'existe pas pour cette méthode)"))
    return '<span class="exts">' + "".join(f'<i class="{"y" if e in have else "n"}" title="{esc(title(e))}">{e}</i>' for e in codes) + "</span>"

def row_strip(variants, lang):
    s = strip(variants, lang)
    return f'<span class="exts none">{T[lang]["none"]}</span>' if s == "none" else s

def legend(lang, rel):
    """the reminder above a table: one line, since the meaning is said once, in the catalogue of the index"""
    t = T[lang]
    return f'<p class="proof">{t["remind"]} <a href="{rel}reference.html#extensions">{t["legend_link"]}</a></p>'

def meaning(code, lang):
    e = next(x for x in qforms.EXTENSIONS if x[0] == code)
    return e[1] if lang == "en" else e[2], e[3]

def mark(name, exts, which):
    """a method name with the letters of one extension highlighted; the extensions end the name, in the order written"""
    n = sum(len(e) for e in exts)
    off, found = 0, False
    for e in exts:
        if e == which: found = True; break
        off += len(e)
    if not found or n > len(name): return esc(name)
    a = len(name) - n + off
    return esc(name[:a]) + f'<mark class="ext">{esc(name[a:a + len(which)])}</mark>' + esc(name[a + len(which):])

def example_html(ex, ext, lang):
    """the example of one extension: its code with the called name's extension letters highlighted, and what the run printed"""
    t = T[lang]
    code = esc(ex["code"])
    name, base = ex["name"], ex["name"][:-len(ext)]
    code = code.replace(f".{esc(name)}(", f'.{esc(base)}<mark class="ext">{esc(ext)}</mark>(')
    return (f'<div class="ext-ex"><div class="lbl">{t["example"]}</div><pre>{code}</pre>'
            f'<div class="lbl">{t["out"]}</div><pre class="ext-out">{esc(ex["out"])}</pre></div>')

def method_table(variants, lang, n_names=4):
    """for one method: each extension, whether it exists, and the names that carry it, their extension letters highlighted"""
    t = T[lang]
    have = qforms.forms_of(variants)
    rows = []
    for code in qforms.CODES:
        if code in qforms.GENERIC: continue          # no method name carries it: a yes or no here would mislead
        text, src = meaning(code, lang)
        names = have.get(code, [])
        shown = ", ".join(f'<span class="mono">{mark(n, exts, code)}</span>' for n, exts in names[:n_names])
        if len(names) > n_names: shown += " " + t["more"].format(n=len(names) - n_names)
        rows.append(f'<div class="lane lane3e"><div class="ln mono">{code}</div>'
                    f'<div class="lr"><span class="exts"><i class="{"y" if names else "n txt"}">{t["yes"] if names else t["no"]}</i></span></div>'
                    f'<div class="lt">{esc(text)}{(" · " + shown) if shown else ""}</div></div>')
    head = f'<div class="lane lane3e rhead"><div class="ln">{t["code"]}</div><div class="lr">{t["exists"]}</div><div class="lt">{t["adds"]} · {t["names"]}</div></div>'
    return f'<h2>{t["for"]}</h2><p class="proof">{t["forp"]}</p><div class="lanes rtable">{head}{"".join(rows)}</div>'

def catalogue(lang, ROOT, n_folded):
    """the table of every documented extension with its source and an example run in the library, and the endings that were left"""
    t = T[lang]
    f = ROOT / "data" / "ext-examples.json"
    data = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"examples": {}, "ran": ""}
    rows = []
    for code, en, fr, src in qforms.EXTENSIONS:
        ex = data["examples"].get(code)
        note = f'<p class="proof">{t["generic"]}</p>' if code in qforms.GENERIC else ""
        rows.append(f'<div class="lane lane3"><div class="ln mono">{code}</div><div class="lr"><a href="{GH}{esc(src)}">{esc(src.split("/")[-1])}</a></div>'
                    f'<div class="lt">{esc(en if lang == "en" else fr)}{note}{example_html(ex, code, lang) if ex and not ex["error"] else ""}</div></div>')
    head = f'<div class="lane lane3 rhead"><div class="ln">{t["code"]}</div><div class="lr">{t["source"]}</div><div class="lt">{t["adds"]}</div></div>'
    left = qforms.unknown_endings(ROOT, 14)
    left_html = ", ".join(f'<b class="mono">{esc(e)}</b> ({n} · <span class="mono">{esc(s[1])}</span>)' for e, n, s in left)
    ran = f'<p class="ran">{t["ex_ran"].format(d=esc(data["ran"]))}</p>' if data["ran"] else ""
    return (f'<h2 id="extensions">{t["h"]}</h2><p>{t["p"].format(n=len(qforms.CODES))}</p>'
            f'<div class="lanes rtable">{head}{"".join(rows)}</div>{ran}'
            f'<h3>{t["left_h"]}</h3><p>{t["left_p"]}</p><p>{left_html}</p>')
