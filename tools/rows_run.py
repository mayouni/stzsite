#!/usr/bin/env python3
"""An example for every method of the reference, run in the library.

A reader should see that Softanza is practical, so each row of a class's reference table gets an
example. Where the library's own tests run an example of the method it is used (tools/examples_run.py).
For the others this tool COMPOSES one and RUNS it:

  - the signature of each method is read from the library source: its parameters are typed by their
    names (pc string, pn number, pa list, pb boolean, pDir a direction, and a table of the common names:
    pItem, pValue, pOtherNumber, pStartingAt...)
  - a sample object is built fresh for each call (a string "banana split", a list, a number, a hash list...)
  - the call is printed with @@( ... ); a method that returns nothing is followed by the object's content
  - only a call that RAN without raising and printed something is kept; the others are dropped, never shown

Methods that read or write files, draw, wait, ask the clock or chance, or print for the eye are not
composed. A call that crashes or hangs the process is isolated and dropped. One process per batch; the
temporary folder created in the library is removed at the end.

    python tools/rows_run.py <path to libraries/stzlib> [class ...] [--limit=N]
"""
import json, re, sys, pathlib, subprocess, datetime, shutil, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qforms
from harvest_examples import FORBIDDEN

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "row-examples.json"
WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)
EXTRA_FORBIDDEN = re.compile(r"(?i)(random|rnd|now|today|sleep|wait|clock|timer|stopwatch|viz|show|print|display|draw|render|plot|speak|say|learn|ask|howto|explain|doc\b|input|give|exit|halt|kill|system|execute|eval|compile|install|deploy|export|import|save|load|read|write|file|folder|path|url|http|socket|download|upload|copy\b)")

# class -> a fresh sample object per call, how to see its content, and the kind that picks the sample arguments
CLASSES = {
    "stzString":        {"setup": 'o1 = new stzString("banana split")',                                  "content": "o1.Content()", "kind": "str"},
    "stzList":          {"setup": 'o1 = new stzList([ 5, 3, 8, 3, 1 ])',                                 "content": "o1.Content()", "kind": "list",
                         "alt": 'o1 = new stzList([ "tea", "rice", "tea", "fish" ])', "altkind": "strlist"},
    "stzNumber":        {"setup": 'o1 = new stzNumber(12)',                                              "content": "o1.Value()",   "kind": "num"},
    "stzListOfNumbers": {"setup": 'o1 = new stzListOfNumbers([ 4, 8, 15, 16, 23, 42 ])',                 "content": "o1.Content()", "kind": "list"},
    "stzHashList":      {"setup": 'o1 = new stzHashList([ :name = "Aya", :age = 30, :city = "Niamey" ])', "content": "o1.Content()", "kind": "hash"},
    "stzStringChar":    {"setup": 'o1 = new stzStringChar("a")',                                         "content": "o1.Content()", "kind": "char"},
    "stzText":          {"setup": 'o1 = new stzText("Alice met Bob in Paris. The weather was fine.")',   "content": "o1.Content()", "kind": "str"},
    "stzListOfPairs":   {"setup": 'o1 = new stzListOfPairs([ [ 1, "a" ], [ 2, "b" ], [ 3, "c" ] ])',    "content": "o1.Content()", "kind": "pairs"},
    "stzMatrix":        {"setup": 'o1 = new stzMatrix([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ])',       "content": "o1.Content()", "kind": "matrix"},
    "stzStringList":    {"setup": 'o1 = new stzStringList([ "tea", "rice", "fish" ])',                   "content": "o1.Content()", "kind": "strlist"},
}

