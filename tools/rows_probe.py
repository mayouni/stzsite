#!/usr/bin/env python3
"""Try the hand-written receivers of data/row-receivers-hand.json: does each build an object of its class?

A receiver is written from how the library's tests and sources build the class; this runs every one (or the named
classes) inside the library and prints the class name it built, or the error it raised, and which of Content() and Value()
answers on it. One process per batch; the temporary folder created in the library is removed at the end.

    python tools/rows_probe.py <path to libraries/stzlib> [class ...]
"""
import json, re, sys, pathlib, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from rows_run import run_all

ROOT = pathlib.Path(__file__).resolve().parent.parent
HAND = ROOT / "data" / "row-receivers-hand.json"

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    only = set(sys.argv[2:])
    hand = json.loads(HAND.read_text(encoding="utf-8"))["classes"]
    names = [c for c in hand if not only or c in only]
    work = lib / "base" / "test" / "_stzsite_probe"
    work.mkdir(parents=True, exist_ok=True)
    try:
        jobs = [(i, hand[c]["setup"], "? classname(o1)") for i, c in enumerate(names)]
        res, crashed = run_all(work, jobs, batch=30, timeout=60)
        pj = [(i * 2 + k, hand[c]["setup"], f"? @@( o1.{acc}() )") for i, c in enumerate(names) for k, acc in enumerate(("Content", "Value"))]
        pres, _ = run_all(work, pj, batch=30, timeout=60)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    ok = 0
    for i, c in enumerate(names):
        r = res.get(i)
        if i in crashed: print(f"CRASH {c}"); continue
        if not r: print(f"NONE  {c}"); continue
        if r[0] == "ok" and r[1].strip().split("\n")[-1].strip().lower() == c.lower():
            ok += 1
            acc = next((a for k, a in enumerate(("Content", "Value")) if pres.get(i * 2 + k, ("", ""))[0] == "ok" and pres[i * 2 + k][1].strip() not in ("", "[ ]", '""')), "-")
            print(f"ok    {c:26} content: {acc:8} {pres.get(i*2 + (0 if acc == 'Content' else 1), ('', ''))[1][:50]!r}")
        else:
            print(f"FAIL  {c:26} {r[1].strip()[:150]!r}")
    print(f"{ok} of {len(names)} build")

if __name__ == "__main__":
    main()
