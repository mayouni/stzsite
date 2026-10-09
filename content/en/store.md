---
title: The store
title_html: The <i>store</i>
kicker: Where a world endures
lede: A governed store, beneath a world's body: plain SQLite, in the process, with a log that only grows and a write that is a proposal. Its charter is ratified and its first two layers are built.
description: HaroBase, the governed data store of Softanza: its six properties in plain words, the rungs built and the rungs ahead, with the stage said as in construction.
---

## Six properties {#six}

<ol class="steps">
<li value="1"><b>An insert-only log.</b> Facts are added and never rewritten in place. History is the truth.</li>
<li value="2"><b>A chain verified on open.</b> Each entry seals the one before, so a store that was altered says so when it is opened.</li>
<li value="3"><b>Facts over time.</b> A fact has an interval in which it was valid and an interval in which it was recorded, so a question can be asked as of a date.</li>
<li value="4"><b>A write is a proposal.</b> A change is proposed and judged before it is admitted.</li>
<li value="5"><b>A merge is a decision.</b> When two versions of a fact meet, someone decides, and the decision is kept.</li>
<li value="6"><b>Lenses.</b> Ways of seeing the same store.</li>
</ol>

## Where it stands {#stage}

<p class="proof"><b>in construction</b> The charter was ratified on 2026-09-29. The first two rungs of the store are built, each with a guard and a negative sibling that fails when the property is broken, and those guards are mutation-checked. Rungs three to six are ahead. The repository is private for now. The Estate page lists this store beside the other products, with its stage.</p>

This page is the store's chapter in the story of a world's body, and the same sentence as the agentic pages say for files, a write is a proposal, stated here for data. The store does not yet carry its own measurements on this site; those numbers come from the author's machine and are not reprinted until a run of the guards can be shown here.

<p class="proof">See <a href="estate.html">the estate</a> and <a href="first.html">your first application</a>.</p>
