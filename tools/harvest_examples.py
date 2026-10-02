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
          "tablex", "timeline", "time", "linguistic", "math", "stats"]
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

# ---------------------------------------------------------------------------- narrated suites
# A narrated suite asserts instead of printing: Then("label", actual, expected), or chk("label", condition).
# Each scenario becomes one example: its setup lines, and for each assertion the label as a comment and the
# actual expression printed. The expected expressions are kept apart: the runner prints them in the same
# process and compares, so the promise is the library's own value, not a text copied by the site.

def split_statements(text):
    """Join physical lines into statements while brackets or quotes are open."""
    out, buf, depth, quote = [], "", 0, None
    for line in text.split("\n"):
        if not buf and (line.strip().startswith("#") or line.strip().startswith("//")):
            continue
        for ch in line:
            if quote:
                if ch == quote: quote = None
            elif ch in "\"'`": quote = ch
            elif ch in "([{": depth += 1
            elif ch in ")]}": depth -= 1
        buf = (buf + "\n" + line) if buf else line
        if depth <= 0 and not quote:
            if buf.strip(): out.append(buf.strip())
            buf, depth, quote = "", 0, None
    if buf.strip(): out.append(buf.strip())
    return out

def call_args(stmt, name):
    """The top-level arguments of name(...) at the start of a statement, or None."""
    m = re.match(rf"(?i){name}\s*\(", stmt)
    if not m or not stmt.rstrip().endswith(")"): return None
    inner = stmt[m.end():stmt.rstrip().rfind(")")]
    args, buf, depth, quote = [], "", 0, None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote: quote = None
            continue
        if ch in "\"'`": quote = ch
        elif ch in "([{": depth += 1
        elif ch in ")]}": depth -= 1
        if ch == "," and depth == 0:
            args.append(buf.strip()); buf = ""; continue
        buf += ch
    if buf.strip(): args.append(buf.strip())
    return args

def unquote(s):
    s = s.strip()
    return s[1:-1] if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'`" else s

def parse_narrated(text):
    text = re.sub(r"/\*.*?\*/", "", text.replace("\r", "").lstrip("﻿"), flags=re.S)
    m = re.search(r"(?mi)^(func|class)\s+\w", text)
    main_part, funcs_part = (text[:m.start()], text[m.start():]) if m else (text, "")
    funcs = {}                       # zero-argument helpers that end in one return: inlinable
    all_funcs = set()
    for fm in re.finditer(r"(?mi)^func\s+(\w+)([^\n]*)\n(.*?)(?=^func\s|^class\s|\Z)", funcs_part, re.S):
        name, params, body = fm.group(1), fm.group(2).strip(), fm.group(3)
        all_funcs.add(name.lower())
        lines = [l.strip() for l in body.split("\n") if l.strip() and not l.strip().startswith("#")]
        if params.strip("() ") == "" and lines and lines[-1].lower().startswith("return ") \
           and sum(1 for l in lines if l.lower().startswith("return")) == 1 and len(lines) <= 10:
            funcs[name.lower()] = lines[:-1] + ["? " + lines[-1][7:].strip()]
    scenarios, prelude, cur = [], [], None
    for st in split_statements(main_part):
        low = st.lower()
        if low.startswith("load "): continue
        a = call_args(st, "Scenario")
        if a is not None:
            cur = {"title": unquote(a[0]) if a else "", "code": [], "expect": []}; scenarios.append(cur); continue
        if re.match(r"(?i)(EndScenario|Summary)\s*\(", st): cur = None; continue
        if re.match(r"(?i)(Given|When)\s*\(", st): continue
        then = call_args(st, "Then")
        chk = call_args(st, "chk")
        if then is not None and len(then) == 3 and cur is not None:
            label, actual, expected = unquote(then[0]), then[1], then[2]
            hm = re.fullmatch(r"(\w+)\s*\(\s*\)", actual.strip())
            if hm and hm.group(1).lower() in funcs:
                cur["code"] += ["# " + label] + funcs[hm.group(1).lower()]
            else:
                cur["code"] += ["# " + label, "? " + actual.strip()]
            cur["expect"].append(expected.strip()); continue
        if chk is not None and len(chk) == 2 and cur is not None:
            cur["code"] += ["# " + unquote(chk[0]), "? " + chk[1].strip()]
            cur["expect"].append("1"); continue
        if cur is None: prelude.append(st)
        else: cur["code"].append(st)
    return prelude, scenarios, all_funcs

