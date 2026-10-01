# Learning from the Wolfram Language site, for Softanza

*Read on 2026-10-01 between 02:05 and 02:30: wolfram.com (home), /language, /language/core-areas,
/language/principles, /language/fast-introduction-for-programmers, /language/elementary-introduction,
/language/core-areas/geography, /language/core-areas/machine-learning, /notebooks,
reference.wolfram.com/language (the Documentation Center), /ref/GeoDistance, /guide/LLMFunctions.
Four pages were also captured as pictures at laptop width. What follows is what the site DOES, then
what transfers to Softanza without borrowing its identity. Softanza is not a symbolic mathematics
system and never claims Wolfram's curated corpus; it is the makers platform of the agentic era, and
the comparison is about how a computational platform is SHOWN.*

## 1. What the Wolfram site does, page by page

**The home page is a wall of outputs, not a paragraph.** Hundreds of real computed pictures (plots,
3D solids, molecules, maps, graphs, images) under one line, "Making the world computable... since
1988". Then three exhaustive lists: fields it serves (about 100: from AgTech to Ruliology), built-in
capabilities (about 100: from device connectivity to LLM programming), and deployment targets
(about 20: web apps, notebooks, mobile, AR/VR, 3D prints, APIs, blockchain). The reader learns the
breadth by scrolling, before reading a single sentence of argument.

**The Language page opens with one definition sentence.** "Wolfram Language is a symbolic language,
deliberately designed with the breadth and unity needed to develop powerful programs quickly. By
integrating high-level forms, like Image, GeoPolygon or Molecule, along with advanced superfunctions,
such as ImageIdentify or ApplyReaction, Wolfram Language makes it possible to quickly express complex
ideas in computational form." One sentence names the kind of thing, the design intent, three example
nouns and two example verbs. Then three principle-and-picture rows (knowledge built in; symbolic
programming; the trajectory, shown as a growth chart of built-in functions from version 1 to 15), a
live playground, the highlighted core areas as 19 tiles each with a real output picture, the complete
scope as 24 coloured tiles (the documentation tree), then learning entries, deployment, community,
design process.

