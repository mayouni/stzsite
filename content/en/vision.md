---
title: The vision
title_html: The <i>vision</i>
kicker: Why Softanza exists
lede: Software was rebuilt here from first principles, by one person, over several years, before coding agents existed. The result is a platform you can own entirely, inside an estate where the machine, the language and the intelligence layer answer to the same laws. This page says it in plain words and shows where each piece stands.
description: Softanza's vision: the maker, the platform and the agentic age defined; the technology estate from the hardware to the intelligence layer; years of work from first principles; sovereignty and honest ownership; the principles; the products with their stages; the African roots.
---

## Three words, three definitions {#words}

Softanza calls itself **the makers platform of the agentic age**. Each word has one meaning here.

<div class="cards">
<div class="card"><h3>A maker</h3><p>Someone who turns what they know about a world into something that runs, without waiting for the software industry: a teacher who declares a course, an analyst who declares a bank's rules, a merchant who declares a shop, a student who declares a game, a civil servant who declares a procedure. A maker is not defined by programming skill but by ownership: the artefact is theirs, in plain text, and it does not expire.</p></div>
<div class="card"><h3>A platform</h3><p>One engine and one language covering twenty-eight areas of computation, from text to maps to neural inference, under one law: everything is declared, everything is judged by running, nothing is believed. Not a library you add to a stack; the stack itself.</p></div>
<div class="card"><h3>The agentic age</h3><p>The years in which machines write and act. Softanza's answer is that humans and agents meet in small, declared languages rather than in general code; that an agent can only propose; and that only a governed actor commits. The agent is the sixth reader of every Softanza language, and the one it was designed for last.</p></div>
</div>

## Where the platform stands in the whole estate {#estate}

Softanza is the foundation of a family. The drawing below places each member, with its stage as read in its repository on 2026-10-01. Two stages matter most: Softanza is **built**, and Haro is **in construction**. Nothing here is promised that does not carry its word.

<figure class="diagram"><img src="../assets/img/diagrams/technology-en.png" alt="The estate as a stack: applications and products on top; Aïcha, the intelligence layer, named; Softanza, the computational foundation, built; Haro, the language of languages, in construction; Harobanda, the declared machine, built; ordinary hardware at the bottom. Beside the stack, Takamba, the harness, built." width="1376" height="768"><figcaption>Drawn from the repositories on 2026-10-01. The orange mark sits on Softanza because this site is about the foundation; every other member has its own place.</figcaption></figure>

<div class="cards">
<div class="card"><h3>Harobanda <span class="pill built">built</span></h3><p>The declared machine. You describe the whole computer in one text file; it boots exactly that and checks every boot against the file. It is Linux underneath, kept as pinned source and built there. Boots in an emulator today; public under the MIT licence.</p><p class="proof"><a href="https://github.com/mayouni/harobanda">github.com/mayouni/harobanda</a></p></div>
<div class="card"><h3>Haro <span class="pill charter">in construction</span></h3><p>The language of languages: you declare the language of your own domain, and Haro runs it. Its virtual machine and compiler exist in Zig and run the platform's code today; its charter awaits ratification. Never called available before it is.</p></div>
<div class="card"><h3>Aïcha <span class="pill named">named</span></h3><p>The name the author gives the coming intelligence layer: knowledge, models and agents, on your own device, bound by the rule that a model proposes and never commits. No product ships under that name today.</p></div>
<div class="card"><h3>Takamba <span class="pill built">built</span></h3><p>The harness: how all of this is built. Many working sessions on one body of work, with a directory and a version control system and no framework; a doctrine of laws, each cited to the incident that paid for it. Formerly named Bangalo; the author renamed it on 2026-10-01. Its repository is not public yet.</p></div>
</div>

## Years of work, from first principles {#years}

Softanza did not start as a wrapper around existing libraries. It started from the question of what programming should feel like when the human is the parser, and it rebuilt text, numbers, lists, tables, errors and documentation from there. The mission has not moved since 2018; the repository has been public since 12 March 2022.

<figure class="diagram"><img src="../assets/img/diagrams/trajectory-en.png" alt="Commits per year on the main branch: 136 in 2022, 390 in 2023, 1,171 in 2024, 935 in 2025, 3,192 in 2026 up to 1 October. End of 2024: 348,000 lines of library, 63,000 of tests, 1,697 commits, no engine yet. On 2026-10-01: 531,000 lines of library, 179,000 lines of engine in Zig, 306,000 lines of tests, 501 narrated guards." width="1376" height="768"><figcaption>Counted in the repository on 2026-10-01: commits per calendar year on the main branch, and the tree as it stood on 31 December 2024 against the tree at commit 0e72e2e2c.</figcaption></figure>

By the end of 2024, after 1,697 commits by one author, the library held 348 thousand lines of code and 63 thousand lines of tests, all in the host language, with no engine yet. The author states that these lines were written by hand, before coding agents. Since then the Zig engine was written (179 thousand lines), the library grew to 531 thousand lines, the tests to 306 thousand, and the pace of commits tripled: that is what building with agents under a harness looks like, when the harness is Takamba and the law is that everything is judged by running.

