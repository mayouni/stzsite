#!/usr/bin/env python3
"""Run the library's narrations, block after block, and record what each block printed.

A narration is a story told in code: each block builds on the ones before it.
So each narration runs in ONE process, its blocks in order, each in its own try
block, the way a reader meets them. A block is judged against its own promise:
the `#-->` lines it carries, or else the output block that follows it in the
document. The code is RUN in Haro's name (ruled by the author 2026-10-07): the
article is renamed by tools/haro.py, the name and nothing else, before it runs,
so what the page shows is what ran. A narration is not run when its code
touches files, input, the network, the clock or chance; the reason is
recorded, and the article is published all the same: the run is a note on the
page, never a gate (B36). One narration at a time; the temporary folder created
in the library is removed at the end.

    python tools/narrations_run.py <path to libraries/stzlib>
    python tools/narrations_run.py <path to libraries/stzlib> --images   # host their pictures
    python tools/narrations_run.py <path to libraries/stzlib> --only=a.md,b.md   # re-run those, keep the others' records
"""
import json, re, sys, pathlib, subprocess, datetime, shutil
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from showcase_run import verdict
from harvest_examples import parse, FORBIDDEN
import haro

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "narrations-run.json"
FENCE = re.compile(r"(?ms)^```([\w+-]*)[^\n]*\n(.*?)^```[ \t]*$")
CODE_TAGS = ("ring", "softanza")

def dedent_fences(text):
    """a fence indented under a list item is still the article's code: bring it to the margin, so the run and the page both see it
    (five articles wrote their code that way, and until 2026-10-08 it was neither run nor shown as code)"""
    out, ind = [], None
    for l in text.split("\n"):
        if ind is None:
            m = re.match(r"([ \t]*)```", l)
            if m: ind = m.group(1)
            out.append(l[len(ind):] if m else l)
        else:
            closing = l.strip().startswith("```")
            out.append(l.strip() if closing else l[len(ind):] if l.startswith(ind) else l.lstrip(" \t"))
            if closing: ind = None
    return "\n".join(out)

def blocks_of(text):
    fences = [(m.group(1).lower(), m.group(2), m.start(), m.end()) for m in FENCE.finditer(text)]
    out = []
    for k, (tag, body, s, e) in enumerate(fences):
        if tag not in CODE_TAGS: continue
        # narrations also write the promise marker with a space, `# -->`, or as `// -->`
        code, promises = parse(re.sub(r"(#|//)[ \t]*-->", "#-->", body))
        promise = "\n".join(promises)
        if not promise and k + 1 < len(fences) and fences[k + 1][0] == "" and not text[e:fences[k + 1][2]].strip():
            promise = fences[k + 1][1].rstrip("\n")        # the output block right under the code
        # a promise written on a line that prints nothing (`Lx(...).Match(x) #--> TRUE`) cannot be checked
        unprinted = sum(1 for l in body.split("\n") if re.search(r"(#|//)[ \t]*-->", l) and not re.match(r"[ \t]*(\?|#|//)", l))
        out.append({"code": code, "promise": promise, "unprinted": unprinted})
    return fences, out

IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s:]+)\)")

