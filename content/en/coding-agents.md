---
title: For coding agents
title_html: Judges for <i>coding agents</i>
kicker: Softanza as a tool stack for the agents that write code
lede: An agent that writes code already has good hands: it reads, searches, edits and runs a shell. What it lacks is a way to know an API it was never trained on, to check that what it wrote keeps its promises, and to show a change before it lands. Softanza has those three on one engine. This page shows them running, says what an agent can reach today, and describes the door that will let it reach the rest.
description: Softanza as a tool stack for coding agents: an API that answers, a judge for code and promises, changes shown as plans, and one engine to compute with; and the stz command that will open them to Claude Code and other agents.
---

## Hands and judges {#judges}

Coding agents such as Claude Code, Codex or Cursor come with their own tools: they read files, search them, edit them and run commands. More ways to find code help them little; they keep coming back to plain search. What they cannot do on their own is know an unfamiliar API without guessing, judge their work against rules and promises, and present a change as an intention a person can review before anything moves.

<p class="way"><span>The Softanza way</span> Softanza does not compete with the agent's tools for finding code. It supplies the judges: something that knows the API, something that checks the claim, and something that shows the change before it lands. The agent keeps its hands.</p>

<figure class="diagram"><img src="../assets/img/diagrams/codingagents-en.png" alt="Three boxes joined by arrows. The coding agent, the hands: read and search, edit files, run a shell; Claude Code, Codex, Cursor and others. The door, one stz command, decided and drawn dashed: a command line, an MCP server, a skill and a hook, a plugin to install. The judges, Softanza, built: know the API, check code and promises, show the change first, compute on one engine. Beneath all three: the model proposes; a person commits; every tool says whether it may act, and refuses with its reason." width="1376" height="650"><figcaption>The judges are built and run today. The door between them and the agent is decided and not built yet.</figcaption></figure>

## The judges, run {#run}

These run today inside the library. An agent can already reach them by writing a short script; the door described below will let it call them as commands.

<!--SHOWCASE:coding-agents-->

## What an agent reaches today {#today}

- **Inside, the judges are deep.** The library explains every method from its own source. House rules and a whole-program checker judge the code. Thousands of written promises and five hundred narrated guards state what the code must print. A change can be rehearsed and then committed through gates, and a schema can hold a local model's answers to a shape.
- **From outside, little reaches.** An agent can run a script, but it cannot yet call a command that answers, judges or plans. A failure does not yet show as an exit code, so no hook can trust a pass, and no instruction file is written for agents.
- **That gap is the finding.** Softanza's own review of the question rated the capability as deep and the reach as almost nil. The work is not new machinery; it is a door.

## The door: one stz command {#door}

<p class="proof"><b>ratified proposal</b> Decided on 2 October 2026. Not built yet. Every verb below answers from the library and the engine, never from a model.</p>

<div class="cards">
<div class="card"><h3>stz ask · explain · howto</h3><p>What a method does, its forms, an example with its promise, and where it lives. The answer comes from a catalogue generated from the source, so it cannot invent a method.</p></div>
<div class="card"><h3>stz check</h3><p>Findings as data: the rule, the file, the line, the severity and what to do. The library's house rules, the whole-program rules and the court of the declared languages, in one shape.</p></div>
<div class="card"><h3>stz promise · guard</h3><p>Each written claim, or each scenario of a guard, kept or broken, with an exit code a hook can trust.</p></div>
<div class="card"><h3>stz rehearse · commit</h3><p>The change as a plan, without touching the disk; then its commit through the gates, by someone entitled to commit.</p></div>
<div class="card"><h3>stz do</h3><p>One short program against the engine, for the work itself: text, tables, graphs, maps, statistics and diagrams, in one call and one binary.</p></div>
<div class="card"><h3>stz grammar</h3><p>The grammar of each declared language, so that an agent's sentence can be validated before it runs, and a local model held to valid sentences only.</p></div>
</div>

Every verb follows the same laws. It answers as data when it is not talking to a person. It exits with 0 for success, 1 for findings and 2 for a refusal. It contains no model: the agent brings the model, Softanza brings the judgement. Every refusal says where, what, why and what to do. And the verbs stay the same whatever language the platform itself is written in.

## Five ways in {#ways}

- **A command line.** Every agent that has a shell can use it, and its answers compose with pipes.
- **An MCP server.** The same verbs as typed tools, for clients without a shell, held in one warm process, read-only first. The platform's application tier already serves a declared project to AI tools this way, read-only and audited, and registers itself with the tools installed on the machine.
- **A skill.** A page the agent loads only when it needs it, teaching which verb to use when.
- **A hook.** An optional check after each edit, so the agent fixes an error in the same turn.
- **A plugin.** One install for Claude Code that brings the skill, the hook and the server together. Other agents read an AGENTS.md file and use the same server.

## Tools that know whether they may act {#governed}

Every tool carries one of the platform's capability kinds: compute, sensing, inference or effect. The agent's model is treated as what it is, an actor that may infer and propose but not act. So a tool that computes or reads answers at once. A tool that would act returns a plan with an identifier and changes nothing. Only a person confirming at the agent's permission prompt, or a governed actor, commits that plan, and every call is recorded.

<p class="way"><span>The Softanza way</span> The difference with an ordinary tool server is not more tools. It is that every tool knows whether it may act, and refuses with its reason when it may not.</p>

## The order of work {#order}

1. Make failure visible: every runner fails with an exit code when a promise breaks.
2. Open the door: an AGENTS.md file and a skill that teach the verbs.
3. The two verbs with the clearest value: `stz check` and `stz ask`.
4. The verbs nobody else offers: `stz promise`, `stz rehearse` and `stz grammar`.
5. The MCP server, generated from the verbs, then the plugin.
6. Measure twenty real tasks with and without the verbs. This site will claim no gain before that measurement.

<p class="proof">Decided on 2 October 2026 on the author's delegation, from Softanza's own review of agent tooling. The judges above ran inside the library at commit 0e72e2e2c.</p>
