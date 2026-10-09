#!/usr/bin/env python3
"""The depth of the foundation, measured: what the library holds, read from a checkout of it, never from memory.

  domains   every folder under base/, with its Ring files and lines (tests, documents and archives not counted as code)
  engine    the engine's Zig modules, by file count and lines
  tests     the test tree: files, scenario guards (the *_narrated.ring files), classic numbered tests
  designs   the design documents under base/doc/design: title and first sentence, so a reader can choose where to start
  commit    the library commit all of this was read at

The count is a text reading (files and lines), not a run. The documents' titles go through the rename (tools/haro.py): the page
shows the platform's present name, as every page of this site does.

    python tools/depth_run.py <path to libraries/stzlib>      -> data/depth.json
"""
import json, re, sys, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import haro

def lines_of(path):
    try: return len(path.read_bytes().split(b"\n"))
    except OSError: return 0

def sentence(text):
    body = re.sub(r"(?ms)^---.*?^---\s*", "", text)
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "|", "```", ">", "-", "*", "<", "=")) or len(p) < 50: continue
        p = re.sub(r"[*_`]", "", re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)); p = " ".join(p.split())
        cut = p.find(". ")
        return (p[:cut + 1] if 40 < cut < 220 else p[:200].rsplit(" ", 1)[0] + "...")
    return ""

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    domains = []
    for d in sorted((lib / "base").iterdir()):
        if not d.is_dir() or d.name in ("test", "doc", "archive", "cache"): continue
        files = [f for f in d.rglob("*.ring") if "archive" not in f.parts]
        if files: domains.append({"name": d.name, "files": len(files), "lines": sum(lines_of(f) for f in files)})
    domains.sort(key=lambda x: -x["lines"])
    eng = [f for f in (lib / "engine" / "src").glob("*.zig")]
    engine = {"modules": len(eng), "lines": sum(lines_of(f) for f in eng),
              "largest": sorted([[f.stem, lines_of(f)] for f in eng], key=lambda x: -x[1])[:12]}
    tests = list((lib / "base" / "test").rglob("*.ring"))
    tcount = {"files": len(tests), "scenario_guards": sum(1 for f in tests if f.name.endswith("_narrated.ring")),
              "numbered": sum(1 for f in tests if re.match(r"\d+_", f.name)), "folders": len({f.parent for f in tests})}
    designs = []
    for f in sorted((lib / "base" / "doc" / "design").glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace").replace("\r", "")
        title = next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), f.stem)
        t, _ = haro.rename(title); one, _ = haro.rename(sentence(text))
        designs.append({"file": f.name, "title": t, "line": one, "lines": lines_of(f)})
    out = {"commit": commit, "domains": domains, "engine": engine, "tests": tcount, "designs": designs}
    (ROOT / "data" / "depth.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(domains)} domains, {sum(d['lines'] for d in domains):,} lines; engine {engine['modules']} modules, {engine['lines']:,} lines; "
          f"tests {tcount['files']} files, {tcount['scenario_guards']} scenario guards; {len(designs)} designs; at {commit}")

if __name__ == "__main__":
    main()
