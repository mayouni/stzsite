#!/usr/bin/env python3
"""Run every area's showcase snippets inside the library and keep what they print.

The site's law: every code block was run on the night of publication and its
output sits beside it. The snippets come from the library's own narrations,
tests and guards (data/showcase-src.json, one list per area); this script runs
them, one area per process and one area at a time, and writes data/showcase.json
with the output each snippet actually produced. A snippet that raises an error
is kept out of the site, and so is one whose output differs from what its source
file promised, unless --keep-differing is given.

    python tools/showcase_run.py <path to libraries/stzlib of a library checkout>
"""
import json, re, sys, subprocess, pathlib, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "showcase-src.json"
OUT = ROOT / "data" / "showcase.json"

def norm(s):
    return re.sub(r"\s+", " ", (s or "").replace("#-->", "").replace("#--", "").strip()).lower()

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    keep_differing = "--keep-differing" in sys.argv
    if not (lib / "base" / "stzBase.ring").exists():
        print("not a library folder:", lib); sys.exit(2)
    src = json.loads(SRC.read_text(encoding="utf-8"))
    work = lib / "base" / "test" / "_stzsite_showcase"
    work.mkdir(parents=True, exist_ok=True)
    result, report = {}, []
    try:
        for slug, snippets in src.items():
            lines = ['load "../../stzBase.ring"', ""]
            usable = []
            for i, sn in enumerate(snippets):
                code = sn["code"].replace("\r", "")
                if re.search(r"^\s*(func|class|load|package|import)\b", code, re.M | re.I) or re.search(r"\btry\b|\bcatch\b|\bdone\b", code, re.I):
                    report.append(f"{slug} #{i+1}: skipped (defines functions or catches errors itself)"); continue
                usable.append(i)
                lines += [f'? "@@BEGIN {i}"', "try", code, "catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
            if not usable: continue
            script = work / f"{slug}.ring"
            script.write_text("\n".join(lines), encoding="utf-8")
            started = datetime.datetime.now()
            p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
            seconds = (datetime.datetime.now() - started).total_seconds()
            out = p.stdout
            kept = []
            for i in usable:
                m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
                sn = snippets[i]
                if not m:
                    report.append(f"{slug} #{i+1}: no output (the process stopped before it)"); continue
                text = m.group(1).rstrip()
                if "@@ERROR" in text:
                    report.append(f"{slug} #{i+1}: error: {text.split('@@ERROR')[1].strip()[:120]}"); continue
                same = norm(text) == norm(sn.get("expected", "")) if sn.get("expected") else None
                if same is False and not keep_differing:
                    report.append(f"{slug} #{i+1}: output differs from its source's promise; left out"); continue
                kept.append({**sn, "out": text, "matches_source": same,
                             "ran": started.strftime("%Y-%m-%d %H:%M"), "seconds": round(seconds, 1)})
                report.append(f"{slug} #{i+1}: ran{'' if same is None else (', matches its source' if same else ', differs from its source')}")
            if kept: result[slug] = kept
    finally:
        shutil.rmtree(work, ignore_errors=True)    # the library is left exactly as it was
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(report))
    print(f"kept {sum(len(v) for v in result.values())} snippets in {len(result)} areas -> data/showcase.json")

if __name__ == "__main__":
    main()