def methods_of(code, own, lower_cls):
    var, methods = {}, []
    for line in code:
        m = re.match(r"\s*(\w+)\s*=\s*new\s+(stz\w+)\b", line, re.I)
        if m: var[m.group(1).lower()] = lower_cls.get(m.group(2).lower()); continue
        m = re.match(r"\s*(\w+)\s*=\s*(stz\w+?)Q\s*\(", line, re.I)
        if m: var[m.group(1).lower()] = lower_cls.get(m.group(2).lower()); continue
        m = re.match(r"\s*(\w+)\s*=\s*Q\s*\(\s*(.)", line)
        if m: var[m.group(1).lower()] = class_of_q(m.group(2))
    for line in code:
        s = line.strip()
        if s.startswith("#"): continue
        cls = meth = None
        if not s.startswith("?"):
            m = re.match(r"(\w+)\s*\.\s*(\w+)\s*\(", s)
            if m and m.group(1).lower() in var: cls, meth = var[m.group(1).lower()], m.group(2)
        else:
            expr = s[1:].strip()
            m = re.search(r"\b(\w+)\s*\.\s*(\w+)\s*\(", expr)
            if m and m.group(1).lower() in var:
                cls, meth = var[m.group(1).lower()], m.group(2)
            else:
                m = re.search(r"\bQ\s*\(\s*(.).*?\)\s*\.\s*(\w+)\s*\(", expr)
                if m: cls, meth = class_of_q(m.group(1)), m.group(2)
                else:
                    m = re.search(r"\bnew\s+(stz\w+)\s*\(.*?\)\s*\)?\s*\.\s*(\w+)\s*\(", expr, re.I) or re.search(r"\b(stz\w+?)Q\s*\(.*?\)\s*\.\s*(\w+)\s*\(", expr, re.I)
                    if m: cls, meth = lower_cls.get(m.group(1).lower()), m.group(2)
        # follow a chain that elevates to another class: Q("...").TextQ().IsSemanticallySimilarTo(...)
        # shows stzText's method, not stzString's TextQ
        if cls and meth:
            names = re.findall(r"\.\s*(\w+)\s*\(", s)
            k = next((j for j, n in enumerate(names) if n.lower() == meth.lower()), None)
            while k is not None and k + 1 < len(names) and meth[-1:] in "Qq" and lower_cls.get("stz" + meth[:-1].lower()):
                cls, k = lower_cls["stz" + meth[:-1].lower()], k + 1
                meth = names[k]
        if cls and meth and cls in own and meth.lower() in own[cls]:
            pair = [cls, own[cls][meth.lower()]]
            if pair not in methods: methods.append(pair)
    VIEWERS = {"content", "items", "copy", "value", "tostring", "show"}
    if any(m[1].lower() not in VIEWERS for m in methods):
        methods = [m for m in methods if m[1].lower() not in VIEWERS]
    return methods

def harvest_narrated(f, rel, own, lower_cls, stats, seen):
    prelude, scenarios, all_funcs = parse_narrated(f.read_text(encoding="utf-8", errors="replace"))
    out = []
    for sc in scenarios:
        if not sc["expect"]: continue
        code = (prelude if len(prelude) <= 4 else []) + sc["code"]
        body = "\n".join(code)
        lines = [l for l in code if not l.strip().startswith("#")]
        if len(lines) > MAX_CODE: stats["too long"] += 1; continue
        calls = {c.lower() for c in re.findall(r"\b(\w+)\s*\(", body + " " + " ".join(sc["expect"]))}
        if calls & all_funcs: stats["defines code"] += 1; continue      # it leans on a helper the page would not show
        if re.search(r"(?i)\b(try|catch|done)\b", body) or FORBIDDEN.search(body) or FORBIDDEN.search(" ".join(sc["expect"])):
            stats["forbidden"] += 1; continue
        if body in seen: continue
        methods = methods_of(code, own, lower_cls)
        if not methods: stats["no method"] += 1; continue
        seen.add(body)
        out.append({"source": rel, "title": sc["title"], "code": body, "expect_exprs": sc["expect"], "methods": methods})
        stats["kept narrated"] = stats.get("kept narrated", 0) + 1
    return out

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
            if f.name.startswith("_"): continue
            stats["files"] += 1
            raw = f.read_text(encoding="utf-8", errors="replace")
            if re.search(r"(?m)^\s*(Then|chk)\s*\(", raw, re.I):
                examples += harvest_narrated(f, f"base/test/{topic}/{f.name}", own, lower_cls, stats, seen); continue
            code, promises = parse(raw)
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
    # the course chapters: each fenced cell is one example, titled by the section heading above it;
    # the course's own guard runs every cell, so these are the best-checked examples of the library
    for course in ("elementary-introduction", "math"):
        folder = lib / "base" / "education" / "program" / "courses" / course / "chapters"
        for f in sorted(folder.glob("*.en.md")):
            text = f.read_text(encoding="utf-8", errors="replace").replace("\r", "")
            heading = ""
            for m in re.finditer(r"(?ms)^(#{2,3} [^\n]+)$|^```(?:ring|softanza)\n(.*?)^```", text):
                if m.group(1):
                    heading = m.group(1).lstrip("#").strip(); continue
                stats["files"] += 1
                code, promises = parse(m.group(2))
                body = "\n".join(code)
                if not promises: stats["no promise"] += 1; continue
                if len(code) > MAX_CODE: stats["too long"] += 1; continue
                if re.search(r"(?mi)^\s*(func|class|def)\s+\w", body) or re.search(r"(?i)\b(try|catch|done)\b", body) or FORBIDDEN.search(body):
                    stats["forbidden"] += 1; continue
                if body in seen: continue
                methods = methods_of(code, own, lower_cls)
                if not methods: stats["no method"] += 1; continue
                seen.add(body)
                examples.append({"source": f"base/education/program/courses/{course}/chapters/{f.name}", "title": heading,
                                 "code": body.strip("\n"), "expected": "\n".join(promises), "methods": methods})
                stats["kept chapters"] = stats.get("kept chapters", 0) + 1
    OUT.write_text(json.dumps(examples, ensure_ascii=False, indent=1), encoding="utf-8")
    pairs = {tuple(p) for e in examples for p in e["methods"]}
    print(stats)
    print(f"{len(examples)} examples, touching {len(pairs)} methods of {len({p[0] for p in pairs})} classes -> data/examples-src.json")

if __name__ == "__main__":
    main()
