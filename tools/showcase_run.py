#!/usr/bin/env python3
"""Run every area's showcase snippets inside the library and keep what they print.

The site's law: every code block was run on the night of publication and its
output sits beside it. The snippets come from the library's own narrations,
tests and guards (data/showcase-src.json, one list per area); this script runs
them, one area per process and one area at a time, and writes data/showcase.json
with the output each snippet actually produced. A snippet that raises an error
is kept out of the site, and so is one whose output differs from what its source
file promised, unless --keep-differing is given.

A snippet taken from a narrated guard may call that guard's own helpers (Then,
Given, When from the shared test helper; a Chk defined in the guard file). The
shared helper is loaded, and a helper defined in the source guard is copied
from that file, word for word, to the end of the script, so the snippet prints
exactly what the guard prints. The snippets of one area run in one process, in
order, so a later snippet may use what an earlier one built. Nothing is written
in the library except a temporary folder, which is removed at the end.

    python tools/showcase_run.py <path to libraries/stzlib of a library checkout> [area ...]
"""
import json, re, sys, subprocess, pathlib, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "showcase-src.json"
OUT = ROOT / "data" / "showcase.json"
SHARED = {"then", "given", "when", "scenario", "endscenario", "summary"}

def norm(s):
    """Compare as the reader would: spacing ignored, and TRUE / FALSE as the 1 / 0 they print as."""
    s = re.sub(r"\s+", " ", (s or "").replace("#-->", "").replace("#--", "").strip()).lower()
    return re.sub(r"\bfalse\b", "0", re.sub(r"\btrue\b", "1", s))

def bare(expected):
    """The promise without the remarks a reader added in brackets, such as '(asserted by the guard)'."""
    return re.sub(r"\s*\((?:[^()]*\b(?:asserted|guard|exact match|each)\b[^()]*)\)", "", expected or "")

def verdict(code, text, expected):
    """True when the run kept its source's promise, False when it did not, None when nothing was promised.
    A snippet that asserts through a guard's helpers (Then, Chk) keeps its promise when every assertion
    printed a pass and none a failure; any other snippet is compared with what its source printed."""
    if re.search(r"\b(Then|Chk|ChkEq)\s*\(", code, re.I):
        passes = len(re.findall(r"(?im)\[PASS\]|\[ok\]|^\s*ok\b", text))
        fails = len(re.findall(r"(?im)\[FAIL\]|^\s*fail\b|^\s*not ok\b", text))
        return passes > 0 and fails == 0
    if not expected:
        return None
    # the same values, whatever the display form: a list printed item by item, or written [ "a", "b" ]
    toks = lambda s: re.findall(r'[^\s\[\]",]+', norm(s))
    return norm(text) == norm(expected) or norm(text) == norm(bare(expected)) or toks(text) == toks(bare(expected))

