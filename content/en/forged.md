---
title: Forged in projects
title_html: Forged <i>in projects</i>
kicker: Built the hard way, and said honestly
lede: Softanza was not built as a research lab, although it can be one. It was built by using it, and by being asked for things by people who had a restaurant, a bank or an organisation to run. This page says, project by project, what was needed, what the library learned, and the file that carries the lesson.
description: The projects that forged Softanza: RestoLean, Organizium and Sonibank, DIKO. What each needed, what the library learned, and where the lesson sits in the code.
---

## How to read this page {#rule}

Three rules, so that the story can be checked. A lesson is listed only when a file of the library carries it, and the file is named. A project is told only as far as a document attests it; where the document is not public yet, the page says so and quotes nothing private: no price, no figure of a client, no name of a person. And where the library only uses a project as its example, the page says "example", not "origin".

## The order things happened {#order}

<ol class="narr">
<li><b>12 March 2022.</b> The first commit of the library (<a href="history.html">From first principles</a>).</li>
<li><b>2024, RestoLean.</b> A mission of analysis (the offer is dated 2 May 2024), the founding analyses (June and July), then a "specification novel": narrations that specify the system by story (August and September).</li>
<li><b>2025, RestoLean.</b> The first product specified to the last detail (February and March); two years of specification in all, with no operational deliverable; a long silence; and the turn to deliver small and fast.</li>
<li><b>February 2026, Organizium.</b> A new version, and the web layer of Softanza born inside it (the repository starts on 4 February).</li>
<li><b>July and August 2026, RestoLean.</b> The first iteration delivered; on 4 July the client reverses the order of the work, and on 4 August the amendment that fixes it is closed.</li>
<li><b>Autumn 2026, DIKO.</b> The design study for a hub that links an organisation's tools in Niger.</li>
</ol>

## RestoLean, Lyon: a specification is not a delivery {#restolean}

RestoLean is a platform for neighbourhood commerce, carried by the owner of a couscous restaurant in Lyon and designed by the author. Its first lesson is about method, and it was paid for. Two years of rich specification produced no operational deliverable, a silence of six months followed, and the project came close to ending. What came out of that is the doctrine of the author's work since: deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery.

Its second lesson is a rule. When the client reversed the order of the work on 4 July 2026 (the customer first, the restaurateur next, the supplier last), the project fixed **the Lock**: no new turn and no growth of scope during a cycle, and any idea goes to a notebook read at the end of the cycle. In the constellation RestoLean was then redrawn as, adding a world or a bond is a declared, visible act, not a silent drift of scope.

What it needed, and where the library carries it:

<div class="cards">
<div class="card"><h3>Try payments without a subscription</h3><p>RestoLean's own guide names the library's service virtualization as the way to try payments before any subscription is taken. The library holds the dependency surface of a solution in one registry, binds a fake while programming, and refuses to call a solution ready for production while a fake is still bound. <span class="mono">base/service/stzServiceRegistry.ring</span>, plan <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md">SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md</a>.</p></div>
<div class="card"><h3>See the whole solution before building it</h3><p>The library's emulation and deployment designs take a solution named restolean as their example: a phone app, a backend, a device. It is an example there, not the origin of the design. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_EMULATION.md">SOFTANZA_EMULATION.md</a>, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/SOFTANZA_DEPLOYMENT.md">SOFTANZA_DEPLOYMENT.md</a>.</p></div>
<div class="card"><h3>A constellation of worlds on one ground</h3><p>After the turn, RestoLean was redrawn as a constellation: a world for the customer's phone, one for the kitchen screen, one for the merchant's workshop, one for management and one for the publisher's console, on a shared ground of identity, catalogue, orders, payments and fleet. The redrawing cites the library's own design. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/STZSUPERAPP_DESIGN.md">STZSUPERAPP_DESIGN.md</a>.</p></div>
<div class="card"><h3>A speed budget is a promise</h3><p>RestoLean's acceptance criteria state a speed budget for each cycle: first display, reaction to a tap, an order reaching the kitchen. The library's performance plane states a promise next to the code it judges, and reports the measured value beside each verdict. <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-perf-judgment-narration.md">stz-perf-judgment-narration.md</a>.</p></div>
</div>

The first of them, run for this page: a solution declares that it depends on a mail service, binds the fake, and is moved to production. The registry does not call it sound.

<!--FORGED:registry-->

The first line is 0, not sound. The second says why: a fake must never ship. The fake is refused by name, and a service that was declared and never bound raises when asked for, instead of silently doing nothing.

<p class="way"><span>The Softanza way</span> "We tested against the sandbox" means something only if the code is byte for byte the code that ships. So the phase decides what comes back, and the check that nothing fake ships is enforced, not remembered.</p>

What is true today, said plainly: RestoLean's first iteration is a web application of single-file worlds with no build step; the constellation is a design the library can run, not yet RestoLean's production.

## Organizium and Sonibank: an organisation judged by its own chart {#organizium}

