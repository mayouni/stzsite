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
                 bands=[("Applications and products", "Studio, specified · COBOL workbench, proposed", "", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Aïcha, the intelligence layer", "knowledge · models · agents, on your device", "named", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Softanza, the computational foundation", "one engine, 28 areas, everything judged by running", "built", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Haro, the language of languages", "you declare yours; it runs it, in one binary", "in construction", NEW_FILL, NEW_LINE, NEW_TEXT),
                        ("Harobanda, the declared machine", "one file describes the computer; every boot is checked", "built", OLD_FILL, OLD_LINE, OLD_TEXT),
                        ("Ordinary hardware", "replaceable, and yours", "", KERN_FILL, KERN_LINE, INK)],
                 side=("Takamba", "the harness", ["how all of this", "is built: many", "sessions, one body", "of work, and laws", "cited to the", "incident that", "paid for them"], "built"),
                 cap="stages as read in the repositories on 2026-10-01"),
      "fr": dict(k="UN SEUL DOMAINE  ·  DÉCLARER  ·  JUGER  ·  GOUVERNER",
                 bands=[("Applications et produits", "Studio, spécifié · atelier COBOL, proposé", "", OLD_FILL, OLD_LINE, OLD_TEXT),
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

# --------------------------------------------------------------------------- 7
def northstar(lang):
    """The author's diagram of 2020, "Softanza -- Programming by heart!", redrawn with what
    exists (softanza/vision/08-NORTH-STAR.md, ratified 2026-09-27): six bands, and the court
    beside everything. Two things are new since 2020: the agents in the first band, and the
    floors beneath."""
    L = {
      "en": dict(k="SOFTANZA  ·  PROGRAMMING BY HEART  ·  2020, READ IN 2026",
                 bands=[("Who it is for", "programmers · analysts · designers · leaders · educators · and agents", "agents · 2026"),
                        ("Solutions", "a software model · a delivery model · an enterprise model", ""),
                        ("Systems", "technical · social · ecological · economic · cultural", ""),
                        ("Languages: what you think is what you write", "a declared language per domain · natural language asks · runs narrated", ""),
                        ("Foundation: Softanza", "one engine · 28 areas · a learnable model · documentation that runs", "built"),
                        ("Beneath", "Haro, language of languages · Harobanda, declared machine · device", "floors · 2026")],
                 side=("The court", "beside everything", ["fixtures judge", "the languages,", "contracts judge", "the foundation,", "the gate judges", "each change, the", "boot judges the", "machine: nothing", "is believed"]),
                 cap="the author, 2020 · redrawn 2026-09-13 · ratified 2026-09-27"),
      "fr": dict(k="SOFTANZA  ·  PROGRAMMER PAR CŒUR  ·  2020, RELU EN 2026",
                 bands=[("Pour qui", "programmeurs · analystes · designers · décideurs · enseignants · agents", "agents · 2026"),
                        ("Solutions", "un modèle logiciel · un modèle de livraison · un modèle d'entreprise", ""),
                        ("Systèmes", "technique · social · écologique · économique · culturel", ""),
                        ("Langues : ce que vous pensez, vous l'écrivez", "une langue par métier · la langue naturelle demande · tout est raconté", ""),
                        ("Fondation : Softanza", "un moteur · 28 domaines · un modèle qui s'apprend · la doc s'exécute", "construite"),
                        ("En dessous", "Haro, langue des langues · Harobanda, machine déclarée · l'appareil", "étages · 2026")],
                 side=("Le tribunal", "à côté de tout", ["les fixtures jugent", "les langues, les", "contrats jugent", "la fondation, la", "porte juge chaque", "changement, le", "démarrage juge la", "machine : rien", "n'est cru"]),
                 cap="l'auteur, 2020 · redessiné 2026-09-13 · ratifié 2026-09-27"),
    }[lang]
    HH = 820
    img, d = canvas(17, h=HH)
    kicker(d, 52, L["k"])
    MX, MW = 68, 964
    SX, SW = 1054, 254
    TOP, BOT = 100, 742
    n = len(L["bands"]); gap = 10.0
    bh = ((BOT - TOP) - (n-1)*gap) / n
    f_t = F_T36; f_sub = sans(28)
    for i, (title, sub, st) in enumerate(L["bands"]):
        y = TOP + i*(bh + gap)
        found = i == 4
        fill, line, ink = (NEW_FILL, NEW_LINE, NEW_TEXT) if found else (OLD_FILL, OLD_LINE, OLD_TEXT)
        band(d, MX, y, MW, bh, 11, fill, line, lw=2.2 if found else 1.8, amp=1.0)
        if found: accent(d, MX, y, bh)
        cw = stage(d, MX + MW - 22, y + 12, st, NEW_LINE if found else OLD_TEXT) if st else 0
        text(d, MX + 44, y + 30, fit(f_t, title, MW - 70 - cw, "band title"), f_t, ink)
        text(d, MX + 44, y + bh - 24, fit(f_sub, sub, MW - 64, "band sub"), f_sub, NEW_SUB if found else OLD_TEXT)
    band(d, SX, TOP, SW, BOT - TOP, 13, KERN_FILL, KERN_LINE, lw=1.8, amp=0.9)
    nm, role, lines = L["side"]
    text(d, SX + SW/2, TOP + 46, fit(F_TITLE, nm, SW - 30, "side name"), F_TITLE, INK, anchor="mm")
    f_role = sans(28, "Medium")
    text(d, SX + SW/2, TOP + 92, fit(f_role, role, SW - 24, "side role"), f_role, NEW_LINE, anchor="mm")
    rule(d, SX + 30, TOP + 122, SX + SW - 30, TOP + 122, HAIR, 1.6)
    f_side = sans(27)
    for j, ln in enumerate(lines):
        text(d, SX + SW/2, TOP + 166 + j*44, fit(f_side, ln, SW - 30, "side line"), f_side, OLD_TEXT, anchor="mm")
    text(d, MX, HH - 40, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"northstar-{lang}.png")

# --------------------------------------------------------------------------- 8
def platforms(lang):
    """A platform of platforms: each organisation declares its own platform in its own words,
    Softanza gives every one of them what a platform needs. The construction is stzApp (a world)
    and stzSuperApp (a constellation of worlds, which may hold constellations)."""
    L = {
      "en": dict(k="A PLATFORM OF PLATFORMS  ·  ONE CONSTRUCTION, MANY WORLDS",
                 tops=[("RestoLean", ["neighbourhood", "commerce", "Lyon"], False),
                       ("Organizium", ["a bank's", "organisation", "Niamey"], False),
                       ("Customs school", ["from assessment", "to organisation", "Tunisia"], False),
                       ("Yours", ["declared in", "your own words"], True)],
                 decl=("Each declares, in its own words", "a shared ground · a world per person and device · bonds · rules · roles"),
                 give=("Softanza gives every one the platform", ["a grammar and its court · web, phone, desktop, server and device",
                                                                 "data with an audit trail and undo · agents held to the same rules"]),
                 base="Beneath: Haro, the language of languages · Harobanda, the declared machine",
                 cap="a world: stzApp · a constellation of worlds: stzSuperApp"),
      "fr": dict(k="UNE PLATEFORME DE PLATEFORMES  ·  UNE CONSTRUCTION, DES MONDES",
                 tops=[("RestoLean", ["commerce de", "quartier", "Lyon"], False),
                       ("Organizium", ["l'organisation", "d'une banque", "Niamey"], False),
                       ("École des douanes", ["de l'évaluation", "à l'organisation", "Tunisie"], False),
                       ("La vôtre", ["déclarée dans", "vos propres mots"], True)],
                 decl=("Chacune déclare, dans ses propres mots", "un socle commun · un monde par personne et appareil · liens · règles · rôles"),
                 give=("Softanza donne à chacune la plateforme", ["une grammaire et son tribunal · web, téléphone, bureau, serveur, appareil",
                                                                 "des données avec journal et retour arrière · des agents tenus aux mêmes règles"]),
                 base="En dessous : Haro, la langue des langues · Harobanda, la machine déclarée",
                 cap="un monde : stzApp · une constellation de mondes : stzSuperApp"),
    }[lang]
    HH = 700
    img, d = canvas(19, h=HH)
    kicker(d, 52, L["k"])
    MX, MW = 68, 1240
    f_t = F_T36; f_sub = sans(28)
    # the platforms, side by side: three references and yours
    n = len(L["tops"]); gap = 18.0
    bw = (MW - (n-1)*gap) / n
    TY, TH = 96, 168
    for i, (title, lines, dashed_box) in enumerate(L["tops"]):
        x = MX + i*(bw + gap)
        if dashed_box:
            dashed(d, rr_path(x*S, TY*S, (x + bw)*S, (TY + TH)*S, 12*S), OLD_LINE, int(2.0*S))
        else:
            band(d, x, TY, bw, TH, 11, OLD_FILL, OLD_LINE, lw=1.8, amp=1.0)
        f_bt = sans(30, "SemiBold")                    # the four boxes share one title size
        text(d, x + 20, TY + 36, fit(f_bt, title, bw - 36, "platform title"), f_bt, OLD_TEXT if dashed_box else INK)
        for j, ln in enumerate(lines):
            text(d, x + 20, TY + 78 + j*32, fit(f_sub, ln, bw - 36, "platform line"), f_sub, MUTED if dashed_box else OLD_TEXT)
        arrow_down(d, x + bw/2, TY + TH + 4, TY + TH + 27, fill=OLD_LINE, lw=2.4, head=8)
    # what each one declares
    y = TY + TH + 30; h = 92
    band(d, MX, y, MW, h, 11, KERN_FILL, KERN_LINE, lw=1.8, amp=1.0)
    text(d, MX + 30, y + 30, fit(f_t, L["decl"][0], MW - 60, "decl title"), f_t, INK)
    text(d, MX + 30, y + h - 24, fit(f_sub, L["decl"][1], MW - 60, "decl sub"), f_sub, OLD_TEXT)
    # what Softanza gives every one: the band that matters most
    y += h + 16; h = 132
    band(d, MX, y, MW, h, 11, NEW_FILL, NEW_LINE, lw=2.2, amp=1.0)
    accent(d, MX, y, h)
    text(d, MX + 44, y + 32, fit(f_t, L["give"][0], MW - 70, "give title"), f_t, NEW_TEXT)
    for j, ln in enumerate(L["give"][1]):
        text(d, MX + 44, y + 74 + j*34, fit(f_sub, ln, MW - 70, "give line"), f_sub, NEW_SUB)
    # beneath
    y += h + 16; h = 64
    band(d, MX, y, MW, h, 11, OLD_FILL, OLD_LINE, lw=1.8, amp=1.0)
    text(d, MX + 30, y + h/2, fit(f_sub, L["base"], MW - 60, "base"), f_sub, OLD_TEXT)
    text(d, MX, HH - 36, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"platforms-{lang}.png")

# --------------------------------------------------------------------------- 9
def codingagents(lang):
    """Hands and judges: a coding agent's own tools are the hands; Softanza supplies the judges;
    one stz command is the door between them (decided 2026-10-02, not built: drawn dashed)."""
    L = {
      "en": dict(k="HANDS AND JUDGES  ·  SOFTANZA FOR CODING AGENTS",
                 cols=[("The coding agent", "the hands", ["read and search", "edit files", "run a shell", "", "Claude Code, Codex,", "Cursor and others"], "old", ""),
                       ("The door", "one stz command", ["a command line", "an MCP server", "a skill and a hook", "a plugin to install"], "door", "decided"),
                       ("The judges", "Softanza", ["know the API", "check code and promises", "show the change first", "compute on one engine"], "new", "built")],
                 rule=("The model proposes; a person commits.", "every tool says whether it may act, and refuses with its reason"),
                 cap="judges built and run today · door decided, not built yet"),
      "fr": dict(k="LES MAINS ET LES JUGES  ·  SOFTANZA POUR LES AGENTS QUI CODENT",
                 cols=[("L'agent qui code", "les mains", ["lire et chercher", "modifier des fichiers", "lancer un shell", "", "Claude Code, Codex,", "Cursor et d'autres"], "old", ""),
                       ("La porte", "une commande stz", ["une ligne de commande", "un serveur MCP", "compétence et hook", "un plugin à installer"], "door", "décidée"),
                       ("Les juges", "Softanza", ["connaître l'API", "juger code et promesses", "montrer le plan d'abord", "calculer sur un moteur"], "new", "construits")],
                 rule=("Le modèle propose ; une personne valide.", "chaque outil dit s'il peut agir, et refuse en disant pourquoi"),
                 cap="juges construits et exécutés · porte décidée, à construire"),
    }[lang]
    HH = 650
    img, d = canvas(23, h=HH)
    kicker(d, 52, L["k"])
    f_t = F_T36; f_role = sans(28, "Medium"); f_l = sans(28)
    xs = [(68, 340), (470, 360), (892, 416)]
    TOP, BH = 100, 360
    for (x, w), (title, role, lines, style, st) in zip(xs, L["cols"]):
        if style == "door":
            dashed(d, rr_path(x*S, TOP*S, (x + w)*S, (TOP + BH)*S, 13*S), NEW_LINE, int(2.2*S))
            ink, sub = NEW_TEXT, NEW_SUB
        elif style == "new":
            band(d, x, TOP, w, BH, 13, NEW_FILL, NEW_LINE, lw=2.4, amp=0.9)
            accent(d, x, TOP, BH); ink, sub = NEW_TEXT, NEW_SUB
        else:
            band(d, x, TOP, w, BH, 13, OLD_FILL, OLD_LINE, lw=1.8, amp=0.9); ink, sub = INK, OLD_TEXT
        px = x + (44 if style == "new" else 28)
        text(d, px, TOP + 40, fit(f_t, title, w - (px - x) - 20, "col title"), f_t, ink)
        text(d, px, TOP + 84, fit(f_role, role, w - (px - x) - 20, "col role"), f_role, NEW_LINE if style != "old" else MUTED)
        rule(d, px, TOP + 112, x + w - 24, TOP + 112, HAIR, 1.6)
        for j, ln in enumerate(lines):
            if ln: text(d, px, TOP + 150 + j*38, fit(f_l, ln, w - (px - x) - 20, "col line"), f_l, sub if j < 4 else MUTED)
        if st:
            cw = F_CHIP.getlength(st) / S + 34
            chip(d, x + w - 22 - cw, TOP + BH - 50, cw, 34, st, F_CHIP, NEW_LINE if style == "new" else OLD_TEXT, ink=BG, ls=1.2)
    # the door sits between the hands and the judges
    for (x0, w0), (x1, _) in ((xs[0], xs[1]), (xs[1], xs[2])):
        link_peer(d, x0 + w0 + 8, x1 - 8, TOP + BH/2, fill=OLD_LINE, lw=2.4, head=9)
    # the rule under all three
    y = TOP + BH + 22; h = 98
    band(d, 68, y, 1240, h, 11, KERN_FILL, KERN_LINE, lw=1.8, amp=1.0)
    text(d, 98, y + 32, fit(f_t, L["rule"][0], 1180, "rule title"), f_t, INK)
    text(d, 98, y + h - 24, fit(f_l, L["rule"][1], 1180, "rule sub"), f_l, OLD_TEXT)
    text(d, 68, HH - 36, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"codingagents-{lang}.png")

# --------------------------------------------------------------------------- 10
def forms(lang):
    """One verb, its family: the forms of Remove in the string class, read off the generated reference
    (data/reference.json), and the suffixes as words with one meaning each across the library."""
    L = {
      "en": dict(k="ONE VERB, ITS FAMILY  ·  THE NAME SAYS WHAT THE CALL DOES",
                 left=("The forms of Remove", [("Remove()", "changes the string"), ("Removed()", "returns a changed copy"),
                                               ("RemoveQ()", "changes it, and chains"), ("RemoveCS()", "with a case dial"),
                                               ("RemoveW()", "where a condition holds"), ("RemoveXT()", "with extended options")]),
                 right=("Suffixes are words", [("ed", "a copy, the original kept"), ("Q", "keep chaining"), ("CS", "case sensitivity"),
                                               ("W", "a condition, written inline"), ("XT", "extended"), ("Z · ZZ", "positions · sections"),
                                               ("ST", "from a start position")]),
                 cap="forms read from the reference generated from the library"),
      "fr": dict(k="UN VERBE, SA FAMILLE  ·  LE NOM DIT CE QUE FAIT L'APPEL",
                 left=("Les formes de Remove", [("Remove()", "modifie la chaîne"), ("Removed()", "rend une copie modifiée"),
                                                ("RemoveQ()", "modifie, et enchaîne"), ("RemoveCS()", "avec un réglage de casse"),
                                                ("RemoveW()", "là où une condition vaut"), ("RemoveXT()", "avec options étendues")]),
                 right=("Les suffixes sont des mots", [("ed", "une copie, l'original gardé"), ("Q", "continuer la chaîne"), ("CS", "sensible à la casse"),
                                                      ("W", "une condition, écrite en ligne"), ("XT", "étendu"), ("Z · ZZ", "positions · sections"),
                                                      ("ST", "depuis une position")]),
                 cap="formes lues dans la référence générée depuis la bibliothèque"),
    }[lang]
    HH = 640
    img, d = canvas(29, h=HH)
    kicker(d, 52, L["k"])
    f_t = F_T36; f_code = mono(28, "Medium"); f_l = sans(28)
    TOP, BH = 96, 470
    # the family: the band that matters most
    x, w = 68, 640
    band(d, x, TOP, w, BH, 13, NEW_FILL, NEW_LINE, lw=2.4, amp=0.9); accent(d, x, TOP, BH)
    text(d, x + 44, TOP + 40, fit(f_t, L["left"][0], w - 70, "forms title"), f_t, NEW_TEXT)
    rule(d, x + 44, TOP + 76, x + w - 24, TOP + 76, NEW_LINE, 1.4)
    for j, (code, means) in enumerate(L["left"][1]):
        y = TOP + 118 + j*58
        text(d, x + 44, y, fit(f_code, code, 250, "form code"), f_code, NEW_TEXT)
        text(d, x + 300, y, fit(f_l, means, w - 320, "form means"), f_l, NEW_SUB)
    # the morphemes
    x2, w2 = 732, 576
    band(d, x2, TOP, w2, BH, 13, OLD_FILL, OLD_LINE, lw=1.8, amp=0.9)
    text(d, x2 + 28, TOP + 40, fit(f_t, L["right"][0], w2 - 50, "suffix title"), f_t, INK)
    rule(d, x2 + 28, TOP + 76, x2 + w2 - 24, TOP + 76, HAIR, 1.4)
    for j, (suf, means) in enumerate(L["right"][1]):
        y = TOP + 116 + j*50
        text(d, x2 + 28, y, fit(f_code, suf, 130, "suffix code"), f_code, INK)
        text(d, x2 + 170, y, fit(f_l, means, w2 - 190, "suffix means"), f_l, OLD_TEXT)
    text(d, 68, HH - 40, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"forms-{lang}.png")

# --------------------------------------------------------------------------- 11
def layers(lang):
    """Three layers of one vocabulary over one engine; a program chooses its layer by the file it loads.
    Counts read in the library at commit 010743cce (classes declared in the files each entry file loads)."""
    L = {
      "en": dict(k="THREE LAYERS, ONE ENGINE  ·  CHOSEN BY THE FILE YOU LOAD",
                 bands=[("Max · stx", "walkers, big numbers, multilingual strings, a test framework · 40 classes", "stxLib", "old"),
                        ("Base · stz", "the full platform: 44 domain folders, 644 classes, some 36,000 method names", "stzLib", "new"),
                        ("Core · stk", "the lean essentials: strings, lists, numbers, objects · 17 classes", "stkLib", "old"),
                        ("The engine · Zig", "89 modules behind a plain C interface: the substance, written once", "", "kern")],
                 cap="counted in the library at commit 010743cce"),
      "fr": dict(k="TROIS COUCHES, UN MOTEUR  ·  CHOISIES PAR LE FICHIER CHARGÉ",
                 bands=[("Max · stx", "marcheurs, grands nombres, chaînes multilingues, tests · 40 classes", "stxLib", "old"),
                        ("Base · stz", "la plateforme entière : 44 dossiers, 644 classes, quelque 36 000 noms de méthodes", "stzLib", "new"),
                        ("Core · stk", "l'essentiel, léger : chaînes, listes, nombres, objets · 17 classes", "stkLib", "old"),
                        ("Le moteur · Zig", "89 modules derrière une interface C simple : la substance, écrite une fois", "", "kern")],
                 cap="comptés dans la bibliothèque au commit 010743cce"),
    }[lang]
    HH = 700
    img, d = canvas(31, h=HH)
    kicker(d, 52, L["k"])
    MX, MW = 68, 1240
    TOP, BOT = 100, 630
    n = len(L["bands"]); gap = 14.0
    bh = ((BOT - TOP) - (n-1)*gap) / n
    f_t = F_T36; f_sub = sans(28)
    for i, (title, sub, entry, style) in enumerate(L["bands"]):
        y = TOP + i*(bh + gap)
        if style == "new":
            band(d, MX, y, MW, bh, 11, NEW_FILL, NEW_LINE, lw=2.4, amp=1.0); accent(d, MX, y, bh); ink, subink = NEW_TEXT, NEW_SUB
        elif style == "kern":
            band(d, MX, y, MW, bh, 11, KERN_FILL, KERN_LINE, lw=1.8, amp=1.0); ink, subink = INK, OLD_TEXT
        else:
            band(d, MX, y, MW, bh, 11, OLD_FILL, OLD_LINE, lw=1.8, amp=1.0); ink, subink = INK, OLD_TEXT
        px = MX + (44 if style == "new" else 30)
        cw = stage(d, MX + MW - 22, y + 14, entry, NEW_LINE if style == "new" else OLD_TEXT) if entry else 0
        text(d, px, y + 34, fit(f_t, title, MW - (px - MX) - cw - 40, "layer title"), f_t, ink)
        text(d, px, y + bh - 28, fit(f_sub, sub, MW - (px - MX) - 30, "layer sub"), f_sub, subink)
    text(d, MX, HH - 36, fit(F_READ, L["cap"], 1240, "cap"), F_READ, MUTED)
    return save(img, f"layers-{lang}.png")

if __name__ == "__main__":
    only = sys.argv[1:]
    for fn in (technology, wise, languages, govern, editions, trajectory, northstar, platforms, codingagents, forms, layers):
        if only and fn.__name__ not in only: continue
        for lang in ("en", "fr"):
            print("wrote", fn(lang))