# the samples of the common parameter names, by kind of receiver ("*" for all)
KNOWN = {
    "pitem": {"str": '"a"', "list": "3", "strlist": '"tea"', "hash": '"Aya"', "pairs": "2", "num": "3", "*": "3"},
    "pvalue": {"str": '"a"', "list": "3", "strlist": '"tea"', "hash": '"Aya"', "num": "3", "*": "3"},
    "pval": {"*": "3"}, "pwith": {"str": '"x"', "*": "9"}, "pof": {"str": '"an"', "*": "3"},
    "pothernumber": {"*": "3"}, "pnumber": {"*": "3"}, "nnumber": {"*": "3"}, "pstartingat": {"*": "2"},
    "nwidth": {"*": "12"}, "cfillchar": {"*": '"*"'}, "anpos": {"*": "[ 1, 2 ]"}, "asections": {"*": "[ [ 1, 3 ] ]"},
    "nfrom": {"*": "2"}, "nstart": {"*": "2"}, "nvalue": {"*": "3"}, "nmin": {"*": "1"}, "nmax": {"*": "5"}, "ncol": {"*": "2"},
    "anumbers": {"*": "[ 1, 2, 3 ]"}, "c": {"*": '"a"'}, "pother": {"*": "3"},
    "pstart": {"*": "2"}, "pend": {"*": "4"}, "p1": {"*": "3"}, "p2": {"*": "4"}, "pnrow": {"*": "2"}, "pnindex": {"*": "2"}, "pnstep": {"*": "2"},
}

# receivers the library's tests build in steps (or only build empty): written by hand, from how the tests use them
HAND = {
    "stzGraph":        {"setup": 'o1 = new stzGraph("g")\no1.AddNode("A") o1.AddNode("B") o1.AddNode("C") o1.AddNode("D")\no1.AddEdge("A", "B") o1.AddEdge("A", "C") o1.AddEdge("B", "D")',
                        "content": None, "kind": "graph"},
    "stzDate":         {"setup": 'o1 = new stzDate([ 2026, 5, 30 ])', "content": None, "kind": "*"},
    "stzBinaryNumber": {"setup": 'o1 = new stzBinaryNumber("0b00101011000011")', "content": None, "kind": "*"},
    "stzHexNumber":    {"setup": 'o1 = new stzHexNumber("0xff")', "content": None, "kind": "*"},
    "stzBytes":        {"setup": 'o1 = new stzBytes("Hello")', "content": None, "kind": "str"},
    "stzListNamedParams": {"setup": 'o1 = new stzListNamedParams([ :Step, 3 ])', "content": None, "kind": "*"},
    # a question is a SENTENCE, not an object to call: each of its 1,078 methods is a word of the chain, closed by Of(...).
    # The frames are tried in turn (a noun of text, a noun of number, then the same after the copula) and the first that answers is kept
    "stzQuestion":     {"setup": "", "alt": "", "alt2": "", "alt3": "", "content": None, "kind": "*", "make": "question"},
}
EMPTY_RECEIVER = re.compile(r"""\(\s*(""|''|\[\s*\]|0)?\s*\)$""")

# a class whose every method is the same question put to a different word: the receiver is made from the method's own name.
# stzListNamedParams has 1,913 methods IsXNamedParam(), each true for a list that holds the keyword X
OVERRIDE = {}                                  # (class, method) -> the setup that method is run on
REQUIRE = {"stzListNamedParams"}               # for these the example is kept only when the answer is the true one (1)
NP = re.compile(r"Is(\w+?)NamedParams?$", re.I)

def named_param_setup(name):
    m = NP.fullmatch(name)
    if not m: return None
    word = re.split(r"(?<=[a-z])Or(?=[A-Z])", m.group(1))[0]          # IsOverOrOverNumber: the first of the words it accepts
    return f"o1 = new stzListNamedParams([ :{word}, 3 ])" if word.isidentifier() else None

FRAMES = {"setup": 'WhatQ().TheQ().{n}().Of("Softanza")', "alt": "WhatQ().TheQ().{n}().Of(12)",
          "alt2": 'IsQ().TheQ().{n}().Of("Softanza")', "alt3": "IsQ().TheQ().{n}().Of(12)"}

