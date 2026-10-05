---
title: What is proved, and what is not
title_html: What is <i>proved</i>, and what is not
kicker: Education · the record
lede: Every figure about the Learning System on this site comes from a guard of the library, named beside it, and every claim has its limit beside it. The translations are drafts, the cells run on the desktop, and no institution has adopted it. This page says each of those first, then the figures, then two tools run for you.
description: The Softanza Learning System, figure by figure: what each guard of the library proves, the limit beside each claim, and the learner's desk run for real.
---

## Three limits, said first {#limits}

<div class="cards">
<div class="card"><h3>The translations are drafts</h3><p>No native speaker has reviewed any of them yet: <b>0 of 35 units</b> in French, in Arabic and in Hausa (the run below prints it). English is the original. Each translated chapter and world page opens with a note in its own language (in French: <i>Traduction provisoire : pas encore relue par un locuteur natif</i>) until a sign-off is recorded for it, and then names who signed. So "four languages", here and on the other pages, means four editions, three of them not yet read by a native speaker.</p></div>
<div class="card"><h3>The cells run on the desktop</h3><p>The reader is a page that opens in any browser, but its cells run on the desktop, and the page says so on every cell. Running them in the browser waits on the Softanza browser engine and is not built. Every figure below was measured on the desktop.</p></div>
<div class="card"><h3>No institution has adopted it</h3><p>A bank and a university exist in the library as two <i>reference overlays</i>, written to show what an overlay is. They are not customers, and this site names no institution as one. The author has not chosen a first institution.</p></div>
</div>

Two more things, in plain words. The tutor is **rule-based**: it uses no language model, and this site does not call it AI. And the licence is the repository's own, MIT, decided on 2026-10-05 on the author's delegation (section 8 of the charter): the author may replace it before a first institution ships.

## The figures, each beside its guard and its limit {#figures}

Measured by the module's authors on 2026-10-05, in a fresh checkout of the library at commit 4a184e6f0. A **guard** is a file of the library that runs and prints how many of its assertions held. This site did not rerun the fourteen guards, which take about twenty minutes together; it reran two tools, the learner's desk and the reviewer's sheet, shown further down.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">The course</div><div class="lt"><b>The Elementary Introduction: 15 chapters in English, French, Arabic and Hausa, which is 60 editions. Every cell ran, every promise was kept, no output is stored.</b> Guard <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/course_narrated.ring">course_narrated</a>, 249 assertions. <b>Beside it:</b> French, Arabic and Hausa are drafts, 0 of 35 units reviewed; the cells run on the desktop.</div></div>
<div class="lane lane2"><div class="ln">The exercises</div><div class="lt"><b>23 exercises that prove themselves:</b> each refuses its wrong answers and accepts its right ones, by running them. The same guard. <b>Beside it:</b> they are checked on the desktop; the tasks in French, Arabic and Hausa are drafts.</div></div>
<div class="lane lane2"><div class="ln">The worlds</div><div class="lt"><b>3 teaching worlds</b> (a restaurant, a cooperative, a school), <b>a page each in 4 languages: 12 pages.</b> Guards <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/worlds_narrated.ring">worlds_narrated</a>, 26 assertions, and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/world_pages_narrated.ring">world_pages_narrated</a>, 45. <b>Beside it:</b> the nine pages in French, Arabic and Hausa are drafts.</div></div>
<div class="lane lane2"><div class="ln">Skills and levels</div><div class="lt"><b>25 skills in 7 families, and 5 levels, each earned by a project folder that passes its guard.</b> Guards <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/spine_narrated.ring">spine_narrated</a>, 33, and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/levels_narrated.ring">levels_narrated</a>, 35. <b>Beside it:</b> the skills' wording in French, Arabic and Hausa is a draft; no institution has adopted the system.</div></div>
<div class="lane lane2"><div class="ln">The tutor</div><div class="lt"><b>It asks the open question, refuses to write the answer, and never explains a chapter ahead of the learner, in 4 languages; no language model.</b> Guards <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/tutor_narrated.ring">tutor_narrated</a>, 45, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/tutor_gaps_narrated.ring">tutor_gaps_narrated</a>, 31, and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/slice_narrated.ring">slice_narrated</a>, 68. <b>Beside it:</b> it is rule-based, not AI; its texts in French, Arabic and Hausa are drafts.</div></div>
<div class="lane lane2"><div class="ln">Institutions</div><div class="lt"><b>An overlay (its own world, exercises, rules and name) passes a court; there are two reference overlays, a bank's and a university's; the steps of the guide are performed by a guard.</b> Guard <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/institution_narrated.ring">institution_narrated</a>, 39. <b>Beside it:</b> no institution has adopted it; the two overlays are references, not adopters.</div></div>
<div class="lane lane2"><div class="ln">Ownership</div><div class="lt"><b>Progress is a text file in the learner's folder, and a pass carries the fingerprint of what was run.</b> Guards <code>slice_narrated</code>, above, and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/desk_narrated.ring">desk_narrated</a>, 24. <b>Beside it:</b> the checker runs on the desktop.</div></div>
<div class="lane lane2"><div class="ln">The demo</div><div class="lt"><b>Fifteen minutes, eight scenes, 20 claims proved.</b> Guard <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/education/demo_narrated.ring">demo_narrated</a>, 17 assertions; the presenter's guide is <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>. <b>Beside it:</b> it runs on one laptop, offline, on the desktop; the French, Arabic and Hausa it shows are drafts.</div></div>
<div class="lane lane2"><div class="ln">The whole</div><div class="lt"><b>14 narrated guards, 716 assertions, run in a fresh checkout in about 20 minutes.</b> The files are <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a>. <b>Beside it:</b> they were run by the module's authors; this site did not rerun them.</div></div>
<div class="lane lane2"><div class="ln">The reader page</div><div class="lt"><b>All of it, 15 chapters and 3 worlds (72 editions), built into one HTML page in about 100 seconds.</b> Tool <code>build_reader.ring</code>, guard <code>desk_narrated</code>. <b>Beside it:</b> the page opens anywhere, its cells run on the desktop, and every draft says so.</div></div>
</div>

