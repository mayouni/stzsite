#!/usr/bin/env python3
"""@@() is for showing a list; a number, a string or a boolean is printed with ? alone.

The author, 2026-10-03: `? @@( o1.IsWord() )` misuses @@(), which turns a LIST into text; for a value that is already a
number or a string, write `? o1.IsWord()`. The composed examples were written with @@() round every call, because the kind of
the answer is not known before the run. Now that it is known, an example whose output is not a list is written in the plain
form and RUN again in that form: the answer is the one the plain form prints (a string without its quotes, as the library's own
tests show it), and an example whose plain form raises or prints nothing keeps the form that ran.

    python tools/rows_plain.py <path to libraries/stzlib>      rewrites data/row-examples.json in place
"""
import json, re, sys, pathlib, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from rows_run import run_all, keep

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "row-examples.json"
SHOW = re.compile(r"^\? @@\( (.*) \)$", re.M)

def is_list(out):
    return out.lstrip().startswith("[")

def plain_code(code):
    """the example with every `? @@( X )` line written `? X`"""
    return SHOW.sub(r"? \1", code)

def plainize(work, kept):
    """kept: {key: example}; rewrites in place every example whose output is not a list and whose plain form ran. Returns the count."""
    keys = [k for k, e in kept.items() if not is_list(e["out"]) and SHOW.search(e["code"])]
    jobs = [(i, kept[k]["setup"], plain_code(kept[k]["code"])) for i, k in enumerate(keys)]
    res, crashed = run_all(work, jobs, batch=60, timeout=60)
    changed = 0
    for i, k in enumerate(keys):
        r = res.get(i)
        if not (r and r[0] == "ok"): continue
        out = r[1].strip()
        if not out or not keep(out, ""): continue
        kept[k]["code"] = jobs[i][2]; kept[k]["out"] = out; changed += 1
    return changed, len(keys)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    d = json.loads(OUT.read_text(encoding="utf-8"))
    flat = {(c, m): e for c, v in d["examples"].items() for m, e in v.items()}
    work = lib / "base" / "test" / "_stzsite_plain"
    work.mkdir(parents=True, exist_ok=True)
    try: changed, asked = plainize(work, flat)
    finally: shutil.rmtree(work, ignore_errors=True)
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    lists = sum(1 for e in flat.values() if is_list(e["out"]))
    print(f"{len(flat)} examples: {lists} print a list and keep @@(); {asked} did not and were run again in the plain form; {changed} now use ? alone -> data/row-examples.json")

if __name__ == "__main__":
    main()
