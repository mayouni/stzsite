"""The narrations as pages of the site, every code block run and judged.

A narration is published here when tools/narrations_run.py ran it inside the
library, block after block in one process, and at least three blocks in four
kept their promise or promised nothing. Each code block is shown as written and
under it what the run did: printed what it promises, promised nothing, printed
something else (shown), or raised (shown). The others stay on GitHub, and the
list says why. Prose maps the platform's former name to Haro, as the site does
everywhere; code is never rewritten, and a narration whose code shows the name
is not published at all.
"""
import json, re, html, posixpath, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def esc(s): return html.escape(str(s), quote=True)
FENCE = re.compile(r"(?ms)^```([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$")
CODE_TAGS = ("ring", "softanza")
GH_BLOB = "https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/"
GH_RAW = "https://raw.githubusercontent.com/mayouni/stzlib/main/libraries/stzlib/base/doc/narrations/"

T = {
  "fr": {"kept": "exécuté : a affiché ce que ce bloc promet", "ran": "exécuté : ce bloc n'annonce pas de sortie ; voici ce qu'il a affiché", "ran0": "exécuté : ce bloc n'annonce pas de sortie et n'a rien affiché",
         "unprinted": "exécuté : sa promesse est écrite sur une ligne qui n'affiche rien, elle n'a pas pu être vérifiée",
         "differs": "exécuté : a affiché autre chose ; voici ce qu'il a affiché", "raised": "exécuté : a levé une erreur",
         "stopped": "n'a pas fini", "promised": "Sortie promise", "compare": "{tag}, montré pour comparaison, non exécuté",
         "kicker": "Narration", "source": "Le fichier sur GitHub",
         "summary": "Exécutée le {d} dans la bibliothèque au commit 0e72e2e2c, bloc après bloc dans un seul processus : {parts}.",
         "parts": {"kept": "{n} bloc a affiché ce qu'il promet|{n} blocs ont affiché ce qu'ils promettent", "ran": "{n} n'annonce pas de sortie|{n} n'annoncent pas de sortie", "differs": "{n} a affiché autre chose|{n} ont affiché autre chose", "raised": "{n} a levé une erreur|{n} ont levé une erreur"},
         "lang": "Cette narration est écrite en anglais, comme la bibliothèque."},
  "en": {"kept": "ran: printed what this block promises", "ran": "ran: this block states no output; here is what it printed", "ran0": "ran: this block states no output and printed nothing",
         "unprinted": "ran: its promise is written on a line that prints nothing, so it could not be checked",
         "differs": "ran: printed something else; here is what it printed", "raised": "ran: raised an error",
         "stopped": "did not finish", "promised": "Promised output", "compare": "{tag}, shown for comparison, not run",
         "kicker": "Narration", "source": "The file on GitHub",
         "summary": "Run on {d} inside the library at commit 0e72e2e2c, block after block in one process: {parts}.",
         "parts": {"kept": "{n} block printed what it promises|{n} blocks printed what they promise", "ran": "{n} states no output|{n} state no output", "differs": "{n} printed something else", "raised": "{n} raised an error"},
         "lang": ""},
}

def slug(name): return re.sub(r"[^a-z0-9]+", "-", name.lower().replace(".md", "")).strip("-")

def publishable(rec):
    if rec.get("status") != "run" or not rec["blocks"]: return False
    if any(b["verdict"] == "stopped" for b in rec["blocks"]): return False
    ok = sum(b["verdict"] in ("kept", "ran") for b in rec["blocks"])
    return ok >= 0.75 * len(rec["blocks"])

def map_prose(text):
    """Under the site's ruling the language is named Haro in prose; inline code is never touched."""
    parts = re.split(r"(`[^`\n]*`)", text)
    for i in range(0, len(parts), 2):
        p = parts[i].replace("Ring++", "Haro")
        p = re.sub(r"\bRING\b", "HARO", p)
        parts[i] = re.sub(r"\bRing\b", "Haro", p)
    return "".join(parts)

