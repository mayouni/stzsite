"""The narrations, the author's articles, as pages of the research section: every one published, none withheld.

Re-ruled by the author 2026-10-07 (12.16 and 12.17 of the external assessment): the narrations are the author's articles, 135 essays
under base/doc/narrations, and the site owes them a research section. So every article is a page, whatever its code does. The run
is a NOTE on the page, never a gate (B36): tools/narrations_run.py runs each article in Haro's name inside the library, and a block
that kept its promise gets one quiet line saying so; every other block is an illustration and says that one word. What a block
printed when it did not keep its promise is not shown: that is drift, and it belongs to the library's drift list, not to the reader.

The code is shown in Haro's name: the article is renamed (tools/haro.py, the name and nothing else, audited) before it runs, and the
text the page shows is the text that ran. The card around each article (abstract, genre, series, area, year, guards, related
reading) is derived by tools/narr_meta.py until the articles carry their own header (B34), and the page says so.
"""
import json, re, html, posixpath, pathlib
import level2, qforms
ROOT = pathlib.Path(__file__).resolve().parent.parent

def esc(s): return html.escape(str(s), quote=True)
FENCE = re.compile(r"(?ms)^```([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$")
CODE_TAGS = ("ring", "softanza", "haro")
GH_BLOB = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/"
GH_RAW = "https://raw.githubusercontent.com/mayouni/stzlib/main/libraries/stzlib/base/doc/narrations/"
GH_TREE = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/"
SITE = "https://mayouni.github.io/stzsite/"

GENRE = {"fr": {"paradigm essay": "essai de paradigme", "feature essay": "essai de fonction", "design essay": "essai de conception",
                "comparison": "comparaison", "tutorial": "tutoriel", "use case": "cas d'usage", "series": "série"},
         "en": {g: g for g in ("paradigm essay", "feature essay", "design essay", "comparison", "tutorial", "use case", "series")}}
SERIES = {"fr": {"performance": "la série performance", "security": "la série sécurité", "delivery": "la série livraison"},
          "en": {"performance": "the performance series", "security": "the security series", "delivery": "the delivery series"}}
T = {
  "fr": {"kicker": "Recherche · narration", "kept": "exécuté le {d} au commit {c} : a tenu sa promesse", "illus": "illustration",
         "promised": "Sortie promise", "compare": "{tag}, montré pour comparaison, non exécuté", "source": "Le fichier sur GitHub",
         "since": "dans le dépôt depuis le {d}", "by": "par {a}", "area": "domaine", "nocard": "sans domaine de l'Atlas",
         "derived": "Genre, domaine et série lus dans le nom du fichier, année tirée du premier commit : dérivés, jusqu'à ce que l'article porte son propre en-tête.",
         "proved": "Prouvé par", "proved_p": "L'article nomme ces gardes de scénario de la bibliothèque :", "related": "Lectures liées", "cite": "Citer",
         "run_ok": "Exécuté au nom de Haro le {d} dans la bibliothèque au commit {c}, bloc après bloc dans un seul processus : {k} bloc(s) sur {n} ont tenu leur promesse ; les autres sont des illustrations.",
         "run_no": {"effects": "Non exécuté : son code touche aux fichiers, au réseau, à l'horloge ou au hasard. L'article est publié tel qu'il est écrit ; ses blocs sont des illustrations.",
                    "does not compile": "Non exécuté : son code ne se charge pas tel qu'il est écrit. L'article est publié tel qu'il est écrit ; ses blocs sont des illustrations.",
                    "no code": "Cet article ne contient pas de code.", "": "Non exécuté."},
         "haro": "Le code des articles est du code Haro. Là où un article a été écrit avant que la langue prenne son nom actuel, le nom a été changé et rien d'autre.",
         "lang": "Cet article est écrit en anglais, comme la bibliothèque.", "back": "Toutes les narrations"},
  "en": {"kicker": "Research · narration", "kept": "run on {d} at commit {c}: kept its promise", "illus": "illustration",
         "promised": "Promised output", "compare": "{tag}, shown for comparison, not run", "source": "The file on GitHub",
         "since": "in the repository since {d}", "by": "by {a}", "area": "area", "nocard": "no single Atlas area",
         "derived": "Genre, area and series read from the file's name, the year from its first commit: derived, until the article carries its own header.",
         "proved": "Proved by", "proved_p": "The article names these scenario guards of the library:", "related": "Related reading", "cite": "Cite",
         "run_ok": "Run in Haro's name on {d} inside the library at commit {c}, block after block in one process: {k} of {n} blocks kept their promise; the others are illustrations.",
         "run_no": {"effects": "Not run: its code touches files, the network, the clock or chance. The article is published as written; its blocks are illustrations.",
                    "does not compile": "Not run: its code does not load as written. The article is published as written; its blocks are illustrations.",
                    "no code": "This article holds no code.", "": "Not run."},
         "haro": "The code of the articles is Haro code. Where an article was written before the language took its present name, the name was changed and nothing else.",
         "lang": "", "back": "All the narrations"},
}

