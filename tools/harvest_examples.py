#!/usr/bin/env python3
"""Harvest method examples from the library's classic test files.

A classic test file is one short idea: some code, and under each printed line
the output the library's authors promised (`#-->`). This script reads those
files in the topics of pure computation, keeps the short ones that touch no
file, no input, no clock and no chance, and works out which class and method
each printed line calls. It writes data/examples-src.json; tools/examples_run.py
then runs every example inside the library and keeps only those whose output
keeps all its promises.

    python tools/harvest_examples.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "examples-src.json"
REF = ROOT / "data" / "reference.json"

TOPICS = ["char", "dataset", "datawrangler", "date", "datetime", "duration", "calendar", "global", "graph", "graphex",
          "graphquery", "grid", "hashlist", "json", "list", "listoflists", "listofnumbers", "listofstrings", "locale",
          "matrex", "matrix", "natural", "number", "object", "orgchart", "regex", "regexmaker", "string", "table",
          "tablex", "timeline", "time"]
# what an example must not do: touch files, read input, depend on the clock or on chance, call out of the process
FORBIDDEN = re.compile(r"\b(give|getchar|input|system|SystemCall|write|read|remove|Now|NowXT|Today|TodayXT|Clock|"
                       r"random|rnd\w*|Sleep|sleep|Download|http\w*|FileCreate|FileOverwrite|FileAppend|FileSave|"
                       r"StzFileSave|RemoveFile|DeleteFile|MakeDir|StzMakeDir|stzFolder|stzFile|shell|Exec\w*|"
                       r"ToPNG\w*|ToSVG\w*|Show\w*|Render\w*|Plot\w*|Draw\w*|Display\w*|pf|pr|load)\s*\(", re.I)
MAX_CODE = 16

def class_of_q(arg_start):
    if arg_start.startswith(('"', "'")): return "stzString"
    if arg_start.startswith("["): return "stzList"
    if re.match(r"-?\d", arg_start): return "stzNumber"
    return None

def parse(text):
    text = re.sub(r"/\*.*?\*/", "", text.replace("\r", "").lstrip("﻿"), flags=re.S)
    code, promises, in_promise = [], [], False
    for raw in text.split("\n"):
        s = raw.strip()
        if not s:
            in_promise = False; continue
        if s.startswith("#-->"):
            promises.append(s[4:].strip()); in_promise = True; continue
        if s.startswith("#") or s.startswith("//"):
            if in_promise and not s.startswith("# Executed"):
                promises[-1] += "\n" + s.lstrip("#").strip()
            continue
        in_promise = False
        if re.match(r"(?i)(load\s|pr\(\)|pf\(\)|StopProfiler\(\)|pron\(\)|proff\(\))", s):
            continue
        m = re.match(r"(.*?)\s#-->\s*(.*)$", s)
        if m and m.group(1).strip().startswith("?"):
            code.append(m.group(1).rstrip()); promises.append(m.group(2).strip()); in_promise = True; continue
        code.append(raw.rstrip())
    return code, [p for p in promises if p]

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    ref = json.loads(REF.read_text(encoding="utf-8"))
    own = {c["name"]: {m[0].lower(): m[0] for m in c["own"]} for c in ref["classes"]}
    lower_cls = {k.lower(): k for k in own}
    examples, seen, stats = [], set(), {"files": 0, "kept": 0, "too long": 0, "forbidden": 0, "defines code": 0, "no promise": 0, "no method": 0}
    for topic in TOPICS:
        folder = lib / "base" / "test" / topic
        if not folder.exists(): continue
        for f in sorted(folder.glob("*.ring")):
            if f.name.startswith("_") or f.name.endswith("_narrated.ring"): continue
            stats["files"] += 1
            code, promises = parse(f.read_text(encoding="utf-8", errors="replace"))
            body = "\n".join(code)
            if not promises: stats["no promise"] += 1; continue
            if len(code) > MAX_CODE: stats["too long"] += 1; continue
            if re.search(r"(?mi)^\s*(func|class|def)\s+\w", body) or re.search(r"(?i)\b(try|catch|done)\b", body):
                stats["defines code"] += 1; continue
            if FORBIDDEN.search(body): stats["forbidden"] += 1; continue
            if body in seen: continue
            # which class each variable holds
            var = {}
            for line in code:
                m = re.match(r"\s*(\w+)\s*=\s*new\s+(stz\w+)\b", line, re.I)
                if m: var[m.group(1).lower()] = lower_cls.get(m.group(2).lower()); continue
                m = re.match(r"\s*(\w+)\s*=\s*(stz\w+?)Q\s*\(", line, re.I)
                if m: var[m.group(1).lower()] = lower_cls.get(m.group(2).lower()); continue
                m = re.match(r"\s*(\w+)\s*=\s*Q\s*\(\s*(.)", line)
                if m: var[m.group(1).lower()] = class_of_q(m.group(2))
            methods = []
            # a call made as a statement on a known object is what the example shows: o1.Remove("x") then ? o1.Content()
            for line in code:
                m = re.match(r"\s*(\w+)\s*\.\s*(\w+)\s*\(", line)
                if m and not line.strip().startswith("?") and m.group(1).lower() in var:
                    cls = var[m.group(1).lower()]
                    if cls in own and m.group(2).lower() in own[cls]:
                        pair = [cls, own[cls][m.group(2).lower()]]
                        if pair not in methods: methods.append(pair)
            for line in code:
                s = line.strip()
                if not s.startswith("?"): continue
                expr = s[1:].strip()
                cls = meth = None
                m = re.search(r"\b(\w+)\s*\.\s*(\w+)\s*\(", expr)
                if m and m.group(1).lower() in var:
                    cls, meth = var[m.group(1).lower()], m.group(2)
                else:
                    m = re.search(r"\bQ\s*\(\s*(.).*?\)\s*\.\s*(\w+)\s*\(", expr)
                    if m: cls, meth = class_of_q(m.group(1)), m.group(2)
                    else:
                        m = re.search(r"\bnew\s+(stz\w+)\s*\(.*?\)\s*\)?\s*\.\s*(\w+)\s*\(", expr, re.I) or re.search(r"\b(stz\w+?)Q\s*\(.*?\)\s*\.\s*(\w+)\s*\(", expr, re.I)
                        if m: cls, meth = lower_cls.get(m.group(1).lower()), m.group(2)
                if cls and meth and cls in own and meth.lower() in own[cls]:
                    pair = [cls, own[cls][meth.lower()]]
                    if pair not in methods: methods.append(pair)
            # a viewer that only prints the object is not what the example teaches, unless nothing else was called
            VIEWERS = {"content", "items", "copy", "value", "tostring", "show"}
            if any(m[1].lower() not in VIEWERS for m in methods):
                methods = [m for m in methods if m[1].lower() not in VIEWERS]
            if not methods: stats["no method"] += 1; continue
            seen.add(body)
            title = re.sub(r"^\d+_", "", f.stem).replace("_", " ").strip()
            examples.append({"source": f"base/test/{topic}/{f.name}", "title": title, "code": body.strip("\n"),
                             "expected": "\n".join(promises), "methods": methods})
            stats["kept"] += 1
    OUT.write_text(json.dumps(examples, ensure_ascii=False, indent=1), encoding="utf-8")
    pairs = {tuple(p) for e in examples for p in e["methods"]}
    print(stats)
    print(f"{len(examples)} examples, touching {len(pairs)} methods of {len({p[0] for p in pairs})} classes -> data/examples-src.json")

if __name__ == "__main__":
    main()