def copy_images(lib):
    """The pictures of the narrations that ran, hosted by the site so its pages open with no network."""
    from PIL import Image
    from build_narration_pages import publishable          # only the narrations the site publishes
    result = json.loads(OUT.read_text(encoding="utf-8"))
    dest = ROOT / "assets" / "img" / "narrations"
    if dest.exists():
        for old in dest.glob("*.webp"): old.unlink()
    dest.mkdir(parents=True, exist_ok=True)
    n = 0
    for rec in result.values():                            # every article is a page now, so every picture is hosted
        for target in IMAGE.findall(rec.get("text", "")):
            src = (lib / "base" / "doc" / "narrations" / target).resolve()
            if not src.is_file(): continue
            im = Image.open(src).convert("RGB")
            if im.width > 1400:
                im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
            im.save(dest / (src.stem + ".webp"), "WEBP", quality=82); n += 1
    print(f"{n} pictures -> assets/img/narrations/")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if "--images" in sys.argv[2:]:
        copy_images(lib); return
    only = next((a.split("=", 1)[1].split(",") for a in sys.argv[2:] if a.startswith("--only=")), None)
    work = lib / "base" / "test" / "_stzsite_narrations"
    work.mkdir(parents=True, exist_ok=True)
    result = json.loads(OUT.read_text(encoding="utf-8")) if only else {}     # --only=a.md,b.md re-runs those and keeps the rest
    t_all = datetime.datetime.now()
    commit = subprocess.run(["git", "-C", str(lib.parent.parent), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    try:
        for f in sorted((lib / "base" / "doc" / "narrations").glob("*.md")):
            if only and f.name not in only: continue
            text = f.read_text(encoding="utf-8", errors="replace").replace("\r", "")
            original = text
            text, renamed = haro.rename(text)
            haro.audit(original, text, f.name)
            text = dedent_fences(text)
            fences, blocks = blocks_of(text)
            hm = next((l[2:].strip() for l in text.split("\n") if l.startswith("# ")), f.stem)
            rec = {"blocks": [], "status": "", "reason": "", "title": hm, "text": text, "renamed": renamed, "commit": commit}
            result[f.name] = rec
            if not blocks:
                rec.update(status="no code"); continue
            allcode = "\n".join(l for b in blocks for l in b["code"])
            if FORBIDDEN.search(allcode) or re.search(r"(?i)\b(give|getchar)\b", allcode):
                rec.update(status="not run", reason="effects"); continue
            # the max entry loads base first, then the max layer (walkers, big numbers...), which narrations use
            main_lines, tail = ['load "../../../max/stzMax.ring"', ""], []
            for i, b in enumerate(blocks):
                code = b["code"]
                cut = next((j for j, l in enumerate(code) if re.match(r"(?i)\s*(func|class)\s+\w", l)), None)
                body, defs = (code[:cut], code[cut:]) if cut is not None else (code, [])
                tail += defs
                main_lines += [f'? "@@BEGIN {i}"', "try"] + body + ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
            script = work / "narration.ring"
            script.write_text("\n".join(main_lines + [""] + tail) + "\n", encoding="utf-8")
            t0 = datetime.datetime.now()
            try:
                p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
                out = (p.stdout or "").replace("\r", "")
            except subprocess.TimeoutExpired as e:
                out = (e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")).replace("\r", "")
            if "@@BEGIN 0" not in out:
                rec.update(status="not run", reason="does not compile"); continue
            for i, b in enumerate(blocks):
                m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
                if not m:
                    rec["blocks"].append({"verdict": "stopped", "out": ""}); continue
                text_out = m.group(1).rstrip()
                if "@@ERROR" in text_out:
                    text_out = text_out.replace("@@ERROR ", "")
                    # a refusal the block promises is the block keeping its promise
                    refusal = re.sub(r"(?im)^[ \t]*(raises|error)[ \t]*:?[ \t]*", "", b["promise"])   # `--> raises: ...`
                    v = "kept" if b["promise"] and verdict("", text_out, refusal) else "raised"
                    if v == "raised" and b["promise"] and re.sub(r"\s+", " ", refusal).strip().lower()[:40] in re.sub(r"\s+", " ", text_out).lower():
                        v = "kept"
                elif b["promise"]:
                    v = "kept" if verdict("\n".join(b["code"]), text_out, b["promise"]) else "differs"
                else:
                    v = "unprinted" if b["unprinted"] else "ran"
                rec["blocks"].append({"verdict": v, "out": text_out})
            rec.update(status="run", ran=t0.strftime("%Y-%m-%d %H:%M"), seconds=round((datetime.datetime.now() - t0).total_seconds(), 1), text=text)
            c = {k: sum(1 for b in rec["blocks"] if b["verdict"] == k) for k in ("kept", "differs", "raised", "ran", "unprinted", "stopped")}
            print(f"{f.name}: {c}", flush=True)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    st = {}
    for r in result.values(): st[r["status"] + (":" + r["reason"] if r["reason"] else "")] = st.get(r["status"] + (":" + r["reason"] if r["reason"] else ""), 0) + 1
    print(st, f"in {(datetime.datetime.now() - t_all).total_seconds():.0f} s -> data/narrations-run.json")

if __name__ == "__main__":
    main()
