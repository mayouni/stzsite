#!/usr/bin/env python3
"""Read every method's and every global function's parameters from the library's source, for the machine readers.

The AI-agent reader of 2026-10-15 (doc/STRUCTURE-2026-10-15.md) could find a method in agents/index.json but not call it:
the index named the method and its example, never its parameters, and the library's global functions (StzReplace, Q,
StzFind...) were not in it at all. Both are in the source. A Ring file declares its global functions before its first
class; after `class X` every func or def belongs to X until the next class. This tool reads that, in the library's
folders that are not tests, and writes what it found; it changes nothing in the library.

    python tools/signatures_run.py <path to libraries/stzlib>      -> data/signatures.json
"""
import json, re, sys, subprocess, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLASS = re.compile(r"^\s*class\s+(\w+)", re.I)
DEF = re.compile(r"^\s*(?:def|func)\s+([A-Za-z_@]\w*)\s*(?:\(([^)]*)\))?", re.I)

def params(raw):
    return [p.strip() for p in (raw or "").split(",") if p.strip()]

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    base = lib / "base"
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    methods = collections.defaultdict(dict)       # class (lower) -> method (lower) -> {"name", "params"}
    functions = {}                                # function (lower) -> {"name", "params", "file"}
    files = 0
    for f in sorted(base.rglob("*.ring")):
        rel = f.relative_to(base).as_posix()
        if rel.startswith("test/") or "/test/" in rel or "/archive/" in rel or rel.startswith("_"): continue       # tests and archived copies are not the library
        files += 1
        cur = None
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            m = CLASS.match(line)
            if m: cur = m.group(1); continue
            d = DEF.match(line)
            if not d: continue
            name, raw = d.group(1), d.group(2)
            entry = {"name": name, "params": params(raw)}
            if cur is None:
                functions.setdefault(name.lower(), {**entry, "file": rel})        # the first definition is the one Ring keeps
            else:
                methods[cur.lower()].setdefault(name.lower(), entry)
    out = {"commit": commit, "about": "Parameters read from the library's source: a global function is declared before a file's "
           "first class, a method after its class. Read by tools/signatures_run.py; nothing in the library was changed.",
           "files": files, "functions": functions, "methods": methods}
    (ROOT / "data" / "signatures.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{files} files, {len(functions)} global functions, {sum(len(v) for v in methods.values())} methods in {len(methods)} classes, at {commit}")

if __name__ == "__main__":
    main()