**Every core area has the same skeleton.** Title ("Wolfram Geography, a core part of Wolfram
Language"), a one-sentence promise ("Analyze, compute and visualize geographic data"), a hero picture
of a real output, "Get started"; then six to eight capability blocks, each a verb-led paragraph of what
YOU can do ("Trust your geographic analysis...", "Answer the where and the why..."), a real picture, and
links to the documentation guides; a live playground; the documentation tree; courses; blog, community
and Stack Exchange; related core areas; the product entry. The page is a template over data, and that
is why 19 of them could be built.

**The principles page turns the thesis into twelve named principles.** Each has a slogan ("Automate as
much as possible"), one philosophy sentence, and three to five bullet proofs with numbers ("thousands of
meta-algorithms", "the codebase in Wolfram|Alpha is over 15 million lines"). Knowledge-based
programming; meta-algorithms; coherence; everything is an expression; a model of the world; natural
language understanding; universal deployment; computable documents; connect to everything; everything
interactive; fully scalable; multiparadigm fusion; three decades of lineage.

**The Documentation Center is the heart.** 24 guide areas, guide pages, and a fixed function-page
template: usage forms, Details and Options, Examples graded Basic / Scope / Options / Applications /
Properties and Relations / Possible Issues / Neat Examples, every example runnable in the cloud, See
Also, Related Guides, History ("Introduced in 2008 (7.0), updated in 2024 (14.1)"), Cite this as.
Workflows ("Working with data", "Deploying to web and mobile") sit beside the reference.

**Learning has one door per reader.** "Fast Introduction for Programmers" (25 short sections, with
notes for Java and Python users), "An Elementary Introduction to the Wolfram Language" (a book, "run
everything in this book", with an interactive open course), a fast introduction for math students,
Wolfram U. The book is the model Softanza's Learning System already follows.

**Numbers that carry, and a trajectory.** "6,000+ built-in functions", "version 15", "since 1988",
"13,000+ Demonstrations", a chart of built-in functions over time. Every number is a count of
something that exists.

**Try it now, everywhere.** A live playground on the Language page and on every core-area page;
"Try now"; "find out if you already have access through your organization".

**The AI era, as a nav entry and a guide.** "For AIs" sits in the top navigation. The LLM guide lists
Chat Notebooks, LLMFunction, LLMTool ("calling the Wolfram Language from within LLMs"), semantic
search and RAG, a prompt repository, and service connections to every model vendor. Wolfram positions
itself as the exact tool an LLM calls.

**The visual system.** One brand colour carries every header band; each core area gets a tinted band
and a real output picture; text and picture alternate row by row; tiles are dense and uniform; the
footer carries the whole map of the site.

## 2. What transfers to Softanza, and how

| Wolfram does | Softanza does, in its own identity |
|---|---|
| defines "computational language" in one sentence at the top | defines its three words at the top of the home page: **maker**, **platform**, **agentic era**, one sentence each, each with a picture and a proof |
| shows the platform as 19 core areas with a real output picture each | shows the 28 Atlas groups as **core areas**, each with a real picture rendered by the engine (a map, a diagram, a plot, a table, a boxed text, a spectrogram); the honest ratings stay one click away as "where it stands" |
| one skeleton for every core-area page | one skeleton for every area page: promise, hero render, capability blocks that say what a maker DOES with it, one example run, the narrations of that area, the chapter of the course that teaches it, related areas, then the Atlas lanes |
| twelve principles with slogan, philosophy and proofs | **Principles & concepts** page: declare a language · everything is judged · one engine, many faces · agents that cannot hurt you · knowledge of your world · code that reads as a sentence · in your language · exact by default · honest by design · sovereign by construction · programming by heart · born in Africa |
| the Documentation Center with a function-page template | the library **documents itself**: a generated reference from the library's own doc-comments (a string alone answers 5,384 methods and can explain each), grouped by area, with examples run; plus the 134 narrations as pages, grouped by area |
| a learning door per reader, a book you run | the Learning System as the book ("run everything in this book"), a fast introduction for programmers built from the mental-model narration, the six doors |
| a trajectory chart | a chart of guards, narrations and commits over time, rendered by the engine from git |
| "For AIs" in the navigation | **For agents** in the navigation: how an agent reads Softanza (Ask, HowTo, ExplainMethod), the constrained grammar, the agent file, the court's refusal sentences, the crossing |
| a live playground | honestly absent until the browser engine runs the library; every example carries its output run on the night of publication, and the Start page gives the one-folder install |
| a wall of outputs on the home page | a wall of outputs on the home page, every tile a render the engine produced, linking to its area |
| numbers that count things | 28 areas, 334 lanes, 401 engine modules, 5,384 methods on one class, 134 narrations, 30 chapters in 4 languages, 38 security guarantees, 5,822 commits |

## 3. What does NOT transfer

- **The claim of the world's facts.** Wolfram knows the world; Softanza knows YOUR world. The site
  keeps the inverse asset and never lists curated data as a strength.
- **The vendor's AI posture.** Wolfram is the tool an LLM calls. Softanza is the world an agent
  cannot hurt: the LLM proposes, only a governed actor commits. "For agents" says this first.
- **Product-first navigation.** Wolfram sells Mathematica, Wolfram|One, the Engine. Softanza's
  products carry stages, and the site leads with the platform and the maker, not the price list.
- **Density as a value.** Wolfram's pages are dense because thirty-five years earn it. Softanza
  shows the same breadth with honesty chips beside it, and never a figure without a file.

## 4. The three words, defined (draft for the author's ruling)

**Maker.** A maker is someone who turns what they know about a world into something that runs,
without waiting for the software industry: a teacher who declares a course, an analyst who declares
the rules of a bank, a merchant who declares a shop, a student who declares a game, a civil servant
who declares a procedure, and an agent that proposes a change under all of them. The maker is not
defined by programming skill but by ownership: the artefact is theirs, in plain text, and it does not
expire.

**Platform.** One engine written in Zig, exposed through one language, Haro, covering 28 areas of
computation, from strings and exact numbers to maps, sound, GPU and neural inference, under one law:
everything is declared, everything is judged by running, nothing is believed. The Atlas rates every
area against the leaders of its category and shows the gaps.

**Agentic era.** Humans and agents meet in declared languages, small and closed, not in general code.
A grammar constrains what an agent can emit; a court judges what it proposes; a safe world lets it
rehearse without touching reality; only a governed actor commits. The agent is the sixth reader of
every Softanza language, and the one it was designed for last.

## 5. The site, re-planned

| page | what changes |
|---|---|
| home | after the onboarding scene: the three words with picture and proof; the wall of outputs (28 tiles); the agentic strip (propose, judge, commit); learn; start |
| why | becomes **Principles & concepts**: the twelve principles, slogan, philosophy, proofs |
| platform | becomes **Core areas**: the 28 tiles with pictures, the complete scope, the engine figures, the trajectory chart |
| atlas | stays: the honest rating view, linked from every area as "where it stands" |
| atlas/<area> | gains the Wolfram skeleton: promise, hero render, "what a maker does with it", example run, narrations, course chapter, related areas; lanes last |
| govern | becomes **Agents**: the agentic paradigm for humans, and "for agents" for the machines that read the site |
| makers | opens with the definition of a maker, then the six doors |
| learn, products, africa, start, tour | kept; Ring removed everywhere; the language is Haro |
| docs (new, Release 1) | the generated reference, by area, from the library's own explanations; the narrations as pages |

## 6. Ring

Ring is retired and the site does not name it: not the runtime, not the bridge, not any product
carrying its name. Code blocks are labelled "Softanza"; the language is Haro, with its stage shown;
the install instructions point to the repository, which carries the runtime details. Product names
with the Ring prefix are shown under their Haro names.
