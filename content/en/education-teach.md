---
title: Teach, or design courses
title_html: <i>I teach</i>, or I design courses
kicker: Education · a cohort, an exercise, a chapter of your own
lede: A teacher uses Softanza to set exercises that are checked by running, to follow a cohort through a report that is itself a narration, and to coach where a program cannot. A course designer writes chapters in plain text whose cells all run. Here is each step, run.
description: Teaching with Softanza: forming a cohort, setting exercises judged by running, reading a cohort's report, and writing a course.
---

## What a teacher does, in order {#steps}

1. **Choose the course and the world.** The library carries four courses today (the elementary introduction, nine missions set in Zindara, governed agents, mathematics) and three worlds the examples reason over: a restaurant, a cooperative, a school. An institution can lay its own world over any of them: <a href="education-programme.html#overlay">the overlay</a>.
2. **Form a cohort.** A cohort is a folder with a three-line file: its name, the course it follows, and, if there is one, the overlay it lives under. Each learner is a folder inside it, holding their own work and their progress.
3. **Set exercises.** The course already holds 23. Yours have the same shape: a task in each language, a promise, at least one answer known to be wrong and one known to be right.
4. **Learners submit.** The checker runs each submission in a fresh process and writes the verdict into the learner's folder. Nobody reads the code and compares it with a model answer.
5. **Read the report.** One call writes the cohort's progress report. The report is a narration: every figure in it is a promise beside the cell that computes it.
6. **Coach.** The tutor asks the one question a learner is missing; it never gives the answer. What a program cannot do is yours: the room, the encouragement, the second explanation, the decision to move on.

## A cohort, run {#cohort}

<!--EDU:cohort-->

The cohort file is the three lines the guide describes, and `AddLearner` made a folder for each learner under it. Nothing else was installed.

## An exercise is a promise {#exercise}

An exercise is a short task and the lines the learner's program must print. It enters the course only when a known-wrong answer has been seen to fail and a known-right one to pass, and the two are run again each time the course is checked.

<!--EDU:exercise-->

The first 0 is the known-wrong answer, refused; the 1 is the known-right answer, accepted. The same call judges a learner's file, in the learner's language, and it is what the checker runs.

## The report is a narration {#report}

<!--EDU:report-->

Under the table, one cell per learner computes that learner's line, with a promise beneath it. Run the file through the library again and it says whether it is still true: after another learner passes, the old report reports its own staleness, and a regenerated one holds. A teacher keeps the report as a file, in a repository if wanted, and it never goes out of date silently.

## Design a course {#design}

A chapter is a plain text file, <span class="mono">NN-slug.en.md</span>, in the house narration format: prose and cells, each cell followed by the lines it must print. A stored output is refused when the course loads, because an output that is stored can be wrong. A chapter ends with a recap in three parts: what was achieved, why it matters, what comes next. The same chapter has one edition per language, and a missing edition is a failing guard.

<div class="cards">
<div class="card"><h3>Built in</h3><p class="stage">built</p><p><b>Twenty-five skills in seven families</b> (formulate, express, patterns, see, know, govern, craft), each at three levels, Foundation, Practitioner, Expert, with an evidence field naming the guard that proves each level. <b>Three stages</b>: Encounter, Expression, Governance. <b>Five profiles</b> (young, student, professional, designer, decision maker) that change the depth and the examples, not only a note. <b>Missions</b> set in Zindara, Niger, so that each step runs real code. <b>Built, not tested</b>: a level is earned by a project that passes its guards, never by an exam.</p></div>
<div class="card"><h3>Refused, with the reason</h3><p>A gentle dialect to export from: not needed, because near-natural chains and instructions in your language are Softanza itself. Experience points and leaderboards: a pass is evidence, not a score. An exam-based certificate or signed credential: the fingerprint of the work handed in replaces it. A language-model tutor: refused by law; the tutor runs on the natural layer.</p></div>
<div class="card"><h3>Proposed</h3><p class="stage">proposed</p><p><b>Progressive revelation</b>: a concept appears only when the learner's previous work shows readiness, judged by the guards. It needs the learner's progress, which only the desktop reader can see, so it is the library's to build. Two neighbours are built: <b>the ladder always visible</b> (every chapter of the reader names its rung) and <b>from the cell to its proof</b> (every cell links to its run).</p></div>
</div>

<p class="way"><span>The Softanza way</span> Narrative before syntax; one idea at a time; errors as information about what still needs to be declared; declare, then see.</p>

<p class="proof">The library's own guide for the people who author courses: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>. Next, the institution's door: <a href="education-programme.html">an overlay, cohorts, ownership</a>.</p>
