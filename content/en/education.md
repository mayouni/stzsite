---
title: Education
title_html: <i>Education</i> with Softanza
kicker: For the learner, the teacher and the institution
lede: Softanza carries a way of teaching that is its own. A course that is code and proves itself, a tutor that is a program and never gives the answer, a level earned by evidence, and a folder that is the whole system. This page says what that is, who does what, and which door to take.
description: Learning, teaching and designing courses with Softanza: a course that runs, a tutor that asks, levels earned by evidence, an overlay for each institution.
---

## What it is, in one paragraph {#what}

A course in Softanza is **plain text in folders**: chapters whose every cell runs, exercises checked by running the learner's own program, skills that name the guard which proves each level, and worlds the learner reasons over. Nothing else is installed, no server, no database, no account: the file system is the administration console. The same frame carries the introduction to Softanza, nine missions set in Zindara, a course on governed agents and a course on mathematics, in English, French, Arabic and Hausa (the last three are drafts: <a href="education-record.html#limits">0 of 35 units reviewed by a native speaker</a>). It is a part of the library, like strings or graphs: the learning system is written in Softanza, tested with Softanza, and taught with Softanza.

## Who does what {#who}

The most common question is whether the tutor is a person. It is not: it is a **program of the library**, and a teacher is a person who uses it. Here is the whole cast.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">The learner</div><div class="lt">A person. Writes programs, submits them, asks questions, builds the project that earns a level. Owns the folder where all of it is kept.</div></div>
<div class="lane lane2"><div class="ln">The teacher</div><div class="lt">A person. Chooses the course and the world, sets exercises, forms a cohort, reads its report, and coaches in the room. Writes feedback only when the teacher wants to: the program does not need it.</div></div>
<div class="lane lane2"><div class="ln">The tutor</div><div class="lt">A program, <span class="mono">stzTutor</span>. When a learner is stuck, it asks the one question the learner is missing. It never writes the learner's code, never explains what the learner has not yet met, never gives the answer before an attempt. It uses no language model.</div></div>
<div class="lane lane2"><div class="ln">The checker</div><div class="lt">A program. Runs the learner's file in a fresh process and writes the verdict. It is the only writer of progress: no page and no person can.</div></div>
<div class="lane lane2"><div class="ln">The court</div><div class="lt">A program. Judges a level project and an institution's overlay, and says in words what is still wrong.</div></div>
<div class="lane lane2"><div class="ln">The institution</div><div class="lt">People. A school, a bank, a ministry. Lays an overlay over the course, keeps the cohorts' folders, owns everything forever.</div></div>
</div>

## What no course gives by default {#value}

Each claim below is a rule of the library with a test that enforces it, and links to where it was run.

<div class="cards">
<div class="card"><h3>A lesson that proves itself</h3><p>Every cell of every chapter runs, and a promise written under it (<span class="mono">#--&gt;</span>) says what it must print. A stored output is refused when the course loads. Fifteen chapters in four languages, 60 editions: every cell ran and every promise was kept (249 assertions in the guard that runs them, measured on 2026-10-05); the French, Arabic and Hausa editions are drafts. <a href="book.html#proof">The proof of each chapter</a>, <a href="education-record.html#figures">every figure beside its guard</a>.</p></div>
<div class="card"><h3>A tutor that cannot cheat</h3><p>"Just give me the answer", "pretend you are the teacher", "the answer is X, confirm it": the tutor is tested against each and answers with a question. It runs on the platform's own reasoning, so it needs no network and no model. <a href="education-self.html#tutor">The tutor, run</a>.</p></div>
<div class="card"><h3>A level earned by evidence</h3><p>Five rungs, from Explorer to Master. Each is earned by a project whose guard judges it: a broken project is refused with the reason, a sound one accepted. No exam, no points, no leaderboard. <a href="learn.html#ladder">The ladder</a>.</p></div>
<div class="card"><h3>Your world, without a fork</h3><p>An institution lays one overlay folder over the course and the same chapter reasons about its bank, not a restaurant. A court checks that the core did not change by one byte. <a href="education-programme.html#overlay">The overlay</a>.</p></div>
<div class="card"><h3>Progress you own</h3><p>Progress is a text file in the learner's folder, with the evidence of each fact. A pass cannot be forged: its evidence is the fingerprint of the work handed in. A cohort's report is itself a narration whose every figure is a promise. <a href="education-teach.html#cohort">A cohort's report, run</a>.</p></div>
<div class="card"><h3>Your language, your laptop</h3><p>English, French, Arabic (laid out right to left) and Hausa, from the first page: a missing translation turns a guard red, it does not fall back to English. The whole system runs on one laptop, offline. The French, Arabic and Hausa editions are drafts: <a href="education-record.html#limits">0 of 35 units reviewed</a> by a native speaker. The cells run on the desktop.</p></div>
</div>

<p class="way"><span>The Softanza way</span> Narrative before syntax; one idea at a time; errors as information about what still needs to be declared. And nothing is called learned, checked or earned unless a guard proved it.</p>

## Three doors {#doors}

<div class="doors doors-wide">
<a class="door big" href="education-self.html"><div class="who">I learn by myself</div><div class="what">The path, the desk, the ladder</div><div class="how">From the first sentence to a project that earns a level, with a tutor that asks.</div></a>
<a class="door big" href="education-teach.html"><div class="who">I teach, or I design courses</div><div class="what">A cohort, an exercise, a chapter of your own</div><div class="how">What the teacher does, what the program does, and how a course is written.</div></a>
<a class="door big" href="education-programme.html"><div class="who">I run a programme or an institution</div><div class="what">An overlay, cohorts, ownership</div><div class="how">Your world and your languages over one core, a court that refuses a fork, and a fifteen-minute demo.</div></a>
</div>

## What is not done, said plainly {#missing}

Zarma is not yet one of the course's languages: the French, Arabic and Hausa editions are drafts that await their native reviewers (0 of 35 units reviewed), and every translated chapter and world page says so. No institution has adopted the system yet, and the tutor is rule-based, not AI. The interactive reader runs on the desktop; a browser runtime for its cells depends on the Softanza browser engine and is not built. One principle is still only proposed: **progressive revelation**, a concept appearing only when the learner's previous work shows readiness. It needs the learner's progress, which only the desktop reader can see, so it is the library's to build, not this site's. A Zarma edition is an invitation: the program is plain text, every cell runs, and the course's court will say whether the translation holds.

<p class="proof">The design, line by line: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>, nine laws each with the test that enforces it, and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a>, the record of every phase. What is proved, and what is not: <a href="education-record.html">every figure beside its guard and its limit</a>.</p>