def slug(name): return re.sub(r"[^a-z0-9]+", "-", name.lower().replace(".md", "")).strip("-")

def publishable(rec):
    """every article is published now (12.16): the run annotates, it never gates"""
    return "text" in rec

def map_prose(text):
    """prose in Haro's name, as the code is; the bridge keeps its own name (Ring++), and inline code was renamed with the code"""
    parts = re.split(r"(`[^`\n]*`)", text)
    for i in range(0, len(parts), 2):
        p = re.sub(r"\bRING\b", "HARO", parts[i])
        parts[i] = re.sub(r"\bRing\b(?!\+\+)", "Haro", p)
    return "".join(parts)

def title_of(rec):
    return map_prose(rec["title"]).replace("`", "")

def fix_links(text, published):
    def link(m):
        label, target = m.group(1), m.group(2)
        if not label.strip(): return ""                    # `[](x.md)` shows the reader nothing; one article has one, to a file that does not exist
        if re.match(r"[a-z]+:|#", target): return m.group(0)
        name = posixpath.basename(target)
        if name.endswith(".md") and name in published:
            return f"[{label}]({slug(name)}.html)"
        return f"[{label}]({GH_BLOB}{target})"
    def image(m):
        alt, target = m.group(1), m.group(2)
        if re.match(r"[a-z]+:", target): return m.group(0)
        hosted = posixpath.splitext(posixpath.basename(target))[0] + ".webp"
        if (ROOT / "assets" / "img" / "narrations" / hosted).exists():
            return f"![{alt}](../../assets/img/narrations/{hosted})"       # copied by narrations_run.py --images
        return f"![{alt}]({GH_RAW.rsplit('narrations/', 1)[0]}{posixpath.normpath('narrations/' + target)})"
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", image, text)
    return re.sub(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", link, text)

def split_lede(text):
    """the first paragraph of prose becomes the page's lede, and leaves the body, so nothing is said twice"""
    body = re.sub(r"(?m)\A\s*# [^\n]*\n", "", text, count=1)
    fence = FENCE.search(body)
    limit = fence.start() if fence else len(body)
    for m in re.finditer(r"(?:^|\n\s*\n)([^\n].*?)(?=\n\s*\n|\Z)", body[:limit], re.S):
        p = m.group(1).strip()
        if not p or p.startswith(("#", "!", ">", "|", "-", "*", "<", "---")) or re.match(r"\d+\.", p): continue
        if len(p) < 40: continue
        return p, body[:m.start(1)] + body[m.end(1):]
    return "", body

def render(rec, lang, md, published, text):
    t = T[lang]
    fences = list(FENCE.finditer(text))
    out, last, code_i, tokens = [], 0, 0, {}
    promised_next = False
    for k, m in enumerate(fences):
        prose = text[last:m.start()]
        if prose.strip(): promised_next = False
        out.append(map_prose(fix_links(prose, published)))
        tag, body = m.group(1).lower(), m.group(2).rstrip("\n")
        key = f"@@FENCE{k}@@"
        if tag in CODE_TAGS:
            b = rec["blocks"][code_i] if code_i < len(rec["blocks"]) else {"verdict": "", "out": ""}
            code_i += 1
            line = (f'<p class="ran nv-kept">{t["kept"].format(d=esc(rec.get("ran", "")), c=esc(rec.get("commit", "")))}</p>' if b["verdict"] == "kept"
                    else f'<p class="ran nv-illus">{t["illus"]}</p>')
            tokens[key] = f'<div class="nblock"><div class="lbl">Haro</div><pre>{esc(body)}</pre>{line}</div>'
            promised_next = True
        elif tag == "" and promised_next and not prose.strip():
            tokens[key] = f'<div class="out"><div class="lbl">{t["promised"]}</div><pre>{esc(body)}</pre></div>'
            promised_next = False
        else:
            label = t["compare"].format(tag=tag.capitalize()) if tag and tag not in ("text", "") else ""
            tokens[key] = (f'<div class="lbl">{esc(label)}</div>' if label else "") + f'<pre>{esc(body)}</pre>'
            promised_next = False
        out.append("\n\n" + key + "\n\n")
        last = m.end()
    out.append(map_prose(fix_links(text[last:], published)))
    html_body = md("".join(out))
    for key, frag in tokens.items():
        html_body = html_body.replace(f"<p>{key}</p>", frag).replace(key, frag)
    return html_body

def citation(card, f, lang):
    url = f"{SITE}{lang}/narrations/{slug(f)}.html"
    return f'{esc(card["author"])}. « {esc(card["title"])} ». Softanza narrations, {esc(card["year"])}. {esc(url)}' if lang == "fr" else \
           f'{esc(card["author"])}. "{esc(card["title"])}". Softanza narrations, {esc(card["year"])}. {esc(url)}'

def build_narration_pages(ctx):
    ROOT, head, header, footer, md = (ctx[k] for k in ("ROOT", "head", "header", "footer", "md"))
    runs = json.loads((ROOT / "data" / "narrations-run.json").read_text(encoding="utf-8"))
    meta = json.loads((ROOT / "data" / "narrations-meta.json").read_text(encoding="utf-8"))
    cards = meta["articles"]
    groups = ctx.get("groups") or []
    area_name = {g["slug"]: g for g in groups}
    published = {f for f, r in runs.items() if publishable(r) and f in cards}
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]
        out_dir = ROOT / lang / "narrations"
        if out_dir.exists():
            for p in out_dir.glob("*.html"): p.unlink()
        out_dir.mkdir(parents=True, exist_ok=True)
        for f in sorted(published):
            rec, card = runs[f], cards[f]
            title = title_of(rec)
            rel = "../../"
            other = "en" if lang == "fr" else "fr"
            lede, body_text = split_lede(rec["text"])
            # the card: who, when, what kind, where in the Atlas, which series
            bits = [t["by"].format(a=esc(card["author"]))]
            if card["date"]: bits.append(t["since"].format(d=esc(card["date"])))
            bits.append(GENRE[lang][card["genre"]] + (" · " + f'<a href="../narrations-{card["series"]}.html">{SERIES[lang][card["series"]]}</a>' if card["series"] else ""))
            if card["area"] and card["area"] in area_name:
                bits.append(f'{t["area"]} <a href="../atlas/{card["area"]}.html">{esc(area_name[card["area"]][lang])}</a>')
            else:
                bits.append(t["nocard"])
            hero = (f'<figure><img src="../../assets/img/narrations/{esc(card["hero"]["src"])}" alt="{esc(card["hero"]["alt"])}" loading="lazy">'
                    f'<figcaption>{esc(card["hero"]["alt"])}</figcaption></figure>') if card.get("hero") else ""
            if rec.get("status") == "run" and rec["blocks"]:
                k = sum(1 for b in rec["blocks"] if b["verdict"] == "kept")
                runline = t["run_ok"].format(d=esc(rec.get("ran", "")), c=esc(rec.get("commit", "")), k=k, n=len(rec["blocks"]))
            else:
                runline = t["run_no"].get(rec.get("reason") or ("no code" if rec.get("status") == "no code" else ""), t["run_no"][""])
            guards = "".join(f'<li><a href="{GH_TREE}{esc(g["path"])}">{esc(g["name"])}</a></li>' if g.get("path") else f'<li class="mono">{esc(g["name"])}</li>' for g in card["guards"])
            related = "".join(f'<li><a href="{slug(g)}.html">{esc(title_of(runs[g]) if g in runs else g)}</a></li>' for g in card["related"] if g in published)
            tail = ""
            if guards: tail += f'<h2>{t["proved"]}</h2><p>{t["proved_p"]}</p><ul>{guards}</ul>'
            if related: tail += f'<h2>{t["related"]}</h2><ul>{related}</ul>'
            tail += f'<h2>{t["cite"]}</h2><p class="mono cite">{citation(card, f, lang)}</p>'
            tail += f'<p class="proof">{runline} {t["haro"]} {t["derived"]} <a href="{GH_BLOB}{esc(f)}">{t["source"]}</a></p>'
            page = head(lang, f"{title} · Narrations · Softanza", card["abstract"] or title, rel)
            page += '\n<body class="page page-narration">\n' + header(lang, "narrations", rel, other_href=f"../../{other}/narrations/{slug(f)}.html", nav_rel="../", tail=[(title, None)])
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{t["kicker"]}</div>
    <h1>{esc(title)}</h1>
    {md(map_prose(fix_links(lede, published))).replace("<p>", '<p class="lede">', 1) if lede else ""}
    <p class="proof">{" · ".join(bits)}</p>
    {f'<p class="proof">{t["lang"]}</p>' if t["lang"] else ""}
  </div></section>
  <div class="wrap page-body narration">
{hero}
{render(rec, lang, md, published, body_text)}
{tail}
  </div>
</main>
"""
            page += footer(lang, rel)
            # the left bar: the articles of the same series, or else of the same area, or else of the same genre
            if card["series"]: sib = [g for g in published if cards[g]["series"] == card["series"]]
            elif card["area"]: sib = [g for g in published if cards[g]["area"] == card["area"] and not cards[g]["series"]]
            else: sib = [g for g in published if cards[g]["genre"] == card["genre"] and not cards[g]["area"] and not cards[g]["series"]]
            sib.sort(key=lambda g: (cards[g]["date"], title_of(runs[g]).lower()))
            bar = level2.nav(level2.LABELS["narrations"][lang],
                             [("", [("../narrations.html", t["back"], "")] + [(f"{slug(g)}.html", title_of(runs[g]), "page" if g == f else "") for g in sib])])
            page = level2.wrap(page, bar)
            (out_dir / f"{slug(f)}.html").write_text(page, encoding="utf-8"); pages += 1
    return pages, published
