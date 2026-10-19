"""What the site holds about an area or a class, printed as a digest to write from.

    python tools/digest.py area <slug> [<slug>...]
    python tools/digest.py class <Class> [<Class>...]
"""
import json, pathlib, sys, re, textwrap
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
def J(name, default=None):
    f = DATA / name
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else default
def w(s, n=150): return textwrap.shorten(re.sub(r"\s+", " ", str(s)), n, placeholder=" ...")

def area(slug):
    idx = {g["slug"]: g for g in J("atlas-index.json")["groups"]}
    g = idx[slug]; d = J(f"atlas/{slug}.json", {}); c = J(f"atlas-compass/{slug}.json", {}); h = J("heritage.json", {}).get(slug, {})
    print(f"\n===== {slug} | {g['en']} | {g['line_en']} | dirs {g['dirs']} | peers {g['peers']}")
    print("THESIS:", c.get("thesis") or d.get("thesis"))
    for n in c.get("notes", []): print("NOTE:", (n.get("lead") or ""), w(n.get("text"), 400))
    print("STANDOUTS:", " | ".join(d.get("standouts", []))); print("GAPS:", " | ".join(d.get("gaps", [])))
    for l in c.get("lanes") or d.get("lanes", []):
        print(f"  LANE {l.get('n','')} {l['lane']} [{l['rating']}] :: {w(l.get('engine') or l.get('note'), 260)} || owed: {w(l.get('owed',''), 160)}")
    for t in c.get("tiers", []): print("  TIER", t["tier"], "|", " ; ".join(f"{i['title']} (v {i.get('value')}, e {i.get('effort')})" for i in t["items"]))
    print("PRINCIPLE:", h.get("principle_en"))
    for k in h.get("kept", []): print("  KEPT:", k["en"], "<", k.get("source"))
    for k in h.get("rethought", []): print("  RETHOUGHT:", k["en"], f"[{k.get('stage')}]", "<", k.get("source"))
    for it in J("showcase.json", {}).get(slug, []): print("  RUN:", it["what_en"], "::", w(it["code"], 160), "=>", w(it["out"], 80))
    dd = J("designdocs.json", {}); ab = J("designdocs-abstracts.json", {})
    for pth in dd.get("areas", {}).get(slug, []):
        x = dd["docs"].get(pth, {}); print("  DOC:", x.get("title"), f"({x.get('lines')} lines, {x.get('first')})", "::", ab.get(pth, {}).get("en", ""))
        print("       outline:", " / ".join(x.get("outline", [])[:10]))
    meta = J("narrations-meta.json", {}).get("articles", {})
    for f, m in meta.items():
        if m.get("area") == slug: print("  ARTICLE:", m.get("title"), f"({m.get('year')}, {m.get('genre')})", "::", w(m.get("abstract"), 200))

def klass(name):
    r = J("reference.json"); c = next(x for x in r["classes"] if x["name"].lower() == name.lower())
    print(f"\n===== {c['name']} | area {c['area']} | {c['file']} | {len(c['own'])} own methods | inherits {c.get('inherited')}")
    secs = c.get("sections", {})
    names = [m[0] for m in c["own"]]
    print("METHODS:", ", ".join(names[:220]))
    # the examples that call this class, from the library's tests (examples.json) and the rows run for the pages (row-examples.json)
    shown = 0
    for ex in J("examples.json", []):
        if any(cl.lower() == c["name"].lower() for cl, _ in ex.get("methods", [])) and shown < 30:
            print("  EX", ",".join(m for _, m in ex["methods"][:4]), "::", w(ex["code"], 220), "=>", w(ex.get("out", ""), 120)); shown += 1
    rows = J("row-examples.json", {}).get("examples", {}).get(c["name"], {})
    for i, (m, v) in enumerate(rows.items()):
        if i >= 25: break
        print("  ROW", m, "::", w(v.get("setup", ""), 90), "|", w(v.get("code", ""), 120), "=>", w(v.get("out", ""), 100))
    for m in c["own"][:70]:
        if m[2]: print("  DESC", m[0], "::", w(m[2], 160))

if __name__ == "__main__":
    kind, *items = sys.argv[1:]
    for it in items: (area if kind == "area" else klass)(it)
