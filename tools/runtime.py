#!/usr/bin/env python3
"""The runtime every example on this site runs on: Ring++'s `rnxc` (the author retired the former runtime, RING-RETIRED-01,
2026-10-23; the library's main branch runs on it since 2026-10-29). One place, so the eighteen runners cannot disagree.

    RNXC     the command, as a list to put in front of a script's name, found in this order:
             the environment variable RNXC; this machine's local path file (.central/PATHS.local.md, its %RINGPP% line,
             never published); `rnxc` on the path.

The runtime runs a file as the former one did (`rnxc file.ring`), prints the program's output on stdout and nothing of its own,
and finds the library's engine inside its own package when the library folder has none built for it.
"""
import os, re, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXE = "rnxc.exe" if os.name == "nt" else "rnxc"


def find():
    """the rnxc to run, as a path string"""
    v = os.environ.get("RNXC", "").strip()
    if v:
        return v
    local = ROOT / ".central" / "PATHS.local.md"
    if local.exists():
        m = re.search(r"%RINGPP%\s*=\s*(\S[^\r\n]*)", local.read_text(encoding="utf-8", errors="replace"))
        if m:
            exe = pathlib.Path(m.group(1).strip()) / "bin" / EXE
            if exe.exists():
                return str(exe)
    return shutil.which("rnxc") or "rnxc"


RNXC = [find()]

if __name__ == "__main__":
    print(RNXC[0])