<p class="proof">The counts: <code>git rev-list --count</code> at the last commit of each year on the main branch; lines counted over <code>*.ring</code> files outside <code>archive</code> folders, split between <code>base/test</code> and the rest, in the tree of <a href="https://github.com/mayouni/stzlib/commit/a395d09cd59a3439154ff1b899db04acce2dfb27">a395d09c</a> (2024-12-31) and of <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> (2026-09-30). The "written by hand" statement is the author's; the dates and sizes are the repository's.</p>

<p class="way"><span>The Softanza way</span> A platform written from first principles can obey one set of laws everywhere. A platform assembled from a hundred libraries cannot, because each library already chose its own.</p>

## Sovereign, and honestly so {#sovereign}

The estate's word for sovereignty has exactly one meaning: **nothing anyone else can withdraw.** It has never meant "every line is ours". It means that every dependency gets a verdict, owned, borrowed and pinned, or vendored with the code, and that the verdict is written down where you can read it.

<div class="cards">
<div class="card"><h3>Technically yours</h3><p>The platform is public under the MIT licence. Your worlds, your rules, your courses and your agents are plain-text files in folders you keep. The engine's source is in the repository and builds for Windows, Linux and macOS. There is no account to create, no licence per seat, and nothing on this site is loaded from a network: it opens from a folder on a laptop.</p></div>
<div class="card"><h3>Educationally yours</h3><p>The course is plain text, in four languages, in the same repository. An institution adapts it with an overlay folder, never a fork, and keeps every learner's progress as a text file it can read forever. A pass is proven by the fingerprint of the work handed in, not by a server anyone else runs.</p></div>
<div class="card"><h3>Honest about lock-in</h3><p>Every platform is a commitment, and this site does not pretend otherwise. What it promises is that the commitment is readable: open formats, open code, open course, and a verdict per dependency. Leaving costs a copy, not a negotiation. The remaining limits are written on this site rather than hidden: Haro is in construction, two areas of the Atlas are absent by design, and no customer yet runs the declared machine in production.</p></div>
</div>

<p class="way"><span>The Softanza way</span> "The data stays here" is not a sentence in a contract; it is a property of a system whose every piece you can read, build and move.</p>

<p class="proof">The definition and the verdict table: the Harobanda site, pages "sovereign" and "status" (<a href="https://github.com/mayouni/harobanda">github.com/mayouni/harobanda</a>); the licence: <a href="https://github.com/mayouni/stzlib/blob/main/LICENSE">LICENSE</a>; the overlay rule: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a>; the evidence rule: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>, section 5.6.</p>

## The principles, in plain words {#principles}

Twelve ideas hold the platform up. Each is one sentence here; the proofs behind them are on the pages this site links.

<div class="cards principles">
<div class="card"><h3>1 · Declare a language</h3><p>In the agentic age you do not write software: you declare your world in a language made for it, and you govern how that world changes. <a href="agentic.html#languages">How</a>.</p></div>
<div class="card"><h3>2 · Everything is judged</h3><p>A narration runs as it is read; a promise is checked by running; a guard counts its assertions. What did not run is not shown, on this site either.</p></div>
<div class="card"><h3>3 · One engine, many faces</h3><p>Substance lives in the Zig engine; the language is its face, and a future face shares the same engine. <a href="platform.html#engine">The engine</a>.</p></div>
<div class="card"><h3>4 · Agents that cannot hurt you</h3><p>A model proposes; a workbench rehearses; a court judges; only a governed actor commits. <a href="agentic.html#govern">The paradigm</a>.</p></div>
<div class="card"><h3>5 · Knowledge of your world</h3><p>Wolfram knows the world's facts. Softanza knows your world: its entities, rules, actors and flows, declared in plain text.</p></div>
<div class="card"><h3>6 · Code that reads</h3><p>The human is the parser: find first, then apply; names are verbs; a natural-language instruction runs. <a href="platform.html#code">Beside Python</a>.</p></div>
<div class="card"><h3>7 · In your language</h3><p>The course speaks English, French, Arabic and Hausa; the engine counts letters, not bytes; the same instruction runs in the four languages.</p></div>
<div class="card"><h3>8 · Exact by default</h3><p>An integer is exact at any size; a decimal says it is decimal; the algebra is proven against an oracle.</p></div>
<div class="card"><h3>9 · Honest by design</h3><p>The Atlas shows the low ratings beside the high ones; every product carries its stage; no figure without a file.</p></div>
<div class="card"><h3>10 · Sovereign by construction</h3><p>Nothing anyone else can withdraw: a verdict per dependency, plain text you keep, a machine you declare. <a href="#sovereign">Above</a>.</p></div>
<div class="card"><h3>11 · Programming by heart</h3><p>What you think is what you write. The court is severe so that the surface can stay warm; a tutor asks and never gives the answer.</p></div>
<div class="card"><h3>12 · Born in Africa</h3><p>Designed between Tunisia, Niamey and Paris; a bank, a customs school and a restaurant as references; a machine named after a bridge. <a href="#africa">Below</a>.</p></div>
</div>

