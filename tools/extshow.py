"""Showing the extensions of a method: the strip on each row, the table of one method, the catalogue.

The ruling (2026-10-03): an extension (Q, CS, XT, Z, ZZ, U, IB, W...) is a syntax variation of the same
method, never another method. The reference lists a method once and each method says which extensions
exist for it and which do not (tools/qforms.py decides, and holds the catalogue with its sources).
"""
import html
import qforms

def esc(s): return html.escape(str(s), quote=True)
GH = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"

SHORT = {   # the short word of each standard extension, for the legend
    "en": {"Q": "chains", "CS": "case sensitivity", "XT": "extended", "Z": "positions", "ZZ": "sections", "IB": "bounds", "W": "condition", "U": "unique"},
    "fr": {"Q": "enchaîne", "CS": "casse", "XT": "étendue", "Z": "positions", "ZZ": "sections", "IB": "bornes", "W": "condition", "U": "sans doublon"},
}
T = {
  "fr": {"label": "Extensions", "none": "aucune extension", "folded": "formes avec extensions, rangées sous leur méthode",
         "legend": "Une extension s'écrit à la fin du nom d'une méthode : c'est la même méthode, avec un mot de plus, jamais une autre méthode. Chaque méthode dit ci-dessous lesquelles existent : un nom en gras et coché existe pour elle, un nom barré n'existe pas.",
         "legend_link": "Les extensions et leur sens",
         "h": "Les extensions", "p": "Un nom qui se termine par une extension est la même méthode écrite avec un mot de plus, jamais une autre méthode : la référence liste la méthode une seule fois, et dit pour chacune quelles extensions existent et lesquelles n'existent pas. Seules les extensions que la bibliothèque documente sont rangées ainsi ({n} ici) ; les formes passives (Removed à côté de Remove) ne sont pas des extensions, car elles ne font pas la même chose : Remove change l'objet, Removed rend une copie.",
         "code": "Extension", "adds": "Ce qu'elle ajoute", "source": "Documentée dans", "exists": "Existe", "yes": "oui", "no": "non", "names": "Les noms",
         "more": "et {n} autres", "for": "Les extensions de cette méthode", "forp": "Chaque extension, et si elle existe pour cette méthode ; une extension qui existe se compose avec les autres (FindSTCS).",
         "left_h": "Des terminaisons laissées telles quelles",
         "left_p": "Ces terminaisons ressemblent à des extensions mais la bibliothèque ne les documente pas comme telles : les noms qui les portent restent listés, chacun comme sa propre méthode. Si l'une d'elles est une extension, elle sera rangée à la prochaine génération du site. Entre parenthèses, le nombre de noms et un exemple.",
         "inherited": "définie dans {owner} ; ses extensions ici", "table_of": "extensions de"},
  "en": {"label": "Extensions", "none": "no extension", "folded": "forms written with extensions, listed under their method",
         "legend": "An extension is written at the end of a method's name: it is the same method with one more word, never another method. Each method says below which exist: a bold, ticked name exists for it, a struck name does not.",
         "legend_link": "The extensions and what they mean",
         "h": "The extensions", "p": "A name that ends in an extension is the same method written with one more word, never another method: the reference lists the method once, and says for each which extensions exist and which do not. Only the extensions the library documents are folded this way ({n} here); passive forms (Removed beside Remove) are not extensions, since they do not do the same thing: Remove changes the object, Removed returns a copy.",
         "code": "Extension", "adds": "What it adds", "source": "Documented in", "exists": "Exists", "yes": "yes", "no": "no", "names": "The names",
         "more": "and {n} more", "for": "The extensions of this method", "forp": "Each extension, and whether it exists for this method; an extension that exists combines with the others (FindSTCS).",
         "left_h": "Endings left as they are",
         "left_p": "These endings look like extensions but the library does not document them as such, so the names that carry them stay listed, each as its own method. If one of them is an extension, it will be folded the next time the site is built. In brackets, the number of names and one example.",
         "inherited": "defined in {owner}; its extensions here", "table_of": "extensions of"},
}

def strip(variants):
    """the strip on one row: yes or no for the standard extensions, and any other that exists; 'none' when the method has none"""
    if not variants: return "none"
    have = qforms.extensions_of(variants)
    codes = qforms.STANDARD + [e for e in qforms.CODES if e in have and e not in qforms.STANDARD]
    return '<span class="exts">' + "".join(f'<i class="{"y" if e in have else "n"}">{e}</i>' for e in codes) + "</span>"

def row_strip(variants, lang):
    s = strip(variants)
    return f'<span class="exts none">{T[lang]["none"]}</span>' if s == "none" else s

def legend(lang, rel):
    t = T[lang]
    words = " · ".join(f"<b>{c}</b> {SHORT[lang][c]}" for c in qforms.STANDARD)
    return f'<p class="proof">{t["legend"]} {words} · <a href="{rel}reference.html#extensions">{t["legend_link"]}</a></p>'

def meaning(code, lang):
    e = next(x for x in qforms.EXTENSIONS if x[0] == code)
    return e[1] if lang == "en" else e[2], e[3]

def method_table(variants, lang, n_names=4):
    """for one method: each extension, whether it exists, and the names that carry it"""
    t = T[lang]
    have = qforms.extensions_of(variants)
    rows = []
    for code in qforms.CODES:
        text, src = meaning(code, lang)
        names = have.get(code, [])
        shown = ", ".join(f'<span class="mono">{esc(n)}</span>' for n in names[:n_names])
        if len(names) > n_names: shown += " " + t["more"].format(n=len(names) - n_names)
        rows.append(f'<div class="lane lane3"><div class="ln mono">{code}</div>'
                    f'<div class="lr"><span class="exts"><i class="{"y" if names else "n txt"}">{t["yes"] if names else t["no"]}</i></span></div>'
                    f'<div class="lt">{esc(text)}{(" · " + shown) if shown else ""}</div></div>')
    head = f'<div class="lane lane3 rhead"><div class="ln">{t["code"]}</div><div class="lr">{t["exists"]}</div><div class="lt">{t["adds"]} · {t["names"]}</div></div>'
    return f'<h2>{t["for"]}</h2><p class="proof">{t["forp"]}</p><div class="lanes rtable">{head}{"".join(rows)}</div>'

def catalogue(lang, ROOT, n_folded):
    """the table of every documented extension with its source, and the endings that were left"""
    t = T[lang]
    rows = []
    for code, en, fr, src in qforms.EXTENSIONS:
        rows.append(f'<div class="lane lane3"><div class="ln mono">{code}</div><div class="lr"><a href="{GH}{esc(src)}">{esc(src.split("/")[-1])}</a></div>'
                    f'<div class="lt">{esc(en if lang == "en" else fr)}</div></div>')
    head = f'<div class="lane lane3 rhead"><div class="ln">{t["code"]}</div><div class="lr">{t["source"]}</div><div class="lt">{t["adds"]}</div></div>'
    left = qforms.unknown_endings(ROOT, 14)
    left_html = ", ".join(f'<b class="mono">{esc(e)}</b> ({n} · <span class="mono">{esc(s[1])}</span>)' for e, n, s in left)
    return (f'<h2 id="extensions">{t["h"]}</h2><p>{t["p"].format(n=len(qforms.CODES))}</p>'
            f'<div class="lanes rtable">{head}{"".join(rows)}</div>'
            f'<h3>{t["left_h"]}</h3><p>{t["left_p"]}</p><p>{left_html}</p>')
