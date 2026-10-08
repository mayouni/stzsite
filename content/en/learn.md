---
title: Learn
title_html: <i>Learn</i>, in three steps
kicker: Step 1 of 3 · find first, then apply
lede: Learning Softanza goes in three steps: a short introduction that gives you the mental model, an interactive book where every cell runs, and the complete documentation generated from the library itself. This page is the first step.
description: How to learn Softanza, step 1: the mental model, find first, then apply.
---

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
<p class="ran">run on 2026-09-30 at 23:11, Softanza at commit 0e72e2e2c. The full introduction is the article <a href="narrations/stz-mental-mode-narration.html">the Softanza mental model</a>.</p>

Three habits complete the model. A method that ends in <b>-ed</b> returns a copy and leaves the object alone; the same verb without it changes the object. A method that ends in <b>Q</b> returns an object you can keep asking, so a sentence can chain. And if you do not know a name, ask: an object answers <code>Ask("how do I remove duplicates")</code> with the methods that do.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("softanza is a platform for makers").SpacesRemovedQ().UppercaseQ().Boxed()</pre></div><div class="out"><div class="lbl">Output</div><pre>┌──────────────────────────────┐
│ SOFTANZAISAPLATFORMFORMAKERS │
└──────────────────────────────┘</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26</p>

## The ladder {#ladder}

<!--LADDER-->

## Learning, teaching, running a programme {#education}

Softanza teaches itself with the system this page has shown, and the same system serves a teacher and an institution. Take the door that is yours:

<div class="doors doors-wide">
<a class="door big" href="education-self.html"><div class="who">I learn by myself</div><div class="what">The path, the desk, the ladder</div><div class="how">From the first sentence to a project that earns a level, with a tutor that asks.</div></a>
<a class="door big" href="education-teach.html"><div class="who">I teach, or I design courses</div><div class="what">A cohort, an exercise, a chapter of your own</div><div class="how">What the teacher does, what the program does, and how a course is written.</div></a>
<a class="door big" href="education-programme.html"><div class="who">I run a programme or an institution</div><div class="what">An overlay, cohorts, ownership</div><div class="how">Your world and your languages over one core, a court that refuses a fork, and a fifteen-minute demo.</div></a>
</div>

<p class="proof"><a href="education.html">Education</a>.</p>

<p class="way"><span>The Softanza way</span> The human is the parser. A line reads like a sentence because it was designed to be read, not only to be executed.</p>
