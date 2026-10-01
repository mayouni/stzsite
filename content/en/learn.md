---
title: Learn
title_html: <i>Learn</i>
kicker: Three steps, one law
lede: Learning Softanza goes in three steps: a short introduction that gives you the mental model, an interactive book where every cell runs, and the complete documentation generated from the library itself. One law holds all three: nothing on these pages shows an output somebody copied one day. Everything ran.
description: How to learn Softanza: the didactic introduction (find first, then apply), the interactive book in four languages where every cell runs, the complete documentation (reference and narrations), the tutor that asks, the overlay for institutions, and the pedagogical engineering taken from the Zin project.
---

## Step 1 · The introduction: find first, then apply {#intro}

Softanza has thousands of features. You do not learn them one by one. You learn one way of thinking, and the features fall into place behind it.

<div class="cards">
<div class="card"><h3>1 · Say your problem in plain words</h3><p>"Are there repeated items in this list, how many, where, and what is left when I remove them?" The words of the sentence, list, repeated, remove, are the words of the library.</p></div>
<div class="card"><h3>2 · Pick the object that holds your data</h3><p>A list, a string, a number, a table. Everything in Softanza is an object that knows what it can do; the letter <code>Q</code> turns any value into one.</p></div>
<div class="card"><h3>3 · Ask in order: does it contain, how many, where</h3><p>Contain, count, find. Each question is a method named like the question. Then apply: remove, replace, keep. Find first, then apply.</p></div>
</div>

<div class="run"><div><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
? o1.NumberOfOccurrence("tea")
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre></div><div class="out"><div class="lbl">Output</div><pre>1
3
[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:11, Softanza at commit 0e72e2e2c. The full introduction is the narration <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">the Softanza mental model</a>, which runs as it is read.</p>

Three habits complete the model. A method that ends in <b>-ed</b> returns a copy and leaves the object alone; the same verb without it changes the object. A method that ends in <b>Q</b> returns an object you can keep asking, so a sentence can chain. And if you do not know a name, ask: an object answers <code>Ask("how do I remove duplicates")</code> with the methods that do.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("softanza is a platform for makers").SpacesRemovedQ().UppercaseQ().Boxed()</pre></div><div class="out"><div class="lbl">Output</div><pre>┌──────────────────────────────┐
│ SOFTANZAISAPLATFORMFORMAKERS │
└──────────────────────────────┘</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26</p>

<p class="way"><span>The Softanza way</span> The human is the parser. A line reads like a sentence because it was designed to be read, not only to be executed.</p>

## Step 2 · The interactive book, in four languages {#book}

The Elementary Introduction is a course of fifteen chapters, in English, French, Arabic and Hausa. It is read in **the reader**, a page of this site built by running every cell of every chapter in every language: the build is red if one cell fails or one exercise's promise is not kept.

<div class="doors doors-wide">
<a class="door big" href="../reader.html"><div class="who">The reader</div><div class="what">Open the interactive book</div><div class="how">Fifteen chapters · en · fr · ar · ha · three teaching worlds · every cell ran when the page was built on 2026-09-30 at 23:02, in 3 minutes 22 seconds. Arabic reads right to left.</div></a>
</div>

<div class="figures">
<div class="figure"><b>15 × 4</b><span>chapters × languages, the Elementary Introduction</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters">chapters/</a></div>
<div class="figure"><b>15 × 4</b><span>chapters × languages, the mathematics course</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/math/chapters">math/chapters/</a></div>
<div class="figure"><b>3</b><span>teaching worlds: the restaurant, the cooperative, the school</span></div>
<div class="figure"><b>11</b><span>guards that judge the learning system itself</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a></div>
</div>

The same chapter opens with the same sentence in the four languages, and the same cell runs in each. The French, Arabic and Hausa editions carry the note that they await review by a native speaker: it is written on the page, not hidden.

<div class="pair">
<div><h4>Hausa · Nemo, sannan ka aiwatar</h4><p>Kowane wurin aiki yana karɓar buƙatu: gidan abinci yana karɓar oda, banki yana karɓar tikiti, kuma buƙata ɗaya takan zo fiye da sau ɗaya.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.ha.md">01-find-then-apply.ha.md</a></p></div>
<div><h4>French · Trouver, puis agir</h4><p>Tout lieu de travail reçoit des demandes : un restaurant reçoit des commandes, une banque reçoit des tickets, et la même demande arrive souvent plusieurs fois.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.fr.md">01-find-then-apply.fr.md</a></p></div>
</div>

The library's natural layer understands an instruction in the four languages of the course and runs it:

<div class="run"><div><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )
? @@( NaturallyIn("ha", "Yi jeri dauke [ 5, 3, 5, 1 ] cire maimaitattu").Result() )
? @@( NaturallyIn("ar", "أنشئ قائمة مع [ 5, 3, 5, 1 ] أزل التكرارات").Result() )</pre></div><div class="out"><div class="lbl">Output</div><pre>[ 5, 3, 1 ]
[ 5, 3, 1 ]
[ 5, 3, 1 ]</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, last line "DEMO: 20 proved, 0 not proved", in 49 seconds</p>

