"""The site's drawn diagrams, in the Harobanda house style (house.py), in French
and in English. Every label is fitted: a label wider than its box stops the
build instead of being set smaller, because text inside a picture is never
shrunk to say it matters less.

    python tools/diagrams/stz_diagrams.py        -> assets/img/diagrams/*.png
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import house
from house import (W, H, S, canvas, save, band, dashed, rule, rr_path, fit, sans, mono, text,
                   ls_text, centre_ls, chip, arrow_down, link_peer, chevron,
                   READ, TITLE, KICKER, INK, MUTED, OLD_FILL, OLD_LINE, OLD_TEXT,
                   NEW_FILL, NEW_LINE, NEW_TEXT, NEW_SUB, ORANGE, BRICK, KERN_FILL, KERN_LINE, HAIR, BG)

house.OUT = pathlib.Path(__file__).resolve().parents[2] / "assets" / "img" / "diagrams"
house.OUT.mkdir(parents=True, exist_ok=True)

F_READ, F_READM = mono(READ), mono(READ, "Medium")
F_LAB, F_LABM, F_TITLE = sans(READ), sans(READ, "Medium"), sans(TITLE, "SemiBold")
F_T36 = sans(36, "SemiBold")
F_KICK = mono(KICKER, "Medium")
F_CHIP = mono(22, "Medium")

def kicker(d, y, s, fill=INK):
    centre_ls(d, W/2, y, fit(F_KICK, s, 1240, "kicker", 3.2), F_KICK, fill, 3.2)

def accent(d, x, y, h):
    """the one orange mark of a diagram: a narrow bar on the left of the band that matters most"""
    d.polygon(rr_path((x+18)*S, (y+18)*S, (x+27)*S, (y+h-18)*S, 4*S), fill=ORANGE)

def stage(d, x, y, label, fill=NEW_LINE):
    w = F_CHIP.getlength(label) / S + 34
    chip(d, x - w, y, w, 34, label, F_CHIP, fill, ink=BG, ls=1.2)
    return w

# --------------------------------------------------------------------------- 1
def technology(lang):
    L = {
      "en": dict(k="ONE ESTATE  ·  DECLARE  ·  JUDGE  ·  GOVERN",
                 bands=[("Applications and products", "Zin, built · Studio, specified · COBOL workbench, proposed", "", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Aïcha, the intelligence layer", "knowledge · models · agents, on your device", "named", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Softanza, the computational foundation", "one engine, 28 areas, everything judged by running", "built", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Haro, the language of languages", "you declare yours; it runs it, in one binary", "in construction", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Harobanda, the declared machine", "one file describes the computer; every boot is checked", "built", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Ordinary hardware", "replaceable, and yours", "", KERN_FILL, KERN_LINE, INK)],
                 side=("Takamba", "the harness", ["how all of this", "is built: many", "sessions, one body", "of work, and laws", "cited to the", "incident that", "paid for them"], "built"),
                 cap="stages as read in the repositories on 2026-10-01"),
      "fr": dict(k="UN SEUL DOMAINE  ·  DÉCLARER  ·  JUGER  ·  GOUVERNER",
                 bands=[("Applications et produits", "Zin, construit · Studio, spécifié · atelier COBOL, proposé", "", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Aïcha, la couche d'intelligence", "savoirs · modèles · agents, sur votre machine", "nommée", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Softanza, la fondation de calcul", "un moteur, 28 domaines, tout jugé en s'exécutant", "construite", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Haro, la langue des langues", "vous déclarez la vôtre ; il l'exécute, en un binaire", "en construction", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Harobanda, la machine déclarée", "un fichier décrit l'ordinateur ; chaque démarrage est vérifié", "construite", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Du matériel ordinaire", "remplaçable, et à vous", "", KERN_FILL, KERN_LINE, INK)],
                 side=("Takamba", "le harnais", ["comment tout ceci", "se construit :", "plusieurs sessions,", "un seul ouvrage,", "et des lois citant", "l'incident qui", "les a payées"], "construit"),
                 cap="stades lus dans les dépôts le 2026-10-01"),
    }[lang]
    img, d = canvas(11)
    kicker(d, 52, L["k"])
    MX, MW = 68, 930
    SX, SW = 1030, 278
    TOP, BOT = 104, 690
    n = len(L["bands"]); gap = 12.0
    bh = ((BOT - TOP) - (n-1)*gap) / n
    f_sub = sans(28)
    for i, (title, sub, st, fill, line, ink) in enumerate(L["bands"]):
        y = TOP + i*(bh + gap)
        band(d, MX, y, MW, bh, 11, fill, line, lw=2.2 if fill is NEW_FILL else 1.8, amp=1.0)
        if i == 2: accent(d, MX, y, bh)
        cw = stage(d, MX + MW - 22, y + 14, st, NEW_LINE if fill is NEW_FILL else OLD_TEXT) if st else 0
        inner = MW - 60 - cw - 10
        text(d, MX + 44, y + 30, fit(F_T36, title, inner, "band title"), F_T36, ink)
        text(d, MX + 44, y + bh - 26, fit(f_sub, sub, MW - 60, "band sub"), f_sub, NEW_SUB if fill is NEW_FILL else (OLD_TEXT if fill is OLD_FILL else MUTED))
    # the harness, beside: it is not a layer, it is how the layers get built
    band(d, SX, TOP, SW, BOT - TOP, 13, KERN_FILL, KERN_LINE, lw=1.8, amp=0.9)
    nm, role, lines, st = L["side"]
    text(d, SX + SW/2, TOP + 46, nm, F_TITLE, INK, anchor="mm")
    text(d, SX + SW/2, TOP + 92, fit(F_READM, role, SW - 30, "side role"), F_READM, NEW_LINE, anchor="mm")
    rule(d, SX + 30, TOP + 122, SX + SW - 30, TOP + 122, HAIR, 1.6)
    for j, ln in enumerate(lines):
        text(d, SX + SW/2, TOP + 160 + j*38, fit(f_sub, ln, SW - 30, "side line"), f_sub, OLD_TEXT, anchor="mm")
    cw = F_CHIP.getlength(st) / S + 34
    chip(d, SX + SW/2 - cw/2, BOT - 60, cw, 34, st, F_CHIP, OLD_TEXT, ink=BG, ls=1.2)
    text(d, MX, 722, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"technology-{lang}.png")

# --------------------------------------------------------------------------- 2
def wise(lang):
    L = {
      "en": dict(k="TWO WAYS OF BUILDING WITH A MACHINE THAT TALKS",
                 left=("VIBE CODING", ["the human prompts", "the machine guesses", "structure is whatever survived", "the knowledge lives nowhere", "code you must trust blindly"], "guessing"),
                 right=("WISE CODING  ·  THE SOFTANZA WAY", ["Softanza asks the question", "the gap to a full model is measured", "each answer judged against the world", "the knowledge base is written", "a governed system stands"], "asking · judging · governing"),
                 cap="proved by two guards: 13 of 13 and 52 of 52 assertions"),
      "fr": dict(k="DEUX FAÇONS DE CONSTRUIRE AVEC UNE MACHINE QUI PARLE",
                 left=("VIBE CODING", ["l'humain souffle une consigne", "la machine devine", "la structure est ce qui survit", "le savoir n'habite nulle part", "un code qu'il faut croire"], "deviner"),
                 right=("WISE CODING  ·  À LA SOFTANZA", ["Softanza pose la question", "l'écart au modèle est mesuré", "chaque réponse jugée sur le monde", "la base de connaissances est écrite", "un système gouverné tient"], "demander · juger · gouverner"),
                 cap="prouvé par deux gardes : 13 sur 13 et 52 sur 52 assertions"),
    }[lang]
    img, d = canvas(12)
    kicker(d, 52, L["k"])
    ML, CW, RX, DIV = 68, 592.0, 716, 688
    TOP, BOT = 150, 600
    f_lab = sans(30)
    for X, (head, items, cap), fill, line, ink, new in ((ML, L["left"], OLD_FILL, OLD_LINE, OLD_TEXT, False), (RX, L["right"], NEW_FILL, NEW_LINE, NEW_TEXT, True)):
        ls_text(d, X*S, 112*S, fit(F_KICK, head, CW, "head", 2.4), F_KICK, NEW_LINE if new else MUTED, 2.4)
        n = len(items); gap = 26.0
        bh = ((BOT - TOP) - (n-1)*gap) / n
        for i, label in enumerate(items):
            y = TOP + i*(bh + gap)
            band(d, X, y, CW, bh, 10, fill, line, lw=2.4 if new else 1.8, amp=1.0)
            if new and i == 0: accent(d, X, y, bh)
            text(d, X + (44 if new else 28), y + bh/2, fit(f_lab, label, CW - 70, "item"), f_lab, ink)
            if i < n - 1: arrow_down(d, X + CW/2, y + bh + 3, y + bh + gap - 3, HAIR, 2.2, 7)
        text(d, X, 640, fit(F_READM if new else F_READ, cap, CW, "cap"), F_READM if new else F_READ, NEW_LINE if new else MUTED)
    rule(d, DIV, 100, DIV, 660)
    text(d, ML, 716, fit(F_READ, L["cap"], 1240, "foot"), F_READ, MUTED)
    return save(img, f"wise-{lang}.png")

# --------------------------------------------------------------------------- 3
def languages(lang):
    L = {
      "en": dict(k="A LANGUAGE OF LANGUAGES: YOU DECLARE YOURS",
                 left=("A domain expert declares", ["DEFINE LANGUAGE tontine", "  ENTITY member, deposit", "  NORM amount > 0", "  FLOW round, payout"]),
                 mid=["one closed", "grammar"],
                 right=[("a language of your domain", "closed, judged, in your jargon", False),
                        ("a knowledge base of your world", "your ontology, as versioned data", True),
                        ("an agent that speaks it, locally", "no API, no model needed", True)],
                 legend="dashed: a direction, not a fact today",
                 cap=["the domain language: 16 of 16 conformance across three runtimes", "the whole chain: specified, not yet running end to end"]),
      "fr": dict(k="UNE LANGUE DES LANGUES : VOUS DÉCLAREZ LA VÔTRE",
                 left=("Un expert du métier déclare", ["DEFINE LANGUAGE tontine", "  ENTITY member, deposit", "  NORM amount > 0", "  FLOW round, payout"]),
                 mid=["grammaire", "fermée"],
                 right=[("une langue de votre métier", "fermée, jugée, dans votre jargon", False),
                        ("une base de connaissances", "votre ontologie, versionnée", True),
                        ("un agent qui la parle, en local", "sans API, sans modèle imposé", True)],
                 legend="en pointillé : une direction, pas un fait aujourd'hui",
                 cap=["la langue du métier : 16 conformités sur 16, sur trois exécutants", "la chaîne entière : spécifiée, pas encore de bout en bout"]),
    }[lang]
    img, d = canvas(13)
    kicker(d, 52, L["k"])
    LX, LW, TOP, BOT = 68, 540, 120, 580
    band(d, LX, TOP, LW, BOT - TOP, 13, NEW_FILL, NEW_LINE, lw=2.4, amp=1.0)
    accent(d, LX, TOP, BOT - TOP)
    title, lines = L["left"]
    f_lt, f_code = sans(34, "SemiBold"), mono(28)
    text(d, LX + 44, TOP + 44, fit(f_lt, title, LW - 70, "left title"), f_lt, NEW_TEXT)
    for j, ln in enumerate(lines):
        text(d, LX + 44, TOP + 130 + j*50, fit(f_code, ln, LW - 70, "code line"), f_code, NEW_SUB)
    # the grammar in the middle, then the three outcomes
    MX = LX + LW + 24
    GY = (TOP + BOT) / 2
    link_peer(d, MX, MX + 100, GY, HAIR, 2.4, 9)
    f_mid = mono(22)
    for j, ln in enumerate(L["mid"]):
        text(d, MX + 50, GY - 58 + j*28, fit(f_mid, ln, 134, "mid"), f_mid, MUTED, anchor="mm")
    RX = MX + 130; RW = W - 68 - RX
    n = len(L["right"]); gap = 22.0
    bh = ((BOT - TOP) - (n-1)*gap) / n
    f_rt, f_sub = sans(31, "SemiBold"), sans(26)
    for i, (t, sub, direction) in enumerate(L["right"]):
        y = TOP + i*(bh + gap)
        if direction:
            dashed(d, rr_path(RX*S, y*S, (RX+RW)*S, (y+bh)*S, 11*S), OLD_LINE, int(2.0*S))
            ink, si = OLD_TEXT, MUTED
        else:
            band(d, RX, y, RW, bh, 11, OLD_FILL, OLD_LINE, lw=1.8, amp=1.0)
            ink, si = OLD_TEXT, OLD_TEXT
        text(d, RX + 26, y + 40, fit(f_rt, t, RW - 46, "right title"), f_rt, ink)
        text(d, RX + 26, y + bh - 30, fit(f_sub, sub, RW - 46, "right sub"), f_sub, si)
    text(d, 68, 626, fit(F_READM, L["legend"], 1240, "legend"), F_READM, MUTED)
    f_cap = mono(23)
    for j, ln in enumerate(L["cap"]):
        text(d, 68, 684 + j*34, fit(f_cap, ln, 1240, "cap"), f_cap, MUTED)
    return save(img, f"languages-{lang}.png")

# --------------------------------------------------------------------------- 4
def govern(lang):
    L = {
      "en": dict(k="THE AGENT PROPOSES.  IT DOES NOT COMMIT.",
                 steps=[("the agent proposes", "a plan, readable step by step", False), ("the workbench rehearses", "a twin of the system; reality is not touched", False),
                        ("the court judges", "scope · capability · reversibility", True), ("a governed actor commits", "a human, or an actor entitled to it", False)],
                 refuse=("refused", ["a language model never holds", "the capability to act,", "even when it is fooled"]),
                 human="a human reads the plan and may refuse one step; the refusal is audited",
                 cap="measured 2026-10-01: 610 deletions proposed, none committed · 27 of 27 assertions"),
      "fr": dict(k="L'AGENT PROPOSE.  IL NE COMMET PAS.",
                 steps=[("l'agent propose", "un plan, lisible pas à pas", False), ("l'atelier répète", "un jumeau du système ; le réel n'est pas touché", False),
                        ("le tribunal juge", "périmètre · capacité · réversibilité", True), ("un acteur gouverné commet", "un humain, ou un acteur habilité", False)],
                 refuse=("refusé", ["un modèle de langage ne détient", "jamais la capacité d'agir,", "même quand on le trompe"]),
                 human="un humain lit le plan et peut refuser une étape ; le refus est consigné",
                 cap="mesuré le 2026-10-01 : 610 suppressions proposées, aucune commise · 27 assertions sur 27"),
    }[lang]
    img, d = canvas(14)
    kicker(d, 52, L["k"])
    X0, BW, TOP, BH, GAP = 68, 760, 112, 96, 22
    f_t, f_sub = sans(32, "SemiBold"), sans(25)
    for i, (t, sub, key) in enumerate(L["steps"]):
        y = TOP + i*(BH + GAP)
        fill, line, ink, si = (NEW_FILL, NEW_LINE, NEW_TEXT, NEW_SUB) if key else (OLD_FILL, OLD_LINE, OLD_TEXT, OLD_TEXT)
        band(d, X0, y, BW, BH, 12, fill, line, lw=2.4 if key else 1.8, amp=1.0)
        if key: accent(d, X0, y, BH)
        x0 = X0 + (44 if key else 26)
        text(d, x0, y + 32, fit(f_t, t, BW - 70, "step title"), f_t, ink)
        text(d, x0, y + BH - 28, fit(f_sub, sub, BW - 70, "step sub"), f_sub, si)
        if i < len(L["steps"]) - 1:
            arrow_down(d, X0 + BW/2, y + BH + 2, y + BH + GAP - 2, HAIR, 2.2, 7)
        if key:
            RX, RW, RH = X0 + BW + 40, W - 68 - (X0 + BW + 40), 150
            RY = y + BH/2 - RH/2
            rule(d, X0 + BW + 4, y + BH/2, RX - 4, y + BH/2, BRICK, 2.4)
            band(d, RX, RY, RW, RH, 11, BG, BRICK, lw=2.4, amp=0.9)
            rt, rl = L["refuse"]
            text(d, RX + 24, RY + 30, fit(F_READM, rt, RW - 40, "refuse title"), F_READM, BRICK)
            f_r = sans(23)
            for j, ln in enumerate(rl):
                text(d, RX + 24, RY + 66 + j*28, fit(f_r, ln, RW - 40, "refuse line"), f_r, BRICK)
    HY, HH = TOP + 4*BH + 3*GAP + 30, 76
    band(d, 68, HY, 1240, HH, 12, KERN_FILL, KERN_LINE, lw=2.0, amp=0.8)
    text(d, W/2, HY + HH/2, fit(sans(27), L["human"], 1180, "human"), sans(27), INK, anchor="mm")
    text(d, 68, 716, fit(mono(23), L["cap"], 1240, "cap"), mono(23), MUTED)
    return save(img, f"govern-{lang}.png")

# --------------------------------------------------------------------------- 5
def editions(lang):
    L = {
      "en": dict(k="TWO EDITIONS.  THE SAME CODE.  NOTHING WITHHELD.",
                 left=("OPEN EDITION  ·  MIT LICENCE", [("the whole platform", "engine, 28 areas, the language"), ("the reference and the narrations", "generated from the library"), ("the course", "15 chapters, 4 languages, every cell runs"), ("the community", "issues and advisories on GitHub")]),
                 right=("ENTERPRISE EDITION", [("the same platform, entire", "not one module held back"), ("dedicated assistance", "from the people who wrote it"), ("the full learning system", "your overlay, cohorts, language"), ("consultancy from the creators", "architecture, governance, sovereignty")]),
                 shared="in both: plain text you own, your data at home, nothing anyone can withdraw",
                 cap="the enterprise edition is an offer today; write through the repository's issues"),
      "fr": dict(k="DEUX ÉDITIONS.  LE MÊME CODE.  RIEN DE RETENU.",
                 left=("ÉDITION OUVERTE  ·  LICENCE MIT", [("toute la plateforme", "moteur, 28 domaines, la langue"), ("la référence et les narrations", "générées depuis la bibliothèque"), ("le cours", "15 chapitres, 4 langues, tout s'exécute"), ("la communauté", "tickets et avis de sécurité sur GitHub")]),
                 right=("ÉDITION ENTREPRISE", [("la même plateforme, entière", "pas un module retenu"), ("une assistance dédiée", "par ceux qui l'ont écrite"), ("tout le système d'apprentissage", "votre surcouche, vos cohortes"), ("le conseil des créateurs", "architecture, gouvernance, souveraineté")]),
                 shared="dans les deux : du texte brut à vous, vos données chez vous, rien à retirer",
                 cap="l'édition entreprise est une offre aujourd'hui ; écrivez par les tickets du dépôt"),
    }[lang]
    img, d = canvas(15)
    kicker(d, 52, L["k"])
    ML, CW, RX, DIV = 68, 592.0, 716, 688
    TOP, BOT = 150, 560
    f_t = sans(32, "SemiBold"); f_sub = sans(25)
    for X, (head, items), new in ((ML, L["left"], False), (RX, L["right"], True)):
        fill, line, ink, sub = (NEW_FILL, NEW_LINE, NEW_TEXT, NEW_SUB) if new else (OLD_FILL, OLD_LINE, OLD_TEXT, OLD_TEXT)
        ls_text(d, X*S, 112*S, fit(F_KICK, head, CW, "head", 2.4), F_KICK, NEW_LINE if new else MUTED, 2.4)
        n = len(items); gap = 16.0
        bh = ((BOT - TOP) - (n-1)*gap) / n
        for i, (t, s) in enumerate(items):
            y = TOP + i*(bh + gap)
            band(d, X, y, CW, bh, 10, fill, line, lw=2.4 if new else 1.8, amp=1.0)
            if new and i == 0: accent(d, X, y, bh)
            x0 = X + (44 if new else 28)
            text(d, x0, y + 34, fit(f_t, t, CW - 70, "ed title"), f_t, ink)
            text(d, x0, y + bh - 28, fit(f_sub, s, CW - 70, "ed sub"), f_sub, sub)
    rule(d, DIV, 100, DIV, 580)
    for cx in (ML + CW/2, RX + CW/2): rule(d, cx, 584, cx, 606)
    KY, KH = 608, 80
    band(d, ML, KY, W - 2*ML, KH, 12, KERN_FILL, KERN_LINE, lw=2.0, amp=0.8)
    text(d, W/2, KY + KH/2, fit(sans(27), L["shared"], W - 2*ML - 50, "shared"), sans(27), INK, anchor="mm")
    text(d, ML, 724, fit(mono(24), L["cap"], 1240, "cap"), mono(24), MUTED)
    return save(img, f"editions-{lang}.png")

# --------------------------------------------------------------------------- 6
def trajectory(lang):
    years = [("2022", 136), ("2023", 390), ("2024", 1171), ("2025", 935), ("2026", 3192)]
    L = {
      "en": dict(k="ON GITHUB SINCE 2022-03-12  ·  COMMITS PER YEAR ON THE MAIN BRANCH",
                 left=("end of 2024, no engine yet", ["348,000 lines of library", "63,000 lines of tests", "1,697 commits, one author"]),
                 right=("2026-10-01", ["531,000 lines of library", "179,000 lines of engine, in Zig", "306,000 lines of tests, 501 narrated guards"]),
                 note="2026 counts to 1 October", cap="counted in the repository at main; the files are listed on the Vision page"),
      "fr": dict(k="SUR GITHUB DEPUIS LE 2022-03-12  ·  COMMITS PAR AN SUR MAIN",
                 left=("fin 2024, pas encore de moteur", ["348 000 lignes de bibliothèque", "63 000 lignes de tests", "1 697 commits, un seul auteur"]),
                 right=("2026-10-01", ["531 000 lignes de bibliothèque", "179 000 lignes de moteur, en Zig", "306 000 lignes de tests, 501 gardes narrés"]),
                 note="2026 compté jusqu'au 1er octobre", cap="compté dans le dépôt sur main ; les fichiers sont listés sur la page Vision"),
    }[lang]
    img, d = canvas(16)
    kicker(d, 52, L["k"])
    X0, X1, BASE, TOPY = 120, 1256, 436, 110
    n = len(years); slot = (X1 - X0) / n; bw = slot * 0.62
    mx = max(v for _, v in years)
    f_num = mono(30, "Medium"); f_yr = sans(30, "Medium")
    rule(d, X0 - 30, BASE, X1 + 10, BASE, HAIR, 2.0)
    for i, (y, v) in enumerate(years):
        h = (BASE - TOPY) * v / mx
        x = X0 + i*slot + (slot - bw)/2
        last = i == n - 1
        band(d, x, BASE - h, bw, h, 8, NEW_FILL if last else OLD_FILL, NEW_LINE if last else OLD_LINE, lw=2.0, amp=0.8)
        if last: d.polygon(rr_path((x + bw/2 - 36)*S, (BASE - h - 14)*S, (x + bw/2 + 36)*S, (BASE - h - 6)*S, 3*S), fill=ORANGE)
        text(d, x + bw/2, BASE - h - 30, f"{v:,}".replace(",", " " if lang == "fr" else ","), f_num, INK, anchor="mm")
        text(d, x + bw/2, BASE + 30, y, f_yr, INK, anchor="mm")
    text(d, X1 - 10, BASE + 66, fit(mono(22), L["note"], 500, "note"), mono(22), MUTED, anchor="rm")
    # two readings of the tree, side by side
    f_t = sans(30, "SemiBold"); f_l = sans(26)
    for X, (t, lines), new in ((68, L["left"], False), (716, L["right"], True)):
        y = 526
        band(d, X, y, 592, 172, 11, NEW_FILL if new else OLD_FILL, NEW_LINE if new else OLD_LINE, lw=2.2 if new else 1.8, amp=0.9)
        text(d, X + 28, y + 30, fit(f_t, t, 540, "tree title"), f_t, NEW_TEXT if new else OLD_TEXT)
        for j, ln in enumerate(lines):
            text(d, X + 28, y + 70 + j*34, fit(f_l, ln, 540, "tree line"), f_l, NEW_SUB if new else OLD_TEXT)
    text(d, 68, 732, fit(mono(24), L["cap"], 1240, "cap"), mono(24), MUTED)
    return save(img, f"trajectory-{lang}.png")

if __name__ == "__main__":
    for fn in (technology, wise, languages, govern, editions, trajectory):
        for lang in ("en", "fr"):
            print("wrote", fn(lang))
