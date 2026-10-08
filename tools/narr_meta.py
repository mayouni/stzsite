#!/usr/bin/env python3
"""The research index's card for each article, DERIVED until the articles carry their own header (B34 of the external assessment).

The narrations are the author's articles (re-ruled 2026-10-07): 135 essays under base/doc/narrations. Each page and the index need a
card: the abstract, the genre, the series, the Atlas area, the year, the author, the guards it names, related reading. The library's
articles carry none of that as data yet, so this tool derives it, and every derived field says so on the page:

  abstract   the first paragraph of prose under the title, in Haro's name, cut at a sentence near 260 characters
  genre      one of: paradigm essay, feature essay, design essay, comparison, tutorial, use case, series; read from the file name
             and the title by the rules below, which are the assessment's taxonomy applied to names, not to bodies
  series     the three 2026 series, by their files: performance (11), security (14), delivery (5)
  area       the Atlas area the name points to, or none when it points to several
  year       the first commit that added the file to the repository (git log --follow), cached in data/narrations-dates.json
  guards     the scenario guards an article names (a *_narrated.ring file), each found in the test tree
  related    the articles it links to, then the ones that share the most classes with it

    python tools/narr_meta.py <path to libraries/stzlib>        -> data/narrations-meta.json
"""
import json, re, sys, pathlib, subprocess, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import haro
from narrations_run import dedent_fences

OUT = ROOT / "data" / "narrations-meta.json"
DATES = ROOT / "data" / "narrations-dates.json"
AUTHOR = "Mansour Ayouni"

SERIES = {
  "performance": ["stz-perf-driven-load", "stz-perf-frame-profiler", "stz-perf-governed-loop", "stz-perf-judgment", "stz-perf-labels",
                  "stz-perf-log-trace", "stz-perf-profile", "stz-perf-seams", "stz-perf-tracing-tail", "stz-metrics-monitor", "stz-structured-logging"],
  "security": ["stz-security-attestation", "stz-security-detection", "stz-security-drill", "stz-security-event", "stz-security-incident",
               "stz-security-ledger", "stz-security-response", "stz-security-seams-2", "stz-security-seams", "stz-security-sentinel",
               "stz-auth-the-front-door", "stz-guarding-secrets-and-credentials", "stz-governing-project-security", "stz-governance-lineage"],
  "delivery": ["stz-deploying-to-target-sites", "stz-emulating-the-whole-solution", "stz-planning-and-provisioning-a-deployment",
               "stz-system-dev-to-deploy", "stz-service-virtualization-code-first-subscribe-later"],
}
GENRES = [   # first match wins; the words are read in the file name and the title, lowercased
  ("comparison", r"-vs-|\bvs\b|opinion|battle|compared"),
  ("paradigm essay", r"mental-mode|bridging-minds|linguistic|function-forms|near-natural-language-programming|knowledge-programming|conditional-code|"
                     r"reaxis|reactive-programming-semantics|regex-as-computational|refinement-centered|domain-driven|beyond-loops|computational-foundation|"
                     r"rules-as-graph|agents-that-cannot|future-actions|fututure-actions|time-programming|temporal-design|sequential-bottlenecks|"
                     r"pattern-langua|pattern-matching|patterns-made|declarative-pattern"),
  ("tutorial", r"tutorial|guide|\bdoc\b|doc\.md|-doc|first-app|intro|getting-started|mastering"),
  ("use case", r"usecase|use-case|bank|real-world|getting-paid"),
  ("design essay", r"philosophy|design|says-no|honest|senses|sees-the|built-on|truth|semantics|lineage|elegance"),
]
AREAS = [    # first match wins: (Atlas slug, words in the file name)
  ("performance", r"perf|metrics|stopwatch|structured-logging"),
  ("security", r"security|auth-|secrets|governance-lineage"),
  ("agents", r"agents-that|adverb"),
  ("regex", r"regex|listex|numbex|numbrex|timex|matrex|tablex|graphex"),
  ("string", r"stzstring|string-|unicode|lookalit|stringart"),
  ("collections", r"stzlist|deep-lists|hashlist|walker|repeat|repetition|sections|named-vars|object-history|find|fastporupdate|istrue"),
  ("numeric", r"matrix|linearsolver|random|probabilistic"),
  ("tables", r"stztable|dataset"),
  ("i18n", r"locale"),
  ("nlp", r"natural|knowledge-programming|linguistic|function-forms|bridging-minds|mental-mode"),
  ("diagramming", r"graph|orgchart|dotcode|planner"),
  ("concurrency", r"reaxis|reactive"),
  ("extensibility", r"excis|exterlib|pycode|r-scripts|polycode"),
  ("system", r"lowlevel|systemcall|system-dev|deploy|emulating|provisioning|service-virtualization|engine-senses"),
  ("web", r"stzapp|appserver|url|getting-paid"),
  ("files", r"stzfile|stzfolder|xml"),
  ("graphics", r"plotting|eye-sees"),
]
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+\.md)\)")
GUARD = re.compile(r"[\w-]+_narrated\.ring")
CLASS = re.compile(r"\bstz[A-Z]\w+")

