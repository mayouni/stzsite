#!/usr/bin/env python3
"""The Learning System at the command line, run: a learner's first minutes, and how many translated units a native speaker has read.

The page "What is proved, and what is not" shows the tools a learner and a reviewer actually run, and every block of it is run before the
page is built, like every other block of the site: against the library at its pinned commit, in a learner's folder that is a temporary
folder of the site's, never the library's (the tools run from base/education/tools, which is their documented place, and write only where
they are told). The output is kept in data/edu-record-run.json; the page puts the command and what it printed side by side.

  status     a fresh learner: where they are, and what the next level still needs
  refused    a wrong answer to exercise 1.1: the checker ran it and says why it is refused
  passed     a right answer: the checker ran it, and the learner moves to chapter 2
  status2    the same learner, one exercise later
  tutor      a question about a later chapter: the tutor will not spoil it, and asks
  review     the number of translated units a native speaker has reviewed, in French, Arabic and Hausa

    python tools/edu_record_run.py <path to libraries/stzlib>      -> data/edu-record-run.json
"""
import json, re, sys, pathlib, subprocess, datetime, shutil, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "edu-record-run.json"
NL = chr(10)
LEARNER = "ada"

def label(en, fr):
    return {"en": en, "fr": fr}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    tools = lib / "base" / "education" / "tools"
    course = lib / "base" / "education" / "program" / "courses" / "elementary-introduction" / "exercises" / "ex-01-01"
    if not (tools / "learn.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    repo = lib.parent.parent                                            # the checkout that holds libraries/stzlib
    def git(*a):
        return subprocess.run(["git", "-C", str(repo)] + list(a), capture_output=True, text=True, encoding="utf-8").stdout.strip()
    commit = git("rev-parse", "--short=9", "HEAD")
    if git("status", "--porcelain"):
        sys.exit("the library worktree has uncommitted changes: the commit would not say what ran")
    work = pathlib.Path(tempfile.mkdtemp(prefix="stzsite_edu_"))
    wrong = sorted((course / "wrong").glob("*.ring"))[0]
    right = sorted((course / "right").glob("*.ring"))[0]
    shutil.copyfile(wrong, work / "wrong.ring")
    shutil.copyfile(right, work / "right.ring")
    folder = str(work / LEARNER).replace(chr(92), "/")
    t0 = datetime.datetime.now()

    def desk(script, args):
        """one tool, run from its own folder; returns (stdout cleaned, exit code)"""
        p = subprocess.run(["ring", script] + args, cwd=tools, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "").replace("\r", "")
        out = out.replace(str(work).replace(chr(92), "/"), "").replace(str(work), "")
        return re.sub(r"\n(?:[ \t]*\n)+", NL + NL, out).strip(), p.returncode

    def program(name):
        return (work / name).read_text(encoding="utf-8").replace("\r", "").strip()

    segs, codes = [], {}
    try:
        o, c = desk("learn.ring", [folder, "status"]);                                   segs.append(("status", f"learn.ring {LEARNER} status", o)); codes["status"] = c
        o, c = desk("learn.ring", [folder, "submit", "ex-01-01", str(work / "wrong.ring")]); segs.append(("refused", "# wrong.ring" + NL + program("wrong.ring") + NL + NL + f"learn.ring {LEARNER} submit ex-01-01 wrong.ring", o)); codes["refused"] = c
        o, c = desk("learn.ring", [folder, "submit", "ex-01-01", str(work / "right.ring")]); segs.append(("passed", "# right.ring" + NL + program("right.ring") + NL + NL + f"learn.ring {LEARNER} submit ex-01-01 right.ring", o)); codes["passed"] = c
        o, c = desk("learn.ring", [folder, "status"]);                                   segs.append(("status2", f"learn.ring {LEARNER} status", o)); codes["status2"] = c
        q = "How do I use KnowRelation to teach a world?"
        o, c = desk("learn.ring", [folder, "ask", "ex-02-01", q]);                       segs.append(("tutor", f'learn.ring {LEARNER} ask ex-02-01 "{q}"', o)); codes["tutor"] = c
        lines, shown = [], []
        for lang in ("fr", "ar", "ha"):
            o, c = desk("review_sheet.ring", [str(work / "sheet.md"), "--lang", lang]);  codes["review-" + lang] = c
            shown.append(f"review_sheet.ring sheet.md --lang {lang}"); lines.append(o.split(NL)[0])
        segs.append(("review", NL.join(shown), NL.join(lines)))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    if git("status", "--porcelain") or git("rev-parse", "--short=9", "HEAD") != commit:
        sys.exit("the library worktree changed while the tools ran")
    expect = {"status": 0, "refused": 2, "passed": 0, "status2": 0, "tutor": 0}
    bad = [k for k, v in expect.items() if codes.get(k) != v] + [k for k, v in codes.items() if k.startswith("review-") and v != 0]
    OUT.write_text(json.dumps({"ran": t0.strftime("%Y-%m-%d %H:%M"), "commit": commit,
                               "segments": [{"name": n, "code": c, "out": o} for n, c, o in segs]}, ensure_ascii=False, indent=1), encoding="utf-8")
    for n, c, o in segs:
        print(f"-- {n}" + NL + o[:700])
    print(f"exit codes {codes}")
    print(f"{len(segs)} segments -> data/edu-record-run.json at commit {commit}" + (f"; UNEXPECTED EXIT: {bad}" if bad else ""))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