## Step 3 · The complete documentation {#docs}

When the book is read, the documentation takes over, and it is generated from the library itself: every class explains its own methods, so the documentation cannot drift from the code.

<div class="cards">
<div class="card"><h3>The reference</h3><p>618 classes and 26,949 methods, each with the explanation the library gives of itself, by area and from A to Z. Generated, never hand-written.</p><p class="proof"><a href="reference.html">Open the reference</a></p></div>
<div class="card"><h3>The narrations</h3><p>134 documents where every code block runs and no output is stored. From the mental model to the agents that cannot hurt you.</p><p class="proof"><a href="narrations.html">The list of narrations</a></p></div>
<div class="card"><h3>The Atlas</h3><p>Twenty-eight areas, each with what a maker does with it, an example run, and its lanes rated honestly.</p><p class="proof"><a href="atlas.html">Open the Atlas</a></p></div>
</div>

## A tutor that asks, and does not give the answer {#tutor}

<pre>Moussa: "I don't understand anything. Just tell me the answer."
Tutor:  I will not write the answer for you: that is the one thing a tutor must never do.
        Try first. Write your attempt and submit it; then I will tell you what is still
        missing, as a question.
Moussa: "What am I missing?"
Tutor:  Where are the repeated items? Which line of your program asks for their positions?
        (why: the mental model finds before it applies)
PROVED  no reply contains a method of the answer, or the answer itself
PROVED  the tutor found the missing step by wise coding, not by guessing
PROVED  no language model was used</pre>
<p class="ran">run on 2026-09-30 at 23:10, demo, scene 4</p>

<p class="way"><span>The Softanza way</span> The tutor has three rules: it does not write the learner's code; it does not explain what the learner has not yet met; it does not give the answer before the learner has tried. It runs on the platform's own natural layer, without a language model.</p>

## For an institution: an overlay, never a fork {#overlay}

A bank, a university, a school lays **one overlay folder** on the program: its world, its chapters, its exercises, its skills, its language, its governance. The course then reasons about its bank and not about a restaurant, and the chapter file has not changed by one byte. A court checks that the overlay is not a fork in disguise. A cohort is a folder of learners whose progress report is a narration; each learner's progress is a text file the institution keeps forever, and a pass cannot be forged, because its evidence is the fingerprint of the work handed in.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>

<p class="proof">Charter: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">education/CHARTER.md</a> · overlay guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a> · demo guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>.</p>

## The pedagogical engineering, taken from Zin {#pedagogy}

The learning system did not invent its pedagogy. It took it from the Zin project's pedagogical model, which was designed for West African learners first, and kept only what two of Zin's own documents agreed on. What was taken, what was refused, and what is still proposed:

<div class="cards">
<div class="card"><h3>Taken <span class="pill built">built</span></h3><p><b>Twenty-five skills in seven families</b> (formulate, express, patterns, see, know, govern, craft), each at three levels, Foundation, Practitioner, Expert, with one addition Zin lacked: an evidence field naming the guard that proves each level. <b>Three stages</b>: Encounter, Expression, Governance. <b>Five profiles</b> (young, student, professional, designer, decision maker) that change the depth and the examples, not only a note. <b>The recap cell</b> at the end of every chapter, in Zin's three cells: achieved, why it matters, coming next. <b>The tutor's three rules.</b> <b>Missions</b> set in Zindara, Niger, rebuilt so that each step runs real code. <b>Built, not tested</b>: a level is earned by a project that passes its guards, never by an exam.</p></div>
<div class="card"><h3>Refused, with the reason</h3><p>A gentle dialect to export from: not needed, because near-natural chains and instructions in your language are Softanza itself. Experience points and leaderboards: a pass is evidence, not a score. An exam-based certificate or signed credential: the fingerprint of the work handed in replaces it. A language-model tutor: refused by law; the tutor runs on the natural layer.</p></div>
<div class="card"><h3>Proposed for Softanza <span class="pill spec">proposed</span></h3><p>Three of Zin's principles are not yet surfaces of the reader, and this site proposes them. <b>Progressive revelation</b>: a concept appears only when the learner's previous work shows readiness, judged by the guards. <b>The ladder always visible</b>: on every page, where the learner stands, from S0 to S4, and what earns the next rung. <b>From the cell to its proof</b>: one gesture from any cell of the book to the guard that proves it in the repository, Zin's "pro bridge" made true by the platform's own evidence.</p></div>
</div>

<p class="proof">The reconciliation, line by line: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>, section 7 "The reconciled Zin design", and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a>. Zin's pedagogical model, learning program and teaching dialect are in a repository that is not public yet; the charter quotes them.</p>

<p class="way"><span>The Softanza way</span> Narrative before syntax; one idea at a time; errors as information about what still needs to be declared; declare, then see. And nothing is called learned unless a guard proved it.</p>

## What is missing, said plainly {#missing}

Zarma is not yet one of the course's languages. The French, Arabic and Hausa editions await their native reviewers. The reader runs on the desktop; a browser runtime for the cells is gated on a decision not yet taken. A Zarma edition is an invitation: the program is plain text, every cell runs, and the course's court will say whether the translation holds.
