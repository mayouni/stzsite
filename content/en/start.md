---
title: Start
title_html: <i>Start</i>
kicker: In one hour
lede: One public repository, an install in three steps, a first program, the course reader as a page of this site. Every command on this page was run on the night of publication.
description: How to start with Softanza: the GitHub repository, the install, the first program, the first narration, the course reader, and where to write.
---

<p class="proof"><b>The runtime, plainly</b> <!--RUNTIME--></p>

## The repository {#repository}

Everything is in one place: the foundation, its engine, its guards, its narrations and its course.

<div class="cards">
<div class="card"><h3>github.com/mayouni/stzlib</h3><p>Public under the MIT licence since 12 March 2022. Issues, security advisories and the whole history are there.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
</div>

## Install {#install}

Three steps. Nothing is installed in the sense of an installer: one folder, copied, and the runtime that runs it.

**1. Get the repository.**

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

**2. Get the runtime**, version 1.27.0, the one these pages were run with, from <a href="https://ring-lang.net">ring-lang.net</a>. Starting the runtime with no argument prints its version, so you know it is there. The Zig engine ships as compiled libraries for Windows and builds for Linux and macOS from source; the repository says how.

**3. Write the first program.** In the folder <code>libraries/stzlib</code>, create a file <code>first.ring</code> whose first line loads the library, then the program of the next section:

<pre>load "stzLib.ring"</pre>

Run it from that folder:

<pre>ring first.ring</pre>

The first run takes about seven seconds, because the library and its engine load.

## The first program {#first}

<div class="run"><div><div class="lbl">first</div><pre>o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()

? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Output</div><pre>1
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">run on 2026-10-09 at 00:52 as <code>ring first.ring</code> from <code>libraries/stzlib</code>, in 6.9 seconds, Softanza at commit <a href="https://github.com/mayouni/stzlib/commit/4a184e6f0">4a184e6f0</a></p>

## The first narration {#narration}

A narration is a document that tells a part of the library as a story, in code written to be run as it is read. Start with <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">the mental model</a>, then <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">the agents that cannot hurt you</a>; both open on GitHub. To see a narration judged block by block, open <a href="narrations/stz-repetition-with-elegance-narration.html">Repetition with Elegance</a>, run for this site: its six blocks print what they promise. All 134 are listed under Learn, in Narrations.

## The course reader {#reader}

The reader is a page of this site: <a href="../reader.html">open the reader</a>. It was built from the library on 2026-09-30, and the Learn page says how to learn with it, step by step. To rebuild it yourself, from your copy of the repository:

<pre>cd libraries/stzlib/base/education/tools
ring build_reader.ring reader.html</pre>

<p class="ran">run on 2026-09-30 at 23:02: "15 of 15 chapters, 3 of 3 world pages", every edition green, in 3 minutes 22 seconds</p>

And to play the fifteen-minute demo for decision makers, whose last line must read "DEMO: 20 proved, 0 not proved":

<pre>cd libraries/stzlib/base/education/demo
ring demo.ring rehearsal</pre>

<p class="ran">run on 2026-09-30 at 23:10, in 49 seconds, 20 proofs out of 20</p>

## Write {#write}

Questions, defect reports and proposals go through the <a href="https://github.com/mayouni/stzlib/issues">issues of the GitHub repository</a>. A security flaw is reported privately through the repository's security advisories, as its <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a> says. An edition of the course in your language starts with a folder of plain-text chapters: the Learn page says how the course's court will judge it. For the enterprise edition, write through the same issues: <a href="editions.html">the Editions page</a> says what it contains.

## Check this site offline {#offline}

Before a presentation with no network, open <a href="../deck-check.html">deck-check.html</a> from the site's folder: the page loads every asset the presentation needs and says which one is missing.
