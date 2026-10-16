---
title: Start
title_html: <i>Start</i>
kicker: In one hour
lede: One public repository, an install in three steps, a first program, the course reader as a page of this site. Every command on this page was run on the night of publication.
description: How to start with Softanza: the GitHub repository, the install, the first program, the first narration, the course reader, and where to write.
---

<p class="proof"><b>The runtime, plainly</b> <!--RUNTIME--></p>

## Who are you? {#who}

Each reader has a page that reads the whole site from their place: where to start, the path, and the pages that matter to them.

<ul class="readings"><li><a href="for-programmers.html">For a programmer</a> · You write the application; Softanza is the part of it that reads like a sentence.</li><li><a href="for-analysts.html">For an analyst or a designer</a> · You know the world of the business; you declare it, and it becomes something that runs.</li><li><a href="for-architects.html">For an architect</a> · You answer for the whole vertical, from the machine to the organisation.</li><li><a href="for-leaders.html">For a decision-maker</a> · A CTO, a government, a business: what you would adopt, and what it is proven to do.</li><li><a href="for-educators.html">For an educator or an author</a> · You teach, design courses or write about code: everything here runs, in your learners&#x27; language.</li><li><a href="for-agents.html">For an AI agent</a> · An agent, or the person who deploys one: what to read, and what the agent may do.</li></ul>

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

## Which page answers what {#map}

The site has one page for each kind of question. When you do not know a name, press <kbd>/</kbd> or <kbd>Ctrl</kbd>+<kbd>K</kbd> on any page: the search finds classes, methods, areas and recipes.

<table class="declared">
<thead><tr><th>You want to</th><th>Open</th></tr></thead>
<tbody>
<tr><td>learn the way of thinking, step by step</td><td><a href="learn.html">Learn</a>, then <a href="book.html">the interactive course</a></td></tr>
<tr><td>do one task now, such as removing duplicates</td><td><a href="howto.html">How-to</a></td></tr>
<tr><td>know exactly what a method does, and its other forms</td><td><a href="reference.html">Reference</a>, or the search</td></tr>
<tr><td>see everything one area offers, from strings to maps</td><td><a href="areas.html">The areas</a></td></tr>
<tr><td>understand why a part was designed the way it is</td><td><a href="narrations.html">Narrations</a></td></tr>
<tr><td>know what is built and what is not yet</td><td><a href="proven.html">Proof</a></td></tr>
<tr><td>decide whether an organisation should use it</td><td><a href="offering.html">Organisations</a></td></tr>
<tr><td>point an AI agent at it</td><td><a href="agents.html">For agents</a></td></tr>
</tbody>
</table>

## The first narration {#narration}

A narration is a document that tells a part of the library as a story, in code written to be run as it is read. Start with <a href="narrations/stz-mental-mode-narration.html">the mental model</a>, then <a href="narrations/stz-agents-that-cannot-hurt-you-narration.html">the agents that cannot hurt you</a>. To see a narration judged block by block, open <a href="narrations/stz-repetition-with-elegance-narration.html">Repetition with Elegance</a>, run for this site: its six blocks print what they promise. All 135 are listed under Learn, in Narrations.

## The course reader {#reader}

The reader is a page of this site: <a href="../reader.html">open the reader</a>. It was built from the library on 2026-09-30, and the Learn page says how to learn with it, step by step. To rebuild it yourself, from your copy of the repository:

<pre>cd libraries/stzlib/base/education/tools
ring build_reader.ring reader.html</pre>

<p class="ran">run on 2026-09-30 at 23:02: "15 of 15 chapters, 3 of 3 world pages", every edition green, in 3 minutes 22 seconds</p>

And to play the fifteen-minute demo for decision makers, whose last line must read "DEMO: 20 proved, 0 not proved":

<pre>cd libraries/stzlib/base/education/demo
ring demo.ring rehearsal</pre>

<p class="ran">run on 2026-09-30 at 23:10, in 49 seconds, 20 proofs out of 20</p>

## Your first application {#application}

A first program is a list. A first application is a world: <a href="first.html">your first application</a> says what it is made of and which narration builds one, and <a href="applications.html">the applications page</a> says what holds it up and which surfaces exist.

## Write {#write}

Questions, defect reports and proposals go through the <a href="https://github.com/mayouni/stzlib/issues">issues of the GitHub repository</a>. A security flaw is reported privately through the repository's security advisories, as its <a href="https://github.com/mayouni/stzlib/blob/main/SECURITY.md">SECURITY.md</a> says. An edition of the course in your language starts with a folder of plain-text chapters: the Learn page says how the course's court will judge it. <a href="editions.html">The Editions page</a> says what exists today and what is to come.

## Check this site offline {#offline}

Before a presentation with no network, open <a href="../deck-check.html">deck-check.html</a> from the site's folder: the page loads every asset the presentation needs and says which one is missing.
