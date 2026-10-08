---
title: Seven design goals
title_html: Seven <i>design goals</i>
kicker: Why a feature exists
lede: A feature that serves no goal is refused, and a goal with no feature is a gap. Seven goals have held Softanza's design together since 2022. This page lays each against the features that serve it, with the state of each today.
description: The seven design goals of Softanza, expressiveness, flexibility, reliability, consistency, human-centric metaphors, practical abstractions and manageability, each with its features, their state today and one run.
---

Four vocabularies tell Softanza's design, and they answer four different questions. A goal says <b>why</b> a feature exists. A principle says <a href="principles.html">what Softanza believes</a>. A convention says <a href="craft.html">how code is written</a>. A law says what the tree refuses. This page is the first: the reason, which a reviewer can read goal by goal instead of line by line.

The 2022 slide laid seven goals against thirty-three features. Here they are redrawn with the state of each feature today, and one run per goal.

<!--GOALS-->

## What the tally says {#tally}

The skeleton held: most features exist as declared, and the ones that changed did so for stated reasons, such as the host language moving to Haro. Manageability is the goal that drifted most. Its visualised call stack is a name and nothing was built under it, and the decorator forms of caching and logging gave way to classes. A design that drifted deserves a decision and not a silent replacement: either the decorators return as tags the engine honours, or the class form is declared final and this table is amended. That decision is the author's.

<p class="proof"><b>in construction</b> The counts were read from the library's files at commit 93d7a39 by an outside assessment on 2026-10-07: a definition found by name is counted as built, and no feature was run for the count. The goals are written in thousands of comment tags above method definitions, in about ninety spellings, and no check yet reads them. A court that does, and prints this table from the code, is specified and not built.</p>
