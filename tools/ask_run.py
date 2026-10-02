#!/usr/bin/env python3
"""Ask the library the questions its own recipes answer, and record what it says.

Every Softanza object answers Ask(question), HowTo(intent) and ExplainMethod(name)
from the doc-comments of its class (base/meta/stzSelfDoc.ring), with no model
loaded: deterministic, and the same text the reference shows. The 28 recipes the
site publishes (data/howto-run.json) each state an intent and name the methods
that do it; so each intent is asked, word for word, of the class the recipe uses,
and the answer is compared with the recipe's methods: the same method, the same
verb in another form, or neither. A few answers are also kept whole, for the page
to show. One process, inside the library; the temporary folder is removed.

    python tools/ask_run.py <path to libraries/stzlib>
    python tools/ask_run.py --regrade      # grade the stored answers again, without asking
"""
import json, re, sys, pathlib, subprocess, datetime, shutil, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "ask-run.json"
SUFFIX = re.compile(r"(?:CS|Q|XT|XTT|Z|ZZ|W|WF|WXT|IB|B|ST|QC)+$")

# answers kept whole, for the page: [call, class, argument]
SHOWN = [("Ask", "stzList", "remove duplicates"), ("HowTo", "stzString", "replace one word with another"),
         ("ExplainMethod", "stzList", "RemoveDuplicates"), ("Ask", "stzText", "what is the mood of this text")]

def ring_str(s): return '"' + s.replace('"', "'") + '"'

def base(name): return (SUFFIX.sub("", name) or name).lower()

def same_verb(a, b):
    """two forms of one verb: Reverse / Reversed, Trim / Trimmed, Repeat / RepeatQ"""
    a, b = base(a), base(b)
    forms = lambda x: {x, x + "d", x + "ed", x + x[-1:] + "ed"}
    return a == b or b in forms(a) or a in forms(b)

def proposed(howto):
    """the method a HowTo answer proposes: the last call of its template, Q("...").TextQ().Sentiment() -> Sentiment"""
    template = howto.split("   --")[0]
    calls = re.findall(r"\.(\w+)\(", template) or re.findall(r"(\w+)\(", template)
    return calls[-1] if calls else ""

def grade(q):
    """the same method the recipe names, the same verb in another form, or another method"""
    def g(name):
        if not name: return "none"
        if name.lower() in {x.lower() for x in q["methods"]}: return "same"
        if any(same_verb(name, x) for x in q["methods"]): return "verb"
        return "other"
    q["howto_method"] = proposed(q.get("howto", ""))
    q["howto_grade"] = g(q["howto_method"])
    gs = [g(a) for a in q.get("ask", [])]
    q["ask_grade"] = "same" if "same" in gs else "verb" if "verb" in gs else ("other" if gs else "none")
    q["ask_first"] = gs[0] if gs else "none"

def report(qs, seconds):
    c = lambda key, g: sum(1 for q in qs if q.get(key) == g)
    print(f"{len(qs)} questions in {seconds} s: HowTo same {c('howto_grade','same')} verb {c('howto_grade','verb')} other {c('howto_grade','other')} none {c('howto_grade','none')}"
          f" | Ask top-3 same {c('ask_grade','same')} verb {c('ask_grade','verb')} | errors {sum(1 for q in qs if q.get('error'))} -> data/ask-run.json")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    if sys.argv[1] == "--regrade":                     # grade the stored answers again, without asking the library
        res = json.loads(OUT.read_text(encoding="utf-8"))
        for q in res["questions"]:
            if not q.get("error"): grade(q)
        OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        report(res["questions"], res["seconds"]); return
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    recipes = [r for r in json.loads((ROOT / "data" / "howto-run.json").read_text(encoding="utf-8")).values()
               if r["status"] == "run" and all(p["verdict"] in ("kept", "ran") for p in r["parts"])]
    qs = []
    for r in recipes:
        cls = collections.Counter(m.split(".")[0] for m in r["methods"] if "." in m).most_common(1)[0][0]
        qs.append({"file": r["file"], "intent": r["intent"], "class": cls, "methods": [m.split(".", 1)[1] for m in r["methods"] if m.startswith(cls + ".")]})
    work = lib / "base" / "test" / "_stzsite_ask"
    work.mkdir(parents=True, exist_ok=True)
    lines = ['load "../../../max/stzMax.ring"', "", "aDocs = []", "func Sd(c)",
             "    for i = 1 to len(aDocs)", "        if aDocs[i][1] = c return aDocs[i][2] ok", "    next",
             "    o = StzSelfDocQ(c)", "    aDocs + [ c, o ]", "    return o", ""]
    body = []
    for i, q in enumerate(qs):
        body += [f'? "@@Q {i}"', "try", f"    oS = Sd({ring_str(q['class'])})",
                 f'    ? "@@HOWTO"', f"    ? oS.HowTo({ring_str(q['intent'])})",
                 f'    ? "@@ASK"', f"    aR = oS.Ask({ring_str(q['intent'])})",
                 "    for k = 1 to len(aR) ? aR[k][1] next",
                 "catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"']
    for j, (call, cls, arg) in enumerate(SHOWN):
        body += [f'? "@@S {j}"', "try", f"    oS = Sd({ring_str(cls)})"]
        if call == "Ask":
            body += [f"    aR = oS.Ask({ring_str(arg)})", "    for k = 1 to len(aR)",
                     '        ? aR[k][1] + "  " + aR[k][2] + "  " + aR[k][3]', "    next"]
        else:
            body += [f"    ? oS.{call}({ring_str(arg)})"]
        body += ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@SEND {j}"']
    # the helper function must follow the main code in a script
    script = work / "ask.ring"
    script.write_text("\n".join(lines[:3] + body + [""] + lines[3:]) + "\n", encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", script.name], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=900)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    seconds = round((datetime.datetime.now() - t0).total_seconds(), 1)
    for i, q in enumerate(qs):
        m = re.search(rf"@@Q {i}\n(.*?)\n?@@END {i}\n", out + "\n", re.S)
        txt = m.group(1) if m else ""
        if not m or "@@ERROR" in txt:
            q.update(error=(txt.split("@@ERROR ", 1)[1].strip() if "@@ERROR" in txt else "no answer")); continue
        howto = txt.split("@@HOWTO\n", 1)[1].split("\n@@ASK", 1)[0].strip()
        ask = [l.strip() for l in txt.split("@@ASK\n", 1)[1].split("\n") if l.strip()] if "@@ASK\n" in txt else []
        q.update(howto=howto, ask=ask)
        grade(q)
    shown = []
    for j, (call, cls, arg) in enumerate(SHOWN):
        m = re.search(rf"@@S {j}\n(.*?)\n?@@SEND {j}", out, re.S)
        shown.append({"call": call, "class": cls, "arg": arg, "out": (m.group(1).strip() if m else "").replace("@@ERROR ", "")})
    res = {"ran": t0.strftime("%Y-%m-%d %H:%M"), "seconds": seconds, "questions": qs, "shown": shown}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    report(qs, seconds)

if __name__ == "__main__":
    main()
