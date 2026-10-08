---
title: The Softanzuter
title_html: The <i>Softanzuter</i>
kicker: A paradigm
lede: Not reactive computing on an abstract machine. A way of programming complex disciplines declaratively: patterns bound to code, faculties that share one state, and a mind built on them.
description: The Softanzuter paradigm: a definition, a ladder of four rungs from the pattern to the agent, two engines that run, a planned universal engine and the siblings that remain vision, each with its stage.
---

## The definition {#definition}

The library's design documents define it in the author's words, adopted and made mechanical:

> A Softanzuter is a computational representation of a thinking machine, based on one or many Regexuters, enabling it to identify and react to patterns of thought.

The unit is the pattern. A pattern over any medium is bound to code. Firing it is the reaction. The state the firing writes is itself a medium that further patterns match over, and every firing keeps its provenance, the answer to why. That is what separates it from a stream of data moving through time.

## The ladder {#ladder}

<ol class="steps">
<li value="0"><b>The pattern.</b> Pure recognition over a medium: a string, a list, a number, a matrix, a table, a time, a graph. It does nothing. <span class="rx-src">built · six pattern languages in the library</span></li>
<li value="1"><b>The Regexuter, and its siblings over other media.</b> A reflex arc: patterns bound to code, one engine per medium. Feed it data and it fires what matches and records a state with its time, its order, the match and the value it computed. A faculty, not a mind. <span class="rx-src">built · a Regexuter and a Listexuter run</span></li>
<li value="2"><b>The Softanzuter.</b> Many Xuters sharing one state and cascading to a fixpoint: the state one faculty writes is a medium the others match over. <span class="rx-src">designed, not built · today each trigger fires once and the Xuters do not share one state</span></li>
<li value="3"><b>The agent.</b> A Softanzuter embodied in a world, with a goal, a memory, tools and accountability. Agents contain Softanzuters, Softanzuters contain Xuters. <span class="rx-src">built · the cascade below runs</span></li>
</ol>

## Rung 1, run {#rung1}

<!--SHOWCASE:softanzuter:1-->

## Rung 3, run {#rung3}

The agent below keeps its memory as facts, and three skills chain: an order placed is cooked, then plated, then served. Each skill's result is a fact the next skill matches over, and the agent goes on until nothing changes.

<!--SHOWCASE:softanzuter:2-->

<p class="way"><span>The Softanza way</span> The mind is programmatic by default, and a model is one faculty among the others, never the definition of the mind. The industry's loop of a model that calls tools is the special case of this ladder: one faculty, no governance. Softanza offers the general case, locally.</p>

## What is still vision {#vision}

<div class="cards">
<div class="card"><h3>The universal engine <b>(planned)</b></h3><p>Any pattern language becomes a computation medium, with one interface to add triggers and computations, process data and read the dependencies. It is one of twelve paradigm engines in the engine's design.</p></div>
<div class="card"><h3>The Genetic Regexuter <b>(vision)</b></h3><p>Evolves a population of patterns against a fitness criterion. Its purpose was found later: inducing a pattern from examples, which <a href="byexample.html">answering by example</a> needs.</p></div>
<div class="card"><h3>The Quantic Regexuter <b>(vision)</b></h3><p>Holds a pattern in several states at once, each reading weighted and ranked. Its purpose: the solution space of the same protocol, where several answers are acceptable.</p></div>
<div class="card"><h3>The Linguistic Regexuter <b>(vision)</b></h3><p>Takes grammar rules as triggers.</p></div>
</div>

## One word, three meanings {#word}

In the design the Softanzuter is the universal medium of rung 2. In the engine as built, the module that carries the name is the agent's substrate, its slots and bounded mailboxes, which is the body of rung 3 and nothing of rung 2's cascade. In the intelligence architecture it is the thinking machine of many Xuters. The three are one ladder read from three sides, and the ladder above is how they fit.

<p class="proof"><b>in construction</b> Rung 2 is the missing middle: the cascade to a fixpoint and the shared state are not built, and the two engines of rung 1 run on their own. One narration of the Regexuter is published with its code, and part of it does not compile: its last blocks are the siblings' pseudo-code. That is why this page tells the siblings as vision.</p>

<p class="proof">Sources: the article <a href="narrations/stzregexuter-regex-as-computational-reactive-medium.html">the Regexuter as a computational reactive medium</a>; the guards <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/regexuter/06_computing_multiple_triggers.ring">06_computing_multiple_triggers.ring</a> and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/piagent_narrated.ring">piagent_narrated.ring</a>; the ladder is in <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a>.</p>
