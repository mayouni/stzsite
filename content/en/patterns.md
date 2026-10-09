---
title: Pattern languages
title_html: Pattern <i>languages</i>
kicker: A paradigm
lede: One regex-shaped grammar, across seven kinds of data: strings, lists, numbers, time, tables, matrices and graphs, in one library, with one habit.
description: The pattern languages of Softanza: a regular expression raised to lists, numbers, time, tables, matrices and graphs, each run, with the two whose own tests no longer pass said plainly.
---

## One grammar, seven subjects {#seven}

Regular expressions were redesigned first, as a class, a maker and a data library. Their grammar, braces and the at sign, was then lifted to six more kinds of data, each a class with its own small function. The same habit holds in all seven: write the pattern, ask <code>Match</code>, and ask the pattern to explain itself.

<ol class="steps">
<li value="1"><b>Strings.</b> <code>rx(pat(:email))</code> <span class="rx-src">the regular expression, backed by a standard engine</span></li>
<li value="2"><b>Lists.</b> <code>[@N1-3, @S]</code>, and stepped ranges, and nested lists <span class="rx-src">Lx()</span></li>
<li value="3"><b>Numbers.</b> <code>{@Property(Even) &amp; @Property(Prime)}</code> <span class="rx-src">Nx()</span></li>
<li value="4"><b>Time.</b> <code>{@Event(Meeting) -&gt; @Duration(30m) -&gt; @Event(Break)}</code> <span class="rx-src">Tmx()</span></li>
<li value="5"><b>Tables.</b> <code>{cols(3) &amp; unique(id) &amp; avgcol(salary:&gt;40000)}</code> <span class="rx-src">Tx()</span></li>
<li value="6"><b>Matrices.</b> <code>{shape(square) &amp; property(symmetric)}</code> <span class="rx-src">Mx()</span></li>
<li value="7"><b>Graphs.</b> <code>{@Node(start) -&gt; @Edge(flows) -&gt; @Node(done)}</code> <span class="rx-src">Gx()</span></li>
</ol>

The patterns in this list are written, not run. The runs below are the ones that kept their promise.

<!--SHOWCASE:patterns-->

## What can be said of it {#claim}

The library's articles compare it with the field: Wolfram has list patterns, uniqueness and stepped ranges; Elixir, Haskell and Rust match structures; graph query languages and complex-event languages exist. What the articles find in none of them is one regex-shaped grammar across seven kinds of data in one library, with the same small-function habit, the same Match, Explain and Debug surface, and the same test discipline. That is the library's own reading of the field, not a survey.

## The honest state {#state}

<p class="proof"><b>in construction</b> Two of the seven runs above are missing, and they are missing because they failed. The library's own tests for the table and the time patterns promise a match and print none at the commit read for this page. They are reported to the library, and the two languages are shown here without a run. Graph quantifiers are parsed and not yet used. The regex analyser is a name, and the siblings of the Regexuter are <a href="softanzuter.html">a vision</a>.</p>

<p class="proof">Sources: the articles <a href="narrations/stzregex-mastering-regex-with-softanza-narration.html">regex</a>, <a href="narrations/stzlistex-pattern-matching-for-lists.html">lists</a>, <a href="narrations/stznumbex-number-patterns-made-simple.html">numbers</a>, <a href="narrations/stztimex-a-pattern-language-for-time-in-softanza.html">time</a>, <a href="narrations/stztablex-pattern-langauge-for-tables.html">tables</a> and <a href="narrations/stzmatrex-declarative-pattern-matching-for-matrices.html">matrices</a>; the guards in the library's test folders for each, linked under every run.</p>
