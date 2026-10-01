---
title: The agentic paradigm
title_html: The agentic <i>paradigm</i>
kicker: Agents
lede: Humans and agents meet in declared languages, small, closed, judged. A grammar constrains what an agent can emit; a court judges what it proposes; a safe world lets it rehearse without touching reality; only a governed actor commits.
description: Softanza's agentic paradigm, for humans and for agents: the constrained grammar, the workbench, the court, the governed commit, and how an agent reads the platform.
---

## The agent, sixth reader of every Softanza language

A Softanza language has six readers: the programmer, the analyst, the designer, the decision maker, the educator, and the agent. The agent is the one the language was designed for last, and the one that speaks it most. Three things make that meeting safe.

<div class="cards">
<div class="card"><h3>1 · The grammar constrains</h3><p>Every declared language emits its constraint grammar, and the engine's decoder makes a violating token impossible to emit. The agent can only utter valid sentences of the language. Malformedness dies by construction; falsehood still faces the court.</p></div>
<div class="card"><h3>2 · The workbench rehearses</h3><p>Every file write, every deletion, every memory update goes to a virtual twin that holds no reference to reality. The real file still exists; the workbench holds the proposed version. The agent's only export is a plan, readable operation by operation.</p></div>
<div class="card"><h3>3 · The court judges, the actor commits</h3><p>An actor that does not say what it covers, nor whether its acts are reversible, is refused before its first tick. The plan passes scope, capabilities, governance. A language model never holds the "effectful" capability: it commits nothing, even when fooled. A human can reject a single step, and the refusal is audited.</p></div>
</div>

## The plan an agent proposed and a human refused

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

## For agents: how to read Softanza

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

## The security numbers

<div class="figures">
<div class="figure"><b>38</b><span>guarantees, each tied to a guard</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/security/SOFTANZA_THREAT_MODEL.md">SOFTANZA_THREAT_MODEL.md</a></div>
<div class="figure"><b>351–357 ms</b><span>to detect credential stuffing over real HTTP, three runs</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/security/containment_drill_narrated.ring">containment_drill_narrated</a></div>
<div class="figure"><b>53–57 ms</b><span>to contain it: account locked, sessions ended, verified from outside</span></div>
<div class="figure"><b>27 / 27</b><span>assertions of the containment drill, tonight</span></div>
</div>

The drill was replayed on this machine on 2026-10-01 at 00:41. A language model plays the investigator, proposes the right plan, and commits nothing; the on-call human commits the same plan, and containment holds. Limits, stated by the threat model itself: one attack shape, on loopback, on one machine; detection runs on demand, not continuously.

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

## What governance declares

Six declarable contracts per actor: an action's risk tier, the authority type, the commitment state, the decommission contract, the decision lineage, and the reversibility class. A low-tier action that cannot be undone deserves more ceremony than a high-tier action that can: risk and irreversibility are two axes.

<p class="proof">The full narration: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">stz-agents-that-cannot-hurt-you-narration.md</a> · the workbench guard: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/safeworld_narrated.ring">safeworld_narrated</a> (76 assertions) · the governed crossing: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/governance_crossing_narrated.ring">governance_crossing_narrated</a> · the "Governance by construction" page: <a href="https://claude.ai/artifact/JgUS6fdkp3EUw4sEJVhpLb">claude.ai/artifact/JgUS6fdkp3EUw4sEJVhpLb</a> · the areas in the Atlas: <a href="atlas/governance.html">governance doctrine</a>, <a href="atlas/agents.html">agents and conversation</a>, <a href="atlas/security.html">security</a>.</p>
