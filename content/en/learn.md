---
title: The Learning System
title_html: The Learning <i>System</i>
kicker: Learn
lede: Two courses of fifteen chapters, in English, French, Arabic and Hausa. Every cell runs. Every exercise is a promise checked by running it. No output is stored.
description: The Softanza Learning System: fifteen chapters in four languages, missions, kits for institutions, cohorts and a tutor that asks questions instead of giving the answer.
---

## The law of the course

An ordinary course page shows outputs somebody copied one day. Here the page is **built by running** every cell of every chapter in every language, and the build is red if one cell fails or one promise is not kept. What you read below was built tonight.

<div class="figures">
<div class="figure"><b>15 × 4</b><span>chapters × languages, the Elementary Introduction</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters">chapters/</a></div>
<div class="figure"><b>15 × 4</b><span>chapters × languages, the mathematics course</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/program/courses/math/chapters">math/chapters/</a></div>
<div class="figure"><b>3</b><span>teaching worlds: the restaurant, the cooperative, the school</span></div>
<div class="figure"><b>11</b><span>guards that judge the system itself</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test/education">test/education</a></div>
</div>

## The reader, built tonight

The reader below was produced by the tool <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/tools/build_reader.ring">build_reader</a> on 2026-09-30 at 23:02, in 3 minutes 22 seconds: fifteen chapters in the four languages and three world pages, all green. Pick the language in its menu; Arabic reads right to left. Its cells ran on the desktop when the page was built, and the page says so on every cell.

<div class="embed"><div class="embed-bar"><a href="../reader.html">Open the reader full screen</a><span>Elementary Introduction · en · fr · ar · ha</span></div><iframe src="../reader.html" title="The Softanza course reader, built on 2026-09-30" loading="lazy"></iframe></div>

<pre>BUILD elementary-introduction in en, fr, ar, ha: 15 of 15 chapters, 3 of 3 world pages
  chapter 1 find-then-apply: en fr ar ha
  chapter 2 a-first-sentence: en fr ar ha
  ...
  chapter 14 an-agent-that-cannot-hurt: en fr ar ha
  chapter 15 write-a-narration: en fr ar ha
  world cooperative: en fr ar ha
  world school: en fr ar ha
  world workplace: en fr ar ha
WROTE reader.html
real    3m22.821s</pre>

## The same chapter in Hausa and in French

Chapter 1 opens with the same sentence in the four languages, and the same cell runs in each. The French, Arabic and Hausa editions carry the note that they await review by a native speaker: it is written on the page, not hidden.

<div class="pair">
<div><h4>Hausa · Nemo, sannan ka aiwatar</h4><p>Kowane wurin aiki yana karɓar buƙatu: gidan abinci yana karɓar oda, banki yana karɓar tikiti, kuma buƙata ɗaya takan zo fiye da sau ɗaya. Wannan babin yana maganin buƙatun da aka maimaita ta hanyar Softanza.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.ha.md">01-find-then-apply.ha.md</a></p></div>
<div><h4>French · Trouver, puis agir</h4><p>Tout lieu de travail reçoit des demandes : un restaurant reçoit des commandes, une banque reçoit des tickets, et la même demande arrive souvent plusieurs fois. Ce chapitre traite les demandes répétées à la manière de Softanza.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/program/courses/elementary-introduction/chapters/01-find-then-apply.fr.md">01-find-then-apply.fr.md</a></p></div>
</div>

## In your language, literally

The library's natural layer understands an instruction in the four languages of the course and runs it. The demonstration below ran tonight; it is one of the twenty proofs of the decision-makers' demo.

<div class="run"><div><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )
? @@( NaturallyIn("ha", "Yi jeri dauke [ 5, 3, 5, 1 ] cire maimaitattu").Result() )
? @@( NaturallyIn("ar", "أنشئ قائمة مع [ 5, 3, 5, 1 ] أزل التكرارات").Result() )</pre></div><div class="out"><div class="lbl">Output</div><pre>[ 5, 3, 1 ]
[ 5, 3, 1 ]
[ 5, 3, 1 ]</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo</a>, last line: "DEMO: 20 proved, 0 not proved", in 49 seconds</p>

## A tutor that asks, and does not give the answer

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

## For an institution: an overlay, never a fork

A bank, a university, a school lays **one overlay folder** on the program: its world, its chapters, its exercises, its skills, its language, its governance. The course then reasons about its bank and not about a restaurant, and the chapter file has not changed by one byte. A court checks that the overlay is not a fork in disguise. A cohort is a folder of learners whose progress report is a narration; each learner's progress is a text file the institution keeps forever, and a pass cannot be forged, because its evidence is the fingerprint of the work handed in.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>

## What is missing, said plainly

Zarma is not yet one of the course's languages. The four current editions are English, French, Arabic and Hausa, and the Hausa one awaits its native review. A Zarma edition is an invitation: the program is plain text, every cell runs, and the course's court will say whether the translation holds.

<p class="proof">Charter and plan: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">education/CHARTER.md</a> · overlay guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a> · demo guide: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>.</p>
