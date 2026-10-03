"""The extensions of Softanza method names, as the author rules them (2026-10-03).

A method name can end in extensions: Q, CS, XT, Z, ZZ, U, IB, W, ST and the rest. The
author's ruling, first for Q and then for all of them: an extension is a SYNTAX
VARIATION of the same method, never another method. So the site

  - lists a method once: a name that is a method plus one or more extensions is folded
    into that method (FindCS, FindCSZ and FindQ are Find), and each method says which
    extensions exist for it and which do not;
  - shows no example that calls a ...Q() form and then does nothing with the result:
    o1.FilterQ(...) alone on a line is wrong, since o1.Filter(...) does the job. A Q
    call whose result is chained on, assigned, printed, returned or looped over is right.

Only extensions the library documents are folded (EXTENSIONS below, each with its
source: the forms document, stz-functions-as-linguistic-expressions.md, and the library's own
descriptions). A name that ends like an extension but whose ending is not documented stays
listed, and unknown_endings() reports what was left, so that a doubtful ending is named
on the reference page and not guessed. FF (the free form) and the prefixes (@, rnd, viz, Deep...) are generic mechanisms of the forms document, not name suffixes of the reference. S is left: it is used for seconds in ElapsedS and for
a start position in NthStzS, two meanings in six names. X, the statement form, is left: three of
its four endings are unrelated words (IsMacOSX). A name whose base is not a method
(an accessor ending in Q with no plain twin, say) is the method itself and stays.

Passive forms (Removed beside Remove) are not extensions: they do not do the same thing
(Remove changes the object, Removed returns a copy), so they stay listed.
"""
import json, re

# code, what it adds (en), (fr), the library file that documents it
EXTENSIONS = [
    ("Q",   "does what the method does, then returns the object, so the call can be chained",
            "fait ce que fait la méthode, puis rend l'objet, pour que l'appel puisse s'enchaîner",
            "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("QQ",  "chains on the next, more specific type of object (the Q ladder)",
            "enchaîne sur le type d'objet suivant, plus précis (l'échelle des Q)",
            "base/common/stzSmallFuncs.ring"),
    ("QQQ", "chains on the most specific type of object (the Q ladder)",
            "enchaîne sur le type d'objet le plus précis (l'échelle des Q)",
            "base/common/stzSmallFuncs.ring"),
    ("QC",  "chains on a copy, so the original object stays unchanged",
            "enchaîne sur une copie, l'objet d'origine reste inchangé",
            "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("QRT", "returns the result as an object of the requested type",
            "rend le résultat comme un objet du type demandé",
            "base/natural/stzNaturalCode.ring"),
    ("CS",  "takes a case-sensitivity flag",
            "prend un indicateur de sensibilité à la casse",
            "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("ST",  "takes the position to start from (StartingAt)",
            "prend la position de départ (StartingAt)",
            "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("IB",  "takes bounds that are included (IncludingBounds)",
            "prend des bornes incluses (IncludingBounds)",
            "base/reflect/stzReflectFuncs.ring"),
    ("XT",  "the extended form: more parameters than the base method",
            "la forme étendue : plus de paramètres que la méthode de base",
            "base/doc/design/STRING_ENGINE_DESIGN_v2.md"),
    ("XTT", "yet another extension: a further extended form, after XT",
            "encore une extension : une forme étendue de plus, après XT",
            "base/doc/narrations/stzlist-diff.md"),
    ("Z",   "includes the position in what it returns",
            "inclut la position dans ce qu'elle rend",
            "base/doc/quickers/stz-notes-quickers.md"),
    ("ZZ",  "returns positions as sections, [start, end]",
            "rend les positions comme des sections, [début, fin]",
            "base/doc/quickers/stz-notes-quickers.md"),
    ("W",   "selects by a condition",
            "choisit selon une condition",
            "base/reflect/stzReflectFuncs.ring"),
    ("WF",  "selects by a condition, with the expressive keywords (@NextItem, @PreviousItem...)",
            "choisit selon une condition, avec les mots-clés expressifs (@NextItem, @PreviousItem...)",
            "base/reflect/stzReflectFuncs.ring"),
    ("D",   "takes a direction, forward or backward (Directional)",
            "prend une direction, en avant ou en arrière (Directional)",
            "base/string/stzString.ring"),
    ("F",   "takes a function (the condition or the update is given as a function); the forms document also uses F for the future form, which defers the action",
            "prend une fonction (la condition ou la mise à jour est donnée comme une fonction) ; le document des formes emploie aussi F pour la forme future, qui diffère l'action",
            "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("Many", "works on a collection of items instead of one (the plural form)",
             "travaille sur une collection d'éléments au lieu d'un seul (la forme plurielle)",
             "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("Except", "takes exceptions, what to leave out (the exceptional form)",
               "prend des exceptions, ce qu'il faut laisser de côté (la forme exceptionnelle)",
               "base/doc/narrations/stz-functions-as-linguistic-expressions.md"),
    ("U",   "returns the result without duplication",
            "rend le résultat sans doublon",
            "base/list/stzList.ring"),
]
CODES = [e[0] for e in EXTENSIONS]
TOKENS = sorted(CODES, key=len, reverse=True)           # longest first: WXT before W and XT, QRT before Q
GENERIC = {"QC"}          # works on any method through the library's immutable-form dispatch: no method name carries it, so a per-method yes/no would mislead
STANDARD = ["Q", "CS", "XT", "Z", "ZZ", "IB", "W", "U"]  # shown yes or no on every method; the others only when they exist

