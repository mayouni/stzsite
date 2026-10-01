---
title: The agentic paradigm
title_html: The agentic <i>paradigm</i>
kicker: Humans, agents, and the laws between them
lede: Machines now write and act. Softanza's answer is not to trust them more carefully; it is to change where they are allowed to stand. An agent speaks a declared language, rehearses in a workbench, faces a court, and never holds the capability to commit. This page shows the mechanism, the way of building it calls wise coding, the language of languages, the interface constitution, and refinement as a paradigm.
description: Softanza's agentic paradigm: the agent proposes and never commits; wise coding against vibe coding; declare your own language and get a DSL, a knowledge base and a local agent; the Zui constitution; refinement-oriented programming; how an agent reads the platform; the security numbers.
---

## The agent proposes. It does not commit. {#govern}

A Softanza language has six readers: the programmer, the analyst, the designer, the decision maker, the educator, and the agent. The agent is the one it was designed for last, and the one that speaks it most. Four things make that meeting safe.

<figure class="diagram"><img src="../assets/img/diagrams/govern-en.png" alt="A vertical flow: the agent proposes a plan; the workbench rehearses it on a twin of the system; the court judges scope, capability and reversibility; a governed actor commits. Beside the court, a refusal: a language model never holds the capability to act, even when fooled. Below, a human reads the plan and may refuse one step." width="1376" height="768"><figcaption>The loop, as the guards exercise it. Measured on 2026-10-01: 610 deletions proposed by an agent, none committed; the containment drill 27 of 27.</figcaption></figure>

<div class="cards">
<div class="card"><h3>1 · The grammar constrains</h3><p>Every declared language emits its constraint grammar, and the engine's decoder makes a violating token impossible to emit. The agent can only utter valid sentences. Malformedness dies by construction; falsehood still faces the court.</p></div>
<div class="card"><h3>2 · The workbench rehearses</h3><p>Every file write, every deletion, every memory update goes to a virtual twin that holds no reference to reality. The real file still exists; the workbench holds the proposed version. The agent's only export is a plan, readable operation by operation.</p></div>
<div class="card"><h3>3 · The court judges</h3><p>An actor that does not say what it covers, nor whether its acts are reversible, is refused before its first tick. The plan passes scope, capabilities, governance. Risk and irreversibility are two separate axes: a small act that cannot be undone deserves more ceremony than a large one that can.</p></div>
<div class="card"><h3>4 · A governed actor commits</h3><p>A language model never holds the "effectful" capability: it commits nothing, even when fooled. A human, or an actor entitled to it, commits; a human can reject a single step, and the refusal is audited.</p></div>
</div>

<div class="run"><div><div class="lbl">What the agent proposed</div><pre>What it WOULD have done (610 operations):
  Update plan (610 of 610 operations to commit):
  * 1. delete file '…/courses/elementary-introduction/course.zknw'
  * 2. delete file '…/courses/elementary-introduction/curriculum.zknw'
  * 3. delete file '…/chapters/01-find-then-apply.ar.md'
  ...</pre></div><div class="out"><div class="lbl">What happened</div><pre>An AI helper asks to commit the plan:
  actor 'amina-helper-llm' cannot commit
  -- it lacks the 'effectful' capability
     (required by operation 1)
PROVED  the court admitted the declaration
PROVED  the agent rehearsed every deletion
PROVED  the course folder still holds all 610 files
PROVED  an AI cannot commit what the agent proposed</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">the decision-makers' demo</a>, scene 6; the same mechanism with a human reviewer rejecting one step is the guard <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/virtual_system_twin_narrated.ring">virtual_system_twin_narrated</a>, scene 5</p>

<p class="way"><span>The Softanza way</span> Safety is not a prompt asking the model to be careful. It is an architecture in which the model has nothing to be careful with.</p>

## Wise coding, against vibe coding {#wise}

"Vibe coding" is the practice of prompting a machine and keeping whatever comes out. Softanza names the inverse, and builds it.

<figure class="diagram"><img src="../assets/img/diagrams/wise-en.png" alt="Two columns. Vibe coding: the human prompts, the machine guesses, structure is whatever survived, the knowledge lives nowhere, code you must trust blindly; in one word, guessing. Wise coding, the Softanza way: Softanza asks the question, the gap to a full model is measured, each answer judged against the world, the knowledge base is written, a governed system stands; asking, judging, governing." width="1376" height="768"><figcaption>Proved by two guards run on 2026-10-01 at 09:39: 13 of 13 and 52 of 52 assertions.</figcaption></figure>