def make_code(R, name, stage):
    """the code of a class whose methods are words of a sentence"""
    return "? @@( " + FRAMES[stage].format(n=name) + " )"

def mined():
    """the receivers mined from the library's tests (tools/rows_mine.py), for the classes with no hand-written one;
    a receiver built from nothing (an empty string, an empty list) says nothing about its methods and is left out"""
    f = ROOT / "data" / "row-receivers.json"
    if not f.exists(): return {}
    got = json.loads(f.read_text(encoding="utf-8"))["classes"]
    out = {c: {"setup": v["setup"], "kind": v["kind"], "content": None, "mined": True} for c, v in got.items() if c not in CLASSES and not EMPTY_RECEIVER.search(v["setup"])}
    out.update({c: dict(v, mined=True) for c, v in HAND.items() if c not in CLASSES})
    h = ROOT / "data" / "row-receivers-hand.json"                  # written by hand, probed by tools/rows_probe.py: an empty construction is meant
    if h.exists():
        out.update({c: {"setup": v["setup"], "kind": v["kind"], "content": None, "mined": True} for c, v in json.loads(h.read_text(encoding="utf-8"))["classes"].items() if c not in CLASSES})
    return out

def sample(p, nth, kind):
    """the sample argument for a parameter (nth: how many numeric parameters came before it), or None when its name says nothing"""
    p0 = p.strip("_")
    q = p0.lower()
    m0 = re.match(r"([cnab])([A-Z]\w*)$", p0)               # cStr, nRow, aToken, bShow: the same prefixes as pcStr, pnRow, paToken, pbShow
    if m0: q = ("p" + m0.group(1) + m0.group(2)).lower()
    if kind == "graph":
        core = re.sub(r"^(pc|pn|pa|pb|c|n)", "", q)
        if core in ("from", "source", "start", "root", "node", "nodeid", "id", "node1", "a", "name"): return '"A"'
        if core in ("to", "target", "end", "dest", "destination", "node2", "b"): return '"D"'
    if q in KNOWN:
        d = KNOWN[q]; return d.get(kind, d.get("*"))
    if q.startswith("pc") or re.fullmatch(r"c\d?", q):
        if re.search(r"lang", q): return '"en"'
        if re.search(r"new|with|replac", q): return '"AN"'
        if re.search(r"delim|sep", q): return '" "'
        if re.search(r"cond|expr|where", q): return '"@char = \'a\'"' if kind in ("str", "char") else '"@item > 3"'
        if re.search(r"case", q): return "TRUE"
        return '"an"' if kind in ("str",) else '"a"'
    if q.startswith("pn") or re.fullmatch(r"n\d?", q) or q.startswith("n") and q[1:2].isupper():
        return {0: "2", 1: "5"}.get(nth, "2")
    if q.startswith("pa") or re.fullmatch(r"a\d?", q):
        return '[ "an", "a" ]' if kind == "str" else "[ 2, 3 ]"
    if q.startswith("pb") or "casesensitive" in q or q in ("pcs", "bcs"):
        return "TRUE"
    if q.startswith("pdir") or q == "pdirection":
        return ":Forward"
    return None

DEF = re.compile(r"^\s*def\s+(\w+)\s*\(([^)]*)\)", re.I)

def signatures(lib, c):
    f = lib / "base" / c["file"]
    lines = f.read_text(encoding="utf-8", errors="replace").split("\n")
    start = next((i for i, l in enumerate(lines) if re.match(rf"\s*class\s+{re.escape(c['name'])}\b", l, re.I)), 0)
    out = {}
    for l in lines[start:]:
        m = DEF.match(l)
        if m: out.setdefault(m.group(1).lower(), (m.group(1), [p.strip() for p in m.group(2).split(",") if p.strip()]))
    return out

