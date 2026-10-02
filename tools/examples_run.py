#!/usr/bin/env python3
"""Run the harvested method examples inside the library and keep the ones that keep their promises.

Reads data/examples-src.json (written by tools/harvest_examples.py), runs the
examples in batches, one batch per process and one process at a time, each
example inside its own try block, and writes data/examples.json with the
output each example actually printed. An example is kept only when its whole
output keeps every promise its test file wrote; the comparison is the one the
area showcases use (tools/showcase_run.py). The temporary folder created in
the library is removed at the end.

    python tools/examples_run.py <path to libraries/stzlib> [batch size]
"""
import json, re, sys, pathlib, subprocess, datetime, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from showcase_run import verdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "examples-src.json"
OUT = ROOT / "data" / "examples.json"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(args[0]).resolve()
    size = int(args[1]) if len(args) > 1 else 40
    src = json.loads(SRC.read_text(encoding="utf-8"))
    work = lib / "base" / "test" / "_stzsite_examples"
    work.mkdir(parents=True, exist_ok=True)
    kept, report = [], {"kept": 0, "differs": 0, "error": 0, "no output": 0}
    started_all = datetime.datetime.now()
    queue = [src[b:b + size] for b in range(0, len(src), size)]
    n_run = 0
    try:
        while queue:
            batch = queue.pop(0); n_run += 1
            lines = ['load "../../stzBase.ring"', ""]
            for i, ex in enumerate(batch):
                lines += [f'? "@@BEGIN {i}"', "try", ex["code"], "catch", '    ? "@@ERROR " + cCatchError', "done"]
                if ex.get("expect_exprs"):
                    # a narrated example's promise is the library's own value: print it in the same run
                    lines += [f'? "@@MID {i}"', "try"] + ["? " + e for e in ex["expect_exprs"]] + ["catch", '    ? "@@ERROR " + cCatchError', "done"]
                lines += [f'? "@@END {i}"', ""]
            script = work / f"batch_{n_run:03d}.ring"
            script.write_text("\n".join(lines) + "\n", encoding="utf-8")
            t0 = datetime.datetime.now()
            try:
                p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
                out = (p.stdout or "").replace("\r", "")
            except subprocess.TimeoutExpired as e:
                out = (e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")).replace("\r", "")
            secs = (datetime.datetime.now() - t0).total_seconds()
            if "@@BEGIN 0" not in out:
                # the script never started: one example does not compile; split until it stands alone
                if len(batch) > 1:
                    half = len(batch) // 2; queue[:0] = [batch[:half], batch[half:]]
                else:
                    report["no output"] += 1
                continue
            n_kept, stopped_at = 0, None
            for i, ex in enumerate(batch):
                m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
                if not m:
                    stopped_at = i; report["no output"] += 1; break   # this one stopped the process
                text = m.group(1).rstrip()
                expected = ex.get("expected", "")
                if ex.get("expect_exprs"):
                    text, _, expected = text.partition(f"@@MID {i}")
                    text, expected = text.rstrip(), expected.strip("\n").rstrip()
                if "@@ERROR" in text or "@@ERROR" in expected: report["error"] += 1; continue
                if not expected or not verdict(ex["code"], text, expected): report["differs"] += 1; continue
                kept.append({**ex, "out": text, "expected": expected, "ran": t0.strftime("%Y-%m-%d %H:%M")}); n_kept += 1; report["kept"] += 1
            if stopped_at is not None and stopped_at + 1 < len(batch):
                queue.insert(0, batch[stopped_at + 1:])                # resume after the example that stopped it
            print(f"run {n_run}: {n_kept} of {len(batch)} kept{'' if stopped_at is None else f', stopped at {stopped_at + 1}'}, {secs:.1f} s", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)    # the library is left exactly as it was
    OUT.write_text(json.dumps(kept, ensure_ascii=False, indent=1), encoding="utf-8")
    pairs = {tuple(p) for e in kept for p in e["methods"]}
    print(report, f"in {(datetime.datetime.now() - started_all).total_seconds():.0f} s")
    print(f"{len(kept)} examples kept, covering {len(pairs)} methods of {len({p[0] for p in pairs})} classes -> data/examples.json")

if __name__ == "__main__":
    main()
