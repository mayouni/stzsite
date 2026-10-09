---
title: Why Softanza leaves Ring
title_html: Why Softanza <i>leaves Ring</i>
kicker: The story, told once
lede: Softanza was born on Ring and is leaving it. This page says why, in three reasons, and what stays. It names decisions and documents and never a person's character, and it says thank you first.
description: Why Softanza leaves Ring: thanks first, then three reasons, the limits met at production scale, a direction that could not be influenced, and governance as a design property, and what stays.
---

## Thank you first {#thanks}

Softanza was born on Ring. For years its author wrote the library in Ring, taught the language, promoted it in the field, and wrote its book, <i>Beginning Ring Programming</i> (Apress, 2020). In 2021 the library was first described to the Ring community, and the first presentation of Softanza, in 2022, called it a best friend of existing Ring programmers.

Ring's simplicity and its multiparadigm expressiveness are the two things Softanza keeps, because they were never the problem.

## Three reasons {#reasons}

<ol class="steps">
<li value="1"><b>The limits were met at production scale.</b> A scalar costs hundreds of bytes, and a list item seven times a double, by the arithmetic of the language's own author. Strings are copied at every call boundary. There is no stable sort, no regular-expression engine and no strict mode, and Unicode is left to a graphics toolkit. The author reproduced each of these limits while writing a library of this size.</li>
<li value="2"><b>The direction could not be influenced.</b> In the author's experience, narrow defects were fixed quickly and with thanks, while questions about where the language is going were answered, over years, with the same advice: keep the core simple, and do the rest in C extensions or in the graphics bridge. Ring++ was made to answer three pain points, performance, typing and build, without leaving Ring.</li>
<li value="3"><b>Governance is a design property.</b> A dependency whose direction cannot be influenced and whose behaviour cannot be fenced does not pass due diligence for the regulated domains Softanza serves, a bank or a ministry. The author's concern is also ethical: where one person decides the destination of others' work, the others have nothing to stand on.</li>
</ol>

## What Softanza does about it {#commitments}

The answer is not independence for its own sake. It is independence for the people who build on Softanza, and it takes the form of things this site runs, not of promises.

<ul class="narr">
<li><b>An engine with no third-party dependency</b>, written in Zig since 2025. <span class="rx-src">built · see <a href="architecture.html">the architecture</a></span></li>
<li><b>A sovereign virtual machine and compiler</b>, for Haro. <span class="rx-src">in construction · see <a href="platform.html">the platform</a></span></li>
<li><b>An open core</b> under the MIT licence, public from 12 March 2022. <span class="rx-src">built · see <a href="start.html">Start</a></span></li>
<li><b>Dated decisions and proofs.</b> Every claim on this site links to the file, the guard or the render that proves it. <span class="rx-src">built · see <a href="goals.html">the design goals</a></span></li>
<li><b>A write is a proposal.</b> Nothing changes a world without a governed actor. <span class="rx-src">built for files, in construction for data · see <a href="store.html">the store</a></span></li>
<li><b>A person's right to reach a person.</b> <span class="rx-src">designed, not built · see <a href="agentic.html">agentic</a></span></li>
</ul>

## What stays {#stays}

<!--RUNTIME-->

The scenario guards are the test of the promise that the code already written keeps working. Softanza says thank you to the language it grew up on, and goes where its users' sovereignty requires.

<p class="proof"><b>in construction</b> This page names decisions and documents, never a person's character. The limits in the first reason are the author's measurements; their reproductions are not public yet, and when they are, each limit will link to its own. Nothing here quotes a private document. How the history is dated is on <a href="roots.html#dates">the roots page</a>.</p>
