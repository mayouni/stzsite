---
title: Run a programme
title_html: <i>I run</i> a programme or an institution
kicker: Education · an overlay, cohorts, ownership
lede: A school, a bank, a ministry lays one overlay folder over the course. The same chapters then reason about its world, in its languages, under its rules, and the core is not changed by one byte. The cohorts, the progress and the reports are folders the institution keeps forever.
description: Adapting the Softanza learning system to an institution: an overlay, cohorts, languages, governance, and a fifteen-minute demonstration.
---

## What an institution owns {#own}

Everything is a folder of plain text: the programme, its courses, its overlay, its cohorts, each learner's work and progress. There is no database to back up, no server to keep running and no account to renew; copying the folder copies the institution's whole learning system, and a version control system reads its history. The system needs the library and one laptop, and it runs offline.

## An overlay, never a fork {#overlay}

You do not change the course. You lay your **overlay** over it: a folder that gives the same chapters your world, your exercises, your languages, your name and your rules.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>
<p class="ran">run on 2026-09-30, the education demo</p>

An overlay can add a chapter, an exercise, a skill or a world; replace a world by name, which is how the same chapter reasons over a bank; map its own skills onto the core's; add a fifth language as a data-only pack; and govern, with rules its learners' agents must obey. It **cannot** edit or delete a core file: it can only shadow one, and every shadowing is listed, so an institution can always see what differs from the core.

The steps of the guide, which is itself checked by a guard that follows them literally:

<ol>
<li><b>Copy the template</b> folder, and give it a short name: <span class="mono">bank</span>, <span class="mono">university</span>, <span class="mono">ministry</span>.</li>
<li><b>Fill the placeholders</b>: the name, the institution, the world, two things people request there.</li>
<li><b>Write your world</b>: a file of facts, three words per line, <span class="mono">ministry-of-education | is-a | ministry</span>, <span class="mono">request-1 | requested | transcript</span>. Chapter 1 asks this world what was requested, counts the repeats and removes them.</li>
<li><b>Add an exercise of your own</b> if you want one: a task in each language, a promise, an answer that must fail and an answer that must pass.</li>
<li><b>Run the court.</b> It tells you, by name and in words, what is still wrong: a space inside a word of a world, a file that would replace a core chapter.</li>
</ol>

<p class="proof">The guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a>. Two reference overlays, a bank and a university, are in <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/overlays">education/overlays</a>; the charter's fifth law (an overlay never forks) is enforced by a guard that swaps two overlays under one chapter and asserts that the core's hash did not change.</p>

## Cohorts, reports, ownership {#cohorts}

A cohort is a folder of learners who follow one course under one overlay. Its progress report is a narration whose every figure is a promise, so it says by itself when it has gone stale: the teacher's door shows one <a href="education-teach.html#cohort">run</a>. Each learner's progress is a text file in their own folder, written only by the checker and carrying the evidence of every fact; a pass cannot be forged, because its evidence is the fingerprint of the work handed in. At the end of a year the institution holds, as files, who did what and what was proved.

## Languages {#languages}

The course runs in English, French, Arabic (laid out right to left) and Hausa, from the first page; every chapter's guard runs in all four, and a missing translation is a failing guard, not a fallback to English. The French, Arabic and Hausa editions are drafts that await native reviewers (<a href="education-record.html#limits">0 of 35 units reviewed</a>), and every translated chapter and world page says so. A fifth language is a data-only pack, and the institution's own words go in its overlay.

## Governed AI for learners {#governed}

A learner's agent proposes; only a gate commits. Exercises on agents run in a safe world: a guard asserts that the real tree is unchanged after a student's agent "deletes everything". The tutor itself uses no language model and needs no network.

## A fifteen-minute demonstration for decision makers {#demo}

The presenter's guide gives a scene for each minute, runs on one laptop offline, and computes every scene while it is shown. Before a meeting, its rehearsal must end with the line <span class="mono">DEMO: 20 proved, 0 not proved</span>: if a line reads NOT PROVED, the demo says it would be wrong to present, and would say so in front of the audience too.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">0 to 2</div><div class="lt"><b>Zero install.</b> One folder of plain text. Softanza is the only thing this laptop runs.</div></div>
<div class="lane lane2"><div class="ln">2 to 4</div><div class="lt"><b>Their language.</b> The same chapter, run live in English, French, Arabic and Hausa.</div></div>
<div class="lane lane2"><div class="ln">4 to 6</div><div class="lt"><b>Their world.</b> One file from the institution, and the chapter reasons about its bank, not a restaurant.</div></div>
<div class="lane lane2"><div class="ln">6 to 8</div><div class="lt"><b>Nothing faked.</b> A wrong answer fails and a right answer passes, because the program was run, not read.</div></div>
<div class="lane lane2"><div class="ln">8 to 10</div><div class="lt"><b>The tutor.</b> It will not give the answer; it asks the one question the learner is missing.</div></div>
<div class="lane lane2"><div class="ln">10 to 12</div><div class="lt"><b>Safe AI.</b> A student's agent tried to delete the whole course; it could only propose.</div></div>
<div class="lane lane2"><div class="ln">12 to 14</div><div class="lt"><b>All levels.</b> A nine-year-old's mission in Hausa and a bank analyst's governance exercise, on the same engine.</div></div>
<div class="lane lane2"><div class="ln">14 to 15</div><div class="lt"><b>Ownership.</b> Progress is a text file the institution keeps forever, and a pass cannot be forged.</div></div>
</div>

<p class="proof">The presenter's guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">demo/DEMO.md</a>. Its guard runs the demo twice from a clean folder and checks that the two runs say the same thing word for word.</p>

## What an institution should know before it starts {#honest}

The interactive reader runs on the desktop; a browser runtime for the cells is not built yet, and the page says so on every cell. The French, Arabic and Hausa editions await native reviewers (0 of 35 units reviewed); Zarma is not yet a language of the course. No institution has adopted the system yet: the bank's and the university's overlays in the library are references written to show what an overlay is. The tutor is rule-based, not AI. There is no language model in the loop and none is required: one may be added later as an option, never as the mind of the tutor.
