#!/usr/bin/env python3
"""The teacher's door, run: a cohort, an exercise judged by running, a report that is a narration.

The education pages show what a teacher does, and every block of it is run inside the library before the page is built, like every
other block of the site. This writes three segments of code into one script, runs it in one process inside the library at its
pinned commit, and keeps what each printed in data/edu-run.json; the page puts the code and that output side by side.

    python tools/edu_run.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "edu-run.json"
NL = chr(10)

SEGMENTS = [
  ("cohort", NL.join([
    'StzEngineDirCreatePath("cohorts/niamey-2026")',
    'write("cohorts/niamey-2026/cohort.zknw", \'knowledge "niamey-2026"\' + char(10) + char(10) + "facts" + char(10) +',
    '        "    niamey-2026 | is-a | cohort" + char(10) + "    niamey-2026 | follows | elementary-introduction" + char(10))',
    'oCohort = StzCohortQ("cohorts/niamey-2026")',
    'oCohort.AddLearner("amina")',
    'oCohort.AddLearner("moussa")',
    '? @@( oCohort.LearnerIds() )'])),
  ("exercise", NL.join([
    'oProgram = oCohort.ProgramQ("../../education/program")',
    'oExercise = oProgram.CourseQ("elementary-introduction").ExerciseQ("ex-01-01")',
    '? oExercise.Task("en")',
    '? @@( oExercise.Promises() )',
    '? oExercise.Check( read(oExercise.WrongAnswers()[1]) ).Passed()',
    '? oExercise.Check( read(oExercise.RightAnswers()[1]) ).Passed()'])),
  ("report", NL.join([
    'oCohort.LearnerQ("amina").Submit( oExercise, read(oExercise.RightAnswers()[1]) )',
    '? read( oCohort.WriteReport("../../education/program", "") )'])),
]

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    work = lib / "base" / "test" / "_stzsite_edu"
    work.mkdir(parents=True, exist_ok=True)
    lines = ['load "../../stzBase.ring"', ""]
    for name, code in SEGMENTS: lines += [f'? "@@SEG {name}"', code, ""]
    lines.append('? "@@SEG end"')
    (work / "teach.ring").write_text(NL.join(lines) + NL, encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", "teach.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    parts = re.split(r"@@SEG (\w+)\n", out)
    got = {parts[i]: parts[i + 1].rstrip() for i in range(1, len(parts) - 1, 2)}
    segs = []
    for name, code in SEGMENTS:
        o = re.sub(r"\n(?:[ \t]*\n)+", "\n\n", got.get(name, ""))       # a file with Windows line ends prints its blank lines twice
        if name == "report":
            o = o.split("\n## ")[0].rstrip() + "\n\n[...]"          # the table; under it, one cell per learner whose lines name the learner's folder
        segs.append({"name": name, "code": code, "out": o})
    bad = [s["name"] for s in segs if not s["out"] or "Error" in s["out"]]
    OUT.write_text(json.dumps({"ran": t0.strftime("%Y-%m-%d %H:%M"), "commit": "0e72e2e2c", "segments": segs}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(segs) - len(bad)} of {len(segs)} segments ran -> data/edu-run.json" + (f"; FAILED: {bad}" if bad else ""))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
