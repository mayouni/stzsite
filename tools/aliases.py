#!/usr/bin/env python3
"""One name per thing: which classes and which methods are only other names of one.

The author, 2026-10-03: stz2DList is just another name of stzListOfLists, stzList2D too: they are ONE class under several names
for a better programmer experience, so the reference and the whole site list ONE entry; and the same for the alternative names of
methods and functions, which the documentation presents as semantic variations of a root, as it does for the extensions.

This reads the library's sources once and writes data/names.json:

  classes   {alias: root}   a class with nothing in it but its parent (`class stzItems from stzList`, an empty body): the name only
                            says the same thing another way. Followed to the end of the chain.
  methods   {class: {alias lower: root}}   a method whose whole body is `return This.Root(<its own parameters, unchanged>)`: it
                            is the root under another name. Followed to the end of the chain. Only a pure forward counts: a form
                            that adds or changes an argument does something of its own and stays a method.
  detours   {name: natural name}   a spelling the host language forces: IsAString() where IsString() reads right, because the host
                            language (or a global function of the library) already holds IsString. Examples show the natural name.

    python tools/aliases.py <path to libraries/stzlib>     -> data/names.json
"""
import json, re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import qforms

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "names.json"

# the host language's own functions that a method of the form IsX would collide with (read from the host: tools/aliases.py does
# not guess them, the list below was probed by calling each name), and the author's own example
HOST = set("isstring isnumber islist isobject isalpha isdigit islower isupper isspace isalnum ispunct isnull isfunction isunix iswindows "
           "ismacosx islinux isglobal islocal isattribute ismethod ispackage iscfunction isfreebsd isandroid iscntrl isgraph isprint "
           "isxdigit isclass".split())
HAND_DETOURS = {"IsAChar": "IsChar"}                      # the author's own example, 2026-10-03
# what the author ruled, by name (2026-10-03): stzList2D and stz2DList are other names of stzListOfLists, though stzList2D holds a few
# methods of its own (Transpose...) and a stricter constructor: one class on the site, those methods listed with it
HAND_MERGES = {"stzList2D": "stzListOfLists"}
# the name the author wants as the main reference when the library keeps the body under a shorter one: HasMoreCharsThan(3) is
# the sentence, HasMoreChars(3) and HasMoreChars(:Than = 3) are cited as alternatives
MAIN_NAMES = {"stzString": {"HasMoreChars": "HasMoreCharsThan", "HasLessChars": "HasLessCharsThan"}}
# the ways the main name is also called, read from the source (stzString._CharsOf: "unwrap a :Than / :Then named param"): a call that
# gives the number alone, or the number as a named parameter. A hand list until the documentation session's record carries them
FORMS = {"stzString": {"HasMoreCharsThan": ["HasMoreChars(3)", "HasMoreChars(:Than = 3)", "HasMoreChars(:Then = 3)"],
                       "HasLessCharsThan": ["HasLessChars(3)", "HasLessChars(:Than = 3)", "HasLessChars(:Then = 3)"]}}

CLASS = re.compile(r"^\s*class\s+(\w+)(?:\s+from\s+(\w+))?\s*$", re.I)
DEFN = re.compile(r"^(\s*)def\s+(\w+)\s*\(([^)]*)\)\s*$", re.I)
BOUND = re.compile(r"^(class|func)\s", re.I)
FORWARD = re.compile(r"return\s+This\.(\w+)\s*\((.*)\)\s*$", re.I)

def class_aliases(lib):
    """{alias: parent} for every class whose body holds nothing"""
    out = {}
    for f in lib.rglob("*.ring"):
        if "test" in f.parts or "doc" in f.parts: continue
        L = f.read_text(encoding="utf-8", errors="replace").split("\n")
        for i, l in enumerate(L):
            m = CLASS.match(l)
            if not m or not m.group(2): continue
            body = []
            for j in range(i + 1, min(len(L), i + 400)):
                if BOUND.match(L[j]): break
                s = L[j].strip()
                if s and not s.startswith("#"): body.append(s)
            if not body: out[m.group(1)] = m.group(2)
    return out

