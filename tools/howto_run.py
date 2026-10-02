#!/usr/bin/env python3
"""Run the library's recipes (base/doc/quickers/recipes) and record what each one printed.

A recipe answers one "how do I...?" with one block of code: its title is its
`# Intent:` line, its promise the `#-->` lines, and it names the methods it uses,
the words a reader would search with, and the recipes it leads to. A recipe
writes an expression and the value it has, as a reader would at a prompt; so an
expression that carries a promise and does not print is printed for the run
(`? ` before it), and the page says so. A recipe whose code shows the platform's
former name, or that touches files, input, the network, the clock or chance, is
not run; the reason is recorded. All recipes run in one process, each in its own
try block; the temporary folder created in the library is removed at the end.

    python tools/howto_run.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib, subprocess, datetime, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from showcase_run import verdict
from harvest_examples import FORBIDDEN

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "howto-run.json"
WORD = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)
FENCE = re.compile(r"(?ms)^```([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$")
PROMISE = re.compile(r"(#|//)[ \t]*-->[ \t]?(.*)$")
STATEMENT = re.compile(r"(?i)^\s*(\?|see\b|load\b|for\b|while\b|if\b|but\b|else\b|ok\b|next\b|end\b|func\b|class\b|return\b|try\b|catch\b|done\b|[\w@.\[\]]+\s*[+\-*/]?=(?!=))")

def parse_recipe(text):
    intent = re.search(r"(?m)^# Intent:\s*(.+)$", text)
    fences = list(FENCE.finditer(text))
    code_fences = [m for m in fences if m.group(1).lower() in ("ring", "softanza")]
    field = lambda name: [x.strip() for x in re.split(r",\s*", (re.search(rf"(?m)^- \*\*{name}:\*\*\s*(.+)$", text) or [None, ""])[1]) if x.strip()]
    # the explanation: prose between the code and the field list
    after = text[code_fences[-1].end():] if code_fences else ""
    notes = re.split(r"(?m)^- \*\*", after)[0].strip()
    return {"intent": intent.group(1).strip() if intent else "", "blocks": [m.group(2).rstrip("\n") for m in code_fences],
            "notes": notes, "methods": field("Methods"), "tags": field("Tags"), "see": field("See also")}

def runnable(block):
    """the block as run: an expression that carries a promise and prints nothing is printed"""
    lines, promises, printed = [], [], 0
    src = block.split("\n")
    for i, line in enumerate(src):
        m = PROMISE.search(line)
        if m and not line.strip().startswith(("#", "//")):          # `expr  #--> value` on one line
            code = line[:m.start()].rstrip()
            promises.append(m.group(2).strip())
            if not STATEMENT.match(code): code, printed = "? " + code.strip(), printed + 1
            lines.append(code); continue
        if m:                                                       # `#--> value` under the expression
            promises.append(m.group(2).strip())
            j = len(lines) - 1
            while j >= 0 and not lines[j].strip(): j -= 1
            if j >= 0 and not STATEMENT.match(lines[j]) and not lines[j].strip().startswith(("#", "//")):
                lines[j], printed = "? " + lines[j].strip(), printed + 1
            continue
        if re.match(r"(?i)\s*load\s", line): continue
        lines.append(line)
    return lines, [p for p in promises if p], printed

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    src_dir = lib / "base" / "doc" / "quickers" / "recipes"
    work = lib / "base" / "test" / "_stzsite_howto"
    work.mkdir(parents=True, exist_ok=True)
    result, queue = {}, []
    for f in sorted(src_dir.rglob("*.md")):
        rel = f.relative_to(src_dir).as_posix()
        text = f.read_text(encoding="utf-8", errors="replace").replace("\r", "")
        rec = parse_recipe(text)
        rec.update(category=f.parent.name, slug=f.stem, file=rel, status="", reason="", parts=[])
        result[rel] = rec
        if not rec["blocks"]:
            rec.update(status="no code"); continue
        if any(WORD.search(b) for b in rec["blocks"]):
            rec.update(status="not run", reason="names"); continue
        allcode = "\n".join(rec["blocks"])
        if FORBIDDEN.search(allcode) or re.search(r"(?i)\b(give|getchar)\b", allcode):
            rec.update(status="not run", reason="effects"); continue
        queue.append(rel)
    # one process: each block of each recipe in its own try, between markers
    chunks = {}
    for qi, rel in enumerate(queue):
        rec = result[rel]; chunk = []
        for bi, block in enumerate(rec["blocks"]):
            lines, promises, printed = runnable(block)
            rec["parts"].append({"promise": "\n".join(promises), "printed": printed})
            tag = f"{qi}.{bi}"
            chunk += [f'? "@@BEGIN {tag}"', "try"] + lines + ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {tag}"', ""]
        chunks[qi] = chunk
    def run(lines):
        script = work / "howto.ring"
        script.write_text("\n".join(['load "../../../max/stzMax.ring"', ""] + lines) + "\n", encoding="utf-8")
        p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        return (p.stdout or "").replace("\r", "")
    t0 = datetime.datetime.now()
    try:
        out = run([l for qi in chunks for l in chunks[qi]])
        if queue and "@@BEGIN 0.0" not in out:
            # one recipe does not compile and took the others with it: run each alone, once
            out = ""
            for qi in chunks:
                one = run(chunks[qi])
                if f"@@BEGIN {qi}.0" not in one: result[queue[qi]].update(reason="does not compile")
                out += one + "\n"
    finally:
        shutil.rmtree(work, ignore_errors=True)
    ran = t0.strftime("%Y-%m-%d %H:%M")
    for qi, rel in enumerate(queue):
        rec = result[rel]
        for bi, part in enumerate(rec["parts"]):
            m = re.search(rf"@@BEGIN {qi}\.{bi}\n(.*?)\n?@@END {qi}\.{bi}", out, re.S)
            if not m:
                part.update(verdict="stopped", out=""); continue
            text_out = m.group(1).rstrip()
            if "@@ERROR" in text_out:
                part.update(verdict="raised", out=text_out.replace("@@ERROR ", ""))
            elif part["promise"]:
                part.update(verdict="kept" if verdict(rec["blocks"][bi], text_out, part["promise"]) else "differs", out=text_out)
            else:
                part.update(verdict="ran", out=text_out)
            if WORD.search(part["out"]):                                   # an output that shows the word is not shown
                rec.update(reason="names in output")
        rec.update(status="run" if not rec["reason"] else "not run", ran=ran)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    st = {}
    for r in result.values():
        k = r["status"] + (":" + r["reason"] if r["reason"] else "")
        if r["status"] == "run": k += ":" + ("kept" if all(x["verdict"] in ("kept", "ran") for x in r["parts"]) else "not kept")
        st[k] = st.get(k, 0) + 1
    print(st, f"in {(datetime.datetime.now() - t0).total_seconds():.0f} s -> data/howto-run.json")

if __name__ == "__main__":
    main()
