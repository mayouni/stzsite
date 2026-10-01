"""The phone drawings of the site's six diagrams, in French and English.

A wide diagram drawn at 1376 px lands at about 8 px on a phone, and a picture
may never be dragged sideways. So the phone gets a DIFFERENT drawing of the
same argument: one column, 640 px wide, shown at 340 px, where the 32 px type
lands at 17 px beside 19 px prose. This is the Harobanda method
(narrowlib.py, copied unchanged); the items below are the ones this site needs.
Every label is wrapped or fitted, never set smaller.

    python tools/diagrams/stz_narrow.py   -> assets/img/diagrams/*-narrow-{en,fr}.png
"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import house
house.OUT = HERE.parents[1] / "assets" / "img" / "diagrams"
import narrowlib
narrowlib.OUT = house.OUT
from narrowlib import Col, wrap, M, INNER, NW, STYLES
from house import (S, band, dashed, rr_path, text, sans, mono, fit, READ, TITLE,
                   INK, MUTED, OLD_FILL, OLD_LINE, OLD_TEXT, NEW_FILL, NEW_LINE,
                   NEW_TEXT, NEW_SUB, ORANGE, BRICK, KERN_FILL, KERN_LINE, BG, HAIR)

F_ITEM = sans(READ)
F_ITEM_B = sans(READ, "Medium")


class Narrow(Col):
    """Col plus four items: a wrapped band, a dashed direction, a refusal, a bar row."""

    def item(self, s, style="old", accent=False, strong=False):
        fill, line, ink, _, lw = STYLES[style]
        f = F_ITEM_B if strong else F_ITEM
        pad = 44 if accent else 26
        lines = wrap(f, s, INNER - pad - 22)
        h = 22 + len(lines) * 40 + 18

        def fn(d, y):
            band(d, M, y, INNER, h, 11, fill, line, lw=lw, amp=1.0)
            if accent:
                d.polygon(rr_path((M + 14) * S, (y + 14) * S, (M + 22) * S, (y + h - 14) * S, 4 * S), fill=ORANGE)
            for i, ln in enumerate(lines):
                text(d, M + pad, y + 42 + i * 40, ln, f, ink)
        self._push(h + 12, fn)

    def titled(self, title, sub, style="old", accent=False):
        fill, line, ink, subink, lw = STYLES[style]
        ft = sans(TITLE - 4, "SemiBold")
        pad = 44 if accent else 26
        tl = wrap(ft, title, INNER - pad - 22)
        sl = wrap(F_ITEM, sub, INNER - pad - 22) if sub else []
        h = 24 + len(tl) * 44 + len(sl) * 40 + 20

        def fn(d, y):
            band(d, M, y, INNER, h, 12, fill, line, lw=lw, amp=1.0)
            if accent:
                d.polygon(rr_path((M + 14) * S, (y + 18) * S, (M + 23) * S, (y + h - 18) * S, 4 * S), fill=ORANGE)
            for i, ln in enumerate(tl):
                text(d, M + pad, y + 46 + i * 44, ln, ft, ink)
            for i, ln in enumerate(sl):
                text(d, M + pad, y + 46 + len(tl) * 44 + i * 40, ln, F_ITEM, subink)
        self._push(h + 12, fn)

    def direction(self, title, sub):
        """dashed: a direction, not a fact today"""
        ft = sans(READ, "Medium")
        tl = wrap(ft, title, INNER - 48)
        sl = wrap(F_ITEM, sub, INNER - 48)
        h = 24 + len(tl) * 40 + len(sl) * 40 + 18

        def fn(d, y):
            dashed(d, rr_path(M * S, y * S, (NW - M) * S, (y + h) * S, 12 * S), OLD_LINE, int(2.0 * S))
            for i, ln in enumerate(tl):
                text(d, M + 26, y + 44 + i * 40, ln, ft, OLD_TEXT)
            for i, ln in enumerate(sl):
                text(d, M + 26, y + 44 + len(tl) * 40 + i * 40, ln, F_ITEM, MUTED)
        self._push(h + 12, fn)

    def refusal(self, title, sub):
        ft = mono(READ, "Medium")
        sl = wrap(F_ITEM, sub, INNER - 48)
        h = 24 + 40 + len(sl) * 40 + 18

        def fn(d, y):
            band(d, M, y, INNER, h, 12, BG, BRICK, lw=2.4, amp=0.9)
            text(d, M + 26, y + 44, title, ft, BRICK)
            for i, ln in enumerate(sl):
                text(d, M + 26, y + 84 + i * 40, ln, F_ITEM, BRICK)
        self._push(h + 12, fn)

    def hbar(self, label, value, vmax, shown, hot=False):
        fl, fv = mono(READ, "Medium"), mono(READ)
        x0, x1 = M + 96, NW - M - 120

        def fn(d, y):
            text(d, M, y + 26, label, fl, INK)
            w = max(10, (x1 - x0) * value / vmax)
            band(d, x0, y + 4, w, 44, 8, NEW_FILL if hot else OLD_FILL, NEW_LINE if hot else OLD_LINE, lw=2.0, amp=0.7)
            text(d, x0 + w + 12, y + 26, shown, fv, INK)
        self._push(62, fn)


def technology(lang):
    T = {
     "en": dict(t="ONE ESTATE · DECLARE · JUDGE · GOVERN", rows=[
        ("Applications", "Zin, built · Studio, specified · COBOL workbench, proposed", "old", False),
        ("Aïcha", "the intelligence layer: knowledge, models and agents on your device · named", "old", False),
        ("Softanza", "the computational foundation: one engine, 28 areas, everything judged by running · built", "machine", True),
        ("Haro", "the language of languages: you declare yours, it runs it · in construction", "machine", False),
        ("Harobanda", "the declared machine: one file describes the computer · built", "old", False),
        ("Your hardware", "ordinary, replaceable, and yours", "kern", False)],
        side=("Takamba", "the harness, beside the stack: how all of this is built, many sessions on one body of work · built"),
        cap="stages as read in the repositories on 2026-10-01"),
     "fr": dict(t="UN SEUL DOMAINE · DÉCLARER · JUGER · GOUVERNER", rows=[
        ("Applications", "Zin, construit · Studio, spécifié · atelier COBOL, proposé", "old", False),
        ("Aïcha", "la couche d'intelligence : savoirs, modèles et agents sur votre machine · nommée", "old", False),
        ("Softanza", "la fondation de calcul : un moteur, 28 domaines, tout jugé en s'exécutant · construite", "machine", True),
        ("Haro", "la langue des langues : vous déclarez la vôtre, il l'exécute · en construction", "machine", False),
        ("Harobanda", "la machine déclarée : un fichier décrit l'ordinateur · construite", "old", False),
        ("Votre matériel", "ordinaire, remplaçable, et à vous", "kern", False)],
        side=("Takamba", "le harnais, à côté de la pile : comment tout ceci se construit, plusieurs sessions sur un seul ouvrage · construit"),
        cap="stades lus dans les dépôts le 2026-10-01"),
    }[lang]
    c = Narrow(21)
    c.title(T["t"]); c.gap(8)
    for title, sub, style, accent in T["rows"]:
        c.titled(title, sub, style, accent)
    c.gap(14)
    c.titled(T["side"][0], T["side"][1], "plain")
    c.note(T["cap"])
    return c.render(f"technology-narrow-{lang}.png")


def wise(lang):
    T = {
     "en": dict(t="TWO WAYS OF BUILDING WITH A MACHINE THAT TALKS", vk="VIBE CODING",
        vibe=["the human prompts", "the machine guesses", "structure is whatever survived", "the knowledge lives nowhere", "code you must trust blindly"],
        wk="WISE CODING · THE SOFTANZA WAY",
        wisel=["Softanza asks the question", "the gap to a full model is measured", "each answer is judged against the world", "the knowledge base is written", "a governed system stands"],
        cap="proved by two guards: 13 of 13 and 52 of 52 assertions"),
     "fr": dict(t="DEUX FAÇONS DE CONSTRUIRE AVEC UNE MACHINE QUI PARLE", vk="VIBE CODING",
        vibe=["l'humain souffle une consigne", "la machine devine", "la structure est ce qui survit", "le savoir n'habite nulle part", "un code qu'il faut croire"],
        wk="WISE CODING · À LA SOFTANZA",
        wisel=["Softanza pose la question", "l'écart au modèle complet est mesuré", "chaque réponse est jugée sur le monde", "la base de connaissances est écrite", "un système gouverné tient"],
        cap="prouvé par deux gardes : 13 sur 13 et 52 sur 52 assertions"),
    }[lang]
    c = Narrow(22)
    c.title(T["t"]); c.gap(8)
    c.kicker(T["vk"])
    for s in T["vibe"]: c.item(s, "old")
    c.gap(22)
    c.kicker(T["wk"], NEW_LINE)
    for i, s in enumerate(T["wisel"]): c.item(s, "machine", accent=(i == 0))
    c.note(T["cap"])
    return c.render(f"wise-narrow-{lang}.png")


def languages(lang):
    T = {
     "en": dict(t="A LANGUAGE OF LANGUAGES: YOU DECLARE YOURS", k="A DOMAIN EXPERT DECLARES",
        out=[("a language of your domain", "closed, judged, in your jargon", False),
             ("a knowledge base of your world", "your ontology, as versioned data", True),
             ("an agent that speaks it, locally", "no API, no model needed", True)],
        mid="one closed grammar", legend="dashed: a direction, not a fact today",
        cap="the domain language: 16 of 16 conformance across three runtimes; the whole chain: specified, not yet running end to end"),
     "fr": dict(t="UNE LANGUE DES LANGUES : VOUS DÉCLAREZ LA VÔTRE", k="UN EXPERT DU MÉTIER DÉCLARE",
        out=[("une langue de votre métier", "fermée, jugée, dans votre jargon", False),
             ("une base de connaissances", "votre ontologie, versionnée", True),
             ("un agent qui la parle, en local", "sans API, sans modèle imposé", True)],
        mid="une grammaire fermée", legend="en pointillé : une direction, pas un fait aujourd'hui",
        cap="la langue du métier : 16 conformités sur 16, sur trois exécutants ; la chaîne entière : spécifiée, pas encore de bout en bout"),
    }[lang]
    c = Narrow(23)
    c.title(T["t"]); c.gap(8)
    c.kicker(T["k"], NEW_LINE)
    c.code(["DEFINE LANGUAGE tontine", "  ENTITY member, deposit", "  NORM amount > 0", "  FLOW round, payout"], "machine", accent=(0, 3))
    c.arrow(); c.note(T["mid"]); c.gap(6)
    for title, sub, direction in T["out"]:
        if direction: c.direction(title, sub)
        else: c.titled(title, sub, "old")
    c.note(T["legend"], medium=True)
    c.note(T["cap"])
    return c.render(f"languages-narrow-{lang}.png")


def govern(lang):
    T = {
     "en": dict(t="THE AGENT PROPOSES. IT DOES NOT COMMIT.", steps=[
        ("the agent proposes", "a plan, readable step by step", False),
        ("the workbench rehearses", "a twin of the system; reality is not touched", False),
        ("the court judges", "scope · capability · reversibility", True),
        ("a governed actor commits", "a human, or an actor entitled to it", False)],
        refuse=("refused", "a language model never holds the capability to act, even when it is fooled"),
        human="a human reads the plan and may refuse one step; the refusal is audited",
        cap="measured 2026-10-01: 610 deletions proposed, none committed; 27 of 27 assertions"),
     "fr": dict(t="L'AGENT PROPOSE. IL NE COMMET PAS.", steps=[
        ("l'agent propose", "un plan, lisible pas à pas", False),
        ("l'atelier répète", "un jumeau du système ; le réel n'est pas touché", False),
        ("le tribunal juge", "périmètre · capacité · réversibilité", True),
        ("un acteur gouverné commet", "un humain, ou un acteur habilité", False)],
        refuse=("refusé", "un modèle de langage ne détient jamais la capacité d'agir, même quand on le trompe"),
        human="un humain lit le plan et peut refuser une étape ; le refus est consigné",
        cap="mesuré le 2026-10-01 : 610 suppressions proposées, aucune commise ; 27 assertions sur 27"),
    }[lang]
    c = Narrow(24)
    c.title(T["t"]); c.gap(8)
    for i, (title, sub, key) in enumerate(T["steps"]):
        c.titled(title, sub, "machine" if key else "old", accent=key)
        if key: c.refusal(*T["refuse"])
        if i < len(T["steps"]) - 1: c.arrow()
    c.gap(10)
    c.item(T["human"], "kern")
    c.note(T["cap"])
    return c.render(f"govern-narrow-{lang}.png")


def editions(lang):
    T = {
     "en": dict(t="TWO EDITIONS. THE SAME CODE. NOTHING WITHHELD.", ok="OPEN EDITION · MIT LICENCE",
        open=[("the whole platform", "engine, 28 areas, the language"), ("the reference and the narrations", "generated from the library"),
              ("the course", "15 chapters, 4 languages, every cell runs"), ("the community", "issues and advisories on GitHub")],
        ek="ENTERPRISE EDITION",
        ent=[("the same platform, entire", "not one module held back"), ("dedicated assistance", "from the people who wrote it"),
             ("the full learning system", "your overlay, your cohorts, your language"), ("consultancy from the creators", "architecture, governance, sovereignty")],
        shared="in both: plain text you own, your data at home, nothing anyone can withdraw",
        cap="the enterprise edition is an offer today; write through the repository's issues"),
     "fr": dict(t="DEUX ÉDITIONS. LE MÊME CODE. RIEN DE RETENU.", ok="ÉDITION OUVERTE · LICENCE MIT",
        open=[("toute la plateforme", "moteur, 28 domaines, la langue"), ("la référence et les narrations", "générées depuis la bibliothèque"),
              ("le cours", "15 chapitres, 4 langues, tout s'exécute"), ("la communauté", "tickets et avis de sécurité sur GitHub")],
        ek="ÉDITION ENTREPRISE",
        ent=[("la même plateforme, entière", "pas un module retenu"), ("une assistance dédiée", "par ceux qui l'ont écrite"),
             ("tout le système d'apprentissage", "votre surcouche, vos cohortes, votre langue"), ("le conseil des créateurs", "architecture, gouvernance, souveraineté")],
        shared="dans les deux : du texte brut à vous, vos données chez vous, rien que quiconque puisse retirer",
        cap="l'édition entreprise est une offre aujourd'hui ; écrivez par les tickets du dépôt"),
    }[lang]
    c = Narrow(25)
    c.title(T["t"]); c.gap(8)
    c.kicker(T["ok"])
    for title, sub in T["open"]: c.titled(title, sub, "old")
    c.gap(18)
    c.kicker(T["ek"], NEW_LINE)
    for i, (title, sub) in enumerate(T["ent"]): c.titled(title, sub, "machine", accent=(i == 0))
    c.gap(10)
    c.item(T["shared"], "kern")
    c.note(T["cap"])
    return c.render(f"editions-narrow-{lang}.png")


def trajectory(lang):
    years = [("2022", 136), ("2023", 390), ("2024", 1171), ("2025", 935), ("2026", 3192)]
    T = {
     "en": dict(t="ON GITHUB SINCE 2022-03-12", k="COMMITS PER YEAR ON MAIN", note="2026 counts to 1 October",
        left=("end of 2024, no engine yet", "348,000 lines of library · 63,000 lines of tests · 1,697 commits, one author"),
        right=("2026-10-01", "531,000 lines of library · 179,000 lines of engine in Zig · 306,000 lines of tests, 501 narrated guards"),
        sep=","),
     "fr": dict(t="SUR GITHUB DEPUIS LE 2022-03-12", k="COMMITS PAR AN SUR MAIN", note="2026 compté jusqu'au 1er octobre",
        left=("fin 2024, pas encore de moteur", "348 000 lignes de bibliothèque · 63 000 lignes de tests · 1 697 commits, un seul auteur"),
        right=("2026-10-01", "531 000 lignes de bibliothèque · 179 000 lignes de moteur en Zig · 306 000 lignes de tests, 501 gardes narrés"),
        sep=" "),
    }[lang]
    c = Narrow(26)
    c.title(T["t"]); c.gap(8)
    c.kicker(T["k"])
    mx = max(v for _, v in years)
    for y, v in years:
        c.hbar(y, v, mx, f"{v:,}".replace(",", T["sep"]), hot=(y == "2026"))
    c.note(T["note"])
    c.gap(14)
    c.titled(T["left"][0], T["left"][1], "old")
    c.titled(T["right"][0], T["right"][1], "machine", accent=True)
    return c.render(f"trajectory-narrow-{lang}.png")


if __name__ == "__main__":
    for fn in (technology, wise, languages, govern, editions, trajectory):
        for lang in ("en", "fr"):
            fn(lang)
