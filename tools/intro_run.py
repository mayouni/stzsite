#!/usr/bin/env python3
"""Run the small samples that sit inside the class introductions, and keep what they print.

The class introductions narrate, and show their code in samples of their own, one after the other, never in the sentence
(the author, 2026-10-19). A sample is written by hand in the Softanza style (data/intro-snippets.json, one list per class:
{"id", "code"}, a promise is a `?` line and the page writes `#-->` under it from what the run printed). This script runs
every sample inside the library, the samples of one class in one process and in order, and writes data/intro-run.json with
what each printed. A sample that raises an error is reported and kept out of the site.

    python tools/intro_run.py <path to libraries/stzlib of a library checkout> [Class ...]
"""
import json, re, sys, subprocess, pathlib, datetime, shutil, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "intro-snippets.json"
OUT = ROOT / "data" / "intro-run.json"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(args[0]).resolve()
    only = {a.lower() for a in args[1:]}
    if not (lib / "base" / "stzBase.ring").exists():
        print("not a library folder:", lib); sys.exit(2)
    src = json.loads(SRC.read_text(encoding="utf-8"))
    result = json.loads(OUT.read_text(encoding="utf-8")) if (only and OUT.exists()) else {}
    result = {k: v for k, v in result.items() if k in src}          # a class that no longer has samples keeps none
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    work = pathlib.Path(tempfile.mkdtemp(prefix="stzsite_intro_"))          # the scripts live here, never in the library
    cwd = lib / "base" / "test"                                              # the engine finds its libraries from a folder inside the checkout
    stz_base = (lib / "base" / "stzBase.ring").as_posix()
    report = []
    try:
        for cls, snippets in src.items():
            if only and cls.lower() not in only:
                continue
            result.pop(cls, None)
            body = []
            for i, sn in enumerate(snippets):
                code = sn["code"].replace("\r", "")
                body += [f'? "@@BEGIN {i}"', "try", code, "catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
            script = work / (re.sub(r"[^A-Za-z0-9]+", "_", cls) + ".ring")
            script.write_text("\n".join(['load "' + stz_base + '"', ""] + body) + "\n", encoding="utf-8")
            started = datetime.datetime.now()
            try:
                p = subprocess.run(["ring", str(script)], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
                out = p.stdout + ("\n" + p.stderr if p.stderr else "")
            except subprocess.TimeoutExpired as e:
                out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
                report.append(f"{cls}: timed out after 240 s")
            seconds = (datetime.datetime.now() - started).total_seconds()
            out = out.replace("\r", "")
            kept = []
            for i, sn in enumerate(snippets):
                m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
                if not m:
                    why = [l for l in out.splitlines() if re.search(r"error|line \d", l, re.I)][:3] or ["(no output)"]
                    report.append(f"{cls} #{i+1} {sn['id']}: the process stopped before it: {' | '.join(why)[:300]}"); continue
                text = m.group(1).rstrip()
                if "@@ERROR" in text:
                    report.append(f"{cls} #{i+1} {sn['id']}: error: {text.split('@@ERROR', 1)[1].strip()[:200]}"); continue
                kept.append({**sn, "out": text, "ran": started.strftime("%Y-%m-%d %H:%M"), "commit": commit})
                report.append(f"{cls} #{i+1} {sn['id']}: ran")
            if kept:
                result[cls] = kept
            print(f"{cls}: {len(kept)} of {len(snippets)} kept, {seconds:.1f} s", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(r for r in report if not r.endswith(": ran")))
    print(f"kept {sum(len(v) for v in result.values())} samples in {len(result)} classes -> data/intro-run.json")

if __name__ == "__main__":
    main()
