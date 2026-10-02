#!/usr/bin/env python3
"""The learner's ladder, read from the library and proved by running it.

The Learning System has five rungs, S0 Explorer to S4 Master (program/levels.zknw).
A rung is earned when every exercise of its chapters has passed and its project
has passed, each with evidence that still matches; never by a score. This tool
asks the library itself, in one process run inside it:

  - which chapters each rung needs (StzProgramQ(...).ChaptersForLevel)
  - each project's guard proving itself: its wrong samples refused, its right
    samples accepted (StzProjectQ(...).ProveItself), with the reason given
  - where a new learner stands: what is missing for S0 (StzLearnerQ(...).MissingFor)

and reads, from the files, each chapter's title and each project's brief in the
four languages of the course. Writes data/ladder-run.json; the temporary folder
created in the library is removed at the end.

    python tools/ladder_run.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "ladder-run.json"
LANGS = ("en", "fr", "ar", "ha")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    prog = lib / "base" / "education" / "program"
    if not (prog / "levels.zknw").is_file():
        sys.exit(f"not the library folder: {lib}")
    # the rungs, as the library declares them
    facts = re.findall(r"(?m)^\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*$", (prog / "levels.zknw").read_text(encoding="utf-8"))
    levels = {}
    for s, p, o in facts:
        if re.fullmatch(r"s\d", s): levels.setdefault(s, {"id": s})[p] = o
    levels = [levels[k] for k in sorted(levels)]
    work = lib / "base" / "test" / "_stzsite_ladder"
    work.mkdir(parents=True, exist_ok=True)
    code = ['load "../../stzBase.ring"', "", 'oP = StzProgramQ("../../education/program")', 'oC = oP.CourseQ("elementary-introduction")', ""]
    for lv in levels:
        code += [f'? "@@CH {lv["id"]}"', f'acCh = oP.ChaptersForLevel(oC, "{lv["id"]}")', "for i = 1 to len(acCh) ? acCh[i] next"]
    code += ['acPr = oP.ProjectIds()', 'for i = 1 to len(acPr)',
             '    ? "@@PROJECT " + acPr[i]', "    try",
             "        aPr = oP.ProjectQ(acPr[i]).ProveItself()",
             '        ? "@@COUNTS " + aPr[:wrong] + " " + aPr[:wrongrefused] + " " + aPr[:right] + " " + aPr[:rightaccepted]',
             "        for k = 1 to len(aPr[:checks])",
             '            ? "@@SAMPLE " + aPr[:checks][k][1]',
             '            ? "@@PASSED " + aPr[:checks][k][2].Passed()',
             '            ? "@@WHY " + aPr[:checks][k][2].Why()',
             "        next",
             '    catch', '        ? "@@ERROR " + cCatchError', "    done", "next",
             'oL = StzLearnerQ("t_ladder/a-new-learner")',
             '? "@@EARNED " + oL.HasEarned(oP, oC, "s0")',
             '? "@@MISSING " + @@(oL.MissingFor(oP, oC, "s0"))', '? "@@END"']
    (work / "ladder.ring").write_text("\n".join(code) + "\n", encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", "ladder.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    seconds = round((datetime.datetime.now() - t0).total_seconds(), 1)
    if "--raw" in sys.argv: pathlib.Path(sys.argv[sys.argv.index("--raw") + 1]).write_text(out, encoding="utf-8")
    if "@@END" not in out:
        print(out[-3000:]); sys.exit("the ladder run did not finish")
    for lv in levels:
        block = re.search(rf"@@CH {lv['id']}\n(.*?)(?=\n@@)", out, re.S)
        lv["chapters"] = [l.strip() for l in block.group(1).split("\n") if l.strip()] if block else []
    projects = {}
    for m in re.finditer(r"@@PROJECT (\S+)\n(.*?)(?=\n@@PROJECT |\n@@EARNED)", out, re.S):
        pid, txt = m.group(1), m.group(2)
        rec = {"id": pid, "samples": []}
        c = re.search(r"@@COUNTS (\d+) (\d+) (\d+) (\d+)", txt)
        if c: rec.update(wrong=int(c.group(1)), wrong_refused=int(c.group(2)), right=int(c.group(3)), right_accepted=int(c.group(4)))
        for s in re.finditer(r"@@SAMPLE ([^\n]+)\n@@PASSED (\d)\n@@WHY (.*?)(?=\n@@SAMPLE |\Z)", txt, re.S):
            path = s.group(1).strip().replace("\\", "/")
            rec["samples"].append({"kind": path.split("/")[-2], "name": path.split("/")[-1], "passed": s.group(2) == "1", "why": s.group(3).strip()})
        if "@@ERROR" in txt: rec["error"] = txt.split("@@ERROR ", 1)[1].strip()
        d = prog / "projects" / pid
        rec["brief"] = {}
        for lang in LANGS:
            f = d / f"brief.{lang}.md"
            if f.exists():
                t = f.read_text(encoding="utf-8").replace("\r", "")
                paras = [x.strip() for x in re.split(r"\n\s*\n", t) if x.strip() and not x.strip().startswith(("#", ">"))]
                checks = re.findall(r"(?m)^- (.+)$", t)
                rec["brief"][lang] = {"what": paras[0] if paras else "", "checks": checks}
        projects[pid] = rec
    # chapter titles, from each chapter file's first heading, in the four languages
    chap_dir = prog / "courses" / "elementary-introduction" / "chapters"
    titles = {}
    for f in sorted(chap_dir.glob("*.md")):
        m = re.match(r"(\d+)-(.+)\.(\w\w)\.md$", f.name)
        if not m: continue
        h = re.search(r"(?m)^# (.+)$", f.read_text(encoding="utf-8"))
        titles.setdefault(m.group(2), {"n": int(m.group(1)), "slug": m.group(2)})[m.group(3)] = h.group(1).strip() if h else m.group(2)
    earned = re.search(r"@@EARNED (\d)", out).group(1) == "1"
    missing = re.search(r"@@MISSING (.*)", out).group(1).strip()
    res = {"ran": t0.strftime("%Y-%m-%d %H:%M"), "seconds": seconds, "levels": levels, "projects": projects,
           "chapters": sorted(titles.values(), key=lambda x: x["n"]), "new_learner": {"earned_s0": earned, "missing_s0": missing}}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for pid, r in projects.items():
        print(pid, f"wrong {r.get('wrong_refused')}/{r.get('wrong')} refused, right {r.get('right_accepted')}/{r.get('right')} accepted", r.get("error", ""))
    print([(l["id"], l.get("named"), len(l["chapters"])) for l in levels], "missing:", missing, f"in {seconds} s -> data/ladder-run.json")

if __name__ == "__main__":
    main()
