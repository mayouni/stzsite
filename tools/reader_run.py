#!/usr/bin/env python3
"""The course reader, built by the library from a copy of the program in which the code is shown in Haro's name, and RUN.

The reader (reader.html) is the library's own page: tools/build_reader.ring in base/education/tools runs every cell of every chapter
in every language and writes one HTML file; the build is red if a cell raises or a promise is not kept. The author ruled that the
site shows code in Haro's name (12.17), so the site does not copy the library's page as it is: it renames a COPY of the program
(tools/haro.py: names only, plus the declared data pairs, every file audited), lets the library build the reader from that copy,
and keeps the result only if every cell ran green. A rename that broke a cell is a red build, never a page.

    python tools/reader_run.py <path to libraries/stzlib>      -> reader.html, data/haro-rename.json
"""
import json, re, sys, pathlib, subprocess, datetime, shutil, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import haro

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    tools = lib / "base" / "education" / "tools"
    if not (tools / "build_reader.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    repo = lib.parent.parent
    git = lambda *a: subprocess.run(["git", "-C", str(repo)] + list(a), capture_output=True, text=True, encoding="utf-8").stdout.strip()
    commit = git("rev-parse", "--short=9", "HEAD")
    if git("status", "--porcelain"):
        sys.exit("the library worktree has uncommitted changes: the commit would not say what ran")
    work = pathlib.Path(tempfile.mkdtemp(prefix="stzsite_reader_"))
    t0 = datetime.datetime.now()
    try:
        record = haro.rename_program(lib / "base" / "education" / "program", work / "program")
        out = work / "reader.html"
        p = subprocess.run(["ring", "build_reader.ring", str(out).replace(chr(92), "/"), "--program", str(work / "program").replace(chr(92), "/")],
                           cwd=tools, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1800)
        log = (p.stdout or "").replace("\r", "").replace(str(work).replace(chr(92), "/"), "<copy>")
        print(log.strip())
        if p.returncode != 0 or "=RED" in log or not out.exists():
            sys.exit(f"the reader built from the renamed program is red (exit {p.returncode}): the site keeps its previous reader")
        shutil.copyfile(out, ROOT / "reader.html")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    if git("status", "--porcelain") or git("rev-parse", "--short=9", "HEAD") != commit:
        sys.exit("the library worktree changed while the reader was built")
    shown = {k: v for k, v in record.items() if "/elementary-introduction/" in k or k.startswith("worlds/")}
    (ROOT / "data" / "haro-rename.json").write_text(json.dumps({"ran": t0.strftime("%Y-%m-%d %H:%M"), "commit": commit,
        "rule": "the name changed and nothing else, plus the declared data pairs; every renamed file audited and run",
        "files": {k: [list(x) for x in v] for k, v in sorted(shown.items())}}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"reader.html rebuilt from the renamed program at commit {commit} in {(datetime.datetime.now() - t0).seconds} s; "
          f"{sum(len(v) for v in shown.values())} renamed lines in {len(shown)} files of the course it shows -> data/haro-rename.json")

if __name__ == "__main__":
    main()
