---
title: Agentic
title_html: The agent proposes. <i>It does not commit.</i>
kicker: The agentic paradigm, the Softanza way
lede: Machines now write and act. Softanza's answer is not to trust them more carefully; it is to change where they are allowed to stand. An agent speaks a declared language, rehearses in a workbench, faces a court, and never holds the capability to commit.
description: Softanza's agentic paradigm: the agent proposes, a workbench rehearses, a court judges, only a governed actor commits.
---

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

<p>What makes an agent's mind programmatic and not a model in a loop is a ladder of patterns, faculties and agents: <a href="softanzuter.html">the Softanzuter</a>.</p>
