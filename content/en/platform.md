---
title: The areas of the platform
title_html: The areas <i>of the platform</i>
kicker: The platform
lede: One engine written in Zig, one language, Haro, and twenty-eight areas of computation, from strings to maps, from sound to governed agents, designed to work together. Everything here runs; what does not run yet carries its rating.
description: The twenty-eight areas of the Softanza platform: a Zig engine, the Haro language, and every area rated honestly against the leaders of its category.
---

## One unified computational platform

Softanza is a computational platform: an engine, written in Zig, that handles codepoint-correct strings, exact numbers at any size, tables, graphs, maps on the ellipsoid, images, sound, neural networks, governed agents and the security that holds them; a language, Haro, that reads like a sentence and puts all of it within one line; and a law, everything is judged by running, which is why what you read here ran.

<div class="figures">
<div class="figure"><b>28</b><span>areas, 334 rated lanes</span><a href="atlas.html">the Atlas</a></div>
<div class="figure"><b>401</b><span>Zig source files in the engine</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>5,384</b><span>methods on a single string</span><a href="atlas/meta.html">atlas/meta</a></div>
<div class="figure"><b>134</b><span>run-verified narrations</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations">doc/narrations</a></div>
<div class="figure"><b>5,822</b><span>commits on the main branch</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

## The twenty-eight areas

Every area has its page: what a maker does with it, an example run, its lanes rated against the leaders of its category, what stands out and what is owed. The bars say the rating: <span class="chip strong">Strong</span> <span class="chip solid">Solid</span> <span class="chip partial">Partial</span> <span class="chip emerging">Emerging</span>.

<!--ATLAS-TALLY-->
<!--ATLAS-COMPACT-->

<p class="proof">Atlas version 21, re-read on 2026-09-30 at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>; <a href="atlas.html">the full Atlas, with its cards</a>.</p>

## The language: Haro

<div class="cards">
<div class="card"><h3>Haro <span class="pill charter">in construction</span></h3><p>The platform's language: designed for an agent to write and a human to govern, on a register virtual machine and a compiler written in Zig, sovereign. Its charter is a v0.1 draft of 2026-09-26 awaiting the author's ratification; the virtual machine and the compiler exist and run the platform's code of today. This site will never present Haro as available before it is.</p></div>
<div class="card"><h3>The code on this site</h3><p>Every code block on this site is Softanza code as it runs on the platform today, run on the night of publication, its output beside it. It reads like a sentence: find first, then apply.</p></div>
<div class="card"><h3>The engine</h3><p>Fourteen GPU modules, nine geographic ones, six neural, seven for sound, plus strings, tables, graphs, cryptography, database, HTTP, regular expressions, statistics, linear algebra and Fourier transforms: the families read in the engine's file names, and that is where they are counted.</p><p class="proof"><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></p></div>
</div>

## What "engine" means here

A tiny, real example: the engine counts characters, not bytes. The Arabic word "سلام" is eight bytes and four letters.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len("سلام")
? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q("SOFTANZA").BoxedXT([ :Rounded = TRUE ])</pre></div><div class="out"><div class="lbl">Output</div><pre>8
4
arabic
╭──────────╮
│ SOFTANZA │
╰──────────╯</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:11, Softanza at commit 0e72e2e2c</p>