def forwards(file, cname):
    """{alias lower: target} for the pure forwards of one class's source"""
    L = file.read_text(encoding="utf-8", errors="replace").split("\n")
    start = next((i for i, l in enumerate(L) if re.match(rf"\s*class\s+{re.escape(cname)}\b", l, re.I)), None)
    if start is None: return {}
    end = next((j for j in range(start + 1, len(L)) if BOUND.match(L[j])), len(L))
    out = {}
    for i in range(start + 1, end):
        m = DEFN.match(L[i])
        if not m: continue
        k = i + 1
        while k < end and (not L[k].strip() or L[k].strip().startswith("#")): k += 1
        if k >= end: continue
        fm = FORWARD.match(L[k].strip())
        if not fm: continue
        n = k + 1
        while n < end and not L[n].strip(): n += 1
        if n < end and not re.match(r"^\s*(def|func|class)\s|^\s*#", L[n]): continue        # something else follows: not a pure forward
        params = [p.strip().lower() for p in m.group(3).split(",") if p.strip()]
        args = [a.strip().lower() for a in fm.group(2).split(",") if a.strip()]
        if params == args and fm.group(1).lower() != m.group(2).lower(): out[m.group(2).lower()] = fm.group(1)
    return out

def resolve(table, name, depth=0):
    t = table.get(name.lower())
    return name if t is None or depth > 6 else resolve(table, t, depth + 1)

def build(lib, ref):
    classes = class_aliases(lib)
    known = {c["name"] for c in ref["classes"]}
    chains = dict(classes); chains.update(HAND_MERGES)
    roots = {}
    for a in classes:
        r = a
        for _ in range(6):
            if r in chains: r = chains[r]
            else: break
        if a in known and r in known and r != a: roots[a] = r
    for a, r in HAND_MERGES.items():
        if a in known and r in known: roots[a] = r
    methods, listed_aliases = {}, 0
    for c in ref["classes"]:
        f = lib / "base" / c["file"]
        if not f.exists(): continue
        fw = forwards(f, c["name"])
        table = {a: resolve(fw, t) for a, t in fw.items()}
        if table: methods[c["name"]] = table
    detours = dict(HAND_DETOURS)
    glob = set()
    for f in (lib / "base").rglob("*.ring"):
        if "test" in f.parts: continue
        for m in re.finditer(r"(?im)^func\s+(\w+)", f.read_text(encoding="utf-8", errors="replace")): glob.add(m.group(1).lower())
    for c in ref["classes"]:
        own = {m[0].lower() for m in c["own"]}
        for m in c["own"]:
            mm = re.match(r"^Is(An|A)([A-Z]\w*)$", m[0])
            if not mm: continue
            nat = "Is" + mm.group(2)
            if nat.lower() in own: continue                       # the class has both: not a detour
            if nat.lower() in HOST or nat.lower() in glob: detours[m[0]] = nat
    return {"classes": dict(sorted(roots.items())), "methods": methods, "main": MAIN_NAMES, "forms": FORMS, "detours": dict(sorted(detours.items()))}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    raw = qforms.reference(ROOT, names=False)                 # the reference before any name is folded
    names = build(lib, raw)
    OUT.write_text(json.dumps(names, ensure_ascii=False, indent=1), encoding="utf-8")
    nm = sum(1 for c in raw["classes"] for m in c["own"] if m[0].lower() in names["methods"].get(c["name"], {}))
    print(f"{len(names['classes'])} classes are other names of a class; {nm} of {sum(len(c['own']) for c in raw['classes'])} listed methods are other names of a method; "
          f"{len(names['detours'])} detours -> data/names.json")

if __name__ == "__main__":
    main()
