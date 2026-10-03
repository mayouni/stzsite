"""The example of one row of a reference table.

Examples must be everywhere on the site (the author, 2026-10-03): a reader should see that Softanza
is a practical technology and not only a concept. So each row of a class's reference table carries one:

  - the library's own shortest run example of the method, when its tests have one (tools/examples_run.py);
  - otherwise an example composed from the method's signature and run in the library for this site
    (tools/rows_run.py): a fresh sample object, the call, what it printed;
  - last, a library example of one of the method's extended forms (FindW for Find): the row's extension
    line already says the form exists.

Both are shown the way the library writes a promise: the code, then `#-->` and what the run printed. A
composed example is shown with the object it ran on, so it can be copied whole. The source is named on every
row, and the legend of the page counts how many rows have which.
"""
import json, html, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qforms

def esc(s): return html.escape(str(s), quote=True)
WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)

T = {
  "fr": {"lib": "test de la bibliothèque", "new": "composé à partir de la signature, exécuté pour cette page",
         "legend": "Chaque méthode porte un exemple quand les tests de la bibliothèque, ou cette page, ont pu en exécuter un. {nl} viennent des tests de la bibliothèque ; {nc} ont été composés à partir de la signature de la méthode et exécutés pour cette page, sur un objet neuf, par exemple : <span class=\"mono\">{recv}</span>. {nn} méthodes n'ont pas encore d'exemple.",
         "legend_lib": "Chaque méthode porte un exemple quand les tests de la bibliothèque ont pu en exécuter un : {nl} en ont un ; {nn} n'en ont pas encore.",
         "legend_effects": "Aucune méthode de cette classe n'est exécutée sur cette page : la classe touche aux fichiers, au réseau, aux processus, à l'horloge, au hasard ou au son, et un exemple exécuté ici ne serait que l'exemple de ses effets. Chaque méthode porte l'explication que la bibliothèque donne d'elle-même.",
         "legend_none": "Aucune méthode de cette classe n'a encore d'exemple : la page ne sait pas encore construire un objet de cette classe, ni composer les arguments de ses méthodes.",
         "ran": "Exemples exécutés le {d} dans la bibliothèque au commit 0e72e2e2c."},
  "en": {"lib": "library test", "new": "composed from the signature, run for this page",
         "legend": "Each method carries an example when the library's tests, or this page, could run one. {nl} come from the library's tests; {nc} were composed from the method's signature and run for this page, on a fresh object, for example: <span class=\"mono\">{recv}</span>. {nn} methods have no example yet.",
         "legend_lib": "Each method carries an example when the library's tests could run one: {nl} do; {nn} have none yet.",
         "legend_effects": "No method of this class is run on this page: the class reaches files, the network, processes, the clock, chance or sound, and an example run here would only be an example of its effects. Each method carries the explanation the library gives of itself.",
         "legend_none": "No method of this class has an example yet: the page cannot build an object of this class yet, nor compose the arguments of its methods.",
         "ran": "Examples run on {d} inside the library at commit 0e72e2e2c."},
}

NL = chr(10)

# the classes of the areas that read or write files, talk to a network, run processes, play sound, draw windows or wait on the clock:
# an example composed for them would be an example of side effects, so none is run for them (tools/rows_mine.py reads this too)
SKIP_AREAS = {"files", "system", "sound", "web", "concurrency", "gui", "gpu", "neural", "security", "performance", "extensibility", "agents"}
SKIP_CLASS = re.compile(r"(?i)(file|folder|path|socket|http|server|client|process|thread|worker|cluster|reactor|timer|clock|stopwatch|"
                        r"random|audio|sound|window|screen|keyboard|mouse|log\b|logger|shell|terminal|console|download|upload|database|sql|secret|key|token|password|"
                        r"cache|storage|queue|scheduler|daemon|agent|llm|model|train|neural)")

def effects(c):
    return c["area"] in SKIP_AREAS or bool(SKIP_CLASS.search(c["name"]))

STMT = re.compile(r"(?<=\)) (?=o1\.)")

def reflow(setup, width=54):
    """a setup that puts several statements on a line is repacked so that no line is wider than the example's box:
    the statements stay whole, a line breaks only between two of them"""
    out = []
    for line in setup.split(NL):
        cur = ""
        for st in STMT.split(line):
            if cur and len(cur) + 1 + len(st) > width: out.append(cur); cur = st
            else: cur = (cur + " " + st) if cur else st
        out.append(cur)
    return NL.join(out)

def load(ROOT):
    f = ROOT / "data" / "row-examples.json"
    d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"examples": {}, "classes": {}, "ran": ""}
    d["plain"] = qforms.get(ROOT).plain_anywhere           # for the Q rule: a ...Q() call whose value nothing uses is not an example
    return d