QFORM = re.compile(r"^(.+?)(Q{1,3})$")

class QForms:
    def __init__(self, ROOT):
        ref = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
        self.by = {c["name"]: c for c in ref["classes"]}
        self._rec, self._split = {}, {}
        self.plain_anywhere = set()          # every name that does not end in Q, in any class: for the unchained-call rule
        for c in ref["classes"]:
            for m in c["own"]:
                if not QFORM.match(m[0]): self.plain_anywhere.add(m[0].lower())

    def records(self, cls):
        """the methods of a class and of every class it inherits from: lowercased name -> [name, aka, description, owner class]"""
        if cls in self._rec: return self._rec[cls]
        out, seen, todo = {}, set(), [cls]
        while todo:
            k = todo.pop(0)
            if k in seen or k not in self.by: continue
            seen.add(k)
            c = self.by[k]
            for m in c["own"]: out.setdefault(m[0].lower(), [m[0], m[1], m[2], k])
            todo += list(c["inherited"])
        self._rec[cls] = out
        return out

    def names(self, cls): return self.records(cls)

    def split(self, cls, name):
        """(root, [extensions as written]) when the name is a method plus extensions, else None"""
        key = (cls, name)
        if key in self._split: return self._split[key]
        names = self.records(cls)
        def rec(n):
            for t in TOKENS:
                if n.endswith(t) and len(n) - len(t) >= 2:
                    rem = n[:-len(t)]
                    r = rec(rem)                         # the rest may itself be a method plus extensions
                    if r: return (r[0], r[1] + [t])
                    if rem.lower() in names:
                        # the language is case-insensitive: the rest may be written FindSt for the method FindST,
                        # which is itself Find + ST. Resolve it to the spelling the library gave it, and fold that
                        real = names[rem.lower()][0]
                        if real != rem:
                            r = rec(real)
                            if r: return (r[0], r[1] + [t])
                        return (real, [t])
            return None
        out = self._split[key] = rec(name)
        return out

    def base(self, cls, name):
        r = self.split(cls, name)
        return r[0] if r else None

    def fold(self, cls, name):
        r = self.split(cls, name)
        return r[0] if r else name

    def is_form(self, cls, name):
        return self.split(cls, name) is not None

_CACHE = {}

def get(ROOT):
    """one QForms per run"""
    if "q" not in _CACHE: _CACHE["q"] = QForms(ROOT)
    return _CACHE["q"]

JUNK_DESC = re.compile(r"^[=\-#*_.\s]*$|: =+$")

def clean_descriptions(own, banner=8):
    """A description the harvest took from a banner is not the method's own: the same sentence under `banner` methods or
    more of one class (stzListNamedParams: 1,884 methods "described" by the banner above them; stzDiagram: 110 by "export"),
    or a line of rule marks ("=="). The harvest reads the nearest comment above a method, and a section title is the nearest
    comment for every method below it. Those rows lose the description and keep the section: returns the methods without
    it, and {method name lower: section title}"""
    seen = {}
    for m in own:
        if m[2]: seen[m[2]] = seen.get(m[2], 0) + 1
    out, sections = [], {}
    for m in own:
        bad = m[2] and (seen[m[2]] >= banner or JUNK_DESC.search(m[2]))
        if bad and seen[m[2]] >= banner: sections[m[0].lower()] = m[2]
        out.append([m[0], m[1], "" if bad else m[2]])
    return out, sections

def reference(ROOT):
    """data/reference.json with every extension folded into its method. Each class lists a method once ('own'),
    and says which extensions it has:
      c["variants"][root.lower()] = [(name, [extensions]), ...]   every form of the method written with extensions
      c["extra"] = [[name, aka, description, owner]]               a method of an ancestor that this class gives extensions to
    The counts of inherited methods are those of the methods listed."""
    if "ref" in _CACHE: return _CACHE["ref"]
    raw = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
    Q = get(ROOT)
    classes = []
    for c in raw["classes"]:
        d = dict(c)
        own, sections = clean_descriptions(c["own"])
        c = dict(c, own=own)
        d["own"], d["variants"], extra, own_roots = [], {}, {}, set()
        names = {m[0].lower() for m in c["own"]}
        for m in c["own"]:
            r = Q.split(c["name"], m[0])
            if not r: d["own"].append(m); own_roots.add(m[0].lower())
        for m in c["own"]:
            r = Q.split(c["name"], m[0])
            if not r: continue
            root, exts = r
            d["variants"].setdefault(root.lower(), []).append((m[0], exts))
            if root.lower() not in own_roots and root.lower() not in extra:
                rec = Q.records(c["name"]).get(root.lower())
                if rec: extra[root.lower()] = rec
        d["extra"] = list(extra.values())
        d["folded"] = len(c["own"]) - len(d["own"])
        d["sections"] = sections
        d["raw_names"] = names
        classes.append(d)
    by = {c["name"]: c for c in classes}
    for d in classes:
        inh = {}
        for k, v in d["inherited"].items():
            n = sum(1 for m in by[k]["own"] if m[0].lower() not in d["raw_names"]) if k in by else v
            if n: inh[k] = n
        d["inherited"] = inh
    # a method's variants also come from the classes it inherits: collect them for the roots a class lists
    for d in classes:
        for k in d["inherited"]:
            if k not in by: continue
            for root, vs in by[k]["variants"].items():
                d["variants"].setdefault(root, [])
                have = {v[0] for v in d["variants"][root]}
                d["variants"][root] += [v for v in vs if v[0] not in have]
    for d in classes: del d["raw_names"]
    _CACHE["ref"] = {"harvested": raw["harvested"], "classes": classes}
    return _CACHE["ref"]

