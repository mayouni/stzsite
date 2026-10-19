"""The library's design documents, read for the site: one record per document, and the areas each one belongs to.

    python tools/designdocs_run.py <path to libraries/stzlib>   -> data/designdocs.json

A document is a plan of record, a design or a study the library wrote about one of its areas. Each record keeps the
title, the first paragraph as its abstract, the outline (the second-level headings), the size, the first and last
commit dates, and the classes it names (so a class page can list the documents that speak of it). The mapping from
an area to its documents is written by hand below, from the documents' own subjects; a document may serve two areas.
"""
import json, pathlib, re, subprocess, sys, collections

LIB = pathlib.Path(sys.argv[1]).resolve()
BASE = LIB / "base"
ROOT = pathlib.Path(__file__).resolve().parent.parent

AREAS = {
    "string": ["doc/design/STRING_ENGINE_DESIGN_v2.md", "doc/design/STZSTRING_DECOMPOSITION.md"],
    "regex": [],
    "collections": ["list/_ENGINE_RESIDENCY_PLAN.md"],
    "numeric": ["doc/design/SOFTANZA_NUMERIC_FOUNDATION.md", "doc/design/SOFTANZA_NUMBER_ENGINE_PLAN.md", "math/CHARTER.md", "math/SOFTANZA_MATH_PLAN.md"],
    "tables": [],
    "i18n": ["culture/SOFTANZA_CULTURE_PLAN.md"],
    "nlp": ["doc/design/NATURAL_VISION.md", "doc/design/NNL_REVIEW.md"],
    "neural": ["neural/SOFTANZA_STRUCTURED_OUTPUT.md"],
    "agents": ["doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md", "doc/design/Softaza and Agents That Cannot Hurt You.md"],
    "graphics": ["graphics/SOFTANZA_GRAPHICS_PLAN.md", "graphics/SOFTANZA_COLOR_SYSTEM.md", "graphics/SOFTANZA_VISION_PLAN.md"],
    "geo": ["graphics/SOFTANZA_GRAPHICS_PLAN.md"],
    "diagramming": ["graphics/SOFTANZA_GRAPH_PLANE_PLAN.md", "doc/design/stzGraph-A-Design-Foundation-for-Connected-Domains.md", "doc/design/SOFTANZA_GRAPH_RULES_PLAN.md"],
    "gpu": ["gpu/SOFTANZA_GPU_PLAN.md"],
    "gui": ["gui/SOFTANZA_GUI_PLAN.md", "doc/design/REACTIVE_ENGINE_GAP_ANALYSIS.md", "doc/design/NEXT_SESSION_PROMPT.md",
            "doc/design/STZAPP_DESIGN.md", "doc/design/STZAPP_BODY_DESIGN.md", "doc/design/STZAPP_PURPOSE_DESIGN.md", "doc/design/STZAPP_STATUS_AND_NEXT.md", "doc/design/STZSUPERAPP_DESIGN.md"],
    "stats": ["stats/SOFTANZA_TUKEY_PLAN.md"],
    "system": ["doc/design/SOFTANZA_SYSTEM_FOUNDATION.md", "doc/design/SOFTANZA_DELIVERY_PLANE.md", "doc/design/SOFTANZA_DEPLOYMENT.md", "doc/design/SOFTANZA_DEPLOYMENT_PLAN.md",
               "doc/design/SOFTANZA_EMULATION.md", "doc/design/Softanza Virtual System Framework.md", "doc/design/TIER2_REACTOR_DIRECTION.md", "doc/design/SOFTANZA_CLI_DESIGN.md", "doc/design/SOFTANZA_LOGGING.md"],
    "concurrency": ["concurrent/SOFTANZA_CONCURRENT_PLAN.md", "cluster/SOFTANZA_DISTRIBUTION_PLAN.md", "doc/design/MTLS_PLAN.md"],
    "web": ["doc/design/SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md", "doc/design/SOFTANZA_AUTH_PLAN.md", "service/SOFTANZA_PAYMENTS_PORT.md"],
    "performance": ["doc/design/SOFTANZA_PERF_SYSTEM.md", "doc/design/SOFTANZA_PERF_VS_THE_FIELD.md", "doc/design/SOFTANZA_INCIDENT_ANALYSIS.md", "doc/design/SOFTANZA_INCIDENT_VS_THE_FIELD.md"],
    "meta": ["doc/design/SOFTANZA_GRAPH_RULES_PLAN.md", "doc/design/SCOPE_ORIENTED_PROGRAMMING.md", "doc/design/stz-information-tagging-strategy.md"],
    "files": [],
    "binary": ["binary/SOFTANZA_BINARY_PLAN.md"],
    "security": ["doc/design/SOFTANZA_SECURITY.md", "security/SOFTANZA_THREAT_MODEL.md", "doc/design/SOFTANZA_SECRETS.md", "doc/design/SOFTANZA_AUTH_PLAN.md",
                 "doc/design/MTLS_PLAN.md", "security/SOFTANZA_CRA_RUNBOOK.md", "doc/design/EXTERNAL_DEPENDENCY_AUDIT.md"],
    "extensibility": ["plugin/SOFTANZA_PLUGIN_PLAN.md", "plugin/SOFTANZA_PLUGIN_COMPARATIVE_STUDY.md", "doc/design/stzextertool-design-article.md", "doc/design/stzCloudtool-Design-Article.md"],
    "sound": ["sound/SOFTANZA_SOUND_PLAN.md", "sound/SOFTANZA_MUSIC_PLAN.md", "sound/SOFTANZA_VOICE_PLAN.md"],
    "testing": ["testoor/SOFTANZA_TESTOOR_PLAN.md"],
    "documentation": ["doc/design/DOCREFORM_PROPOSAL.md", "doc/design/DOCREFORM_PILOT_STATE.md", "doc/DOCBLOCK.md", "doc/stz-doc-system-overview.md", "doc/design/SOFTANZA_THROUGH_CLAUDES_EYES.md"],
    "governance": ["doc/design/Softaza and Agents That Cannot Hurt You.md", "doc/design/SOFTANZA_GRAPH_RULES_PLAN.md", "doc/design/SOFTANZA_SECURITY.md"],
}

