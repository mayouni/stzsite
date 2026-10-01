---
title: The platform
title_html: The <i>platform</i>
kicker: One engine, twenty-eight areas
lede: Softanza is one computational platform. One engine, written in Zig, handles text, exact numbers, tables, graphs, maps, images, sound, neural networks, governed agents and the security around them. One language, Haro, puts all of it in a sentence. Nothing on this page is believed; everything here was run on the night of publication.
description: The Softanza platform in plain words: what the engine does, the twenty-eight areas, how it compares with .NET, Python, Wolfram and the JVM, what one install means, and what the code looks like beside Python and JavaScript.
---

## What it is, in plain words {#what}

Most software is assembled from many separate libraries, each written by different people, each with its own rules and its own release calendar. Softanza takes the other road. It is **one** body of code where every area, from counting the letters of an Arabic word to drawing a map of Niger or letting an agent propose a change, obeys the same laws.

<p class="way"><span>The Softanza way</span> Everything is declared, everything is judged by running, and nothing is believed. A page of this site, a chapter of the course, a guard in the repository: each one runs its code when it is read or built. What did not run is not shown.</p>

<div class="figures">
<div class="figure"><b>28</b><span>areas of computation, 334 rated lanes</span><a href="atlas.html">the Atlas</a></div>
<div class="figure"><b>401</b><span>source files in the Zig engine, 179,000 lines</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>531,000</b><span>lines of library code, 1,227 files, outside tests and archives</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base">base/</a></div>
<div class="figure"><b>501</b><span>narrated guards, 306,000 lines of tests</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test">base/test</a></div>
<div class="figure"><b>618</b><span>classes, 26,949 methods, each explained by the library itself</span><a href="reference.html">the reference</a></div>
<div class="figure"><b>5,824</b><span>commits on the main branch since 12 March 2022</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

<p class="proof">Counted on 2026-10-01 in the repository at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>: files named <code>*.ring</code> under <code>libraries/stzlib</code> outside <code>archive</code> folders, split between <code>base/test</code> and the rest; files named <code>*.zig</code> under <code>engine/src</code>; guards are the test files whose name ends in <code>_narrated.ring</code>. The commit count is read from the main branch the same day.</p>

## The twenty-eight areas {#areas}

Each picture below was produced by the platform itself. Click an area to read what a maker does with it, an example run, and an honest rating of each of its lanes against the leaders of its category.

<!--ATLAS-WALL-->

<p class="proof">The ratings, lane by lane, with the gaps shown beside the strengths, live on <a href="atlas.html">the Atlas page</a>. Atlas version 21, read on 2026-09-30 at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a>.</p>

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

Haro is the platform's language. It is designed so that a human can read it like a sentence and an agent can write it under a grammar that forbids malformed sentences. Its register virtual machine and its compiler are written in Zig and already run the platform's code of today. Its charter, a draft of 26 September 2026, awaits the author's ratification.

<p class="proof"><span class="pill charter">in construction</span> This site will not call Haro available before it is. Every code block on this site is Softanza code as it runs on the platform today.</p>

The library documents itself: an object knows its methods and can explain each one. A string alone answers with 5,384 methods. That is how <a href="reference.html">the reference</a> on this site was generated, from the library's own explanations and not from a hand-written manual.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len( Q("Softanza").Methods() )
? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Output</div><pre>5384
Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div>
<p class="ran">run on 2026-10-01 at 09:26 and at 01:40</p>

## The code, beside Python and JavaScript {#code}

The platform is judged on what its code looks like and what it answers. Four short comparisons, each side run tonight, each output as it came out. Python and JavaScript are excellent languages; the point is not that they fail, it is what a line costs and what it answers.

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q(2).Power(64)</pre><pre class="o">18446744073709551616</pre></div>
<div class="side other"><div class="lbl">JavaScript, Node 22</div><pre>console.log(2 ** 64);</pre><pre class="o">18446744073709552000</pre></div>
</div>
<p class="ran">Exact by default: an integer is exact at any size. JavaScript's number is a 64-bit float, so the last digits are rounded; <code>9007199254740993</code> prints as <code>9007199254740992</code>. Run 2026-10-01 at 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre><pre class="o">[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>items = ["tea", "rice", "tea", "fish", "rice", "tea"]
print([i + 1 for i, x in enumerate(items) if x == "tea"])
print(list(dict.fromkeys(items)))</pre><pre class="o">[1, 3, 6]
['tea', 'rice', 'fish']</pre></div>
</div>
<p class="ran">Find first, then apply. The question is spoken as it is thought: find all, remove duplicates. The Python answers are right too; they are built from mechanics (enumerate, a dictionary's keys) that the reader must decode. Run 2026-10-01 at 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q("مرحبا بالعالم").Script()</pre><pre class="o">arabic</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>import unicodedata
s = "مرحبا بالعالم"
print({unicodedata.name(c).split()[0] for c in s if not c.isspace()})</pre><pre class="o">{'ARABIC'}</pre></div>
</div>
<p class="ran">The script of a text is a question the platform answers directly. In Python it is assembled from the Unicode names of each character. Run 2026-10-01 at 09:26.</p>

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )</pre><pre class="o">[ 5, 3, 1 ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre># no counterpart without an external language model</pre><pre class="o"></pre></div>
</div>
<p class="ran">An instruction in English, French, Arabic or Hausa runs. The natural layer is dictionary-driven and local: no network, no model, no API key. Run 2026-10-01 at 09:26.</p>

## Compared with the platforms you know {#compare}

Softanza is meant to stand beside .NET, Python with its ecosystem, the Wolfram stack and the JVM, not beside a single library. The matrix below comes from the platform's own compass. Its ratings of the others are deliberately generous to them, and the two lanes where Softanza is absent are shown in their colour.

<!--COVERAGE-->

<p class="proof">Source: the Softanza compass, section "Functional coverage against the platforms", read from the main branch on 2026-09-17; the file behind this table is <a href="https://github.com/mayouni/stzsite/blob/main/data/coverage.json">data/coverage.json</a>. "Deep" means first-class, often best in its category; "Solid" fully usable; "Partial" present but a subset or young; "Absent" not covered, or refused by design.</p>

<p class="way"><span>The Softanza way</span> One stop. To cover these thirty rows in Python you assemble numpy, pandas, matplotlib, scikit-learn, nltk, cryptography, geopandas and a neural framework, each with its own release calendar and its own idea of a string. Here they are one engine, one vocabulary, one set of laws, and one Atlas that says plainly where the platform is still behind.</p>

## One folder, copied {#install}

There is no installer and no package registry. The repository is one folder; the engine ships as compiled libraries for Windows and builds for Linux and macOS from source. A script placed in the library's folder loads everything with one line.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

The direction, stated as a direction: a Haro program compiled to one static binary that carries the engine with it. Today the platform runs from its folder with the runtime the repository names. <a href="start.html">The Start page</a> walks through it in one hour.

## Where the platform goes next {#next}

The Atlas lists thirty-six "Emerging" lanes beside its hundred and one "Strong" ones, and <a href="vision.html">the Vision page</a> places the platform inside the whole estate: the machine beneath it, the language above it, the intelligence layer to come. A platform that shows its gaps is believed on its strengths.
