#!/usr/bin/env python3
"""Try each form of a function name, in the library, and keep what it printed or the error it raised.

The library's article on functions as linguistic expressions names the forms and gives each an example and a promise. This tool
tries each example in one process, each in its own try block, and keeps beside the promise what came out: the printed answer, or
the library's own error. A form the library no longer has is then a fact the page shows, in the library's words, and not a gap
the page hides.

    python tools/grammar_run.py <path to libraries/stzlib>      -> data/grammar-run.json
"""
import json, re, sys, subprocess, pathlib, datetime, shutil
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from showcase_run import verdict

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    data = json.loads((ROOT / "data" / "grammar.json").read_text(encoding="utf-8"))
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    work = lib / "base" / "test" / "_stzsite_grammar"; work.mkdir(parents=True, exist_ok=True)
    lines, order = ['load "../../stzBase.ring"', ""], []
    for f in data["forms"]:
        for k, t in enumerate(f["tries"]):
            i = len(order); order.append((f["id"], k))
            lines += [f'? "@@BEGIN {i}"', "try", t["code"], "catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
    started = datetime.datetime.now()
    try:
        (work / "grammar.ring").write_text("\n".join(lines) + "\n", encoding="utf-8")
        p = subprocess.run(["ring", "grammar.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    res = {}
    for i, (fid, k) in enumerate(order):
        t = next(f for f in data["forms"] if f["id"] == fid)["tries"][k]
        m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
        text = m.group(1).rstrip() if m else ""
        err = ""
        if "@@ERROR" in text:
            err = text.split("@@ERROR", 1)[1].strip().split("\n")[0]
            text = text.split("@@ERROR", 1)[0].rstrip()
        kept = (not err) and bool(verdict("", text, t["promise"]))
        res.setdefault(fid, []).append({"code": t["code"], "promise": t["promise"], "out": text, "error": err, "kept": kept})
    result = {"commit": commit, "ran": started.strftime("%Y-%m-%d %H:%M"), "forms": res}
    (ROOT / "data" / "grammar-run.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(len(v) for v in res.values()); k = sum(1 for v in res.values() for x in v if x["kept"])
    print(f"{n} tries, {k} kept their promise, {sum(1 for v in res.values() for x in v if x['error'])} raised, at {commit}")
    for fid, v in res.items():
        for x in v:
            print(f"  {fid:12} {'kept' if x['kept'] else ('ERROR ' + x['error'][:70] if x['error'] else 'differs: ' + x['out'][:60].replace(chr(10), ' / '))}")

if __name__ == "__main__":
    main()
