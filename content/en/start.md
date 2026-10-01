---
title: Start
title_html: <i>Start</i>
kicker: In one hour
lede: One public repository, an install in two commands, a first program, the course reader as a page of this site. Every command on this page was run on the night of publication.
description: How to start with Softanza: the GitHub repository, the install, the first program, the first narration, the course reader, and where to write.
---

## The repository {#repository}

Everything is in one place: the foundation, its engine, its guards, its narrations and its course.

<div class="cards">
<div class="card"><h3>github.com/mayouni/stzlib</h3><p>Public under the MIT licence since 12 March 2022. Issues, security advisories and the whole history are there.</p><p class="proof"><a href="https://github.com/mayouni/stzlib">github.com/mayouni/stzlib</a></p></div>
</div>

## Install {#install}

The Zig engine ships as compiled libraries for Windows and builds for Linux and macOS from source; the platform's runtime is described in the repository. There is nothing to install in the sense of an installer: one folder, copied.

<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>

A script placed in the <code>libraries/stzlib</code> folder loads the library with one line; the runtime that launches it, and its version, are the ones the repository names.

## The first program {#first}

<div class="run"><div><div class="lbl">first</div><pre>o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()

? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Output</div><pre>1
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">run on 2026-10-01 at 00:45 from <code>libraries/stzlib</code>, Softanza at commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a></p>

## The first narration {#narration}

A narration is a document where every code block runs and no output is ever stored: what you read was produced while reading. Start with <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-mental-mode-narration.md">the mental model</a>, then <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">the agents that cannot hurt you</a>. All 134 are listed under Learn, in Narrations.

## The course reader {#reader}

The reader is a page of this site: <a href="../reader.html">open the reader</a>. It was built from the library on 2026-09-30, and the Learn page says how to learn with it, step by step. To rebuild it yourself, from your copy of the repository:

<pre>cd libraries/stzlib/base/education/tools
# run build_reader with the repository's runtime:
#   build_reader reader.html</pre>

<p class="ran">run on 2026-09-30 at 23:02: "15 of 15 chapters, 3 of 3 world pages", every edition green, in 3 minutes 22 seconds</p>

And to play the fifteen-minute demo for decision makers, whose last line must read "DEMO: 20 proved, 0 not proved":

<pre>cd libraries/stzlib/base/education/demo
# run demo with the repository's runtime:
#   demo rehearsal</pre>

<p class="ran">run on 2026-09-30 at 23:10, in 49 seconds, 20 proofs out of 20</p>

## Write {#write}

Questions, defect reports and proposals go through the <a href="https://github.com/mayouni/stzlib/issues">issues of the GitHub repository</a>. A security flaw is reported privately through the repository's security advisories, as its <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a> says. An edition of the course in your language starts with a folder of plain-text chapters: the Learn page says how the course's court will judge it. For the enterprise edition, write through the same issues: the Offering page says what it contains.

## Check this site offline {#offline}

Before a presentation with no network, open <a href="../deck-check.html">deck-check.html</a> from the site's folder: the page loads every asset the presentation needs and says which one is missing.
