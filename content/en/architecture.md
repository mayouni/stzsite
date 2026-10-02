---
title: Architecture
title_html: The <i>architecture</i>
kicker: Three layers, one engine, a folder per domain
lede: Softanza is three layers of one vocabulary over one engine. A program chooses its layer by the file it loads; the engine does the heavy work behind a plain C interface; and every domain is a folder with an object that opens it. This page says what each part holds today, and where the single executable stands.
description: How Softanza is built: the core, base and max layers, the Zig engine beneath them, a folder per domain, and the road to one executable without dependencies.
---

## Three layers over one engine {#layers}

Softanza speaks one vocabulary at three depths. Core holds the lean essentials, for programs that need little. Base is the whole platform, the one the rest of this site describes. Max adds advanced pieces on top of base. A program chooses its depth by the file it loads; base loads core first, and max loads base.

<figure class="diagram"><img src="../assets/img/diagrams/layers-en.png" alt="Four bands, top to bottom. Max, stx, loaded by stxLib: walkers, big numbers, multilingual strings, a test framework, 40 classes. Base, stz, emphasised, loaded by stzLib: the full platform, 44 domain folders, 644 classes, some 36,000 method names. Core, stk, loaded by stkLib: the lean essentials, strings, lists, numbers, objects, 17 classes. The engine, Zig: 89 modules behind a plain C interface, the substance written once." width="1376" height="700"><figcaption>Three layers of one vocabulary over one engine. A program chooses its layer by the file it loads.</figcaption></figure>

<!--SHOWCASE:architecture:1,2-->

The same question gets the same verb at both depths; base simply knows more ways to ask it.

## The engine beneath {#engine}

Beneath the three layers is one engine, written in Zig and compiled to machine code: 89 modules built from 401 source files, four for core and 85 for base. Each module has two doors. One is a plain C interface of 752 functions, which any language able to call C can use. The other is the face the library calls, with 2,652 functions registered for it. When the library loads, it opens each module and picks the right file for the system it runs on.

<!--SHOWCASE:architecture:3-->

<p class="way"><span>The Softanza way</span> The substance is written once, in the engine, and the layers above are its faces. A second face, or a second machine, reaches the same modules through the same C interface, so nothing is written twice and nothing drifts apart.</p>

<p class="proof"><b>in construction</b> The engine is built and run on Windows today. A Linux build of 85 of the 89 modules exists on a working branch; the four that remain handle HTTP, events, interfaces and windows.</p>

## A domain is a folder {#modules}

Each domain lives in its own folder, with an object that opens it and a data format of its own; a domain never scatters global functions with no object behind them. That is the first law of the architecture. Base holds 44 such folders today:

<p class="mono">agentic · app · appserver · cluster · common · conversation · data · datetime · education · error · extercode · extincode · file · geo · governance · gpu · graph · graphics · gui · i18n · learning · linguistic · list · math · meta · natural · network · neural · number · object · optim · perf · platform · reactive · refine · reflect · regex · security · service · sound · stats · string · system · table</p>

Loading follows the layers today: a program loads core, base or max, and base brings all its folders at once. A single engine module can also be opened alone, as the GPU guards do. A loader that brings one domain of base without the others is not built yet.

## One executable, no dependency {#binary}

What exists today:

- **A builder that crosses platforms.** From one Windows machine, the builder uses Zig to compile programs for Windows, Linux and the web, and checks each file it produces by its first bytes. Its guard holds 38 checks.
- **A script with nothing to install.** A program in the platform's script becomes a native executable with its virtual machine compiled into it, so the target machine needs no runtime installed. This is proven today on a one-line program.
- **Only what is used, for the web.** A product declares what each of its parts needs, and the builder ships only the engine groups declared: a build that carries the solver alone is smaller than the full one.

<!--SHOWCASE:architecture:4-->

What does not exist yet is a whole Softanza program and its engine packed into one file with no dependency, holding only the code the program uses. That is the direction. The next distribution, still an experiment, is designed as one static binary, and its runner already embeds its virtual machine in a single executable.

<p class="proof">Counts read in the library at commit 010743cce: classes declared in the files each entry file loads, and method names counted as definitions, aliases included. Sources: <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/stzLib.ring">the base entry file</a>, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/engine/build.zig">the engine's build file</a>, <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/system/stzBuilder.ring">the builder</a> and <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/builder_narrated.ring">its guard</a>.</p>
