#!/usr/bin/env python3
"""The projects that forged Softanza, run: two lessons shown as code the library runs today.

The page "Forged in projects" says what each project needed and where the library carries the lesson. Two of them can be SHOWN, so
they are run, inside the library at its pinned commit, like every block of this site:

  orgchart   a bank's governance rules (the BCEAO ones) judge an organisation chart: the library carries them as code
  registry   a solution that declares its outside services and binds a fake to one: the registry refuses to call it ready for
             production (the way a payment can be tried without a subscription, and never shipped as a fake)

    python tools/forged_run.py <path to libraries/stzlib>      -> data/forged-run.json
"""
import json, re, sys, pathlib, subprocess, datetime, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "forged-run.json"
NL = chr(10)

SEGMENTS = [
  ("orgchart", NL.join([
    'oOrg = new stzOrgChart("bank")',
    'oOrg.AddPositionXTT("ceo", "Chief Executive", [ :department = "executive" ])',
    'oOrg.AddPositionXTT("audit", "Internal Audit", [ :department = "audit", :reportsTo = "ceo" ])',
    '? @@( oOrg.ValidateBCEAOGovernance() )'])),
  ("registry", NL.join([
    'oReg = new stzServiceRegistry("restolean")',
    'oReg.Declare(:mail)',
    'oReg.Bind(:mail, new stzMailSandbox())',
    'oReg.SetPhase(:production)',
    '? oReg.IsSound()',
    '? @@( oReg.Findings() )'])),
]

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    lib = pathlib.Path(sys.argv[1]).resolve()
    if not (lib / "base" / "meta" / "stzSelfDoc.ring").is_file():
        sys.exit(f"not the library folder: {lib}")
    work = lib / "base" / "test" / "_stzsite_forged"
    work.mkdir(parents=True, exist_ok=True)
    lines = ['load "../../stzBase.ring"', ""]
    for name, code in SEGMENTS: lines += [f'? "@@SEG {name}"', "try", code, "catch", '    ? "@@ERROR " + cCatchError', "done", ""]
    lines.append('? "@@SEG end"')
    (work / "forged.ring").write_text(NL.join(lines) + NL, encoding="utf-8")
    t0 = datetime.datetime.now()
    try:
        p = subprocess.run(["ring", "forged.ring"], cwd=work, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
        out = (p.stdout or "").replace("\r", "")
    finally:
        shutil.rmtree(work, ignore_errors=True)
    parts = re.split(r"@@SEG (\w+)\n", out)
    got = {parts[i]: parts[i + 1].rstrip() for i in range(1, len(parts) - 1, 2)}
    segs = [{"name": n, "code": c, "out": re.sub(r"\n(?:[ \t]*\n)+", "\n\n", got.get(n, ""))} for n, c in SEGMENTS]
    bad = [s["name"] for s in segs if not s["out"] or "@@ERROR" in s["out"] or "Error" in s["out"]]
    OUT.write_text(json.dumps({"ran": t0.strftime("%Y-%m-%d %H:%M"), "commit": "0e72e2e2c", "segments": segs}, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in segs: print(f"-- {s['name']}\n{s['out'][:600]}")
    print(f"{len(segs) - len(bad)} of {len(segs)} segments ran -> data/forged-run.json" + (f"; FAILED: {bad}" if bad else ""))
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
