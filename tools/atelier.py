#!/usr/bin/env python3
"""The Atelier on the site: its static edition, and the citation of one check (prompt 58, 2026-11-05).

The Atelier (libraries/stzlib/atelier/) runs the library's own narrated assertions live and, at every
commit, carries what it recorded: checks.json, results.json, tours.json. The contract is that folder's
EMBED.md. This module does three things with it and nothing else:

  build(root)         runs the pinned tree's build_static.py into <site>/atelier/, so the edition is a
                      derived folder like the rest of the output (never edited by hand)
  counts_html(lang)   the figures of the edition, each block carrying the commit that recorded it, and
                      the five states of a Then line shown apart, never folded into pass and fail
  cite_html(lang, id) one check rendered in the site's own style, with its citation printed; the
                      resolver (cite.py) answers or REFUSES, and a refusal stops the build

Where the tree is: the environment variable STZ_ATELIER_TREE (the folder that holds libraries/), else
the sibling folder _wtat of this repository: a sparse checkout of the library at the commit named in
data/atelier-pin.json. Without a tree the build prints that it skipped the edition, by name, and a
citation is answered from data/atelier-cites.json, the record of the last resolution (so a fresh
checkout still builds). The site's other pins (the sample runs) are not this pin and do not move.

Nothing here runs the library, shows a comparison with the former language, or edits the library.
"""
import html, json, os, pathlib, shutil, subprocess, sys, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PIN = ROOT / "data" / "atelier-pin.json"
CITES = ROOT / "data" / "atelier-cites.json"
OUT = ROOT / "atelier"


def pin():
    return json.loads(PIN.read_text(encoding="utf-8"))


def tree():
    """the atelier folder of the pinned tree, or None"""
    base = pathlib.Path(os.environ["STZ_ATELIER_TREE"]) if os.environ.get("STZ_ATELIER_TREE") else ROOT.parent / "_wtat"
    d = base / "libraries" / "stzlib" / "atelier"
    return d if (d / "build_static.py").exists() else None


