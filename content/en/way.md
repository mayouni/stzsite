---
title: The Softanza way
title_html: The Softanza <i>way</i>
kicker: How to think, how to write, how it is judged
lede: One discipline, for a person and for an agent. Think the problem in seven steps, write each step in fourteen rules, and let something judge the result.
description: The Softanza way: the mental model in seven steps, the fourteen rules of writing that serve each step, the three widenings of the model, and where each part is judged, with the part not yet judged named.
---

## Thought and code, side by side {#slide}

The first slide of 2022 on expressiveness puts a programmer's steps of thought on the left and, on the right, the same steps as code, as if the text on the left had been copied and pasted and Softanza asked to run it. That slide is the whole discipline on one page. This page is that slide, made to run.

Every step has a rule or two of writing that serves it, and every rule serves some step. A line that follows the rules is a step of the model made visible; a line that breaks them hides a step.

## Seven steps, each written {#steps}

<!--STEPS-->

The rules are numbered as on <a href="craft.html#rules">the page that states them</a>. Here are the steps run on one small problem: clean the empty items out of a list.

<!--SHOWCASE:way:1,2,3-->

<p class="way"><span>The Softanza way</span> Each step is one question asked of one object, and each answer is read under its arrow. A beginner can follow the seven steps in order, an expert can skip to the verb that does it all, and an agent is held to the same shape.</p>

## Three widenings {#widenings}

The seven steps are the core. The library widens them in three directions, each told on its own page.

<div class="cards">
<div class="card"><h3>The world the problem lives in</h3><p>Knowledge sentences and small languages say what the objects are: <code>_("Apple").IsA(:Fruit)_</code>. That is the semantic model beside the mental one. See <a href="natural.html">natural, and executable</a>.</p></div>
<div class="card"><h3>The frame the act depends on</h3><p>Scope-oriented programming names the invisible frame of a behaviour, closes it into a few named scopes, and lets the verb choose the scope at the call.</p></div>
<div class="card"><h3>The gap, for someone who does not code</h3><p>When the person or the agent does not know, Softanza asks, and the answer is judged before it is admitted. See <a href="wise.html">wise coding</a>, and <a href="byexample.html">answering by example</a>.</p></div>
</div>

## Where it is judged {#courts}

A discipline that nothing judges is advice. The courts that exist, and the one that does not, are these.

- **The learner.** The course teaches the thinking first, the families called Formulate and Express, and a ladder of five levels is earned by projects that a guard checks. See <a href="book.html">the book</a> and <a href="education.html">education</a>.
- **The written answer.** The test form of the library, a call with its answer under an arrow, is read as a promise and compared with what really printed.
- **The library's own code.** Fourteen house rules run over a graph of the code and judge the library's naming of its own methods.
- **The forms of the vocabulary.** The grammar of the function forms is declared as data in the charter of Haro, which is in construction, and it judges the names the library ships.
- **A program written with the library.** <b>No court yet (designed).</b> The fourteen rules as checks over a snippet, run on every example on this site and on every line an agent proposes before it is shown, are specified and not built.

## The agents read the way first {#agents}

The files made for agents carry the discipline as data, ahead of the list of methods, so that an agent reads the way before the names, the way a learner does in the first chapter: <a href="../llms.txt">llms.txt</a> and <a href="../agents/index.json">agents/index.json</a>. Both are generated from the same file as this page and the craft page, so one change reaches every surface.

Every callout on this site headed <i>The Softanza way</i> links here.

<p class="proof"><b>in construction</b> The steps and rules are read from the library's articles, its tests and the 2022 slides, and are stated here as rules. What nothing judges yet is the code a person or an agent writes. No visitor and no agent has yet been shown this page, so the claim that an agent learns the way from it, and does not learn a reduced dialect, waits for a measured session.</p>

<p class="proof">Sources: the article <a href="narrations/stz-mental-mode-narration.html">the Softanza mental model</a>, whose seven steps these are; the article <a href="narrations/stz-functions-as-linguistic-expressions.html">functions as linguistic expressions</a>, from which most of the rules are taken.</p>