def forms_of(variants):
    """{extension: [(name, [extensions as written]), ...]} for the variants of one method, the simplest names first"""
    out = {}
    for name, exts in sorted(variants, key=lambda v: (len(v[1]), len(v[0]), v[0])):
        for e in dict.fromkeys(exts): out.setdefault(e, []).append((name, exts))
    return out

def extensions_of(variants):
    """{extension: [names that carry it]} for the variants of one method, the simplest names first"""
    out = {}
    for name, exts in sorted(variants, key=lambda v: (len(v[1]), len(v[0]), v[0])):
        for e in dict.fromkeys(exts): out.setdefault(e, []).append(name)
    return out

def unknown_endings(ROOT, limit=40):
    """endings that look like extensions (one or two capital letters after a method name) but are not documented:
    the names that were left listed, counted by ending, for the author to rule on"""
    Q = get(ROOT)
    import collections
    seen = collections.Counter(); sample = {}
    for cls, c in Q.by.items():
        for m in c["own"]:
            n = m[0]
            if Q.split(cls, n): continue
            for k in (1, 2, 3):
                end = n[-k:]
                if len(n) > k + 2 and end.isalpha() and end.isupper() and (n[:-k]).lower() in Q.records(cls) and end not in CODES:
                    seen[end] += 1; sample.setdefault(end, (cls, n)); break
    return [(e, n, sample[e]) for e, n in seen.most_common(limit)]

def statements(code):
    """the statements of a piece of code, comments cut off; a statement goes on while a bracket or a quote is open"""
    out, buf, depth, quote = [], "", 0, None
    for line in code.split("\n"):
        text = ""
        for ch in line:
            if quote:
                text += ch
                if ch == quote: quote = None
                continue
            if ch == "#": break                                   # a comment: the rest of the line
            if ch in "\"'`": quote = ch
            elif ch in "([{": depth += 1
            elif ch in ")]}": depth -= 1
            text += ch
        buf = (buf + "\n" + text) if buf else text
        if depth <= 0 and not quote:
            if buf.strip(): out.append(buf.strip())
            buf, depth = "", 0
    if buf.strip(): out.append(buf.strip())
    return out

CALL = re.compile(r"\.(\w+)\s*\(")

def closing(stmt, i):
    """the index of the bracket that closes the one opened at stmt[i]"""
    d, q, j = 0, None, i
    while j < len(stmt):
        c = stmt[j]
        if q:
            if c == q: q = None
        elif c in "\"'`": q = c
        elif c in "([{": d += 1
        elif c in ")]}":
            d -= 1
            if d == 0: return j
        j += 1
    return len(stmt)

def top_level(stmt):
    """the calls .Name(...) of a statement at its own level, as [(name, end)], and whether the statement assigns"""
    calls, depth, quote, i, assigns = [], 0, None, 0, False
    while i < len(stmt):
        ch = stmt[i]
        if quote:
            if ch == quote: quote = None
        elif ch in "\"'`": quote = ch
        elif ch in "([{": depth += 1
        elif ch in ")]}": depth -= 1
        elif depth == 0:
            if ch == "=" and stmt[i - 1:i] not in ("=", "<", ">", "!") and stmt[i + 1:i + 2] != "=": assigns = True
            m = CALL.match(stmt, i)
            if m:
                end = closing(stmt, m.end() - 1)
                calls.append((m.group(1), end))
                i = end
        i += 1
    return calls, assigns

KEYWORD = re.compile(r"(?i)(\?|return\b|see\b|for\b|while\b|if\b|but\b|else\b|switch\b|on\b|other\b|load\b|func\b|class\b)")

def unchained(code, plain_names):
    """the ...Q() calls that end a statement whose value nothing uses: [(name, statement number)]"""
    out = []
    for n, stmt in enumerate(statements(code), 1):
        if KEYWORD.match(stmt): continue
        calls, assigns = top_level(stmt)
        if assigns or not calls: continue
        name, end = calls[-1]
        m = QFORM.match(name)
        if end == len(stmt) - 1 and m and m.group(1).lower() in plain_names:
            out.append((name, n))
    return out
