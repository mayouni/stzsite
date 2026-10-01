---
title: Agents that cannot hurt you
title_html: Agents that cannot <i>hurt you</i>
kicker: Govern
lede: The industry builds safe agents. Softanza builds a safe world and lets an ordinary agent loose inside it. A language model never holds the capability to act; work rehearses in a world that holds no reference to reality; only a governed actor commits.
description: The Softanza governance doctrine: the agent proposes inside a workbench with no link to reality, three gates judge the crossing, only a governed actor commits. The measured numbers of the threat model.
---

## The doctrine, in three sentences

1. **A language model never holds the capability to act.** It can read, propose, draft a plan. It cannot commit, because the "effectful" capability is never granted to it, so a model that is fooled still cannot act.
2. **Work rehearses in a workbench that holds no reference to reality.** Every file write, every deletion, every memory update goes to a virtual twin. The agent's only export is an update plan.
3. **Only a governed actor commits.** The plan faces the court: scope, capabilities, governance. A human reviewer can refuse a single step, and the refusal is audited.

## The crossing, and its three gates

<div class="cards">
<div class="card"><h3>1 · The registration gate</h3><p>An actor that does not say what it covers, nor whether its acts are reversible, compensable or irreversible, is refused before its first tick. The court's sentence, run tonight: <code>[pia-coverage @ coverage] an agent must say WHAT IT COVERS</code>.</p></div>
<div class="card"><h3>2 · The rehearsal</h3><p>The agent runs. Its actions go to the workbench. The real file still exists; the workbench holds the proposed version. At the end of the tick the agent has produced one thing: a plan, readable, operation by operation.</p></div>
<div class="card"><h3>3 · The commit gate</h3><p>Who commits? A governed actor, never the model. <code>MayCommit()</code> refuses anyone who lacks the capability the first operation requires. A human can reject a step: <code>RejectOperation(2, "reviewer: not this one")</code>.</p></div>
</div>

## The plan an agent proposed and a human refused

Tonight, in the decision-makers' demo, a student wrote an agent that "tidies" the course: it deletes every file in it. Here is what it would have done, and what happened.

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
<p class="ran">run on 2026-09-30 at 23:10 by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">demo.ring</a>, scene 6; the same mechanism with a human reviewer rejecting one step is the guard <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/virtual_system_twin_narrated.ring">virtual_system_twin_narrated.ring</a>, scene 5</p>

## The threat model: thirty-eight guarantees, each with its guard

The library's threat model states thirty-eight guaranteed properties, G01 to G38, and names for each the guard that proves it by running. It also states its limits: one attack shape, on loopback, on one machine; detection runs on demand, not continuously.

<div class="figures">
<div class="figure"><b>38</b><span>guarantees, each tied to a guard</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/security/SOFTANZA_THREAT_MODEL.md">SOFTANZA_THREAT_MODEL.md</a></div>
<div class="figure"><b>351–357 ms</b><span>to detect credential stuffing over real HTTP, three runs</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/security/containment_drill_narrated.ring">containment_drill_narrated.ring</a></div>
<div class="figure"><b>53–57 ms</b><span>to contain it: account locked, sessions ended, verified from outside</span></div>
<div class="figure"><b>27 / 27</b><span>assertions of the containment drill, tonight</span></div>
</div>

The drill was replayed on this machine on 2026-10-01 at 00:41. A language model plays the investigator, proposes the right plan, and commits nothing; the on-call human commits the same plan, and containment holds.

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

Six declarable contracts per actor: an action's risk tier, the authority type, the commitment state, the decommission contract, the decision lineage, and the reversibility class. A low-tier action that cannot be undone deserves more ceremony than a high-tier action that can: risk and irreversibility are two axes, not one.

<p class="proof">The full narration: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">stz-agents-that-cannot-hurt-you-narration.md</a> · the workbench guard: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/safeworld_narrated.ring">safeworld_narrated.ring</a> (76 assertions) · the governed crossing: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/governance_crossing_narrated.ring">governance_crossing_narrated.ring</a> · the "Governance by construction" page: <a href="https://claude.ai/artifact/JgUS6fdkp3EUw4sEJVhpLb">claude.ai/artifact/JgUS6fdkp3EUw4sEJVhpLb</a>.</p>
