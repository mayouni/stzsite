---
title: Seven languages, one door
title_html: Seven languages, <i>one door</i>
kicker: A rationale before it is a bridge
lede: A solution has layers, and each layer has a language that is best at it. Softanza chose seven, and one that orchestrates them. This page tells why each was chosen, how the door to them works, and what its own record cannot yet say.
description: The polyglot door of Softanza: why seven languages were chosen for seven layers of a solution, how foreign code is run and pasted, the difference between a facet of Haro and a door to a runtime, and the honest state of the door.
---

## The rationale {#why}

The door was never a way to run anything. It is a position: a solution has layers, each layer has a language best at it, seven were chosen and one orchestrates, and a programmer of any of the seven enters through the layer they know.

<ol class="steps">
<li value="1"><b>System performance: C.</b> Low-level operations and performance-critical algorithms.</li>
<li value="2"><b>Event-driven systems: NodeJS.</b> Asynchronous processing, real-time flows, API orchestration.</li>
<li value="3"><b>Scientific computing: Julia.</b> Mathematical modelling and numerical simulation.</li>
<li value="4"><b>Statistical analysis: R.</b> Data transformation, statistical modelling, plotting.</li>
<li value="5"><b>Logical reasoning: SWI-Prolog.</b> Rule-based systems, knowledge representation, backtracking.</li>
<li value="6"><b>Machine learning: Python.</b> Model training and the data-science ecosystem.</li>
<li value="7"><b>AI reasoning: the model.</b> Natural-language understanding and knowledge synthesis, as a faculty and never the definition of the mind.</li>
<li value="8"><b>Solution integration: Softanza's own language.</b> Business-logic orchestration and cross-domain data transformation.</li>
</ol>

The enemy it names is orchestration friction: developers spending a large part of their effort on the plumbing between languages. The answer for the agentic age is to neither force a developer to master every domain nor surrender to code generated for them, but to craft abstractions that expose each domain's power through simple functions.

## Two doors {#doors}

<div class="cards">
<div class="card"><h3>Run foreign code where it lives</h3><p>The code is written to a file, the runtime is run as a process, and the result is read back and converted. The verbs are to set the code, execute it, read the result, read the duration of the last call, and read the trace of the calls. The runtimes are found by paths from the configuration.</p></div>
<div class="card"><h3>Paste foreign code where you are</h3><p>Find a solution on the internet in another language, paste its code, and make little changes. Shims exist for C, C#, JavaScript, Perl, PHP, Python and SQL.</p></div>
</div>

## A facet and a door are different things {#facet}

Two things will carry the word language, and they must not be confused. A <b>facet</b> of Haro is a surface: one grammar, judged by one court, worn in another syntax, so a programmer writes Softanza in a syntax they already know. A <b>door</b> is a runtime: real Python with its libraries, real R, real Prolog, reached from the solution and returning its result into the world. The facet brings the programmer. The door brings the ecosystem. They meet in the same person.

<p class="proof"><b>named</b> Haro's planned facets, in the author's statement of 2026-10-07, are its present face today and, planned, Python and JavaScript. The language's charter does not name them yet, so this page records the plan as the author's and not as a specification.</p>

## The honest state {#state}

<p class="proof"><b>in construction</b> The door is process-based today: it runs by spawning and by files. An engine bridge that would handle marshalling and process management is planned, and its list of languages (five) does not match the rationale's (eight). The door has fifty-eight guard files, with a run script per language. The last recorded run of them shows thirty-eight failures and no pass, and several of their promises cannot match by construction, because they name a random temporary file or a duration. So the run record does not say whether the door works, and this page runs nothing: it will not show a run that its own guards cannot confirm.</p>

The door's performance was set against the field in an article of the library, which publishes the host's losses: a million numbers sorted took far longer through the host than in Python. That measurement predates the present runtime and is owed a re-run, and a loss that stands will be published as it stands.

<p class="proof">Sources: the articles <a href="narrations/stzexcis-polyglot-programming-in-ring.html">polyglot programming</a>, <a href="narrations/stzexterlib-domain-driven-polyglot-programming.html">domain-driven polyglot programming</a> and <a href="narrations/stzexcis-performance-battle.html">the performance battle</a>, whose code mostly does not run in this site's runner for lack of the runtimes. The record was read from the library's files by an outside assessment on 2026-10-07; nothing was run for this page.</p>