def candidates(lib, ref, only):
    """[(class, method, kind, [(variant, code)])] for every method that can be composed"""
    out, skipped = [], collections.Counter()
    for c in ref["classes"]:
        if c["name"] not in CLASSES or (only and c["name"] not in only): continue
        R = CLASSES[c["name"]]
        S = signatures(lib, c)
        for m in c["own"]:
            name = m[0]
            if R.get("make"):
                if name.lower() in ("init", "thesameasq", "of", "in", "ornot", "is", "why") or name.endswith("Q") is False or FORBIDDEN.search(name) or EXTRA_FORBIDDEN.search(name):
                    skipped["not a noun of the sentence"] += 1; continue
                out.append((c["name"], name, [("A", "")])); continue
            if c["name"] in REQUIRE:
                st = named_param_setup(name)
                if not st: skipped["not a keyword question"] += 1; continue
                OVERRIDE[(c["name"], name)] = st
                out.append((c["name"], name, [("A", f"? @@( o1.{name}() )")])); continue
            if FORBIDDEN.search(name) or EXTRA_FORBIDDEN.search(name) or name.lower() in ("init", "content", "value") or "NamedParam" in name:
                skipped["forbidden name"] += 1; continue
            s = S.get(name.lower())
            if not s: skipped["no signature"] += 1; continue
            args, nnum = [], 0
            for p in s[1]:
                args.append(sample(p, nnum, R["kind"]))
                q = p.strip("_").lower()
                if args[-1] is not None and re.fullmatch(r"-?\d+", args[-1]) and not q.startswith(("pitem", "pvalue", "pval", "pother", "pnumber", "nnumber")): nnum += 1
            if any(a is None for a in args): skipped["parameter not understood"] += 1; continue
            call = f'o1.{name}({", ".join(args)})'
            vs = [("A", f"? @@( {call} )")] + ([("B", f"{call}\n? @@( {R['content']} )")] if R.get("content") else [])
            out.append((c["name"], name, vs))
    return out, skipped

