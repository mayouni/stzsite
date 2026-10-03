#!/usr/bin/env python3
"""A sample object for every class of the reference, mined from the library's own tests.

tools/rows_run.py composes an example for each method of a class, on a fresh sample object. For ten classes the
object is written by hand (CLASSES in rows_run.py). For the others it is MINED: the library's tests build objects
from literals all day (`o1 = new stzGraph(...)`), and a literal the library itself uses is a receiver the library
vouches for.

  - candidates: single-line constructions `new stzX( ... )` and `StzXQ( ... )` in base/test/**/*.ring whose
    arguments are literals only (strings, numbers, lists, :atoms, TRUE, FALSE, NULL) and short
  - each class is tried with its three shortest non-empty candidates, then the empty construction; the first one
    that builds an object whose classname is the class wins, and the verdict is its RUN, not its look
  - the kind of receiver (a string, a list of numbers, of strings, of pairs, a hash list, a number) is read from the
    literal, so the sample arguments of the methods fit it

Nothing is composed for the classes of the areas that touch the machine, the network, the clock or the ear.

    python tools/rows_mine.py <path to libraries/stzlib>       -> data/row-receivers.json
"""
import json, re, sys, pathlib, subprocess, datetime, shutil, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qforms
from rows_run import run_all

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "row-receivers.json"

from rowex import SKIP_AREAS, SKIP_CLASS      # the areas and classes that touch the machine: nothing is composed for them

STRIP = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'')

def literal_only(args):
    """the argument text holds literals only: strings, numbers, lists, :atoms, = , TRUE, FALSE, NULL"""
    t = STRIP.sub('""', args)
    t = re.sub(r":\w+", "", t)
    t = re.sub(r"\b(TRUE|FALSE|NULL)\b", "", t, flags=re.I)
    return not re.search(r"[A-Za-z_@$]", t)

def balanced(s):
    d = 0
    for ch in STRIP.sub('""', s):
        if ch in "([": d += 1
        elif ch in ")]": d -= 1
        if d < 0: return False
    return d == 0

def kind_of(args):
    a = args.strip()
    if not a: return "*"
    if a.startswith(('"', "'")): return "str"
    if re.fullmatch(r"-?\d+(\.\d+)?", a): return "num"
    if a.startswith("["):
        inner = a[1:-1].strip()
        if re.match(r":\w+\s*=", inner): return "hash"
        if re.match(r"\[\s*[^\[\]]*,\s*[^\[\]]*\]\s*(,|$)", inner) and not inner.startswith("[ [") and re.fullmatch(r"(\[[^\[\]]*\]\s*,?\s*)+", inner):
            return "pairs" if all(len(p.split(",")) == 2 for p in re.findall(r"\[([^\[\]]*)\]", inner)) else "matrix"
        if re.fullmatch(r"\s*(\"[^\"]*\"\s*,?\s*)+", inner): return "strlist"
        return "list"
    return "*"

PATHLIKE = re.compile(r"[/\\]|\.(ttf|ring|txt|csv|json|md|html)\b|t_edu_")        # a path is a machine, not a receiver
TRIVIAL = re.compile(r"""^(|""|''|\[\s*\]|0|"x"|"o"|"i"|"G")$""")

def rank(a):
    """a receiver with something in it first, of a length that reads as an example; the empty ones last"""
    return (1 if TRIVIAL.match(a.strip()) else 0, abs(len(a) - 28))

def mine_candidates(lib, classes):
    """{class: [ctor text, ...]} shortest first"""
    names = {c["name"].lower(): c["name"] for c in classes}
    found = collections.defaultdict(set)
    ctor = re.compile(r"\bnew\s+(stz\w+)\s*\((.*)\)\s*$|\b(Stz\w+?)Q\s*\((.*)\)\s*$", re.I)
    for f in (lib / "base" / "test").rglob("*.ring"):
        try: text = f.read_text(encoding="utf-8", errors="replace")
        except OSError: continue
        for line in text.split("\n"):
            if len(line) > 200 or "new" not in line.lower() and "stz" not in line.lower(): continue
            for m in re.finditer(r"\bnew\s+(stz\w+)\s*\(|\b(Stz\w+?)Q\s*\(", line, re.I):
                cname = (m.group(1) or ("stz" + m.group(2)[3:])).lower()
                if cname not in names: continue
                i = m.end(); d = 1; j = i
                while j < len(line) and d > 0:
                    if line[j] in "([": d += 1
                    elif line[j] in ")]": d -= 1
                    j += 1
                if d != 0: continue
                args = line[i:j - 1].strip()
                if len(args) > 90 or not literal_only(args) or not balanced(args): continue
                found[names[cname]].add(args)
    return {c: sorted((a for a in v if not PATHLIKE.search(a)), key=rank) for c, v in found.items()}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    ref = qforms.reference(ROOT)
    classes = [c for c in ref["classes"] if c["area"] not in SKIP_AREAS and not SKIP_CLASS.search(c["name"])]
    print(f"{len(classes)} of {len(ref['classes'])} classes are in the areas that may be composed", flush=True)
    cand = mine_candidates(lib, classes)
    print(f"{len(cand)} classes have a literal construction in the library's tests", flush=True)
    work = lib / "base" / "test" / "_stzsite_mine"
    work.mkdir(parents=True, exist_ok=True)
    t0 = datetime.datetime.now()
    jobs, meta = [], {}
    try:
        for cls, args_list in cand.items():
            tries = args_list[:3] + [a for a in ("",) if a in args_list and a not in args_list[:3]]
            for a in tries:
                jid = len(jobs); jobs.append((jid, f"o1 = new {cls}({a})", "? classname(o1)")); meta[jid] = (cls, a)
        res, crashed = run_all(work, jobs, batch=60, timeout=60)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    won = {}
    for jid, setup, code in jobs:
        cls, a = meta[jid]
        r = res.get(jid)
        if cls in won or not r or r[0] != "ok": continue
        if r[1].strip().lower() == cls.lower():
            won[cls] = {"setup": f"o1 = new {cls}({a})", "kind": kind_of(a)}
    out = {"mined": t0.strftime("%Y-%m-%d %H:%M"), "classes": won}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds = collections.Counter(v["kind"] for v in won.values())
    print(f"{len(won)} classes have a receiver that builds ({dict(kinds)}); {len(crashed)} constructions crashed or hung -> data/row-receivers.json")

if __name__ == "__main__":
    main()