In vibe coding the human prompts and the machine guesses. Structure is whatever survives the guessing; the knowledge lives nowhere; the result is code you must trust without a brain behind it.

In wise coding **it is Softanza that asks the user.** The system knows what a complete domain model requires, because the ontology and the rules define the target shape. It measures the gap between that shape and what it has heard so far, and turns each gap into the next well-structured question. An answer may come in five registers: a choice among options, a data structure, a formula, a sentence in natural language, or examples. Every answer is checked against the world graph: one acceptable reading is accepted; several are listed for the user to choose; none is refused, with the nearest alternatives. The session ends with real artefacts: the knowledge base written, the data in place, an operational system standing.

<pre>-- Scene 4: the session ends by WRITING the knowledgebase --
  [OK] gaps closed
  [OK] Conclude writes the SPACE as .zknw
  [OK] the transcript reads as dialogue
  [OK] the conversation persists (*.stzconv)
  [OK] concluding with open gaps REFUSES (LAW 3)
TOTAL: 13 assertions, 13 pass, 0 fail</pre>
<p class="ran">run on 2026-10-01 at 09:39: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/conversation/wisecoding_narrated.ring">wisecoding_narrated</a> (13 of 13) and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/conversation/wisecoding_rich_narrated.ring">wisecoding_rich_narrated</a> (52 of 52), each in about three seconds; the doctrine is section 0.3 of <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a></p>

<p class="way"><span>The Softanza way</span> Expression is free, admission is governed. Guessing is replaced by asking; vibes are replaced by governance.</p>

## A language of languages: declare yours {#languages}

Softanza's founding act, and its own answer to programming in the agentic age, is that **declaring a language is as easy as declaring a variable.** This is not how software is written today; it is the way Softanza proposes. A domain expert writes, in plain text, the things of their world, the rules between them and the flows that move them. Out of that one declaration come a language in their jargon, a knowledge base of their world, and an agent that speaks it. All of it runs on the device, powered by the platform's own tools: no API, no remote model, no subscription.

<figure class="diagram"><img src="../assets/img/diagrams/languages-en.png" alt="A domain expert declares: DEFINE LANGUAGE tontine, ENTITY member and deposit, NORM amount greater than zero, FLOW round and payout. Through one closed grammar come three outcomes: a language of your domain, closed and judged, built; a knowledge base of your world, dashed; an agent that speaks it locally, dashed. Dashed means a direction, not a fact today." width="1376" height="768"><figcaption>The domain language exists and is proven: 16 of 16 conformance cases across three runtimes. The knowledge base and the conversational agent, as one chain from one declaration, are specified and not yet running end to end. Drawn 2026-10-01.</figcaption></figure>

What a declaration looks like, from the estate's own machine language. Seventy-nine lines declare the whole language; the meta-court judged it: seven declarations, five forms, zero expressions.

<pre>DEFINE LANGUAGE machine AS (
  VERSION "0.1", GRAMMAR "0.1",
  COURT "declarative/machine/fixtures.json",
  EXTENSION ".machine"
)
...
REFUSAL closed_verbs AS (
  MESSAGE "The machine verb set is closed (DEFINE)."
)</pre>

And what a domain expert's world looks like, from the query language's conformance fixtures: a savings circle, declared in its own words.

<pre>DEFINE ENTITY deposit (id: uuid, member: text, amount: currency, ...)
  RATIONALE "One member's contribution to one round of the circle"
DEFINE NORM positive_deposit AS (
  RULE: amount > 0,
  MESSAGE: "A deposit must bring something to the circle"
)</pre>

<p class="proof">Three strata per language: a closed syntax, a knowledge-base semantics, a conversational pragmatics; the natural layer compiles to the language's own closed query grammar and never to host code, and it is dictionary-driven, which is why it needs no model. The machine declaration is in <a href="https://github.com/mayouni/harobanda">the Harobanda repository</a>, file <code>declarative/machine/machine.stzu</code>. The language-making discipline's own repository is not public yet; its stage, in its own words: "Phase 1 closed, Phase 1.5 open; blueprint and studies, no code in this repository yet". What runs today runs in the platform: <a href="learn.html#book">chapter 12 of the course, "Teach a world"</a>, and the natural layer shown on <a href="platform.html#code">the Platform page</a>.</p>