def git(*args):
    return subprocess.run(["git", *args], cwd=LIB, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()

def record(rel):
    p = BASE / rel
    s = p.read_text(encoding="utf-8", errors="replace")
    lines = s.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), rel)
    # the abstract: the first paragraph of prose after the title (not a status line, not a table, not a heading)
    abstract = ""; fallback = ""; buf = []
    started = False
    def close():
        nonlocal abstract, fallback, buf
        para = " ".join(buf); buf = []
        low = para.lower()
        if len(para) < 120 or low.startswith(("status", "supersedes", "run in", "precondition", "|", "author", "written 20", "> ")): return
        if para.endswith(":"):
            if not fallback: fallback = para[:-1] + "."
            return
        abstract = para
    for l in lines:
        if abstract: break
        if l.startswith("# "): started = True; continue
        if not started: continue
        t = l.strip()
        if not t or t.startswith(("#", "|", "```", "- ", "* ", ">", "---")) or re.match(r"^\d+\.", t):
            if buf: close()
            continue
        buf.append(t)
    if buf and not abstract: close()
    abstract = abstract or fallback
    abstract = re.sub(r"\*\*|__|`", "", abstract)
    abstract = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", abstract)
    h2 = [re.sub(r"\s*\{#.*\}$", "", l[3:].strip()) for l in lines if l.startswith("## ")]
    rel_lib = (p.relative_to(LIB)).as_posix()
    first = git("log", "--diff-filter=A", "--format=%ad", "--date=short", "--follow", "--", rel_lib).splitlines()
    last = git("log", "-1", "--format=%ad", "--date=short", "--", rel_lib)
    classes = collections.Counter(m for m in re.findall(r"\bstz[A-Z]\w+", s))
    return {"path": "base/" + rel, "title": title, "abstract": abstract, "outline": h2[:14], "sections": len(h2), "lines": len(lines),
            "first": first[-1] if first else None, "last": last or None,
            "classes": {k: v for k, v in classes.most_common(40) if v >= 2}}

docs = {}
for slug, rels in AREAS.items():
    for rel in rels:
        assert (BASE / rel).exists(), rel
        if rel not in docs: docs[rel] = record(rel)
out = {"read_at": git("rev-parse", "--short", "HEAD"), "docs": {("base/" + k): v for k, v in docs.items()},
       "areas": {slug: ["base/" + r for r in rels] for slug, rels in AREAS.items()}}
(ROOT / "data" / "designdocs.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print(len(docs), "documents;", sum(1 for v in docs.values() if not v["abstract"]), "without an abstract;",
      sum(1 for v in docs.values() if not v["first"]), "without a first date")
for k, v in docs.items():
    if not v["abstract"]: print("  no abstract:", k)
