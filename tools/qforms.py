"""The ...Q() forms of Softanza method names, as the author rules them (2026-10-03).

A method's ...Q() form does what the method does, then returns the object so a
sentence can go on: Q([1, 2, 3]).FilterQ('{ @item > 1 }').Content(). It is a
syntax detail, not another method. So the site

  - lists a method once: a ...Q() (or ...QQ(), ...QQQ()) form whose plain method
    exists in the class or a class it inherits from is folded into it;
  - shows no example that calls a ...Q() form and then does nothing with the
    result: o1.FilterQ(...) alone on a line is wrong, since o1.Filter(...) does
    the job. A Q call whose result is chained on, assigned, printed, returned or
    looped over is right.

A ...Q() name with no plain twin is the method itself (an accessor that returns
an object) and stays listed.
"""
import json, re

QFORM = re.compile(r"^(.+?)(Q{1,3})$")

class QForms:
    def __init__(self, ROOT):
        ref = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
        self.by = {c["name"]: c for c in ref["classes"]}
        self._chain = {}
        self.plain_anywhere = set()          # every plain name some class has
        for c in ref["classes"]:
            for m in c["own"]:
                if not QFORM.match(m[0]): self.plain_anywhere.add(m[0].lower())

    def names(self, cls):
        """the method names of a class and of every class it inherits from, lowercased"""
        if cls in self._chain: return self._chain[cls]
        out, seen, todo = set(), set(), [cls]
        while todo:
            k = todo.pop()
            if k in seen or k not in self.by: continue
            seen.add(k)
            c = self.by[k]
            out |= {m[0].lower() for m in c["own"]}
            todo += list(c["inherited"])
        self._chain[cls] = out
        return out

    def base(self, cls, name):
        """the plain method a ...Q() form folds into, or None when the name is a method of its own"""
        m = QFORM.match(name)
        if not m: return None
        return m.group(1) if m.group(1).lower() in self.names(cls) else None

    def fold(self, cls, name):
        return self.base(cls, name) or name

    def is_form(self, cls, name):
        return self.base(cls, name) is not None

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

_CACHE = {}

def get(ROOT):
    """one QForms per run"""
    if "q" not in _CACHE: _CACHE["q"] = QForms(ROOT)
    return _CACHE["q"]

def reference(ROOT):
    """data/reference.json with every ...Q() form folded into its plain method: each class lists
    a method once, and the counts of inherited methods are those of the methods listed"""
    if "ref" in _CACHE: return _CACHE["ref"]
    raw = json.loads((ROOT / "data" / "reference.json").read_text(encoding="utf-8"))
    Q = get(ROOT)
    classes = []
    for c in raw["classes"]:
        d = dict(c)
        d["own"] = [m for m in c["own"] if not Q.is_form(c["name"], m[0])]
        d["folded"] = len(c["own"]) - len(d["own"])
        d["raw_names"] = {m[0].lower() for m in c["own"]}
        classes.append(d)
    by = {c["name"]: c for c in classes}
    for d in classes:
        inh = {}
        for k, v in d["inherited"].items():
            n = sum(1 for m in by[k]["own"] if m[0].lower() not in d["raw_names"]) if k in by else v
            if n: inh[k] = n
        d["inherited"] = inh
    for d in classes: del d["raw_names"]
    _CACHE["ref"] = {"harvested": raw["harvested"], "classes": classes}
    return _CACHE["ref"]
