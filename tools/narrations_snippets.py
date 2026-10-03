#!/usr/bin/env python3
"""One short example from each narration, for the list of narrations.

Examples must be everywhere on the site (the author, 2026-10-03): a list of 134 titles is abstract, and
a reader should see the practical technology behind each. So each narration of the list carries a few lines of its
own code, with what they print.

  - a narration that ran (tools/narrations_run.py): the first short block whose run printed something, and that
    output, as the run printed it
  - a narration that did not run (it touches files, the clock or the network, or shows the platform's former name
    in another fence): the first short block that is clean, with the output the narration itself promises for it
    when it promises one, labelled as written in the narration and not run for this page

No library code runs here: this reads the narrations' files and the verdicts already recorded.

    python tools/narrations_snippets.py <path to libraries/stzlib>   -> data/narration-snippets.json
"""
import json, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from narrations_run import blocks_of, WORD
from harvest_examples import FORBIDDEN
import qforms

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "narration-snippets.json"

def short(code, out="", lines=8, chars=420):
    c = code.strip("\n")
    return bool(c) and c.count("\n") < lines and len(c) <= chars and out.count("\n") < 6 and len(out) <= 300

def clean(*texts):
    return not any(WORD.search(t) for t in texts)

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    runs = json.loads((ROOT / "data" / "narrations-run.json").read_text(encoding="utf-8"))
    plain = qforms.get(ROOT).plain_anywhere          # a ...Q() call whose value nothing uses is not an example (the Q rule)
    res, n_ran, n_written = {}, 0, 0
    for f, rec in sorted(runs.items()):
        path = lib / "base" / "doc" / "narrations" / f
        if not path.is_file(): continue
        text = path.read_text(encoding="utf-8", errors="replace").replace("\r", "")
        _, blocks = blocks_of(text)
        pick = None
        if rec["status"] == "run":
            for b, r in zip(blocks, rec["blocks"]):
                code = "\n".join(b["code"])
                if r["verdict"] in ("kept", "ran") and r["out"].strip() and short(code, r["out"]) and clean(code, r["out"]) and not b["unprinted"] and not qforms.unchained(code, plain):
                    pick = {"code": code.strip("\n"), "out": r["out"].strip(), "how": "ran"}; break
        for lines, chars, strict in ((8, 420, True), (8, 420, False), (14, 800, False)):     # written in the narration: the plainest first, then any short one
            if pick: break
            for b in blocks:
                code = "\n".join(b["code"])
                if short(code, b["promise"], lines, chars) and clean(code, b["promise"]) and not qforms.unchained(code, plain) and not (strict and FORBIDDEN.search(code)):
                    pick = {"code": code.strip("\n"), "out": b["promise"].strip(), "how": "written"}; break
        if pick:
            res[f] = pick
            if pick["how"] == "ran": n_ran += 1
            else: n_written += 1
    OUT.write_text(json.dumps({"snippets": res}, ensure_ascii=False, indent=1), encoding="utf-8")
    with_out = sum(1 for v in res.values() if v["out"])
    print(f"{len(res)} of {len(runs)} narrations carry a snippet: {n_ran} from a run, {n_written} written in the narration ({with_out} with an output) -> data/narration-snippets.json")

if __name__ == "__main__":
    main()