def run_batch(work, items, timeout):
    """items: [(id, setup, code)] -> {id: ('ok', out) | ('error', text)} and the id that was running when the process stopped, if any"""
    lines = ['load "../../../max/stzMax.ring"', ""]
    for i, setup, code in items:
        lines += [f'? "@@BEGIN {i}"', "try"] + ["    " + l for l in setup.split("\n")] + ["    " + l for l in code.split("\n")] + ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"']
    (work / "rows.ring").write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        p = subprocess.run(["ring", "rows.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        out = (p.stdout or "").replace("\r", "")
    except subprocess.TimeoutExpired as e:
        out = (e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")).replace("\r", "")
    res, running = {}, None
    for i, setup, code in items:
        m = re.search(rf"@@BEGIN {i}\n(.*?)(?:\n?@@END {i}\n|\Z)", out + "\n", re.S)
        if not m: continue
        body = m.group(1)
        if f"@@END {i}" not in out:
            running = i; break
        if "@@ERROR" in body: res[i] = ("error", body.split("@@ERROR ", 1)[1].strip())
        else: res[i] = ("ok", body.rstrip())
    return res, running

def run_all(work, jobs, batch=100, timeout=90):
    """jobs: [(id, setup, code)]; a call that crashes or hangs the process is isolated by halving the batch, and reported as crashed"""
    results, crashed = {}, []
    stack = [jobs[i:i + batch] for i in range(0, len(jobs), batch)][::-1]
    while stack:
        chunk = stack.pop()
        if not chunk: continue
        res, running = run_batch(work, chunk, timeout)
        results.update(res)
        rest = [j for j in chunk if j[0] not in res]
        if running is not None:
            crashed.append(running); rest = [j for j in rest if j[0] != running]
            if rest: stack.append(rest)
        elif rest:                                               # the process ended without saying where: halve it
            if len(rest) == 1: crashed.append(rest[0][0])
            else:
                h = len(rest) // 2
                stack.append(rest[h:]); stack.append(rest[:h])
    return results, crashed

EMPTY = ("", '""', "[ ]", "NULL")
# a method that returns nothing is shown with the object's content afterwards only when its first word is a verb that changes it:
# for a query (Find, Value, Is...) that returned nothing, the content would read as the result
MUTATOR = (r"(Remove|Replace|Add|Insert|Set|Update|Reverse|Sort|Uppercase|Lowercase|Clear|Trim|Swap|Move|Extend|Shorten|Simplify|Normalize|"
           r"Capitalize|Capitalise|Append|Prepend|Push|Pop|Delete|Erase|Fill|Merge|Shuffle|Rotate|Repeat|Transform|Convert|Increment|Decrement|"
           r"Negate|Double|Halve|Pad|Strip|Truncate|Wrap|Unwrap|Compact|Flatten|Duplicate|Rename|Change|Make|Turn|Cut|Split|Join|Mutate)(?=[A-Z]|$)")

def keep(out, receiver="", cls=""):
    """an example says something: not nothing, not the object's own content again, not a wall of text"""
    t = out.strip()
    if cls in REQUIRE: return t == "1"
    if t in EMPTY or t == receiver or len(t) > 220 or t.count("\n") > 6: return False
    if re.fullmatch(r'[\[\]\s,"]*', t): return False                       # [ "", "" ] or [ [ ], [ ] ]: nothing in it
    if re.search(r"(?i)\berror\b|exception|^object|not defined|without definition", t) or re.match(r"@\w+$", t): return False   # an object's name is not an answer
    return not WORD.search(t)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    args = [a for a in sys.argv[2:] if not a.startswith("--")]
    limit = next((int(a.split("=")[1]) for a in sys.argv[2:] if a.startswith("--limit=")), 0)
    only = set(args)
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    ref = qforms.reference(ROOT)
    CLASSES.update(mined())
    work = lib / "base" / "test" / "_stzsite_rows"
    work.mkdir(parents=True, exist_ok=True)
    t0 = datetime.datetime.now()
    kept, stats = {}, collections.Counter()
    try:
        # a mined receiver has no known way to show its content: the first of these that answers on it is its way
        names = [c["name"] for c in ref["classes"] if c["name"] in CLASSES and (not only or c["name"] in only) and CLASSES[c["name"]].get("mined")]
        pj = [(i * 2 + k, CLASSES[c]["setup"], f"? @@( o1.{acc}() )") for i, c in enumerate(names) for k, acc in enumerate(("Content", "Value"))]
        pres, _ = run_all(work, pj, timeout=60)
        for i, c in enumerate(names):
            for k, acc in enumerate(("Content", "Value")):
                r = pres.get(i * 2 + k)
                if r and r[0] == "ok" and r[1].strip() not in EMPTY:
                    CLASSES[c]["content"] = f"o1.{acc}()"; break
        print(f"{len(names)} mined classes; {sum(1 for c in names if CLASSES[c]['content'])} show their content", flush=True)
        cands, skipped = candidates(lib, ref, only)
        if limit: cands = cands[:limit]
        print(f"{len(cands)} methods composed; skipped {dict(skipped)}", flush=True)
        # what each sample object prints for its own content, to drop an example that only repeats it
        classes = sorted({c for c, _, _ in cands if CLASSES[c].get("content")})
        rj = [(i, CLASSES[c]["setup"], f"? @@( {CLASSES[c]['content']} )") for i, c in enumerate(classes)]
        rres, _ = run_all(work, rj)
        recv = {c: rres[i][1].strip() for i, c in enumerate(classes) if i in rres and rres[i][0] == "ok"}
        for stage in ("setup", "alt", "alt2", "alt3"):
            jobs, meta = [], {}
            for cls, name, variants in cands:
                if (cls, name) in kept: continue
                R = CLASSES[cls]
                setup = (OVERRIDE.get((cls, name)) or R["setup"]) if stage == "setup" else R.get(stage)
                if setup is None or (not setup and not R.get("make")): continue
                for v, code in variants:
                    if R.get("make"): code = make_code(R, name, stage)
                    jid = len(jobs); jobs.append((jid, setup, code)); meta[jid] = (cls, name, v, setup, code)
            if not jobs: continue
            # first the plain call (A); the content variant (B) only for what printed nothing
            a_jobs = [j for j in jobs if meta[j[0]][2] == "A"]
            bjob = {meta[j[0]][:2]: j for j in jobs if meta[j[0]][2] == "B"}
            res, crashed = run_all(work, a_jobs)
            stats["crashed"] += len(crashed)
            b_jobs = []
            for jid, setup, code in a_jobs:
                cls, name, v, st, cd = meta[jid]
                r = res.get(jid)
                if r and r[0] == "ok" and keep(r[1], recv.get(cls, ""), cls): kept[(cls, name)] = {"setup": st, "code": cd, "out": r[1].strip(), "variant": "A", "stage": stage}
                elif r and r[0] == "ok" and r[1].strip() in ("", '""', "NULL") and re.match(MUTATOR, name) and (cls, name) in bjob:
                    b_jobs.append(bjob[(cls, name)])
            res_b, crashed_b = run_all(work, b_jobs)
            stats["crashed"] += len(crashed_b)
            for jid, setup, code in b_jobs:
                cls, name, v, st, cd = meta[jid]
                r = res_b.get(jid)
                if r and r[0] == "ok" and keep(r[1], recv.get(cls, ""), cls): kept[(cls, name)] = {"setup": st, "code": cd, "out": r[1].strip(), "variant": "B", "stage": stage}
            print(f"stage {stage}: {len(kept)} kept so far", flush=True)
        # an example must not depend on the calls that ran before it in the same process: run every kept one again,
        # in the opposite order and in other batches, and keep only those that print the same
        vkeys = list(kept)[::-1]
        vjobs = [(i, kept[k]["setup"], kept[k]["code"]) for i, k in enumerate(vkeys)]
        vres, vcrashed = run_all(work, vjobs, batch=37, timeout=60)
        for i, k in enumerate(vkeys):
            r = vres.get(i)
            if not (r and r[0] == "ok" and r[1].strip() == kept[k]["out"]): del kept[k]; stats["unstable"] += 1
        print(f"verify: {stats['unstable']} dropped because a second run, in another order, printed something else", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    seconds = round((datetime.datetime.now() - t0).total_seconds(), 1)
    by = collections.defaultdict(dict)
    meta_classes, stamp = {}, t0.strftime("%Y-%m-%d %H:%M")
    if only and OUT.exists():                                  # a partial run replaces its own classes and keeps the others, with the date of their own run
        before = json.loads(OUT.read_text(encoding="utf-8"))
        for c, v in before["examples"].items():
            if c not in only: by[c] = v; meta_classes[c] = dict(before["classes"].get(c, {}), ran=before["classes"].get(c, {}).get("ran", before.get("ran", "")))
    for (cls, name), v in kept.items(): by[cls][name] = v
    for c in by:
        if c in CLASSES and c not in meta_classes: meta_classes[c] = {"receiver": CLASSES[c]["setup"], "content": CLASSES[c].get("content"), "ran": stamp}
    res = {"ran": stamp, "seconds": seconds, "classes": meta_classes, "examples": by}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    tot = collections.Counter({c: len(v) for c, v in by.items()})
    n = collections.Counter({c: sum(1 for x in cands if x[0] == c) for c in tot})
    for c in sorted(tot): print(f"{c:20} composed {n[c]:5} kept {tot[c]:5}")
    print(f"{len(kept)} of {len(cands)} composed methods kept an example in {seconds} s; crashed or hung: {stats['crashed']}; unstable: {stats['unstable']} -> data/row-examples.json")

if __name__ == "__main__":
    main()
