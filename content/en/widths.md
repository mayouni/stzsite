---
title: Four widths
title_html: Four <i>widths</i>
kicker: One function, four widths
lede: One function can run on lanes, on cores, on the graphics card or across nodes. The engine chooses by measurement, and the person sees nothing but the speed.
description: The four widths of Softanza computation: lanes, cores, the graphics card and nodes under one measured dispatch, each width bit-identical or justified in writing, with the stage of each.
---

<ol class="steps">
<li value="1"><b>Lanes.</b> The same instruction on several values at once, inside the engine's loops. <span class="rx-src">built</span></li>
<li value="2"><b>Cores.</b> The same work across the machine's cores, used only where a measured threshold says it pays. <span class="rx-src">built</span></li>
<li value="3"><b>The graphics card.</b> Computation on the card, with the card woken before anything is timed. <span class="rx-src">built · see <a href="atlas/gpu.html">the GPU area</a></span></li>
<li value="4"><b>Nodes.</b> The same work across machines, supervised. <span class="rx-src">built · see <a href="host.html">the host</a></span></li>
</ol>

The rule that holds the four together: a route is taken only where a measurement shows it wins, and its answer is bit-identical to the plain route's or the difference is justified in writing. Elementwise work on small data was measured and left on the plain route, because it did not win.

<p class="proof"><b>in construction</b> The widths are built. A vocabulary that would let a programmer say which width they want in plain words is specified and has no code. The measurements behind each threshold are in the library's own records and are not reprinted here.</p>
