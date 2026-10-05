---
title: Learn by yourself
title_html: <i>I learn</i> by myself
kicker: Education · the path, the desk, the ladder
lede: You need a laptop, the library, and the afternoon. The path goes from a first sentence to a project that earns a level, in your language, and a tutor that asks questions when you are stuck. Nobody marks you: your own program is run.
description: Learning Softanza by yourself: the fifteen chapters, the learner's desk, the five levels earned by projects, and a tutor that asks.
---

## The path {#path}

The fifteen chapters of the book are one story, told in cells you can run. Read a cell, run it, change it, run it again. The first four chapters give the whole mental model; the rest widen it.

<ol class="narr">
<li>Find, then apply</li><li>A first sentence</li><li>Read the name as a sentence</li><li>Say it in your language</li><li>One object, any structure</li><li>Walk, ask, produce, act</li><li>Declare what, not how</li><li>Patterns in text</li><li>Patterns in structure</li><li>When code meets cells</li><li>Draw the answer</li><li>Teach a world</li><li>The gap question</li><li>An agent that cannot hurt</li><li>Write a narration</li>
</ol>

<p class="proof">Open <a href="../reader.html">the interactive book</a>, or read <a href="book.html">the book's page</a>: each chapter has a <a href="book.html#proof">proof page</a> that records its run, cell by cell, in its four editions. Chapter 12 is where you build a world of your own, and chapter 15 is where you write a chapter.</p>

You choose three things, and can change them at any time: **the language** of the chapters, the checker and the tutor (English, French, Arabic, Hausa; the last three are drafts, <a href="education-record.html#limits">0 of 35 units reviewed by a native speaker</a>); **the world** the examples reason over (a restaurant, a cooperative, or a school); and **the pace**. The mental model in five questions is on the <a href="learn.html">Learn page</a>.

## The desk {#desk}

The learner's desk is one tool of the library, <span class="mono">learn.ring</span>, run from its folder with your folder and one verb. It tells you where you are, judges a program you wrote, answers a question as a tutor would, and judges the project that earns a level. Every verdict is the checker's: it **ran** your file in a fresh process, and nobody read it.

<pre>learn.ring  &lt;your folder&gt; status
learn.ring  &lt;your folder&gt; submit &lt;exercise id&gt; &lt;your file&gt;
learn.ring  &lt;your folder&gt; ask &lt;exercise id&gt; "&lt;your question&gt;"
learn.ring  &lt;your folder&gt; project &lt;project id&gt;

options:  --lang en|fr|ar|ha   --world workplace|cooperative|school   --overlay &lt;folder&gt;</pre>
<p class="proof">The usage as the library writes it: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/tools/learn.ring">education/tools/learn.ring</a>. The exit code is 0 when a submission passed and 2 when it was refused.</p>

An exercise is a short task with a promise: the lines your program must print. This one is the first of the course:

<pre>The kitchen received these orders today:

    [ "tea", "rice", "tea", "fish", "rice", "tea" ]

Print the list of dishes to cook, each one once, in the order in which
it was first ordered.

PROMISE   [ "tea", "rice", "fish" ]</pre>

Your answer is checked by running it. A known-wrong answer fails and a known-right one passes: the exercise is not accepted into the course until both have been seen to do so.

## The tutor {#tutor}

When you are stuck, you ask. The tutor answers with a question about the gap between what you wrote and what the exercise needs. It is a program of the library, with three rules it cannot break: it does not write your code, it does not explain what you have not yet met, and it does not give the answer before you have tried.

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
<p class="ran">run on 2026-09-30 at 23:10, the education demo, scene 4</p>

If you do not know a name in the library, ask the library instead: an object answers <span class="mono">Ask("how do I remove duplicates")</span> with the methods that do. <a href="ask.html">Ask the library</a>.

## The ladder {#ladder}

You do not sit an exam. A level is earned by a **project** you build in your own folder, and a guard judges it: it runs the project, says which promises are kept, and when one is not, says why in words.

<div class="cards">
<div class="card"><h3>S0 · Explorer</h3><p>After chapter 4. <b>Project:</b> a five-cell narration over a list of your own, where every cell runs and every cell carries a promise that holds.</p></div>
<div class="card"><h3>S1 · Builder</h3><p>After chapter 7. <b>Project:</b> a small tool over your workplace, its conditions declared as data (a rule such as <span class="mono">{ @item &gt; 20 }</span> in a file), not written into the code.</p></div>
<div class="card"><h3>S2 · Craftsperson</h3><p>After chapter 11. <b>Project:</b> a report over a real data file, with the patterns it finds, a table and a picture.</p></div>
<div class="card"><h3>S3 · Architect</h3><p>After chapter 14. <b>Project:</b> a world you taught, with at least five facts, questioned by an agent you govern, admitted by the court, every act of which can be reversed.</p></div>
<div class="card"><h3>S4 · Master</h3><p>Chapter 15. <b>Project:</b> a new chapter for this course, in two languages, whose guard is green.</p></div>
</div>

<p class="proof">Each rung's project is judged by a guard shown run on a wrong sample and a right one: <a href="learn.html#ladder">the ladder on the Learn page</a>. Where you stand is named by the library on your machine, from the evidence in your folder; this site cannot see that folder.</p>

## When you finish {#end}

You have a folder of plain text that is yours: your programs, and a progress file that records each fact with its evidence. Take it to the next laptop, keep it in a repository, show it to an employer. The next step is the other door: <a href="education-teach.html">teach what you learned</a>, which is chapter 12 and 15 turned outward.
