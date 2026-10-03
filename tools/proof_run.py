#!/usr/bin/env python3
"""Prove the book: run every chapter of the Elementary Introduction, and record the proof.

The reader is the library's page and stores no output, by the course's own law.
The proof of a cell is a run: the chapter's cells run in one fresh process per
edition, each in its own try block, every promise (`#-->`) compared with what
the cell printed; the four editions must make the same promises, cell for cell;
and every exercise must prove itself, its wrong answers refused and its right
answers accepted. That is what the library's own guard, test/education/
course_narrated.ring, does; this tool asks the same questions of the same
objects, in one process inside the library, and writes what it found:

    data/proof-run.json     per chapter: the editions' verdicts, each cell with
                            what it printed, each exercise with its samples

Each cell is also tied to its place in the four chapter files (the line range
of its fence), so that a link can go from the cell to its source. One process;
the temporary folder created in the library is removed at the end.

    python tools/proof_run.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "proof-run.json"
LANGS = ("en", "fr", "ar", "ha")
COURSE = "elementary-introduction"

SCRIPT = '''load "../../stzBase.ring"
oP = StzProgramQ("../../education/program")
oC = oP.CourseQ("%s")
aLangs = [ "en", "fr", "ar", "ha" ]
acAll = oC.ChapterIds()
for c = 1 to len(acAll)
    cId = acAll[c]
    ? "@@CH " + cId + " " + oC.ChapterNumber(cId)
    try
        aCh = oC.RunChapterInQ(cId, aLangs)
        for i = 1 to len(aLangs)
            ? "@@TITLE " + aLangs[i] + " " + oC.TitleOf(cId, aLangs[i])
            oCh = aCh[i]
            ? "@@ED " + aLangs[i] + " " + oCh.NumberOfCells() + " " + oCh.NumberOfPromises() + " " + oCh.HasStoredOutput() + " " + oCh.AllCellsRan() + " " + oCh.AllPromisesKept()
            for j = 1 to oCh.NumberOfCells()
                ? "@@CELL " + aLangs[i] + " " + j + " " + oCh.CellRan(j) + " " + oCh.CellKept(j) + " " + len(oCh.CellPromises(j))
                if i = 1
                    ? "@@OUT"
                    ? oCh.CellOutput(j)
                    ? "@@ERR"
                    ? oCh.CellError(j)
                    ? "@@ENDOUT"
                ok
            next
        next
        for i = 2 to len(aLangs)
            if aCh[i].NumberOfCells() != aCh[1].NumberOfCells()
                ? "@@DRIFT " + aLangs[i] + " cells " + aCh[i].NumberOfCells() + " against " + aCh[1].NumberOfCells()
            else
                for j = 1 to aCh[1].NumberOfCells()
                    if @@(aCh[i].CellPromises(j)) != @@(aCh[1].CellPromises(j))
                        ? "@@DRIFT " + aLangs[i] + " cell " + j + " promises differ from en"
                    ok
                next
            ok
        next
        acEx = aCh[1].ExerciseIds()
        for e = 1 to len(acEx)
            oEx = oC.ExerciseQ(acEx[e])
            ? "@@EX " + acEx[e]
            aPr = oEx.ProveItself()
            ? "@@EXC " + aPr[:wrong] + " " + aPr[:wrongrefused] + " " + aPr[:right] + " " + aPr[:rightaccepted]
            for k = 1 to len(aPr[:checks])
                ? "@@EXS " + aPr[:checks][k][1]
                ? "@@EXP " + aPr[:checks][k][2].Passed()
            next
        next
        ? "@@ENDCH"
    catch
        ? "@@ERROR " + cCatchError
    done
next
? "@@END"
''' % COURSE

def fences(path):
    """the ring cells of a chapter file, as the library cuts them: [(first line, last line, nearest heading)], 1-based"""
    out, state, start, heading = [], 0, 0, ""
    lines = path.read_text(encoding="utf-8").replace("\r", "").split("\n")
    for i, raw in enumerate(lines, 1):
        t = raw.strip()
        if state == 0:
            if t.startswith("```"):
                info = t[3:].strip().lower()
                state = 1 if info == "ring" else 2
                start = i
            elif t.startswith("## "):
                heading = t[3:].strip()
            elif t.startswith("# ") and not heading:
                pass
        else:
            if t.startswith("```"):
                if state == 1: out.append((start, i, heading))
                state = 0
    return out

def cell_code(path, a, b):
    lines = path.read_text(encoding="utf-8").replace("\r", "").split("\n")
    return "\n".join(lines[a:b - 1]).rstrip("\n")          # between the two fence lines

def first_heading(path):
    """the first heading of a file, whatever its level: `# Title` of a chapter, `### Exercise 1.1 · Title` of a task"""
    for l in path.read_text(encoding="utf-8").replace("\r", "").split("\n"):
        m = re.match(r"#{1,6}\s+(.+)", l)
        if m: return m.group(1).strip()
    return ""

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    if sys.argv[1] == "--retitle":                       # refresh what is read from files, without running anything
        lib = pathlib.Path(sys.argv[2]).resolve()
        res = json.loads(OUT.read_text(encoding="utf-8"))
        for ch in res["chapters"]:
            for ex in ch["exercises"]:
                ex["title"] = {}
                for lang in LANGS:
                    tf = lib / "base" / "education" / "program" / "courses" / res["course"] / "exercises" / ex["id"] / f"task.{lang}.md"
                    if tf.exists(): ex["title"][lang] = first_heading(tf)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print("exercise titles refreshed:", sum(len(c["exercises"]) for c in res["chapters"])); return
    lib = pathlib.Path(sys.argv[1]).resolve()
    prog = lib / "base" / "education" / "program" / "courses" / COURSE
    if not (prog / "chapters").is_dir():
        sys.exit(f"not the library folder: {lib}")
    work = lib / "base" / "test" / "_stzsite_proof"
    work.mkdir(parents=True, exist_ok=True)
    (work / "proof.ring").write_text(SCRIPT, encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", "proof.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=3000)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    seconds = round((datetime.datetime.now() - t0).total_seconds(), 1)
    if "--raw" in sys.argv: pathlib.Path(sys.argv[sys.argv.index("--raw") + 1]).write_text(out, encoding="utf-8")
    if "@@END" not in out:
        print(out[-2500:]); sys.exit("the proof run did not finish")
    chapters = []
    for m in re.finditer(r"@@CH (\S+) (\d+)\n(.*?)(?=\n@@CH |\n@@END\s*\Z)", out, re.S):
        cid, n, body = m.group(1), int(m.group(2)), m.group(3)
        ch = {"id": cid, "n": n, "title": {}, "editions": {}, "drift": [], "cells": [], "exercises": []}
        if "@@ERROR" in body: ch["error"] = body.split("@@ERROR ", 1)[1].strip()
        for t in re.finditer(r"@@TITLE (\w\w) ([^\n]*)", body): ch["title"][t.group(1)] = t.group(2).strip()
        for e in re.finditer(r"@@ED (\w\w) (\d+) (\d+) (\d+) (\d+) (\d+)", body):
            ch["editions"][e.group(1)] = {"cells": int(e.group(2)), "promises": int(e.group(3)), "stored_output": e.group(4) == "1",
                                         "all_ran": e.group(5) == "1", "all_kept": e.group(6) == "1", "cell_flags": []}
        for c in re.finditer(r"@@CELL (\w\w) (\d+) (-?\d+) (-?\d+) (\d+)", body):
            ch["editions"][c.group(1)]["cell_flags"].append({"ran": c.group(3) == "1", "kept": int(c.group(4)), "promises": int(c.group(5))})
        outs = re.findall(r"@@OUT\n(.*?)\n@@ERR\n(.*?)\n?@@ENDOUT", body, re.S)
        for d in re.finditer(r"@@DRIFT ([^\n]+)", body): ch["drift"].append(d.group(1))
        # where each cell sits in the four chapter files
        files, fz = {}, {}
        for lang in LANGS:
            f = next(iter((prog / "chapters").glob(f"{ch['n']:02d}-{cid}.{lang}.md")), None)
            files[lang] = f
            fz[lang] = fences(f) if f else []
        ch["file"] = {lang: f"base/education/program/courses/{COURSE}/chapters/{files[lang].name}" for lang in LANGS if files[lang]}
        n_cells = ch["editions"]["en"]["cells"] if "en" in ch["editions"] else 0
        for lang in LANGS:
            if lang in ch["editions"] and len(fz[lang]) != ch["editions"][lang]["cells"]:
                ch.setdefault("mismatch", []).append(f"{lang}: {len(fz[lang])} fences, {ch['editions'][lang]['cells']} cells")
        for j in range(n_cells):
            en = fz["en"][j] if j < len(fz["en"]) else None
            code = cell_code(files["en"], en[0], en[1]) if en else ""
            promise = "\n".join(l.split("#-->", 1)[1].strip() for l in code.split("\n") if "#-->" in l)
            flags = ch["editions"]["en"]["cell_flags"]
            fl = flags[j] if j < len(flags) else {"ran": False, "kept": 0, "promises": 0}      # a chapter that stopped part-way
            o, e = (outs[j] if j < len(outs) else ("", ""))
            ch["cells"].append({"n": j + 1, "code": code, "promise": promise, "out": o.strip(), "error": e.strip(),
                                "ran": fl["ran"], "kept": fl["kept"],
                                "heading": {lang: fz[lang][j][2] for lang in LANGS if j < len(fz[lang])},
                                "lines": {lang: [fz[lang][j][0], fz[lang][j][1]] for lang in LANGS if j < len(fz[lang])},
                                "kept_in": {lang: ch["editions"][lang]["cell_flags"][j]["kept"] for lang in LANGS if lang in ch["editions"] and j < len(ch["editions"][lang]["cell_flags"])}})
        for x in re.finditer(r"@@EX (\S+)\n@@EXC (\d+) (\d+) (\d+) (\d+)\n(.*?)(?=\n@@EX |\n@@ENDCH|\Z)", body, re.S):
            ex = {"id": x.group(1), "wrong": int(x.group(2)), "wrong_refused": int(x.group(3)), "right": int(x.group(4)), "right_accepted": int(x.group(5)), "samples": [], "title": {}}
            for s in re.finditer(r"@@EXS ([^\n]+)\n@@EXP (\d)", x.group(6)):
                path = s.group(1).strip().replace("\\", "/")
                ex["samples"].append({"kind": path.split("/")[-2], "name": path.split("/")[-1], "passed": s.group(2) == "1"})
            for lang in LANGS:
                tf = prog / "exercises" / ex["id"] / f"task.{lang}.md"
                if tf.exists(): ex["title"][lang] = first_heading(tf)
            ch["exercises"].append(ex)
        chapters.append(ch)
    res = {"ran": t0.strftime("%Y-%m-%d %H:%M"), "seconds": seconds, "course": COURSE, "chapters": chapters}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    cells = sum(len(c["cells"]) for c in chapters)
    kept = sum(1 for c in chapters for x in c["cells"] if x["kept"] == 1)
    nop = sum(1 for c in chapters for x in c["cells"] if x["kept"] == -1)
    ed = sum(1 for c in chapters for e in c["editions"].values() if e["all_ran"] and e["all_kept"] and not e["stored_output"])
    ex = sum(len(c["exercises"]) for c in chapters); exok = sum(1 for c in chapters for x in c["exercises"] if x["wrong_refused"] == x["wrong"] and x["right_accepted"] == x["right"])
    print(f"{len(chapters)} chapters, {sum(len(c['editions']) for c in chapters)} editions ({ed} ran with every promise kept and no stored output), "
          f"{cells} english cells ({kept} kept, {nop} promise nothing), drift {sum(len(c['drift']) for c in chapters)}, "
          f"mismatch {sum(1 for c in chapters if c.get('mismatch'))}, errors {sum(1 for c in chapters if c.get('error'))}, "
          f"exercises {exok}/{ex} prove themselves, in {seconds} s -> data/proof-run.json")

if __name__ == "__main__":
    main()