## The learner's desk, run for real {#runs}

The learner's desk is a command of the library, run from its own folder with a learner's folder and a verb. Everything below was run by this site, on the library at commit 4a184e6f0, in a temporary learner's folder that is not the library's.

A learner who has just begun is on chapter 1 and has passed nothing. The desk says where they are, and what the first level still needs: four exercises and a project, and the later levels after them.

<!--EDUREC:status-->

A wrong answer to exercise 1.1 is refused. The checker ran the file in a fresh process and says what it printed; it does not say what it should have printed.

<!--EDUREC:refused-->

A right answer passes. The verdict is the checker's: it ran the file, and nobody read it. The learner is now on chapter 2 and one exercise nearer the first level, with four missing instead of five.

<!--EDUREC:passed-->

<!--EDUREC:status2-->

On chapter 2, the learner asks about something they have not reached. The tutor names the later chapter, explains nothing of it, and asks about the exercise in hand. It is rule-based: no language model, no network.

<!--EDUREC:tutor-->

Asked in French, Arabic or Hausa, the tutor answers in that language, and those answers are drafts like the chapters. How many units a native speaker has read is a number the library prints, and today it is none:

<!--EDUREC:review-->

## How a draft stops being a draft {#reviews}

The library's own definition of a **unit**: a chapter with its exercises, a world page, the skills, or the tutor's texts. French, Arabic and Hausa each have 35. A unit stops being a draft when a native speaker's sign-off is recorded for it in a file named for the language; the page then drops the notice and names who signed. The reviewer does not need to know Softanza or Git: the sheet is one text file with everything to read, and says what to judge (the wording) and what not to touch (the code in the cells, and every line that begins with <span class="mono">#--&gt;</span>, which a guard checks by running it).

If you read French, Arabic or Hausa as your own language and would review a unit, open an issue on the library's repository and ask for the sheet. Zarma is not a language of the course; a Zarma edition is an invitation, as the <a href="education.html#missing">Education page</a> says.

## What this page does not claim {#claims}

That the course is available in four reviewed languages; that it runs in the browser; that any institution uses it; that the tutor is AI; that the figures above were re-measured by this site, apart from what the two tools above printed. Where the site says "four languages" elsewhere, read it with the first limit of this page beside it.

<p class="proof">The design and its record, line by line: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a> (nine laws, each with the test that enforces it), <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a> (every phase and what it does not claim), <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a>. Back to <a href="education.html">Education</a>.</p>
