#!/usr/bin/env python3
"""One small example for each extension of a method name, run inside the library.

The reference page lists the extensions the library documents (tools/qforms.py). Each one is
shown with an example whose called name carries the extension, the extension's letters
highlighted. The library's tests rarely hold a short, self-contained call for each, so these are
composed from the usage the library itself documents (its tests, narrations and descriptions) with
real method names, and every one is RUN here, in one process inside the library; the output shown
is that run's, and an example that raises is reported, never shown as working.

    python tools/ext_examples_run.py <path to libraries/stzlib>
"""
import json, re, sys, pathlib, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "ext-examples.json"

# extension -> (the extended name called in the code, the code)
EXAMPLES = {
 "Q":      ("UppercaseQ",    '? Q("softanza").UppercaseQ().Content()'),
 "QQ":     ("WordsQQ",       '? Q("one two three").WordsQ().ClassName()\n? Q("one two three").WordsQQ().ClassName()'),
 "QQQ":    ("SentencesQQQ",  '? Q("It is. It works.").SentencesQ().ClassName()\n? Q("It is. It works.").SentencesQQ().ClassName()\n? Q("It is. It works.").SentencesQQQ().ClassName()'),
 "QC":     ("RemoveQC",      'o1 = new stzString("softanza")\n? o1.RemoveQC("a").Content()\n? o1.Content()'),
 "QRT":    ("MultiplesUntilQRT", '? Q(25).MultiplesUntilQRT(100, :stzListOfNumbers).ClassName()'),
 "CS":     ("ContainsCS",    '? Q("Softanza").ContainsCS("SOFT", FALSE)'),
 "ST":     ("FindFirstST",   '? Q("banana").FindFirstST("a", :StartingAt = 3)'),
 "IB":     ("RemoveBetweenIB", 'o1 = new stzString("a[b]c")\no1.RemoveBetweenIB("[", "]")\n? o1.Content()'),
 "D":      ("FindD",         '? @@( Q("banana").FindD("a", :Backward) )'),
 "XT":     ("TypesXT",       '? @@( Q([ "AB", 12, [ "A", "B" ] ]).TypesXT() )'),
 "XTT":    ("DiffXTT",       '? @@( StzListQ([ "a", "b" ]).DiffXTT([ "b", "c" ]) )'),
 "Z":      ("FindZ",         '? @@( Q("banana").FindZ("an") )'),
 "ZZ":     ("FindZZ",        '? @@( Q("banana").FindZZ("an") )'),
 "W":      ("ItemsW",        '? @@( StzListQ([ 12, 0, 30, -5, 18 ]).ItemsW("@item > 0") )'),
 "WF":     ("FindWF",        'o1 = new stzList([ 1, "a", 2, "b", 3, "c" ])\n? @@( o1.FindWF( func x { return isString(x) } ) )'),
 "F":      ("CheckWF",       'o1 = new stzList([ 1:3, 1:3, 1:3 ])\n? o1.CheckWF( func x { return isList(x) and len(x) = 3 } )'),
 "Many":   ("MultiplyByMany", 'o1 = new stzNumber(11)\no1.MultiplyByMany([ 2, 3 ])\n? o1.Value()'),
 "Except": ("RemoveAllExcept", 'o1 = new stzString("s-o-f-t")\no1.RemoveAllExcept("-")\n? o1.Content()'),
 "U":      ("ContentU",      '? @@( StzListQ([ 1, 2, 2, 3, 1 ]).ContentU() )'),
}

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    work = lib / "base" / "test" / "_stzsite_ext"
    work.mkdir(parents=True, exist_ok=True)
    lines = ['load "../../../max/stzMax.ring"', ""]
    for i, (ext, (name, code)) in enumerate(EXAMPLES.items()):
        lines += [f'? "@@BEGIN {i}"', "try"] + code.split("\n") + ["catch", '    ? "@@ERROR " + cCatchError', "done", f'? "@@END {i}"', ""]
    (work / "ext.ring").write_text("\n".join(lines) + "\n", encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", "ext.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    res = {"ran": t0.strftime("%Y-%m-%d %H:%M"), "examples": {}}
    bad = []
    for i, (ext, (name, code)) in enumerate(EXAMPLES.items()):
        m = re.search(rf"@@BEGIN {i}\n(.*?)\n?@@END {i}", out, re.S)
        text = m.group(1).rstrip() if m else ""
        err = text.split("@@ERROR ", 1)[1].strip() if "@@ERROR" in text else ("did not run" if not m else "")
        res["examples"][ext] = {"name": name, "code": code, "out": "" if err else text, "error": err}
        if err: bad.append((ext, err))
        print(f"{ext:7} {name:18} -> {('ERROR ' + err[:70]) if err else repr(text[:70])}")
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(EXAMPLES) - len(bad)} of {len(EXAMPLES)} ran -> data/ext-examples.json")

if __name__ == "__main__":
    main()
