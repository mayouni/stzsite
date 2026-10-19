"""Two checks over the built site, run before every commit (it used to live in a temporary folder and vanished):

  - every local link and source in every page resolves to a file of the site;
  - the platform's former language is never named in PROSE (library code is shown as written, so code and pre
    blocks are left out), except on the pages that tell the history (whyring, history, roots) and in the runtime sentence.

    python tools/integrity_check.py        -> "<files> files; <links> local links; <dangling> dangling; <n> files with the word in code"
"""
import pathlib, re, sys, urllib.parse, html, posixpath

ROOT = pathlib.Path(__file__).resolve().parent.parent
HREF = re.compile(r'(?:href|src)="([^"]+)"')
CODE = re.compile(r"<(code|pre)[^>]*>(.*?)</\1>", re.S)
WORD = re.compile(r"\bRing\b")
RUNTIME = re.compile(r"(?:sa face Ring|its Ring face|Ring\+\+ (?:est le pont|is the bridge))")   # the runtime sentence, allowed everywhere

pages = [ROOT / "index.html", ROOT / "deck-check.html", ROOT / "404.html"] + [p for lang in ("en", "fr") for p in (ROOT / lang).rglob("*.html")]
pages = [p for p in pages if p.exists()]
EXISTS = {f.relative_to(ROOT).as_posix() for f in ROOT.rglob("*") if f.is_file() and ".git" not in f.parts}   # one listing, not a million resolve() calls
links = dangling = 0; word_files = []
for p in pages:
    s = p.read_text(encoding="utf-8", errors="replace")
    for m in HREF.finditer(s):
        h = html.unescape(m.group(1))
        if h.startswith(("http://", "https://", "mailto:", "data:", "#", "javascript:")): continue
        h = h.split("#", 1)[0].split("?", 1)[0]
        if not h: continue
        target = posixpath.normpath(posixpath.join(p.parent.relative_to(ROOT).as_posix(), urllib.parse.unquote(h))).replace("\\", "/")
        links += 1
        if target not in EXISTS and not (ROOT / target).is_dir():
            dangling += 1
            if dangling <= 20: print("  dangling:", p.relative_to(ROOT).as_posix(), "->", h)
    if p.stem not in ("whyring", "history", "roots", "glossary"):
        body = s[s.find("<main"):s.rfind("</main>")] if "<main" in s else s
        prose = html.unescape(re.sub("<[^>]+>", " ", CODE.sub(" ", body)))
        prose = RUNTIME.sub(" ", prose)                  # the one sentence allowed everywhere: the runtime, named on purpose
        if WORD.search(prose): word_files.append(p.relative_to(ROOT).as_posix())
for w in word_files[:12]: print("  the word in prose:", w)
print(f"{len(pages)} files; {links} local links; {dangling} dangling; {len(word_files)} files with the word in prose")
sys.exit(1 if dangling or word_files else 0)