def helpers_from(lib, source, code):
    """The functions the snippet calls that its source guard defines, copied from that file."""
    path = source.split(" (")[0].strip()
    f = lib / path
    if not f.exists() or f.suffix != ".ring":
        return [], set()
    text = f.read_text(encoding="utf-8", errors="replace").replace("\r", "")
    heads = list(re.finditer(r"(?mi)^(func|class)\s+(\w+)", text))
    defs = {}
    for k, m in enumerate(heads):
        if m.group(1).lower() != "func":
            continue
        end = heads[k + 1].start() if k + 1 < len(heads) else len(text)
        defs[m.group(2).lower()] = text[m.start():end].rstrip()
    called = {c.lower() for c in re.findall(r"\b(\w+)\s*\(", code)} | {c.lower() for c in re.findall(r"(?m)^\s*(\w+)\s+\S", code)}
    out, counters, taken = [], set(), set()
    todo = [c for c in called if c in defs and c not in SHARED]
    while todo:                                   # a helper may call another helper of the same file
        name = todo.pop(0)
        if name in taken:
            continue
        taken.add(name)
        body = defs[name]
        out.append(body)
        counters |= set(re.findall(r"\b(n[A-Z]\w*)\+\+", body))
        todo += [c.lower() for c in re.findall(r"\b(\w+)\s*\(", body) if c.lower() in defs and c.lower() not in SHARED]
    return out, counters

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(args[0]).resolve()
    only = set(args[1:])
    keep_differing = "--keep-differing" in sys.argv
    if not (lib / "base" / "stzBase.ring").exists():
        print("not a library folder:", lib); sys.exit(2)
    src = json.loads(SRC.read_text(encoding="utf-8"))
    result = json.loads(OUT.read_text(encoding="utf-8")) if (only and OUT.exists()) else {}
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    work = lib / "base" / "test" / "_stzsite_showcase"
    work.mkdir(parents=True, exist_ok=True)
    report = []
    try:
        for slug, snippets in src.items():
            if only and slug not in only:
                continue
            result.pop(slug, None)
            body, usable, tail, counters = [], [], [], set()
            for i, sn in enumerate(snippets):
                code = sn["code"].replace("\r", "")
                if sn.get("skip"):
                    report.append(f"{slug} #{i+1}: not run ({sn['skip']})"); continue
                if re.search(r"^\s*(func|class|load|package|import)\b", code, re.M | re.I):
                    report.append(f"{slug} #{i+1}: skipped (defines functions itself)"); continue
                hs, cs = helpers_from(lib, sn.get("source", ""), code)
                for h in hs:
                    hname = re.match(r"(?i)func\s+(\w+)", h).group(1).lower()
                    if hname not in [re.match(r"(?i)func\s+(\w+)", t).group(1).lower() for t in tail]:
                        tail.append(h)                    # one definition per name: a second one is a compile error
                counters |= cs
                usable.append(i)
                body += [f'? "@@BEGIN {i}"', "try", code, "catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
            if not usable:
                continue
            lines = ['load "../../stzBase.ring"', 'load "../_narrated.ring"', ""] + [f"{c} = 0" for c in sorted(counters)] + [""] + body + [""] + tail
            script = work / f"{slug}.ring"
            script.write_text("\n".join(lines) + "\n", encoding="utf-8")
            started = datetime.datetime.now()
            try:
                p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
                out = p.stdout + ("\n" + p.stderr if p.stderr else "")
            except subprocess.TimeoutExpired as e:
                out = (e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
                report.append(f"{slug}: timed out after 240 s")
            seconds = (datetime.datetime.now() - started).total_seconds()
            out = out.replace("\r", "")
            kept = []
            for i in usable:
                m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
                sn = snippets[i]
                if not m:
                    why = [l for l in out.splitlines() if re.search(r"error|line \d", l, re.I)][:3] or ["(no output)"]
                    report.append(f"{slug} #{i+1}: no output (the process stopped before it): {' | '.join(why)[:300]}"); continue
                text = m.group(1).rstrip()
                exp = sn.get("expected", "")
                if "@@ERROR" in text:
                    err = text.split("@@ERROR", 1)[1].strip()
                    # a refusal the source promises IS the output: shown as the message the caller receives
                    if exp and norm(bare(exp)) and norm(bare(exp)) in norm(err):
                        text = (text.split("@@ERROR", 1)[0] + err).strip()
                        same = True                      # the refusal its source promises, word for word inside it
                    else:
                        report.append(f"{slug} #{i+1}: error: {err[:140]}"); continue
                elif sn.get("contains"):
                    same = all(c in text for c in sn["contains"])   # the fragment its guard asserts is in the output
                else:
                    same = verdict(sn["code"], text, exp)
                if same is False and not keep_differing:
                    report.append(f"{slug} #{i+1}: output differs from its source's promise; left out\n      got: {text[:200]!r}\n      exp: {sn.get('expected','')[:200]!r}"); continue
                kept.append({**sn, "out": text, "matches_source": same,
                             "ran": started.strftime("%Y-%m-%d %H:%M"), "seconds": round(seconds, 1), "commit": commit})
                report.append(f"{slug} #{i+1}: ran{'' if same is None else (', matches its source' if same else ', differs from its source')}")
            if kept:
                result[slug] = kept
            print(f"{slug}: {len(kept)} of {len(snippets)} kept, {seconds:.1f} s", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)    # the library is left exactly as it was
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(report))
    print(f"kept {sum(len(v) for v in result.values())} snippets in {len(result)} areas -> data/showcase.json")

if __name__ == "__main__":
    main()
