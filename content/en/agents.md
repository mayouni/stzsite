---
title: For agents
title_html: For <i>agents</i>
kicker: How a machine reads Softanza
lede: This section also addresses an agent reading this site. Softanza is designed to be read by a machine as much as by a human.
description: How an agent reads Softanza: ask the library, declare yourself in an agent file, speak the grammar.
---

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
<div class="card"><h3>Speak the grammar, not general code</h3><p>A schema already compiles to a constraint grammar: a local model whose sampler is held to it can only emit valid answers. That is the platform's contract C9: structure kills malformedness, never falsehood. Emitting such a grammar for every declared language is the next step, decided as the command stz grammar.</p><p class="proof"><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_INTELLIGENCE_ARCHITECTURE.md">SOFTANZA_INTELLIGENCE_ARCHITECTURE.md</a></p></div>
</div>
