---
title: Platform
title_html: The <i>platform</i>
kicker: One engine, twenty-eight areas
lede: Softanza is one computational platform. One engine, written in Zig, handles text, exact numbers, tables, graphs, maps, images, sound, neural networks, governed agents and the security around them. One language, Haro, in construction, is to put all of it in a sentence. Everything on this page was run on the night of publication.
description: The Softanza platform in plain words: what it is, what the engine does, and the language, Haro.
---

## What it is, in plain words {#what}

Most software is assembled from many separate libraries, each written by different people, each with its own rules and its own release calendar. Softanza takes the other road. It is **one** body of code where every area, from counting the letters of an Arabic word to drawing a map of Niger or letting an agent propose a change, obeys the same laws.

<p class="way"><span>The Softanza way</span> Everything is declared, everything is judged by running, and nothing is believed. A page of this site, a chapter of the course, a guard in the repository: each one runs its code when it is read or built. What did not run is not shown.</p>

<div class="figures">
<div class="figure"><b>28</b><span>areas of computation, 334 rated lanes</span></div>
<div class="figure"><b>401</b><span>source files in the Zig engine, 179,000 lines</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>531,000</b><span>lines of library code, 1,227 files, outside tests and archives</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base">base/</a></div>
<div class="figure"><b>501</b><span>scenario guards, 306,000 lines of tests</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test">base/test</a></div>
<div class="figure"><b><!--CLASSES--></b><span>classes, <!--METHODS--> methods, each explained by the library itself</span></div>
<div class="figure"><b>5,824</b><span>commits on the main branch since 12 March 2022</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

<p class="proof">Counted on 2026-10-01 in the repository at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>: files named <code>*.ring</code> under <code>libraries/stzlib</code> outside <code>archive</code> folders, split between <code>base/test</code> and the rest; files named <code>*.zig</code> under <code>engine/src</code>; guards are the test files whose name ends in <code>_narrated.ring</code>. The commit count is read from the main branch the same day.</p>

## What "engine" means here {#engine}

Underneath the language there is a program written in Zig, a systems language, compiled to machine code. It does the heavy work: it counts characters rather than bytes, keeps integers exact at any size, renders pictures to the pixel, runs the neural inference and watches the clock. The language you write is its face.

A small, real example. The Arabic word "سلام" is eight bytes long and four letters long. Many tools answer eight. The engine answers four, and knows the script.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q(2).Power(64)
? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Output</div><pre>4
arabic
18446744073709551616
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26 from <code>libraries/stzlib</code>, Softanza at commit 0e72e2e2c, in 6.6 seconds including the library's load</p>

<p class="way"><span>The Softanza way</span> Substance lives in the engine, and the language is one face of it. A second language, or a second machine, shares the same engine through one C interface, so nothing is written twice and nothing diverges.</p>

## The language: Haro {#haro}

Haro is the platform's language. It is designed so that a human can read it like a sentence and an agent can write it under a grammar that forbids malformed sentences. It is not finished: its road is a register virtual machine and a compiler written in Zig, onto which the platform's code is being moved. Its charter, a draft of 26 September 2026, awaits the author's ratification.

<p class="proof"><b>in construction</b> <!--RUNTIME--> This site will not call Haro available before it is. The code it shows is in Haro's name: where a text was written before the language took its present name, the name was changed and nothing else, and the code was run again.</p>

The library documents itself: an object knows its methods and can explain each one. A string alone answers with 5,384 methods. That is how the reference on this site was generated, from the library's own explanations and not from a hand-written manual.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len( Q("Softanza").Methods() )
? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Output</div><pre>5384
Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26 and at 01:40</p>
