#!/usr/bin/env python3
"""Code is shown in Haro's name: the rename, and its audit (B37 of the external assessment, ruled by the author 2026-10-07).

The author ruled that the code the site shows is Haro code, which wears the surface of the language it grew from: where a text was
written before the language took its present name, the NAME is changed and nothing else. So this module does exactly one thing:

  rename(text)         the former name, standing alone, becomes Haro in the same case (ring -> haro, Ring -> Haro, RING -> HARO),
                       and the few DATA strings that spell the name inside a value are changed with it (declared below, published)
  audit(before, after) refuses any difference that is not one of those name tokens or one of the declared data pairs

What it leaves, because the library owns it and the code would break or lie if it changed: a file name (learn.ring, stzlib.ring: a
dot before or after), a builtin or an identifier that contains the name (ring_len, stzRingCodeGraph), the agent grammar's prefix
(ring:), the bridge's own name (Ring++), and a fence tag inside a string (```ring), which the library's narration reader parses.

A renamed text whose data changed is a different program: it is RUN again, never trusted. The callers do that: tools/reader_run.py
builds the course reader from a renamed copy of the program, tools/proof_run.py --program runs the book's proof on it. A data pair
was added here only after a run of the renamed cell failed without it, and the run that follows is what proves the pair right.

    python tools/haro.py program <program folder> <copy>     a renamed copy of a course program, with the audit, and the pairs it made
"""
import re, sys, json, shutil, pathlib

NAME = re.compile(r"(?<![\w./\-])(?<!```)(ring|Ring|RING)(?![\w.+:\-])")    # inline `RING` is the name; a ```ring fence tag is not
MAP = {"ring": "haro", "Ring": "Haro", "RING": "HARO"}
# data that spells the name without being the name standing alone, each found by a red run of the renamed chapter:
#   chapter 3   "RIxxNxG" with the x's removed is RING, and a spaced promise "R I N G"
#   chapter 11  a search for the name inside "fjringljringdjringg", positions 3, 9 and 15 (the renamed string keeps them)
DATA = {"RIxxNxG": "HAxxRxO", "rixxnxg": "haxxrxo", "R I N G": "H A R O", "fjringljringdjringg": "fjharoljharodjharog"}
DATA_RX = re.compile(r"\b(" + "|".join(map(re.escape, sorted(DATA, key=len, reverse=True))) + r")\b")
TOKEN = re.compile(r"\w+|\W")
# the former name as the site's gates look for it, in any case, with the same exceptions as the rename: one pattern, not nine copies
FORMER = re.compile(NAME.pattern, re.I)
# the former name in code shown AS THE LIBRARY WROTE IT (method examples, recipes, rows), which is never renamed: a STRICTER pattern,
# because `"ring---"` in a test's data is the name to a reader and nothing renames it. Folding these filters into FORMER on 2026-10-08
# let two such examples through, and the gate could not see it because it reads FORMER too: two meanings, two patterns, one file
SHOWN = re.compile(r"(?<![\w./-])ring(?![\w.])", re.I)

def rename(text):
    """the text with the former name changed to Haro's, and the number of changes"""
    n = [0]
    def data(m):
        n[0] += 1
        return DATA[m.group(1)]
    text = DATA_RX.sub(data, text)
    def name(m):
        n[0] += 1
        return MAP[m.group(1)]
    return NAME.sub(name, text), n[0]

def audit(before, after, where=""):
    """the two texts may differ only by name tokens and declared data pairs; anything else raises"""
    for i, (k, v) in enumerate(DATA.items()):
        mark = chr(0) + f"DATA{i}" + chr(0)
        before = re.sub(r"\b" + re.escape(k) + r"\b", mark, before)
        after = re.sub(r"\b" + re.escape(v) + r"\b", mark, after)
    a, b = TOKEN.findall(before), TOKEN.findall(after)
    if len(a) != len(b):
        raise SystemExit(f"haro audit: {where}: the rename changed the number of tokens ({len(a)} -> {len(b)})")
    for x, y in zip(a, b):
        if x != y and MAP.get(x) != y:
            raise SystemExit(f"haro audit: {where}: '{x}' became '{y}', which is neither a name nor a declared data pair")
    return True

def pairs(before, after):
    """[(line, before, after)] for every line the rename changed: the record the build publishes"""
    out = []
    for i, (x, y) in enumerate(zip(before.split("\n"), after.split("\n")), 1):
        if x != y: out.append((i, x.strip(), y.strip()))
    return out

def rename_program(src, dst):
    """a copy of a course program in which every chapter, task, world page AND every exercise and project file (the checker's
    promise, the right and wrong answers) is renamed and audited, so what the site shows and what proves it are one program;
    returns {file: [pairs]}"""
    src, dst = pathlib.Path(src), pathlib.Path(dst)
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(src, dst)
    record = {}
    for f in sorted(list(dst.rglob("*.md")) + list(dst.rglob("*.ring"))):
        t = f.read_text(encoding="utf-8")
        r, n = rename(t)
        if not n: continue
        rel = f.relative_to(dst).as_posix()
        audit(t, r, rel)
        f.write_text(r, encoding="utf-8")
        record[rel] = pairs(t, r)
    return record

if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "program":
        rec = rename_program(sys.argv[2], sys.argv[3])
        print(f"{sum(len(v) for v in rec.values())} lines renamed in {len(rec)} files; every difference is a name or a declared data pair")
    else:
        print(__doc__)
