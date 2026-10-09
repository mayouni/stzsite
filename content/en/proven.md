---
title: Proven
title_html: <i>Proven</i>
kicker: What judges the foundation
lede: A foundation is proven by what tries to break it. Here is what tries, counted from the library, and what is missing.
description: How the Softanza foundation is proven: test files and scenario guards counted from the library, five fuzzers, three property suites, a local gate and a bill of materials, with what is missing said plainly.
---

<ul class="narr">
<li><b>Tests.</b> 5,284 test files in 158 folders, of which 527 are scenario guards and 4,474 are numbered tests of the classic form, counted from the library at commit 4a184e6f0. <span class="rx-src">built · see <a href="depth.html">depth</a></span></li>
<li><b>Fuzzers and property suites.</b> Five fuzzers and three property suites on the engine's parsers and cryptography. <span class="rx-src">built · a reading by an outside assessment of 2026-10-07</span></li>
<li><b>A gate before every commit.</b> A local security gate checks a change before it is kept. <span class="rx-src">built</span></li>
<li><b>A bill of materials.</b> A tool lists what the engine is made of, its vendored libraries included. <span class="rx-src">built</span></li>
<li><b>A test reader.</b> A runner that reads every test file as a tour, to say which promises it keeps. <span class="rx-src">in construction</span></li>
</ul>

<p class="proof"><b>in construction</b> What is missing: no hosted continuous integration, and no instrument that measures coverage. Five older runners do not emit a machine-readable verdict, which is why this site runs its own. A test that passes proves what it tests, and the pattern page shows two of the library's own tests that now print the wrong answer.</p>
