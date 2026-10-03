#!/usr/bin/env python3
"""A sample object for the classes the tests build in steps, mined WITH the lines that arrange it.

tools/rows_mine.py takes a construction whose arguments are literals, on one line. The classes still without an example
are the ones the library's tests build from VARIABLES or over several lines: `g = new stzGraph("g")`, a few
`g.AddNode(...)` lines, then `q = StzGraphQueryQ(g)`. The receiver of such a class is its construction plus the lines
that make its arguments:

  - the construction `x = new stzX(args)` or `x = StzXQ(args)` in base/test/**/*.ring is found; it may run over several
    lines (up to 14) when it holds no comment
  - walking back from it, a line is kept when it assigns a name the arguments use (and then the names ITS right-hand
    side uses), or calls a method on such a name (the object is built in steps); a print, a comment or a line of the
    test harness is not kept, and the walk stops at the start of the block (func, class, if, for, Scenario...)
  - the shortest candidates of each class are RUN, and the first one that builds an object whose classname is the class wins

The result is added to data/row-receivers.json, which tools/rows_run.py reads; a receiver already there is not replaced.

    python tools/rows_context.py <path to libraries/stzlib> [class ...]      (no class: every one with no example yet)
"""
import json, re, sys, pathlib, shutil, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from rows_run import run_all
from rows_mine import kind_of, literal_only

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "row-receivers.json"
NL = chr(10)
BS = chr(92)

START = re.compile(r"^\s*(\w+)\s*=\s*(?:new\s+(stz\w+)\s*\(|(Stz\w+?)Q\s*\()", re.I)
HEAD = re.compile(r"^\s*\w+\s*=\s*(?:new\s+stz\w+|Stz\w+?Q)\s*\(", re.I)
STOP = re.compile(r"(?i)^\s*(func|class|def|Scenario|EndScenario|Given|When|Then|if|but|else|ok|for|next|while|end|try|catch|done|return|load|import|package)\b")
STRING = re.compile(r'"(?:[^"\\]|\\.)*"|' + r"'(?:[^'\\]|\\.)*'")
IDENT = re.compile(r"\b[a-zA-Z_]\w*\b")
NOT_NAMES = {"new", "true", "false", "null", "nl", "tab", "cr", "and", "or", "not", "in"}
ASSIGN = re.compile(r"^\s*(\w+)\s*=\s*(.*?)\s*(?:#.*)?$")
CALL = re.compile(r"^\s*(\w+)\s*\.\s*\w+")

def names_in(text):
    t = STRING.sub('""', text)
    t = re.sub(r"\bnew\s+\w+", "", t, flags=re.I)
    t = re.sub(r"\.\s*\w+", "", t)                     # a method name is not a variable
    t = re.sub(r"\b\w+\s*\(", "(", t)                  # nor is a function name
    t = re.sub(r":\w+", "", t)                         # nor an atom
    return {n for n in IDENT.findall(t) if n.lower() not in NOT_NAMES}

def balance(line):
    t = STRING.sub('""', line)
    return t.count("(") - t.count(")")

def candidates(lib, wanted):
    """{class: [setup text]} shortest first"""
    low = {w.lower(): w for w in wanted}
    found = collections.defaultdict(set)
    for f in (lib / "base" / "test").rglob("*.ring"):
        try: lines = f.read_text(encoding="utf-8", errors="replace").split(NL)
        except OSError: continue
        for i, line in enumerate(lines):
            m = START.match(line)
            if not m: continue
            cname = (m.group(2) or ("stz" + m.group(3)[3:])).lower()
            if cname not in low: continue
            # the construction may run over several lines: read on until its parenthesis closes
            depth, text = 0, []
            for j in range(i, min(len(lines), i + 14)):
                text.append(lines[j].strip())
                depth += balance(lines[j])
                if depth <= 0: break
            if depth != 0 or sum(len(t) for t in text) > 420: continue
            if any("#" in STRING.sub('""', t) or "//" in STRING.sub('""', t) for t in text): continue
            args = HEAD.sub("", " ".join(text), count=1).rstrip().rstrip(")")
            used, keep = names_in(args), []
            for j in range(i - 1, max(-1, i - 26), -1):
                l = lines[j]
                if not l.strip() or l.strip().startswith(("#", "//", "?")): continue
                if STOP.match(l): break
                a_, c = ASSIGN.match(l), CALL.match(l)
                if a_ and a_.group(1) in used and not l.strip().endswith(("{", "[")):
                    keep.append(l.strip()); used |= names_in(a_.group(2))
                elif c and c.group(1) in used and "=" not in STRING.sub('""', l).replace("==", ""):
                    keep.append(l.strip())
                if len(keep) > 8: break
            if len(keep) > 8: continue
            var = m.group(1)
            if var in used: continue
            ctor = [re.sub(r"^(\w+)(\s*=)", r"o1" + BS + "2", text[0], count=1)] + text[1:]
            setup = [re.sub(r"\b" + re.escape(var) + r"\b", "o1", l) if var in names_in(l) else l for l in reversed(keep)] + ctor
            found[low[cname]].add(NL.join(setup))
    return {c: sorted(v, key=lambda s: (s.count(NL), len(s))) for c, v in found.items()}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    only = set(a for a in sys.argv[2:] if not a.startswith("--"))
    have = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"classes": {}}
    if only: wanted = sorted(only)
    else:
        todo = json.loads(pathlib.Path("/tmp/todo_classes.json").read_text(encoding="utf-8")) if pathlib.Path("/tmp/todo_classes.json").exists() else []
        wanted = [c[0] for c in todo]
    wanted = [w for w in wanted if w not in have["classes"]]
    cand = candidates(lib, wanted)
    print(f"{len(wanted)} classes asked, {len(cand)} have a construction with its arrangement in the tests", flush=True)
    work = lib / "base" / "test" / "_stzsite_ctx"
    work.mkdir(parents=True, exist_ok=True)
    jobs, meta = [], {}
    try:
        for cls, setups in cand.items():
            for s in setups[:4]:
                jid = len(jobs); jobs.append((jid, s, "? classname(o1)")); meta[jid] = (cls, s)
        res, crashed = run_all(work, jobs, batch=40, timeout=60)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    won = {}
    for jid, setup, code in jobs:
        cls, s = meta[jid]
        r = res.get(jid)
        if cls in won or not r or r[0] != "ok": continue
        if r[1].strip().split(NL)[-1].strip().lower() == cls.lower():
            last = s.split(NL)[-1]
            m = re.search(r"\((.*)\)\s*$", last)
            won[cls] = {"setup": s, "kind": kind_of(m.group(1)) if m and literal_only(m.group(1)) else "*", "arranged": True}
    have["classes"].update(won)
    OUT.write_text(json.dumps(have, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(won)} classes have a receiver that builds ({len(crashed)} constructions crashed or hung) -> data/row-receivers.json")
    for c, v in sorted(won.items()): print(f"  {c}: {v['setup'].splitlines()[-1][:90]}  (+{v['setup'].count(NL)} lines)")

if __name__ == "__main__":
    main()
