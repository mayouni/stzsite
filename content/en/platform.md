---
title: The engine and its faces
title_html: The engine <i>and its faces</i>
kicker: The platform
lede: Substance lives in an engine written in Zig. Languages are its faces. Ring is the one you write today, Ring++ is the bridge, Haro is the language after, at charter stage.
description: The Softanza architecture: a Zig engine of hundreds of modules, Ring as today's face, Ring++ as the bridge, Haro at charter stage, and the Atlas that rates every domain.
---

## The engine is the product

Strings, tables, graphs, geography, GPU, sound, neural networks, cryptography, database, HTTP, regular expressions, statistics, linear algebra, Fourier transforms: all of it is written in Zig, in one engine, exposed to languages through a C interface. The language you type is a face; what computes is the engine.

<div class="figures">
<div class="figure"><b>401</b><span>Zig source files in the engine</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>5,822</b><span>commits on the main branch</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
<div class="figure"><b>134</b><span>run-verified narrations</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations">doc/narrations</a></div>
<div class="figure"><b>2</b><span>public repositories, GitHub and Codeberg</span><a href="https://codeberg.org/MAyouni/stzlib">codeberg.org/MAyouni/stzlib</a></div>
</div>

Fourteen GPU modules, nine geographic ones, six neural, seven for sound: the families read in the file names of the folder linked above, and that is where they are counted.

## Ring, Ring++, Haro

<div class="cards">
<div class="card"><h3>Ring <span class="pill built">today</span></h3><p>The face you write today. A small, readable, multiparadigm language that the Softanza library turns into a sentence: <code>o1.ContainsDuplicates()</code> reads as it is written. Ring is not carried forward as a runtime or a governance; its simplicity and expressiveness are.</p></div>
<div class="card"><h3>Ring++ <span class="pill built">the bridge</span></h3><p>A register virtual machine and a compiler, in Zig, "sovereign, not new", that run existing Ring code. They are judged against Ring 1.27's machine, taken as the oracle. The Softanza library, over three hundred thousand lines, is their compatibility specification.</p><p class="proof"><a href="https://github.com/mayouni/ringpp">github.com/mayouni/ringpp</a></p></div>
<div class="card"><h3>Haro <span class="pill charter">charter</span></h3><p>The language after Ring, designed for an agent to write and a human to govern, on the Ring++ virtual machine. Its charter is a v0.1 draft of 2026-09-26 awaiting the author's ratification. Nothing is built: no parser, no compiler. This site will never present Haro as available.</p></div>
</div>

## The Atlas: every domain rated, honestly

The Softanza Atlas is the survey of what the library can do, group by group, lane by lane, with four ratings: <span class="chip strong">Strong</span> <span class="chip solid">Solid</span> <span class="chip partial">Partial</span> <span class="chip emerging">Emerging</span>. It shows its gaps; that is what makes its strengths believable.

<div class="figures">
<div class="figure"><b>28</b><span>groups: 25 module groups and 3 cross-cutting systems</span></div>
<div class="figure"><b>334</b><span>rated lanes</span></div>
<div class="figure"><b>101 · 129</b><span>Strong · Solid</span></div>
<div class="figure"><b>68 · 36</b><span>Partial · Emerging</span></div>
</div>

<p class="proof">Atlas version 21, re-read on 2026-09-30 at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>: <a href="https://claude.ai/artifact/FCeuCNfcZepUDJLxsynwFB">the Atlas online</a>. The Atlas pages will be ported to this site in the next release.</p>

## What "engine" means here

A tiny, real example: Ring counts bytes, the engine counts characters. The Arabic word "سلام" is eight bytes and four letters.

<div class="run"><div><div class="lbl">Ring</div><pre>? len("سلام")
? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q("SOFTANZA").BoxedXT([ :Rounded = TRUE ])</pre></div><div class="out"><div class="lbl">Output</div><pre>8
4
arabic
╭──────────╮
│ SOFTANZA │
╰──────────╯</pre></div></div>
<p class="ran">run on 2026-09-30 at 23:11, Ring 1.27, Softanza at commit 0e72e2e2c</p>