## Every product, with its stage {#products}

A product that does not exist yet says so. The stage is a word you can check: <span class="pill built">built</span> the code exists and its guards pass · <span class="pill charter">in construction</span> the design exists and the code is under way · <span class="pill spec">specification</span> the document and, sometimes, a prototype · <span class="pill proposal">ratified proposal</span> the direction is decided · <span class="pill named">named</span> a name, and nothing else yet.

<div class="cards">
<div class="card"><h3>Softanza <span class="pill built">built</span></h3><p>The foundation: the library and its Zig engine, public. Everything else stands on it.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
<div class="card"><h3>The Learning System <span class="pill built">built</span></h3><p>Two courses of fifteen chapters in four languages, missions, projects, overlays, cohorts, a tutor; eleven guards. <a href="learn.html">Learn</a>.</p></div>
<div class="card"><h3>Haro <span class="pill charter">in construction</span></h3><p>The language of languages, on a sovereign virtual machine and compiler in Zig. Charter of 2026-09-26 awaiting ratification.</p></div>
<div class="card"><h3>Harobanda <span class="pill built">built</span></h3><p>The declared machine, MIT, boots in an emulator. No production workload yet, and it says so.</p><p class="proof"><a href="https://github.com/mayouni/harobanda">github.com/mayouni/harobanda</a></p></div>
<div class="card"><h3>HaroBase <span class="pill spec">specification</span></h3><p>The governed data store: plain SQLite, in the process, governed. Charter ratified 2026-09-29; first layers built. Private for now.</p></div>
<div class="card"><h3>Aïcha <span class="pill named">named</span></h3><p>The coming intelligence layer and conversational agent. No product ships under that name today.</p></div>
<div class="card"><h3>Zin <span class="pill built">built</span></h3><p>The enterprise's constitutional compiler and agentic platform: business logic, governance and organisation as compilation concerns. Commercial, private.</p></div>
<div class="card"><h3>Zui <span class="pill built">built</span></h3><p>The interface constitution: 122 rules a machine can refuse to violate, 22 verbs. <a href="agentic.html#zui">On the Agentic page</a>. Repository not public yet.</p></div>
<div class="card"><h3>Refine <span class="pill spec">specification</span></h3><p>Refinement-oriented programming: a corpus of specifications, a prototype, a book in manuscript. <a href="agentic.html#rop">On the Agentic page</a>.</p></div>
<div class="card"><h3>Takamba <span class="pill built">built</span></h3><p>The harness, formerly Bangalo: how Softanza builds Softanza. Repository not public yet.</p></div>
<div class="card"><h3>The COBOL workbench <span class="pill proposal">ratified proposal</span></h3><p>Modern tooling around unchanged COBOL estates, without a rewrite. Direction ratified 2026-08-16; the name is held back until a prior-use search closes.</p></div>
<div class="card"><h3>Softanza Studio <span class="pill spec">specification</span></h3><p>The commercial visual environment over the same plain-text truth. A design corpus and a browser prototype today.</p></div>
</div>

<p class="proof">Stages read on 2026-09-30 and 2026-10-01 in the repositories themselves. Where a repository is private, the site says so and quotes nothing it cannot link.</p>

## Born in Africa, useful to the world {#africa}

Softanza is designed by a Tunisian, between Tunisia, Niamey and Paris. Its references are a bank, a customs school and a restaurant, each attested by a document. Its course speaks Hausa, and awaits a native reviewer. Its machine, Harobanda, is named for the bridge across the Niger River that joins the two banks of Niamey, "because the machine likewise joins a solution's promises to the hardware that keeps them".

<figure><img src="../assets/img/niger-density.png" alt="Population density map of Niger by region, 2012: Agadez in the north nearly empty at 0.78 people per km²; the southern regions dense; Niamey at 1,844 people per km², off the scale." width="1500" height="1240"><figcaption>"Where Niger lives", rendered by the engine on 2026-09-30 in 5.9 seconds from the official borders (geoBoundaries, ODbL) and the 2012 census (Niger's National Institute of Statistics). The areas are measured by the engine's geodesic routine on the WGS84 ellipsoid, so the density is the library's own number. Guard: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/graphics/niger_density.ring">niger_density</a>.</figcaption></figure>

<div class="cards">
<div class="card"><h3>Sonibank, Niamey</h3><p>Organizium Standard Edition, under licence, on the bank's internal network. The installation guide delivered to the bank attests the reference.</p></div>
<div class="card"><h3>The National Customs School, Tunisia</h3><p>Four requirements, documented one by one, turned an assessment tool into an organisational platform.</p></div>
<div class="card"><h3>RestoLean, Lyon</h3><p>A platform for neighbourhood commerce, carried by the owner of a couscous restaurant. Its ergonomic rule: at most two gestures per action.</p></div>
</div>

Nothing else is a reference until a document proves it. This site quotes no number of countries and no number of developers. The Zarma edition of the course does not exist yet: it is an invitation.