def strip_md(s):
    s = IMAGE.sub("", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"[*_`]{1,3}", "", s)
    return re.sub(r"\s+", " ", s).strip()

def abstract(text):
    body = re.sub(r"(?m)\A\s*# [^\n]*\n", "", text, count=1)
    body = re.sub(r"(?ms)^```.*?^```[ \t]*$", "", body)
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "!", ">", "|", "-", "*", "<", "---")) or re.match(r"\d+\.", p): continue
        t = strip_md(p)
        if len(t) < 40: continue
        if len(t) > 260:
            cut = max(t.rfind(". ", 0, 260), t.rfind("; ", 0, 260))
            t = t[:cut + 1] if cut > 120 else t[:257].rstrip() + "..."
        return t
    return ""

def first_dates(lib, files):
    cache = json.loads(DATES.read_text(encoding="utf-8")) if DATES.exists() else {}
    repo = lib.parent.parent
    todo = [f for f in files if f not in cache]
    for i, f in enumerate(todo, 1):
        p = subprocess.run(["git", "-C", str(repo), "log", "--follow", "--format=%as", "--", f"libraries/stzlib/base/doc/narrations/{f}"],
                           capture_output=True, text=True)
        lines = [l for l in p.stdout.split("\n") if l.strip()]
        cache[f] = lines[-1] if lines else ""
        if i % 20 == 0: print(f"  dated {i} of {len(todo)}", flush=True)
    DATES.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")
    return cache

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    folder = lib / "base" / "doc" / "narrations"
    files = sorted(f.name for f in folder.glob("*.md"))
    guard_paths = {p.name: p.relative_to(lib).as_posix() for p in (lib / "base" / "test").rglob("*_narrated.ring")}
    dates = first_dates(lib, files)
    hosted = {p.stem for p in (ROOT / "assets" / "img" / "narrations").glob("*.webp")}
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    cards, classes = {}, {}
    for f in files:
        raw = (folder / f).read_text(encoding="utf-8", errors="replace").replace("\r", "")
        text = dedent_fences(haro.rename(raw)[0])           # the same text the run and the page read
        key = (f.lower() + " " + next((l[2:] for l in text.split("\n") if l.startswith("# ")), "")).lower()
        stem = f[:-3]
        series = next((s for s, names in SERIES.items() if any(stem == n or stem.startswith(n + "-narration") for n in names)), None)
        genre = "series" if series else next((g for g, rx in GENRES if re.search(rx, key)), "feature essay")
        area = next((a for a, rx in AREAS if re.search(rx, f.lower())), None)
        img = IMAGE.search(text)
        hero = None
        if img:
            st = pathlib.PurePosixPath(img.group(2)).stem
            if st in hosted: hero = {"src": st + ".webp", "alt": strip_md(img.group(1))}
        named = sorted(set(GUARD.findall(text)))
        classes[f] = set(CLASS.findall(text))
        cards[f] = {"title": next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), stem), "abstract": abstract(text),
                    "genre": genre, "series": series, "area": area, "date": dates.get(f, ""), "year": dates.get(f, "")[:4], "author": AUTHOR,
                    "hero": hero, "guards": [{"name": g, "path": guard_paths.get(g)} for g in named],
                    "links": [l for l in dict.fromkeys(pathlib.PurePosixPath(t).name for t in LINK.findall(text)) if l in files and l != f]}
    for f, c in cards.items():
        share = sorted(((len(classes[f] & classes[g]), g) for g in files if g != f and g not in c["links"] and classes[f] & classes[g]), reverse=True)
        c["related"] = c["links"][:6] + [g for n, g in share[:max(0, 4 - len(c["links"][:6]))] if n >= 2]
    OUT.write_text(json.dumps({"commit": commit, "derived": "genre, series, area: from the file name and the title; year: the first commit "
                               "that added the file; abstract: the first paragraph. The articles' own header (B34) replaces each.",
                               "articles": cards}, ensure_ascii=False, indent=1), encoding="utf-8")
    g = collections.Counter(c["genre"] for c in cards.values()); a = collections.Counter(c["area"] or "-" for c in cards.values())
    print(f"{len(cards)} cards at {commit}: genres {dict(g)}; areas {dict(a)}; with a hero {sum(1 for c in cards.values() if c['hero'])}; "
          f"naming a guard {sum(1 for c in cards.values() if c['guards'])}; with no abstract {sum(1 for c in cards.values() if not c['abstract'])}")

if __name__ == "__main__":
    main()
