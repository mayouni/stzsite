---
title: Six doors
title_html: Six <i>doors</i>
kicker: The makers
lede: One story, six ways in. For each reader: what they declare, what they get, where they start, and one example run tonight.
description: The six audiences of Softanza, from the programmer to the agent: what each declares, gets and starts with, with a real example run.
---

## What is a maker?

A maker turns what they know about a world into something that runs, without waiting for the software industry. They are not defined by programming skill but by ownership: the artefact is theirs, in plain text, and it does not expire. A teacher, an analyst, a merchant, a student, a civil servant, and an agent that proposes under all of those worlds. Softanza tells one story; each door below opens it at the place that concerns you.

<div class="door-section" id="programmer" markdown="1">
<div class="kicker">Door 1</div>
## A programmer, alone or in a small team

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
## A functional or data analyst

**What you declare:** your organisation's entities, rules and flows, in a plain-text knowledge file. **What you get:** a queryable world, where the dependency graph and the symbol table are the same graph, plus tables and statistics computed by the engine. **Where to start:** chapter 12 of the course, "Teach a world", in [the reader](learn.html).

<div class="run"><div><div class="lbl">Softanza</div><pre>o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()
? Q([ 487620, 593821, 2037713, 3402094,
      1026848, 3328365, 2722482, 3539764 ]).Sum()</pre></div><div class="out"><div class="lbl">Output</div><pre>╭────────┬────────────╮
│ Region │ Population │
├────────┼────────────┤
│ Agadez │     487620 │
│ Maradi │    3402094 │
│ Zinder │    3539764 │
╰────────┴────────────╯
17138707</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:11; the figures are the RGPH 2012 census of Niger's National Institute of Statistics, as read by the map guard</p>
</div>

<div class="door-section" id="designer" markdown="1">
<div class="kicker">Door 3</div>
## A UI, UX or CX designer

**What you declare:** a picture, a map, a screen, as a program. **What you get:** a render produced by the engine, reproducible to the byte, and an interface language of twenty-four closed verbs in the Zin family. **Where to start:** chapter 11 of the course, "Draw the answer", in [the reader](learn.html).

<figure><img src="../assets/img/niger-density.png" alt="Population density map of Niger by region: Agadez nearly empty in the north, the southern regions dense, Niamey off the scale." width="1500" height="1240"><figcaption>"Where Niger lives", rendered tonight in 5.9 seconds by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/graphics/niger_density.ring">niger_density</a>: geoBoundaries borders (ODbL), the 2012 census, areas measured by the engine's geodesic routine on the WGS84 ellipsoid.</figcaption></figure>
</div>

<div class="door-section" id="decision-maker" markdown="1">
<div class="kicker">Door 4</div>
## A CTO, a government, a startup, a business

**What you declare:** your world, your governance, and what each actor, human or agent, may commit. **What you get:** agents that cannot hurt you, a threat model of thirty-eight guarantees with their guards, measured containment, and ownership of everything: code, configuration, data, in plain text. **Where to start:** [Govern](govern.html), then [Products](products.html) for the stages.

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
## An educator, linguist, author or knowledge architect

**What you declare:** a course, an overlay for your institution, an edition in your language, a world of knowledge. **What you get:** a plain-text program where every cell runs and every exercise is checked by running, a tutor that asks, cohorts whose report is a narration. **Where to start:** [Learn](learn.html), and the overlay guide.

<div class="run"><div><div class="lbl">Zara, 9, answers Mission 1 in Hausa</div><pre>? len( NaturallyIn("ha",
   'Yi jeri dauke [ "Ibrahim", "Fatima", "Ibrahim",
                    "Moussa", "Fatima" ] cire maimaitattu').Result() )
-> Every promise of the exercise was kept when your program ran.
PROVED  the child's Hausa program passed, checked by running it</pre></div><div class="out"><div class="lbl">The engine counts letters, not bytes</div><pre>? len("سلام")                       --> 8
? Q("سلام").NumberOfChars()         --> 4
? Q("مرحبا بالعالم").Script()        --> arabic</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 and 23:11</p>
</div>

<div class="door-section" id="agent" markdown="1">
<div class="kicker">Door 6</div>
## An agent

**What you declare:** yourself, in an agent file: what you cover, the reversibility of your acts, the posture of every function you call. **What you get:** a workbench where everything you do is rehearsed without touching reality, a constrained grammar that keeps you from emitting a malformed sentence, and a court that judges your plan. **What you do not get:** the capability to commit. **Where to start:** [Govern](govern.html), and chapter 14 of the course, "An agent that cannot hurt".

<div class="run"><div><div class="lbl">An agent proposes 610 deletions</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">The court answers</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
   (required by operation 1)
PROVED  the course folder still holds all 610 files</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, scene 6</p>
</div>
