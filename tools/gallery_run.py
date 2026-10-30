#!/usr/bin/env python3
"""Render the library's pictures again, tonight, and keep the result beside the picture the library committed.

The library's graphics tests each write a picture. A picture can be right or wrong in a way no counter sees (a map with a
province missing, a label across an edge), so the site shows each one and leaves a place for a person's verdict. This tool does
the part a machine can do: it runs each script that has a picture of the same name, in a temporary folder of the library, keeps
what it wrote, says whether it is byte for byte the picture the library committed, and hosts a copy for the page.

The scripts are the library's tests, and the library's main branch migrated its code to Rule A (a top-level name is written
$name inside a function) but not yet its tests: their `chk` helpers count with a bare `nOk++`, which Ring++ refuses. So the
copy that runs is migrated first, as `rnxc migrate` lists it -- each name it names spelt $name in the copy, outside strings and
comments, until it lists none -- and the record says which names were respelt. Ring reads the two spellings alike.

    python tools/gallery_run.py <path to libraries/stzlib>     -> data/gallery-run.json, assets/img/gallery/*.webp
"""
import json, re, sys, hashlib, subprocess, pathlib, datetime, shutil, time
from runtime import RNXC          # the runtime the examples run on (tools/runtime.py)
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import haro

def dollar(src, names):
    """src with every identifier in `names` (any case) spelt $name, outside strings and comments; a member (.x), a symbol
    (:x) and a name already carrying $ or @ are left as they are"""
    low, out, i, n = {x.lower() for x in names}, [], 0, len(src)
    while i < n:
        c = src[i]
        if c in "\"'`":
            j = src.find(c, i + 1); j = n - 1 if j < 0 else j
            out.append(src[i:j + 1]); i = j + 1; continue
        if c == "#" or src.startswith("//", i):
            j = src.find(chr(10), i); j = n if j < 0 else j
            out.append(src[i:j]); i = j; continue
        if src.startswith("/*", i):
            j = src.find("*/", i + 2); j = n if j < 0 else j + 2
            out.append(src[i:j]); i = j; continue
        if c.isalpha() or c in "_$@":
            j = i
            while j < n and (src[j].isalnum() or src[j] in "_$@"): j += 1
            tok, prev = src[i:j], (src[i - 1] if i else "")
            out.append("$" + tok if tok.lower() in low and prev not in (".", ":") else tok); i = j; continue
        out.append(c); i += 1
    return "".join(out)

def migrated(work, name):
    """ask rnxc which names of this copy break Rule A, spell them $name, and ask again until it lists none"""
    path, seen = work / f"{name}.ring", set()
    for _ in range(8):
        p = subprocess.run(RNXC + ["migrate", path.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
        found = {f[2].strip() for f in (l.split(chr(9)) for l in (p.stdout or "").splitlines())
                 if len(f) >= 3 and pathlib.Path(f[0]).name == path.name and f[2].strip()[:1] not in "$@"}
        found = {x for x in found if x.lower() not in {s.lower() for s in seen}}
        if not found: break
        seen |= found
        path.write_text(dollar(path.read_text(encoding="utf-8"), found), encoding="utf-8")
    return sorted(seen)

def caption(src):
    """the script's own first comment, in the platform's present name"""
    lines = []
    for l in src.split("\n"):
        t = l.strip()
        if t.startswith("load "): continue
        if t.startswith("#"): lines.append(t.lstrip("#").strip()); continue
        if not t and not lines: continue
        break
    text = " ".join(x for x in lines if x and not set(x) <= set("-=~#*"))
    return haro.rename(text)[0][:240]

def main():
    if len(sys.argv) < 2: print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    gdir = lib / "base" / "test" / "graphics"
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    names = sorted(p.stem for p in gdir.glob("*.png") if (gdir / f"{p.stem}.ring").exists())
    only = [a for a in sys.argv[2:] if not a.startswith("--")]
    prev = json.loads((ROOT / "data" / "gallery-run.json").read_text(encoding="utf-8")) if (only and (ROOT / "data" / "gallery-run.json").exists()) else {"pictures": {}}
    if only: names = [n for n in names if n in only]
    work = lib / "base" / "test" / "_stzsite_gallery"
    dest = ROOT / "assets" / "img" / "gallery"; dest.mkdir(parents=True, exist_ok=True)
    if not only:
        for old in dest.glob("*.webp"): old.unlink()
    out, t_all = dict(prev["pictures"]), datetime.datetime.now()
    try:
        for n in names:
            work.mkdir(parents=True, exist_ok=True)
            for f in work.glob("*"): f.unlink()
            src = (gdir / f"{n}.ring").read_text(encoding="utf-8", errors="replace").replace("\r", "")
            (work / f"{n}.ring").write_text(src, encoding="utf-8")
            respelt = migrated(work, n)
            t0 = time.time(); status = "ran"; stdout = ""
            try:
                p = subprocess.run(RNXC + [f"{n}.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
                stdout = (p.stdout or "") + "\n" + (p.stderr or "")
                if p.returncode != 0 and not (work / f"{n}.png").exists(): status = "failed"
            except subprocess.TimeoutExpired:
                status = "timed out"
            sec = round(time.time() - t0, 1)
            png = work / f"{n}.png"; committed = (gdir / f"{n}.png").read_bytes()
            said = [l.strip() for l in (stdout or "").splitlines() if l.strip()]
            rec = {"note": (said[-1][:160] if said else ""), "caption": caption(src), "seconds": sec, "status": status, "committed_bytes": len(committed), "source": f"base/test/graphics/{n}.ring"}
            if respelt: rec["respelt"] = respelt          # the names the copy spelt $name (Rule A), as rnxc migrate listed them
            if png.exists():
                fresh = png.read_bytes()
                rec.update(rendered=True, bytes=len(fresh), identical=hashlib.sha256(fresh).digest() == hashlib.sha256(committed).digest())
                im = Image.open(png).convert("RGB"); rec["size"] = list(im.size)
                if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
                im.save(dest / f"{n}.webp", "WEBP", quality=82)
            else:
                rec.update(rendered=False)
                im = Image.open(gdir / f"{n}.png").convert("RGB"); rec["size"] = list(im.size)       # the committed picture is shown, and said to be the committed one
                if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
                im.save(dest / f"{n}.webp", "WEBP", quality=82)
            out[n] = rec
            print(f"{n:28} {status:9} {sec:6.1f}s  {'identical' if rec.get('identical') else ('differs' if rec.get('rendered') else 'not rendered')}", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    (ROOT / "data" / "gallery-run.json").write_text(json.dumps({"commit": commit, "ran": t_all.strftime("%Y-%m-%d %H:%M"), "pictures": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    ident = sum(1 for r in out.values() if r.get("identical")); print(f"{len(out)} pictures, {ident} identical to the committed one, in {(datetime.datetime.now() - t_all).total_seconds():.0f} s at {commit}")

if __name__ == "__main__":
    main()
