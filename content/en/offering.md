---
title: The offering
title_html: The <i>offering</i>
kicker: Who it is for, and in which edition
lede: Softanza tells one story to six kinds of makers. It comes in two editions that contain the same code: an open edition under the MIT licence, and an enterprise edition that adds the people behind it. This page says who each door is for, what each edition contains, and what the references are.
description: The Softanza offering: the six doors (programmer, analyst, designer, decision maker, educator, agent) with a real example each; the open edition and the enterprise edition, same code; the references; how to write.
---

## What is a maker? {#maker}

A maker turns what they know about a world into something that runs, without waiting for the software industry. They are not defined by programming skill but by ownership: the artefact is theirs, in plain text, and it does not expire. A teacher, an analyst, a merchant, a student, a civil servant, and an agent that proposes under all of those worlds. Softanza tells one story; each door below opens it at the place that concerns you.

## Six doors {#doors}

<div class="door-section" id="programmer" markdown="1">
<div class="kicker">Door 1</div>
### A programmer, alone or in a small team

**What you declare:** your intent, in a library that reads like a sentence: find first, then apply. **What you get:** a Zig engine under every call, correct in Unicode, and a narration that runs for every idea. **Where to start:** [the Start page](start.html), then chapter 1 of the course.

<div class="run"><div><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
? o1.NumberOfOccurrence("tea")
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre></div><div class="out"><div class="lbl">Output</div><pre>1
3
[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:11, Softanza at commit 0e72e2e2c</p>
</div>

<div class="door-section" id="analyst" markdown="1">
<div class="kicker">Door 2</div>
### A functional or data analyst

**What you declare:** your organisation's entities, rules and flows, in a plain-text knowledge file. **What you get:** a queryable world, where the dependency graph and the symbol table are the same graph, plus tables and statistics computed by the engine. **Where to start:** chapter 12 of the course, "Teach a world", in [the reader](../reader.html).

<div class="run"><div><div class="lbl">Softanza</div><pre>o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()</pre></div><div class="out"><div class="lbl">Output</div><pre>╭────────┬────────────╮
│ Region │ Population │
├────────┼────────────┤
│ Agadez │     487620 │
│ Maradi │    3402094 │
│ Zinder │    3539764 │
╰────────┴────────────╯</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26; the figures are the RGPH 2012 census of Niger's National Institute of Statistics, as read by the map guard</p>
</div>

<div class="door-section" id="designer" markdown="1">
<div class="kicker">Door 3</div>
### A UI, UX or CX designer

**What you declare:** a picture, a map, a screen, as a program. **What you get:** a render produced by the engine, reproducible to the byte, and an interface constitution of 122 rules and 22 verbs that a machine can check. **Where to start:** chapter 11 of the course, "Draw the answer", and [the Zui constitution](agentic.html#zui).

<figure><img src="../assets/img/areas/graphics.webp" alt="A picture rendered by the engine for the graphics area." width="1100" height="660"><figcaption>One of the twenty-eight pictures of <a href="platform.html#areas">the Platform page</a>, each produced by the platform itself; the map of Niger on <a href="vision.html#africa">the Vision page</a> is another.</figcaption></figure>
</div>

<div class="door-section" id="decision-maker" markdown="1">
<div class="kicker">Door 4</div>
### A CTO, a government, a startup, a business

**What you declare:** your world, your governance, and what each actor, human or agent, may commit. **What you get:** agents that cannot hurt you, a threat model of thirty-eight guarantees with their guards, measured containment, and ownership of everything: code, configuration, data, in plain text. **Where to start:** [the agentic paradigm](agentic.html), then [the editions below](#editions).

<div class="run"><div><div class="lbl">A bank analyst declares an agent</div><pre>A bank analyst declares a stock-watcher agent,
first without saying what it covers:
-> refused / [pia-coverage @ coverage]
   an agent must say WHAT IT COVERS.
...then with its coverage stated:
-> The court judged your declaration,
   and every promise of the exercise was kept.</pre></div><div class="out"><div class="lbl">The containment drill</div><pre>>> TIME TO DETECT : 395 ms
>> TIME TO CONTAIN: 50 ms
TOTAL: 27 assertions, 27 pass, 0 fail</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 (demo, scene 7) and on 2026-10-01 at 00:41 (containment drill)</p>
</div>

<div class="door-section" id="educator" markdown="1">
<div class="kicker">Door 5</div>
### An educator, linguist, author or knowledge architect

**What you declare:** a course, an overlay for your institution, an edition in your language, a world of knowledge. **What you get:** a plain-text program where every cell runs and every exercise is checked by running, a tutor that asks, cohorts whose report is a narration. **Where to start:** [Learn](learn.html), and the overlay guide.

<div class="run"><div><div class="lbl">Zara, 9, answers Mission 1 in Hausa</div><pre>? len( NaturallyIn("ha",
   'Yi jeri dauke [ "Ibrahim", "Fatima", "Ibrahim",
                    "Moussa", "Fatima" ] cire maimaitattu').Result() )
-> Every promise of the exercise was kept when your program ran.
PROVED  the child's Hausa program passed, checked by running it</pre></div><div class="out"><div class="lbl">The engine counts letters, not bytes</div><pre>? Q("سلام").NumberOfChars()         --> 4
? Q("مرحبا بالعالم").Script()        --> arabic</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 and 2026-10-01 at 09:26</p>
</div>

<div class="door-section" id="agent" markdown="1">
<div class="kicker">Door 6</div>
### An agent

**What you declare:** yourself, in an agent file: what you cover, the reversibility of your acts, the posture of every function you call. **What you get:** a workbench where everything you do is rehearsed without touching reality, a constrained grammar that keeps you from emitting a malformed sentence, and a court that judges your plan. **What you do not get:** the capability to commit. **Where to start:** [the agentic paradigm](agentic.html#agents), and chapter 14 of the course, "An agent that cannot hurt".

<div class="run"><div><div class="lbl">An agent proposes 610 deletions</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">The court answers</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
   (required by operation 1)
PROVED  the course folder still holds all 610 files</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, scene 6</p>
</div>

## Two editions, the same code {#editions}

<figure class="diagram"><img src="../assets/img/diagrams/editions-en.png" alt="Two columns. The open edition, MIT licence: the whole platform; the reference and the narrations; the course; the community. The enterprise edition: the same platform, entire; dedicated assistance; the full learning system; consultancy from the creators. In both: plain text you own, your data at home, nothing anyone can withdraw." width="1376" height="768"><figcaption>The enterprise edition holds back no module of the platform. What it adds is the people who wrote it. Drawn 2026-10-01.</figcaption></figure>

<div class="cards">
<div class="card"><h3>The open edition</h3><p>Everything on this site, under the MIT licence: the engine, the twenty-eight areas, the language as it runs today, the reference, the 134 narrations, the course in four languages, the guards. Issues and security advisories on GitHub. No account, no licence per seat, no telemetry: a folder, copied.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a> · <a href="https://github.com/mayouni/stzlib/blob/main/LICENSE">LICENSE</a></p></div>
<div class="card"><h3>The enterprise edition</h3><p>The same platform, entire: not one module is held back for paying customers. Added to it: <b>dedicated assistance</b> from the people who wrote the platform; <b>the full learning system</b> deployed for your institution, with your overlay, your cohorts and your language; and <b>consultancy from the platform's creators</b> on architecture, governance and sovereignty, including a sovereignty verdict for every dependency of your system.</p><p class="proof">An offer today, not a product page with a price: write through <a href="https://github.com/mayouni/stzlib/issues">the repository's issues</a>.</p></div>
</div>

<p class="way"><span>The Softanza way</span> The platform is free and whole for everyone. What an enterprise buys is time with the people who built it, and a guarantee that what it builds remains its own.</p>

## What you own, in both editions {#own}

Your worlds, rules, courses and agents are plain-text files in folders you keep. The engine's source is in the repository and builds for Windows, Linux and macOS. The course is plain text, adapted by overlay and never by fork, and a learner's progress is a text file you can read forever. Nothing anyone else can withdraw; <a href="vision.html#sovereign">the Vision page</a> says what that sentence means and what it does not.

## The references {#references}

<div class="cards">
<div class="card"><h3>Sonibank, Niamey</h3><p>Organizium Standard Edition, under licence, installed on the bank's internal network. The installation guide delivered to the bank attests the reference.</p></div>
<div class="card"><h3>The National Customs School, Tunisia</h3><p>Four requirements, documented one by one, turned an assessment tool into an organisational platform.</p></div>
<div class="card"><h3>RestoLean, Lyon</h3><p>A platform for neighbourhood commerce, carried by the owner of a couscous restaurant. Amendment no. 1 closed on 4 August 2026; its ergonomic rule is "at most two gestures per action".</p></div>
</div>

Nothing else is a reference until a document proves it. This site quotes no number of countries and no number of developers.

## Write {#write}

Questions, defect reports, proposals, and requests for the enterprise edition go through <a href="https://github.com/mayouni/stzlib/issues">the issues of the GitHub repository</a>. A security flaw is reported privately through the repository's security advisories, as its <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a> says.