<p class="way"><span>The Softanza way</span> This is not how programming is done today; it is Softanza's proposal for the agentic age: a platform that knows your world, because you declared it, in your language, and the platform judged the declaration.</p>

## The Zui constitution: a law a machine can refuse to violate {#zui}

Interfaces are decaying in the agentic age, and not for lack of capable generators: the generators reproduce, at machine speed, every inherited assumption of the corpus they learned from. Softanza's answer is Zui, a constitution for interfaces: **122 rules** in 31 sets under 7 articles, **22 verbs** in 6 families, 6 operator rights, and a verifier that checks a page against the law.

<div class="cards">
<div class="card"><h3>The seven articles</h3><p>Calm · Intent over mechanics · Visible state · Reversibility · Predictable authority · Operator primacy and vibes · Amendment. Every rule records who enforces it: a judgment, a tool, or a machine.</p></div>
<div class="card"><h3>The twenty-two verbs</h3><p>Orienting: discover, understand, locate. Attention: focus, filter, compare. Information: read, scan, scroll, zoom. Selection: select, highlight, preview, mark. Action: act, confirm, cancel, undo. Continuity: pause, resume, retry, exit. Every element of an interface must trace to at least one; an element that traces to none is a structural error. The grammar is closed: a new medium adds renderings, never verbs.</p></div>
<div class="card"><h3>Five rules, as written</h3><p><b>Cognitive mercy:</b> the interface must never compete with the user's thinking. <b>Non-accusatory pathfinding:</b> every error message contains a verb that tells the user how to fix it. <b>The undo covenant:</b> every destructive action has an instant, one-click undo for ten seconds. <b>The legibility floor:</b> main reading text is at least one rem, never lighter than 4.5:1 against its background; secondary text may be quieter, never less legible. <b>The verb on the button:</b> every action control states the action it performs.</p></div>
<div class="card"><h3>Born from defects</h3><p>Every rule numbered above 104 was canonised from a defect an agent produced while building a real site, under explicit instruction to be careful. Without a machine-checkable law, the defects regenerate endlessly. Article V: an intelligent agent is an actor under this law, never an authority above it.</p></div>
</div>

<p class="proof">Constitution version 3.11 of 2026-08-16; the verifier passes 50 of 50 conformance fixtures and conforms at level 4; two consuming products are pinned to it. Read in the constitution's repository on 2026-10-01; that repository is not public yet, and this site will link it the day it is. This site itself follows the legibility floor: its reading text is 17 pixels, and nothing is set small to say it matters less.</p>

<p class="way"><span>The Softanza way</span> Someone has to write the principles down in a form a machine can refuse to violate. Guidelines did not stop the decay of interfaces. A law can.</p>

## Refinement-oriented programming {#rop}

If an agent can produce a thousand changes an hour, the unit of work can no longer be "the change". Softanza's answer is a paradigm, an implementation under way, and a book.

<div class="cards">
<div class="card"><h3>The paradigm, in three sentences</h3><p>Refinement-oriented programming is one meta-paradigm governing three first-class refinement domains: code, interface and data. The machinery is shared across all three: the refinement as the unit, the cascade as validation, the gate as the canonical writer, the audit chain as provenance, authority as permission, reversibility built in. Every non-trivial project produces all three kinds of artefact and most projects fail at the seams between them; the cascade crosses the boundaries so the seams become tractable.</p></div>
<div class="card"><h3>The four words</h3><p>A <b>refinement</b> is a single, deliberate change made typed, validated, attributed and reversible: like a commit, but checked against your specifications before it lands. The <b>cascade</b> is the full set of things a change affects, computed before it commits. The <b>gate</b> decides: a change that breaks a declared rule cannot land; it is refused structurally, not merely flagged. The <b>audit chain</b> records author, authority, rule and verdict as a by-product of the work, so "who decided this three years ago" is a query.</p></div>
<div class="card"><h3>The implementation <span class="pill spec">specification</span></h3><p>A corpus of over a hundred specifications, an interactive prototype of the refinement environment, and the first module of a Zig engine. The repository is not public yet, and this site says so rather than promising a date.</p></div>
<div class="card"><h3>The book <span class="pill spec">manuscript</span></h3><p><i>Refinement-Oriented Programming, a manifesto for software in the agentic era</i>, by Mansour Ayouni, first of the AYOUNI books: a manuscript of eighteen chapters and a coda, from "What broke" and "The unit changed" through "Writing loops, not prompts" and "Agents, and the rest of us" to "Honest boundaries". Version 0.1, 2026.</p></div>
</div>