def _run(args, cwd):
    return subprocess.run([sys.executable, "-I", "-X", "utf8", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                          env={**os.environ, "PYTHONIOENCODING": "utf-8"})


def edition():
    """the built edition (its edition.json), or None"""
    for f in sorted(OUT.glob("*/edition.json")):
        return json.loads(f.read_text(encoding="utf-8"))
    return None


def build():
    """derive the edition from the pinned tree; returns a line to print"""
    t = tree()
    if t is None:
        return "atelier edition: SKIPPED, no tree (set STZ_ATELIER_TREE or make the sibling _wtat); the edition on disk is kept as it is"
    if OUT.exists(): shutil.rmtree(OUT)
    r = _run(["build_static.py", "--out", str(OUT)], t)
    if r.returncode != 0:
        raise SystemExit("atelier edition REFUSED by build_static.py:\n" + r.stdout + r.stderr)
    ed = edition()
    if not ed or ed.get("mixed") or ed.get("ring_column"):
        raise SystemExit("atelier edition: mixed commits or a comparison column; the site publishes neither (EMBED.md, section 5)")
    return (f"atelier edition: {ed['commit']} derived from the pinned tree ({pin()['tree_commit']}): {ed['checks']} checks, "
            f"{ed['tours']['totals']['judged']} of {ed['tours']['totals']['claims']} Then lines judged")


def _n(lang, v):
    return f"{v:,}".replace(",", " " if lang == "fr" else ",")


SAY = {
    "en": {"checks": "checks recorded", "pass": "passed", "fail": "failed", "err": "ended in an error",
           "claims": "Then lines in {files} narrated test files", "judged": "judged",
           "kept": "kept", "diverged": "diverged", "unreached": "unreached", "unjudged": "unjudged", "unperceived": "unperceived",
           "rec": "Recorded at library commit <code>{commit}</code>, taken {taken}, judged by rnxc <code>{rnxc}</code> with the engine {engine}. These figures are the edition's; read them there:",
           "open": "the edition", "cov": "its coverage",
           "state_title": "The five states of a Then line"},
    "fr": {"checks": "vérifications enregistrées", "pass": "réussies", "fail": "échouées", "err": "terminées en erreur",
           "claims": "lignes Then dans {files} fichiers de test narrés", "judged": "jugées",
           "kept": "tenues", "diverged": "divergentes", "unreached": "non atteintes", "unjudged": "non jugées", "unperceived": "non perçues",
           "rec": "Enregistré au commit <code>{commit}</code> de la bibliothèque, pris le {taken}, jugé par rnxc <code>{rnxc}</code> avec le moteur {engine}. Ces chiffres sont ceux de l'édition ; lisez-les là :",
           "open": "l'édition", "cov": "sa couverture",
           "state_title": "Les cinq états d'une ligne Then"},
}


def _fig(n, label):
    return f'<div class="figure"><b>{n}</b><span>{label}</span></div>'


def counts_html(lang):
    ed = edition()
    if ed is None:
        raise SystemExit("<!--ATELIER:counts--> needs the edition: run the build with the pinned tree")
    s, c, t = SAY[lang], ed["counts"], ed["tours"]["totals"]
    q = f"?lang={lang}"
    base = f"../atelier/{ed['commit']}/"
    checks = "".join([_fig(_n(lang, ed["checks"]), s["checks"]), _fig(_n(lang, c["pass"]), s["pass"]),
                      _fig(_n(lang, c["fail"]), s["fail"]), _fig(_n(lang, c["err"]), s["err"])])
    # the five states, each its own figure: judged lines are kept or diverged, the others are not judged at all
    states = "".join(_fig(_n(lang, t[k]), s[k]) for k in ("kept", "diverged", "unreached", "unjudged", "unperceived"))
    rec = s["rec"].format(commit=html.escape(ed["commit"]), taken=html.escape(ed["taken"]), rnxc=html.escape(ed["rnxc"]),
                          engine=html.escape(ed["engine"]))
    return (f'<div class="figures">{checks}</div>'
            f'<h3>{s["state_title"]}</h3>'
            f'<p>{s["claims"].format(files=_n(lang, t["files"]))}: {_n(lang, t["claims"])}; {s["judged"]}: {_n(lang, t["judged"])}.</p>'
            f'<div class="figures">{states}</div>'
            f'<p class="proof">{rec} <a href="{base}index.html{q}">{s["open"]}</a> · <a href="{base}coverage.html{q}">{s["cov"]}</a></p>')


def _cache():
    return json.loads(CITES.read_text(encoding="utf-8")) if CITES.exists() else {}


def resolve(cid):
    """one check: from the pinned tree's resolver, else from the record of the last resolution; refuses by stopping the build"""
    ed = edition()
    if ed is None:
        raise SystemExit(f"<!--CITE:{cid}--> needs the edition")
    key = f"{ed['commit']}:{cid}"
    t = tree()
    cache = _cache()
    if t is not None:
        r = _run(["cite.py", key, "--format", "json"], t)
        if r.returncode != 0:
            raise SystemExit(f"citation REFUSED: {r.stdout.strip()} {r.stderr.strip()}".strip())
        rec = json.loads(r.stdout)
        if cache.get(key) != rec:
            cache[key] = rec
            CITES.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        return rec
    if key in cache: return cache[key]
    raise SystemExit(f"citation {key} cannot be resolved: no tree, and no record of an earlier resolution")


CITE_UI = {
    "en": {"state": {"pass": "passed", "fail": "failed", "err": "ended in an error"},
           "line": "{file}, line {line}, scenario {scenario}", "rec": "recorded: {state}, at library commit {commit}",
           "cit": "Citation", "open": "the check, in the edition"},
    "fr": {"state": {"pass": "réussie", "fail": "échouée", "err": "terminée en erreur"},
           "line": "{file}, ligne {line}, scénario {scenario}", "rec": "enregistré : {state}, au commit {commit} de la bibliothèque",
           "cit": "Citation", "open": "la vérification, dans l'édition"},
}


def cite_html(lang, cid):
    """one check as a card of the site's own, the citation printed; the code stays in the edition, which wraps it"""
    rec, u = resolve(cid), CITE_UI[lang]
    href = f"../atelier/{rec['commit']}/check.html?id={urllib.parse.quote(rec['id'], safe='')}&amp;lang={lang}"
    said = f'<p class="ran">{html.escape(rec["said"])}</p>' if rec["state"] != "pass" and rec.get("said") else ""
    return ('<div class="cards"><div class="card">'
            f'<h3>{html.escape(rec["description"])}</h3>'
            f'<p>{html.escape(u["line"].format(file=rec["file"], line=rec["line"], scenario=rec["scenario"]))}. '
            f'{html.escape(u["rec"].format(state=u["state"][rec["state"]], commit=rec["commit"]))}.</p>{said}'
            f'<p class="proof">{u["cit"]} <code>{html.escape(rec["citation"])}</code> · <a href="{href}">{u["open"]}</a></p>'
            '</div></div>')


if __name__ == "__main__":
    print(build())