def fix_links(text, published):
    def link(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"[a-z]+:|#", target): return m.group(0)
        if target.endswith(".md") and "/" not in target:
            return f"[{label}]({slug(target)}.html)" if target in published else f"[{label}]({GH_BLOB}{target})"
        return f"[{label}]({GH_BLOB}{target})"
    def image(m):
        alt, target = m.group(1), m.group(2)
        if re.match(r"[a-z]+:", target): return m.group(0)
        hosted = posixpath.splitext(posixpath.basename(target))[0] + ".webp"
        if (ROOT / "assets" / "img" / "narrations" / hosted).exists():
            return f"![{alt}](../../assets/img/narrations/{hosted})"       # copied by narrations_run.py --images
        return f"![{alt}]({GH_RAW.rsplit('narrations/', 1)[0]}{posixpath.normpath('narrations/' + target)})"
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", image, text)
    return re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, text)

def render(rec, lang, md, published):
    t = T[lang]
    text = rec["text"]
    text = re.sub(r"(?m)\A\s*# [^\n]*\n", "", text, count=1)          # the title becomes the page's heading
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
            b = rec["blocks"][code_i] if code_i < len(rec["blocks"]) else {"verdict": "stopped", "out": ""}
            code_i += 1
            v = b["verdict"]
            label = t["ran0"] if v == "ran" and not b["out"] else t[v]
            extra = f'<pre class="ran-out">{esc(b["out"])}</pre>' if v in ("differs", "raised", "ran") and b["out"] else ""
            tokens[key] = (f'<div class="nblock"><div class="lbl">Softanza</div><pre>{esc(body)}</pre>'
                           f'<p class="ran nv-{v}">{label}</p>{extra}</div>')
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

def build_narration_pages(ctx):
    ROOT, head, header, footer, md = (ctx[k] for k in ("ROOT", "head", "header", "footer", "md"))
    runs = json.loads((ROOT / "data" / "narrations-run.json").read_text(encoding="utf-8"))
    published = {f for f, r in runs.items() if publishable(r)}
    pages = 0
    for lang in ("fr", "en"):
        t = T[lang]
        out_dir = ROOT / lang / "narrations"
        if out_dir.exists():
            for p in out_dir.glob("*.html"): p.unlink()
        out_dir.mkdir(parents=True, exist_ok=True)
        for f in sorted(published):
            rec = runs[f]
            c = {v: sum(1 for b in rec["blocks"] if b["verdict"] == v) for v in ("kept", "ran", "differs", "raised")}
            title = map_prose(rec["title"]).replace("`", "")      # a heading shows names, not markdown
            rel = "../../"
            other = "en" if lang == "fr" else "fr"
            page = head(lang, f"{title} · {t['kicker']} · Softanza", title, rel)
            page += '\n<body class="page page-narration">\n' + header(lang, "narrations", rel, other_href=f"../../{other}/narrations/{slug(f)}.html", nav_rel="../")
            # only the counts that are not zero, each in its singular or plural form
            def part(v):
                forms = t["parts"][v].split("|"); form = forms[0] if c[v] == 1 or len(forms) == 1 else forms[1]
                return form.format(n=c[v])
            parts = [part(v) for v in ("kept", "ran", "differs", "raised") if c[v]]
            sep = " ; " if lang == "fr" else "; "
            summary = t["summary"].format(d=esc(rec["ran"]), parts=sep.join(parts))
            page += f"""
<main id="main">
  <section class="page-head"><div class="wrap">
    <div class="eyebrow">{t["kicker"]}</div>
    <h1>{esc(title)}</h1>
    <p class="proof">{summary} <a href="{GH_BLOB}{esc(f)}">{t["source"]}</a></p>
    {f'<p class="proof">{t["lang"]}</p>' if t["lang"] else ""}
  </div></section>
  <div class="wrap page-body narration">
{render(rec, lang, md, published)}
  </div>
</main>
"""
            page += footer(lang, rel)
            (out_dir / f"{slug(f)}.html").write_text(page, encoding="utf-8"); pages += 1
    return pages, published