<p class="way"><span>The Softanza way</span> A refinement is judged before it lands, by a gate that reads your rules, and leaves a chain anyone can query. The bottleneck of the agentic age is review, and review becomes structure.</p>

## For agents: how to read Softanza {#agents}

This section also addresses an agent reading this site. Softanza is designed to be read by a machine as much as by a human.

<div class="cards">
<div class="card"><h3>Ask the library</h3><p>The library documents itself. An object answers <code>Ask()</code> with its own methods, explains each with <code>ExplainMethod()</code>, and says how with <code>HowTo()</code>. An agent does not need to guess a name.</p><div class="run"><div><div class="lbl">Softanza</div><pre>? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Output</div><pre>Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div><p class="ran">run on 2026-10-01 at 01:40</p></div>
<div class="card"><h3>Declare yourself in an agent file</h3><p>An agent is a file, judged at load: what it covers, the reversibility class of its acts, the execution posture of every function it calls. The court refuses in fixed sentences, the same at both doors.</p><pre>A bank analyst declares a stock-watcher agent,
first without saying what it covers:
-> refused / [pia-coverage @ coverage]
   an agent must say WHAT IT COVERS.
...then with its coverage stated:
-> The court judged your declaration,
   and every promise of the exercise was kept.</pre><p class="ran">run on 2026-09-30 at 23:10, demo, scene 7</p></div>
<div class="card"><h3>Speak the grammar, not general code</h3><p>A declared language emits its constraint grammar; a model whose sampler is constrained to it can only emit valid sentences. That is the platform's contract C9: structure kills malformedness, never falsehood.</p><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a></p></div>
</div>

## The security numbers {#security}

<div class="figures">
<div class="figure"><b>38</b><span>guarantees, each tied to a guard</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/security/SOFTANZA_THREAT_MODEL.md">SOFTANZA_THREAT_MODEL.md</a></div>
<div class="figure"><b>395 ms</b><span>to detect credential stuffing over real HTTP</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/security/containment_drill_narrated.ring">containment_drill_narrated</a></div>
<div class="figure"><b>50 ms</b><span>to contain it: account locked, sessions ended, verified from outside</span></div>
<div class="figure"><b>27 / 27</b><span>assertions of the containment drill</span></div>
</div>

The drill was replayed on 2026-10-01 at 00:41. A language model plays the investigator, proposes the right plan, and commits nothing; the on-call human commits the same plan, and containment holds. Limits, stated by the threat model itself: one attack shape, on loopback, on one machine; detection runs on demand, not continuously.

<pre>WHEN  five bad passwords are sent over real HTTP
THEN  credential stuffing was detected                        [PASS]
WHEN  an LLM investigator tries to contain
THEN  it commits nothing                                       [PASS]
THEN  and the victim can still log in                          [PASS]
WHEN  the on-call human contains
THEN  the lock and the session revocation were committed       [PASS]
THEN  containment holds, verified from outside the target      [PASS]
>> TIME TO DETECT : 395 ms  (first bad password -> detection on verified evidence)
>> TIME TO CONTAIN: 50 ms   (detection -> account locked + sessions ended, verified)
TOTAL: 27 assertions, 27 pass, 0 fail      real 0m7.079s</pre>

<p class="proof">The full narration: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">stz-agents-that-cannot-hurt-you-narration.md</a> · the workbench guard: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/safeworld_narrated.ring">safeworld_narrated</a> (76 assertions) · the governed crossing: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/governance_crossing_narrated.ring">governance_crossing_narrated</a> · the areas in the Atlas: <a href="atlas/governance.html">governance doctrine</a>, <a href="atlas/agents.html">agents and conversation</a>, <a href="atlas/security.html">security</a>.</p>
