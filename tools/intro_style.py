#!/usr/bin/env python3
"""The style gate for the introductions of class pages and area essays.

Ruled by the author 2026-10-21 after the stzKMeans page opened on "Groups found
where nobody gave them:": always direct, precise and didactic, written for a
learner; no metaphor. Two checks, both mechanical:

  1. the first sentence of a class introduction names the class (so a reader who
     searched for the class name learns at once what it is);
  2. no figure of speech from the list of words that have been found in the
     texts. The list is a floor, not a definition: a new offender is added here
     the day it is found.

Exit 1 when a text fails. Reads data/class-intros.json and data/area-intros.json.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BANNED = {
    "en": ["gift", "buys", "sibling", "brother", "cousin", "honest", "a sentence away",
           "teeth", "nobody gave", "raised to", "profound", "most unusual", "speaks",
           "earns", "pays for", "story the library tells", "the price of"],
    "fr": ["cadeau", "frère", "soeur", "sœur", "cousin", "honnête", "à une phrase",
           "dents", "personne n'a donné"],
}


def paragraphs(items):
    return [t for t in items if not t.startswith("@")]


def first_sentence(text):
    m = re.search(r"(?<=[.!?:])\s", text)
    return text[: m.start()] if m else text


def main():
    bad = []
    classes = json.load(open(ROOT / "data" / "class-intros.json", encoding="utf-8"))
    areas = json.load(open(ROOT / "data" / "area-intros.json", encoding="utf-8"))
    for src, data, named in (("class", classes, True), ("area", areas, False)):
        for key, entry in data.items():
            if not isinstance(entry, dict):
                continue
            for lang in ("en", "fr"):
                ps = paragraphs(entry.get(lang, []))
                if not ps:
                    continue
                if named and key.lower() not in first_sentence(ps[0]).lower():
                    bad.append(f"{src} {key} [{lang}]: the first sentence does not name the class")
                low = " ".join(ps).lower()
                for w in BANNED[lang]:
                    if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", low):
                        bad.append(f"{src} {key} [{lang}]: figure of speech '{w.strip()}'")
    for b in bad:
        print("  " + b)
    print(f"{len(bad)} style failures")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
