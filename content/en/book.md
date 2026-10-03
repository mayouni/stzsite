---
title: The book
title_html: The interactive <i>book</i>
kicker: Step 2 of 3 · fifteen chapters, four languages
lede: The Elementary Introduction is a course of fifteen chapters, in English, French, Arabic and Hausa. It is read in **the reader**, a page of this site built by running every cell of every chapter in every language: the build is red if one cell fails or one exercise's promise is not kept.
description: The Softanza interactive book: fifteen chapters in English, French, Arabic and Hausa, every cell run.
---

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

## The proof of each chapter {#proof}

<!--PROOF-->