Organizium is an assessment platform for organisations: a questionnaire, a scoring engine, a maturity model, a referential of norms and indicators, an organisation chart with its gaps of conformity, a simulation of before and after, and recommendations. It was first built for a bank: Organizium Standard Edition is installed, under licence, on the internal network of Sonibank in Niamey, and the installation guide delivered to the bank attests it. A second version, in 2026, carried 48 questions in eight dimensions, an agent made of rules with no language model, and a funding matcher, first for DIKO.

What the library carries of it is easy to point at. A bank's regulator has rules about who reports to whom: a board must exist, the audit function must report to the board, a risk function must exist, operations must not report through treasury. The library's organisation chart carries these as validators, with the regulators' rule bases beside it (BCEAO, Basel III, SOX, PCI DSS, ISO 27001, GDPR, HIPAA).

<!--FORGED:orgchart-->

Three findings, each a rule with a number a bank's auditor can read. <span class="mono">base/graph/stzOrgChart.ring</span> holds the validators; the library also names the rule bases <span class="mono">stzBCEAORuleBase</span>, <span class="mono">stzBaselIIIRuleBase</span> and their siblings.

The other thing that was born in Organizium is the web layer. Its repository, started on 4 February 2026, holds a framework of single-file worlds for the web, a first query notation, and the interface constitution with its rule file and the verifier that checks a page against it: an early form of what the site calls <a href="zui.html">Zui</a> today. They are not public yet; the site quotes none of their text.

## DIKO, Niamey: the platform speaks the organisation's language {#diko}

DIKO is an organisation working in Niger, with a head office in Niamey and bases in the field. It is already connected and already equipped with tools. What it lacks is the link between them: a request travels on paper or in a document for days, and the rules exist but live in separate files. The design study for **DIKO Hub**, a single entry point that links the existing tools without replacing any, asks six things of a platform. Each sits on a piece of Softanza, or on a gap the study names.

<div class="cards">
<div class="card"><h3>Its own words and rules</h3><p>The platform speaks DIKO's vocabulary, and its rules are written plainly, changed without a programmer, each change recorded and undoable. In the study's notation a rule reads as a sentence: <span class="mono">RULE: budget &lt;= ligne.disponible</span>, with the message the person will read. The library carries rules as data, with a governance that records each change.</p></div>
<div class="card"><h3>A person decides</h3><p>An agent that knows DIKO prepares files and checks documents, and a person always decides. The library's agents propose and only a gate commits; their acts are rehearsed in a safe world first.</p></div>
<div class="card"><h3>Everything traced</h3><p>Every approval, every refusal and every consultation of a sensitive file is recorded with its author and date, and nothing can be erased. Data has three levels of sensitivity. The library's security plane carries the guarantees; each has a test.</p></div>
<div class="card"><h3>Offline by default</h3><p>Each device keeps what is entered and sends it when the network returns. <b>This is a gap, not a lesson learned.</b> RestoLean asked for the same (use in the storeroom, without a connection). The study names the pieces for it, HaroScript and HaroServ, whose stage the <a href="estate.html">estate page</a> tells; this page does not claim it closed.</p></div>
<div class="card"><h3>A circuit with its deadlines</h3><p>A request is described once, and the advance, the purchase and the mission follow from it. Every step has a deadline that shows, and an unreturned approval is deemed given, as the organisation's own responsibility chart provides. The library's workflow classes carry the steps and their simulation.</p></div>
<div class="card"><h3>A document chain</h3><p>The study itself was produced by a chain from Markdown to a paginated PDF. It showed what the estate lacks: the chains that produce its documents, this site's included, are written in Python and Node, and none calls the engine.</p></div>
</div>

An organisation chart module, built on Organizium's core, is proposed as an extension of the hub: the bank's chart and the NGO's are the same engine with different words, which is the point of the platform.

What is true today, said plainly: DIKO Hub is a design. The study is written; nothing of the hub is in production.

## What the projects have in common {#common}

A restaurant, a bank and an NGO have nothing in common, and each asked for the same five things in its own words: a shared ground, a world for each person and each device, bonds between them, rules, and roles. The library names that construction, a constellation of worlds, and the site calls it <a href="platforms.html">a platform of platforms</a>. It is not a theory that was applied afterwards: it is what the projects had in common once they were set side by side.

## What the projects did not prove {#limits}

The customer platforms run today on ordinary stacks: Organizium at Sonibank is a Python application, RestoLean is single-file web worlds, DIKO Hub is not built. Their declarations are being written as Softanza's own, so that moving them onto the Softanza engine is a change of engine, not of plan; it is a step ahead, not a step taken. Some lessons above are carried by public files and some only by documents that are not public yet: the page marks which. And what the author remembers and no file proves is not listed.

<p class="proof">The library's files named above are public; the repositories of the projects are not, and the site quotes none of their text beyond what each section says. Every run on this page was made inside the library on <!--FORGED-RAN--> at commit 0e72e2e2c.</p>