def out_lines(out, n=4):
    ls = [l.rstrip() for l in str(out).split(NL) if l.strip() != ""]
    return ls[:n] + (["..."] if len(ls) > n else [])

def library_example(exs, name=None):
    """the shortest example of the library's tests that fits a row: a few lines of code, a short output.
    With a name, only an example that calls that very method (the name, then an open parenthesis) counts:
    an example of FindW is not the example of Find"""
    call = re.compile(r"\b" + re.escape(name) + r"\s*\(", re.I) if name else None
    best = None
    for e in exs or []:
        code = e["code"].strip(NL)
        if code.count(NL) > 5 or len(code) > 300 or e["out"].count(NL) > 5 or len(e["out"]) > 300: continue
        if WORD.search(code) or WORD.search(e["out"]): continue
        if call and not call.search(code): continue
        key = (code.count(NL), len(code))
        if best is None or key < best[0]: best = (key, e)
    return best[1] if best else None

def pick(cls, name, exs, data):
    """(code, output, source) of the example for one row, or None"""
    e = library_example(exs, name)
    if e: return e["code"].strip(NL), e["out"], "lib"
    c = data["examples"].get(cls, {}).get(name)
    if c:
        code = (reflow(c["setup"]) + NL + c["code"]) if c.get("setup") else c["code"]
        if not (WORD.search(code) or WORD.search(c["out"]) or qforms.unchained(code, data.get("plain", ()))): return code, c["out"], "new"
    e = library_example(exs)
    if e: return e["code"].strip(NL), e["out"], "lib"
    return None

def example_html(cls, name, exs, data, lang):
    ex = pick(cls, name, exs, data)
    if not ex: return ""
    code, out, src = ex
    body = esc(code) + NL + NL.join("#--&gt; " + esc(l) for l in out_lines(out))
    return f'<pre class="rx">{body}</pre><span class="rx-src">{T[lang][src]}</span>'

def class_counts(c, entries, data):
    """how many of a class's listed methods have a library example, a composed one, or none"""
    nl = nc = 0
    for m in c["own"]:
        exs = entries.get((c["name"], m[0]))
        if library_example(exs, m[0]): nl += 1
        elif pick(c["name"], m[0], None, data): nc += 1
        elif library_example(exs): nl += 1
    return nl, nc, len(c["own"]) - nl - nc

def legend(c, entries, data, lang):
    t = T[lang]
    nl, nc, nn = class_counts(c, entries, data)
    if nl + nc == 0: return f'<p class="proof">{t["legend_effects"] if effects(c) else t["legend_none"]}</p>'
    recv = data["classes"].get(c["name"], {}).get("receiver", "").replace(NL, " ")
    text = t["legend"].format(nl=nl, nc=nc, nn=nn, recv=esc(recv)) if nc else t["legend_lib"].format(nl=nl, nn=nn)
    day = data["classes"].get(c["name"], {}).get("ran") or data.get("ran")
    ran = f' {t["ran"].format(d=esc(day))}' if day and nc else ""
    return f'<p class="proof">{text}{ran}</p>'

def _html(code, out, src, lang, on=None):
    body = esc(code) + NL + NL.join("#--&gt; " + esc(l) for l in out_lines(out))
    label = T[lang][src] + (f" · {on}" if on else "")
    return f'<pre class="rx">{body}</pre><span class="rx-src">{label}</span>'

def example_for_method(name, classes, entries, data, lang):
    """the A-Z index lists a method name once, with every class that has it: the example is the best one any of them has
    (the library's own first, then the shortest composed), and says which class it ran on"""
    best = None
    for cl in sorted(classes):
        ex = pick(cl, name, entries.get((cl, name)), data)
        if not ex: continue
        key = (0 if ex[2] == "lib" else 1, len(ex[0]))
        if best is None or key < best[0]: best = (key, cl, ex)
    if not best: return ""
    _, cl, (code, out, src) = best
    return _html(code, out, src, lang, on=cl)

def example_of_class(c, entries, data, lang):
    """the class index gives each class one example: of its methods, the one whose code is shortest, the library's own first"""
    best = None
    for m in c["own"]:
        ex = pick(c["name"], m[0], entries.get((c["name"], m[0])), data)
        if not ex or ex[0].count(NL) > 3: continue
        key = (0 if ex[2] == "lib" else 1, len(ex[0]) + len(ex[1]))
        if best is None or key < best[0]: best = (key, ex)
    if not best: return ""
    code, out, src = best[1]
    return _html(code, out, src, lang)
