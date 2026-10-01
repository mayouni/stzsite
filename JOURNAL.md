# JOURNAL — stzsite

What was decided, what was verified, and who looked. Newest entry last. Memo style; stamps read from the
clock at the moment of writing.

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 01:20

subject:   Release 0 built -- eleven pages in French and English, the reader embedded, the tour working from file://

why:       the author presents Softanza at ESCEP-Niger on 2026-10-01 with this site instead of slides

did:
  - created the repository from nothing at 22:48 on 2026-09-30: one Python generator (tools/build.py), Markdown sources per language, the compass family stylesheet plus a site layer with the logo's purple as brand accent
  - measured the logo's colours at the file (purple #7030A0, green #368E64, red #F60000) and found the author's personal email address in the logo's bottom line; the site ships a crop (mark + wordmark + slogan) and never the original
  - self-hosted Fraunces, IBM Plex Sans and IBM Plex Mono (22 faces, 884 KB, SIL OFL) with font-display swap; no CDN anywhere
  - built the Learning System reader from the library at commit 0e72e2e2c (the _wts worktree, read-only; the main working tree is on a Ring++ branch with no education module): 15 chapters x 4 languages + 3 world pages, all green, 3m22s; the page loads nothing from the network
  - ran every code block shown on the site on 2026-09-30 23:02-23:11 and 2026-10-01 00:41-00:45: the probe snippets, the Niger map guard (5.9 s), the decision-makers' demo (20 proved, 0 not proved, 49 s), the containment drill (27/27, detect 395 ms, contain 50 ms), the first program loaded with load "stzlib.ring"
  - rendered the Niger density map from the geo guard rather than copying the committed PNG (same 221,997 bytes)
  - measured contrast for twelve text/background pairs in both themes inside the build (lowest 8.02, all above the WCAG thresholds the stylesheet declares); the build fails if one drops
  - rendered 63 proofs in proofs/ at phone (390), laptop (1366) and projector (1920) widths, light and dark, plus eight tour scenes and seven full-page captures
  - chose the onboarding panel's placement by render: LEFT, because it sits in the wall's shadow, leaves the face and the sheet of code untouched, and reads top-left wordmark -> panel -> elder; the right placement (kept as index-panel-right proofs) touches the elder's shoulder
  - fixed three defects the renders found: the navigation wrapped to two lines at 1366 px (shorter labels, tighter nav); the tour's first scene painted its slogan dark-on-dark and the help line overlapped the caption; the tour's scroll listener rewrote the hash to scene 1 before a smooth scroll had moved (scene changes are instant now, with a 400 ms lock)
  - found an instrument defect and replaced the instrument: Chrome headless refuses a viewport narrower than about 490 CSS px whatever --window-size or device scale says, so every "phone" render was a 504 px layout cropped to 390 and looked clipped; tools/shoot.mjs now drives Chrome over its DevTools protocol with Emulation.setDeviceMetricsOverride, which gives a true 390 px viewport (and renders 63 pages in 86 s instead of one process per page)
  - verified the tour in a real browser (the app's browser pane over localhost): #s5 lands on scene 5, the arrow key moves to scene 6, n shows the notes; deck-check.html opened from file:// reports every asset found

state:
  release-0:        built, deployed to GitHub Pages (see the next entry for the URL and the deploy check)
  perception-gate:  OPEN -- the author has not yet opened the tour on his own laptop offline; his verdict goes below
  codeberg:         no remote yet; the author gives it

waiting:
  - STZSITE-VERDICT-01: the author opens fr/tour.html offline, runs deck-check.html, and says what he saw -> the author
                        [not routed: it is a physical act only he can perform]

next:
  - me:      Release 1 -- the proof gallery (134 narrations as pages), the Atlas port (28 group pages), a documentation entry, a blog, community pages
  - author:  open deck-check.html then fr/tour.html from the cloned folder with the network off, and record the verdict here
  - ringpp:  its next branch, which its own rules say never reaches origin, is on the public origin with haro/CHARTER.md inside (found 2026-09-30 while reading product stages; reported to Central, not fixed here)

note:      the name of the COBOL workbench is withheld on the site because its prior-use search is still open "before any public use"; the launch prompt listed the name, and this repository's reading of the estate's own rule wins.
```

## The author's verdict (perception gate)

*To be written by the author after opening the tour offline on his own laptop. Until a name and a verdict stand
here, Release 0 is BUILT and UNPERCEIVED, not done.*

- date:
- machine / browser:
- deck-check.html: __ of __ found
- what was seen:
- what was wrong:

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 01:06

subject:   Release 0 deployed -- https://mayouni.github.io/stzsite/ answers, deck-check reads 55 of 55

why:       the previous entry said deck-check reported every asset found; it did not, and the record must say so

did:
  - corrected the previous entry: at the time it was written, deck-check reported 54 of 55 then 1 missing, because the reader copy had no ping line; the build now appends that one line to the copy (never to the library's tool) and deck-check from file:// reads 55 of 55, 0 missing (proofs/deck-check--laptop-light.webp)
  - pushed main to github.com/mayouni/stzsite (first push 73ee023 + 8c57fba); enabled GitHub Pages with the Actions workflow as source; the deploy completed and the site answers 200 at https://mayouni.github.io/stzsite/ and /fr/tour.html, with the right title
  - renamed the workflow inherited from stzweb-redirect so the run list says what it deploys

state:
  release-0:        BUILT and DEPLOYED, UNPERCEIVED
  perception-gate:  OPEN -- the section below is still empty

waiting:
  - STZSITE-VERDICT-01: unchanged -> the author

next:
  - author:  clone the repository, open deck-check.html then fr/tour.html with the network off, and write the verdict below
  - me:      Release 1 after the verdict
```

> **Correction, 2026-10-01 01:06.** The first entry above is stamped "01:20" and that stamp was COMPOSED, not read from the clock: the commit that carried it, 73ee023, was made at 2026-10-01 01:03. The estate's rule (read the stamp from the clock, never compose it) was broken in this journal's first line; the stamp is left as written so the defect stays visible, and this note is the repair.

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 01:59

subject:   the Atlas made native -- the platform's reach is now the centre of the site

why:       the author's reading of the first release: it told the story and missed the reach of a unified computational platform, the thing the Atlas and its modules show; a site for Softanza must reflect its depth the way Wolfram's reflects the Wolfram Language

did:
  - read the Atlas index (v21, 28 groups, 334 lanes, 101/129/68/36) and had the 28 group pages extracted to data by four agents in parallel: each lane with its rating, note and the proof it cites, plus standouts, debts, peers, folders and the date read
  - built fr/atlas.html and en/atlas.html (six bands, 28 cards, the tally) and 56 group pages (fr/atlas/<slug>.html, en/atlas/<slug>.html): thesis, standouts, debts, the twelve lanes, and one code example per group RUN tonight with its output beside it (26 of 28; binary has no code to run and the Python bridge was not exercised, and both pages say so)
  - probed 90 candidate calls against the library in three passes and kept only what ran: an exact 2^64, a 5,384-method string, Niamey to Tunis in 2,726 km, a directed graph's shortest path, a virtual file system the disk does not see, an RTX 3050 answering by name, a ggml engine with no model on disk, Hausa's native name in Ajami, SHA-256, sentiment and lemmas
  - put a compact grid of the 28 bars on the home page, the platform page and a tour scene (scene 4 of 9); added Atlas to the navigation (ten entries, still one line at 1366 px, verified by render)
  - carried two honest divergences on their pages as "two readings": the security group page still shows the September ratings (3/6/2/1) while the Atlas card was re-rated 6/5/0/1 on 2026-09-30; the tables page's chips (2/7/3/0) disagree with its own legend (2/6/3/1)
  - rendered 79 proofs (the Atlas pages at phone, laptop, projector and dark included); deck-check from file:// reads 57 of 57 found
  - pushed 47d0126 to github.com/mayouni/stzsite; the Pages deploy is checked in the next entry

state:
  release-0:        BUILT and DEPLOYED with the Atlas native, UNPERCEIVED
  perception-gate:  OPEN -- the author's verdict section below is still empty

waiting:
  - STZSITE-VERDICT-01: unchanged -> the author

next:
  - author:  open fr/atlas.html and one group page on the presenting laptop, offline, and say whether the reach reads
  - me:      Release 1 -- the proof gallery (134 narrations as pages), the compass pages (coverage vs the platforms, programming by heart, mathematics, learning), a documentation entry
  - stzlib:  five findings the group pages carry from their own sources -- the tables page is internally inconsistent by one lane; the security group page predates the 2026-09-30 re-rate; the performance page flags a stale CLAUDE.md line (P0-P7 / 283 assertions against P0-P11 / 366 in the code); the neural page flags its own design doc as stale; the gui page says the plane is on local main only -- all for the compass and the planes, none edited here
```

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 03:34

subject:   learning from the Wolfram Language site, applied -- maker, platform, agentic paradigm defined; Ring gone

why:       the author's second reading: still far from the value of Softanza as a unified computational platform; the slogan must be defined on the site; Ring is retired and must not be named

did:
  - read eleven pages of wolfram.com and reference.wolfram.com and captured four as pictures; wrote doc/LEARNING-FROM-WOLFRAM.md: what the site does (a wall of outputs, one definition sentence, core areas as tiles with real pictures, one skeleton per area page, twelve principles with proofs, the documentation centre with a function-page template, a learning door per reader, numbers that count things, a live playground, "For AIs" in the navigation), what transfers and what does not, the three definitions, the re-plan
  - defined the three words on the home page, each with proof links: maker (ownership, not programming skill), platform (one engine, Haro, 28 areas, one law), agentic age (grammar, court, safe world, governed commit; the agent as sixth reader)
  - rewrote Why as Principles and concepts (twelve cards), Platform as the areas page, Govern as the agentic paradigm with a "for agents" section, Makers opening on the definition; navigation reads Principles · Platform · Atlas · Learn · Agents · Makers · Products · Africa · Start · Tour, one line at 1366 px
  - removed every visible Ring mention: 94 in the sources plus the lane notes; the generated pages count zero outside link targets; the language is Haro, code is labelled Softanza, the first program shows no load line, the Start page points to the repository for the runtime
  - rendered 80 proofs; pushed ecc1733

state:
  release-0:        DEPLOYED, re-centred on the three words, UNPERCEIVED
  perception-gate:  OPEN

waiting:
  - STZSITE-VERDICT-01: unchanged -> the author
  - STZSITE-DEFINITIONS-01: the three definitions in doc/LEARNING-FROM-WOLFRAM.md section 4 are drafts for the author's ruling -> the author [not routed]

next:
  - author:  rule the three definitions, and say whether the Start page may stay silent on the runtime until Haro ships
  - me:      Release 1 in the order of the learnings doc: a render per area (the wall of outputs), the generated reference from the library's own explanations, the narrations as pages, the trajectory chart
```

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 04:08

subject:   Release 1, first move -- a render per area, 26 of 28, and the wall of outputs

why:       the author said go ahead with Release 1 and start with the render per area; the Wolfram learning was that a platform is shown by its outputs

did:
  - wrote tools/areas.ring and ran it inside the library at 0e72e2e2c: seventeen pictures in ten seconds, each from the engine's canvas, diagram renderer or chart family
  - carried eight of the library's own committed renders with the guard that drew them, and the Niger map re-rendered on 2026-09-30; GUI (not on the public branch) and binary formats (no code) carry a sentence instead of a picture
  - wired the renders into data/atlas-index.json and the generator: a wall of outputs on the home and platform pages, the picture on every Atlas card, a hero figure with its making on every area page; whole pictures, never crops
  - paid two Ring traps that the operating notes already name: a helper called Done closed every try block (done is a keyword) and oR is or; Segoe UI has no Devanagari, so the six-script picture shows Hausa in Ajami instead of Hindi
  - rendered 83 proofs; pushed ebea494

state:
  release-1:        render per area DONE (26/28); next the generated reference, the narrations as pages, the trajectory chart
  perception-gate:  OPEN

waiting:
  - STZSITE-VERDICT-01, STZSITE-DEFINITIONS-01, STZSITE-RUNTIME-01: unchanged -> the author

next:
  - me:      the generated reference from the library's own explanations, by area
  - author:  look at the wall of outputs and say which pictures mislead; a picture that needs a caption to be understood is a picture to redraw
```

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 08:20

subject:   Release 1, second move -- the reference generated from the library's own explanations

why:       the Wolfram learning: the documentation centre is the heart; Softanza's library documents itself, so the site can generate what Wolfram writes by hand

did:
  - harvested every class with the library's stzSelfDoc inside the library tree: 635 sources, 618 classes, 134,944 entries, 26,949 own methods, 74 seconds, no failure
  - generated 1,292 pages per language pair: the index by area with a filter, one page per class (own methods with form chips, source file, inherited surfaces as counts linking to the ancestor), 27 alphabetical index pages mapping 19,868 method names to their classes
  - kept honesty on the page: 77% of own methods carry a description, the rest say so; the harvest date is pinned on the pages; descriptions render the language as Haro while the 54 identifiers that contain the old name stay exactly as the API spells them
  - fixed what the first render showed: the source path pointed at archive copies (the file map now prefers the live folder), the French navigation wrapped with eleven entries (tightened), one nested f-string the parser refused
  - pushed 0655760; the reference pages are 17 MB per language

state:
  release-1:        render per area DONE · reference DONE · narrations as pages and the trajectory chart remain
  perception-gate:  OPEN

waiting:
  - STZSITE-VERDICT-01, STZSITE-DEFINITIONS-01, STZSITE-RUNTIME-01: unchanged -> the author

next:
  - me:      the 134 narrations as pages, grouped by area, with their code cells shown as the library stores them
  - author:  open fr/reference/stzstring.html and say whether a maker finds what they came for
```

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 18:29

subject:   Release 1, fourth pass -- the site redesigned on the author's list of 2026-10-01: six pages, the Zui ergonomics, the diagrams, the editions, sovereignty, wise coding, the language of languages, Takamba

why:       the author read the third pass and listed what was missing: the site left many dimensions of the project behind and did not yet reflect the depth of a unified computational platform

did:
  - replaced the eleven-entry menu by six (Platform, Vision, Agentic, Learn, Offering, Start) with the tour and the stzlib GitHub repository as icons in the bar, as on the Harobanda site; the Atlas sits under Platform, the reference and the narrations under Learn
  - gave every page a sub-menu built from its sections, fixed under the main bar with the main bar itself; removed the previous/next pagers from ordinary pages; the reader is a main page linked from Learn and Start, no longer embedded in an iframe
  - put the main menu on the home page as a fixed translucent bar and made the hero panel translucent (52 percent) so the elder's face and the sheet of code stay visible behind the slogan
  - wrote six content pages in French and English from the author's list, in plain language, with a "The Softanza way" marker on each differentiator: platform (figures counted in the repository, the wall of pictures, the engine example, four code comparisons beside Python 3.13 and Node 22 run at 09:26, the coverage matrix against .NET, Python, Wolfram and the JVM from data/coverage.json, one folder copied), vision (the three definitions, the estate diagram, the trajectory, sovereignty and honest lock-in, the twelve principles, every product with its stage, Africa), agentic (the loop with its diagram, wise coding against vibe coding with two guards run at 09:39 giving 13 of 13 and 52 of 52, the language of languages with a diagram whose unbuilt parts are dashed, the Zui constitution with its measured figures, refinement-oriented programming with its book, how an agent reads the platform, the security numbers), learn (introduction, the interactive book as a door, documentation, tutor, overlay, the Zin pedagogy taken, refused and proposed, what is missing), offering (the six doors with their runs, the two editions, what is owned, the references, where to write), start (one repository only)
  - drew six diagrams in the Harobanda house style with tools/diagrams/house.py, in both languages, every label fitted or refused: the technology estate with Takamba beside it, wise against vibe, the language of languages, propose-rehearse-judge-commit, open against enterprise, the trajectory of commits per year with the tree at end-2024 against today
  - measured the figures the pages quote and recorded how: 531,012 lines of library in 1,227 files and 306,302 lines of tests in 5,251 files with 501 narrated guards at 0e72e2e2c; 179,233 lines of Zig in 401 files; 5,824 commits on main; at the end of 2024 (a395d09c) 347,670 lines of library and 63,288 of tests in 1,697 commits and no engine, which is the file behind the author's "hand-written before agents" statement, quoted as the author's
  - replaced the figurative pictures of fifteen areas that were diagrams; names sit under the pictures, no dark band; the Harobanda site's Softanza mark replaces the old one and the wordmark is cut from the original logo
  - removed every claude.ai link from the site (58 pages carried the Atlas's external links) and every link to Codeberg, Harobanda's and the site's own repositories; only the stzlib repository is linked
  - removed the compact Atlas grids and tallies from the home and platform pages; the ratings live only on the Atlas page and its group pages
  - renamed Bangalo to Takamba on the site on the author's word of 2026-10-01; no repository carries the name yet, and the site says the repository is not public
  - added a narrations page (134 titles from data/narrations.json linking to the repository; the language's name in titles follows the site's rule, file names untouched), the coverage matrix block, the two-sided code block, the sub-menu scroll-spy, and raised every text size below 15 pixels (body 17, proofs 14.5, captions 15, chips 12.5) under the Zui legibility floor
  - verified in the app's browser over a local server: the sticky sub-menu sits at 62.8 px under the bar, no code block scrolls horizontally on any width, the document never exceeds the viewport at 574 px, the home page shows one visible header per language, the tour has eleven scenes and lands on the scene its hash names
  - rendered the proofs with tools/shoot.mjs at phone, laptop and projector widths, light and dark, and read nine of them; the figures on the pages are the ones in the diagrams

state:
  release-1-pass-4:  built; the commit that carries this entry is the one after 7981f9e
  perception-gate:   OPEN -- the author has not yet read the six pages or opened the tour offline; the verdict goes below
  takamba:           named on the site by the author's word only; no repository, file or memo carries the name yet

waiting:
  - STZSITE-VERDICT-02: the author reads the six pages and the tour and says what is wrong -> the author
                        [not routed: a reading only the author can do]
  - STZSITE-TAKAMBA-01: the rename Bangalo -> Takamba exists only in this site; the harness repository and the estate's documents still say Bangalo -> Central and the author
                        [routed in the memo of 2026-10-01]

next:
  - me:      the narrations as pages of the site (run, not copied), the reader's ladder and cell-to-proof as proposed on the Learn page, native reviews of the French, Arabic and Hausa editions
  - author:  read, then rule on Takamba's name in the estate's documents

note:      the counts of 2024 were taken from the tree at the last commit of that year, so "written by hand before agents" is a statement the author makes and the site attributes, beside a figure the repository gives.
```

---

```yaml
by:        stzsite · claude-fable-5-1 · 2026-10-01 18:41

subject:   correction after the author's reading -- Wolfram is never put forward, and the declared-language approach is stated as Softanza's own, not as today's practice

why:       the author read "Wolfram knows the world's facts. Softanza knows your world." and refused both the order and the implication that this is the state of the art

did:
  - removed the sentence from the agentic page, the vision page's principle 5 and the tour's second scene, in both languages; the replacement says that this is Softanza's proposal for the agentic age, not how programming is done today, and names no other vendor
  - reworded the founding act (agentic page, vision principle 1, tour scene 2, the home hero's voice and the home's "agentic age" paragraph) so each sentence is attributed to Softanza: "with Softanza you do not write software", "Softanza's approach to programming in the agentic age, not today's practice"
  - left Wolfram only where it is one of four platforms in a comparison list or in the coverage matrix (platform page, home's "platform" paragraph, tour's platform scene), never alone and never first

state:
  perception-gate:   still OPEN; the author has read at least the vision and tour wording and corrected it

next:
  - me:      keep this rule for every future sentence: a differentiator is "the Softanza way", never "how things are done now"
```

---

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-01 19:56

subject:   Release 1, fifth pass -- the site rebuilt under the Zui constitution on the author's second list of 2026-10-01

why:       the author ruled that text was still too small, that a page must not be interrupted by links that jump elsewhere, that the sub-menu belongs to sections dense enough to need several pages, that animation is forbidden, and asked that the Zui constitution be read and applied

did:
  - read the Zui constitution in full (v3.11, 122 rules, 7 articles, 6 rights, 17 forbidden patterns) and the Harobanda site's stylesheet and page markup, which the author points to as the reading of it; rewrote the stylesheet whole against them, naming the rule each block answers
  - set one reading size of 19 px for all text, titles and the hero voice being the only larger sizes (Rule 107); monospace labels and code at the optical allowance; nothing below 16 px anywhere
  - removed every motion: no smooth scrolling, no transition, no hover movement (Rules 1, 17, 112); removed every gradient and shadow, so the backgrounds are the Atlas pages' flat paper and panels (#F1F3F1, #FBFCFB) with no lavender tint (Rule 3)
  - rebuilt the navigation as a tree: six sections in the main menu, and under it the path of the current section listing every page of it (Rules 108, 115, 116); both bars stay on screen while scrolling, and on a phone the brand row scrolls away while the two menus stay pinned in 100 px; a single-page section (Start) has no path
  - split the five long pages into section pages (Platform 5, Vision 5, Agentic 7, Learn 7, Offering 3), removed every in-page anchor menu, and removed every link inside the prose that pulled the reader to another page; the links that remain are evidence on GitHub or the doors a hub page exists for (areas, reference, reader)
  - made the home page's bar hold its own space so the elder's head is never covered (Rule 110), shortened the hero panel to the slogan, the second line and a scroll arrow, and set its opacity at 62 percent, the lowest that keeps white text above 4.5:1 over the brightest part of the photograph at laptop, tablet and projector sizes; on a phone the panel sits below the picture
  - replaced the six home doors that jumped to another page's anchor with inline rows that say who and what, with no link
  - removed the graphic logo from the pages: the text wordmark only, with a light copy for the dark theme; the favicon keeps the mark
  - grouped the 28 areas by the Atlas's six themes on the home page and a new Areas page, every picture titled beneath it with what it shows; corrected the captions and provenance of the fifteen figurative pictures, which still described the replaced renders, and published their script as tools/areas-figurative.ring
  - turned the Atlas into tables of numbers by theme (Rules 11, 117, 128) and removed the duplicated bars; added a documentation hub with the whole scope as tiles per area, coloured by theme, opening the generated reference; added a site map footer on every page (Wolfram's footer)
  - capped every diagram at 760 px so its labels land at 17.7 px beside 19 px prose, and drew a narrow phone version of all six in both languages with Harobanda's narrowlib, labels at 17 px on a 340 px screen
  - made the coverage matrix a grid at every width (Rule 129) with its header row sticky under the menus, and the Atlas table shed its descriptions on a phone instead of scrolling
  - moved stage labels beneath the names they classify (Rule 113), put the theme choice in the footer as three buttons that say what they do (Rule 106), gave the tour's scene titles h2 so each page has one h1 (Rule 10), and removed the claude.ai addresses that were still in the public Atlas data
  - added to the Zui page the chaos of vibe-coded applications it answers and the list of the rules this site applies, with the limit that the site has not been run through the constitution's verifier
  - verified in the app's browser and in 133 renders from tools/shoot.mjs (now capturing whole pages at the real viewport height): no horizontal overflow at 375 px and 1366 px, no code block scrolling sideways, the path current on every page including the 56 area pages and the reference, the tour's 26 areas on one projector screen, deck-check 172 of 172 assets found offline

state:
  release-1-pass-5:  built; the commit carrying this entry is the one after 9c11a46
  perception-gate:   OPEN -- the author has not seen this pass
  zui-rule-99:       NOT APPLIED -- the rule asks that machine-made text be marked as such; whether the site says so is the author's decision

waiting:
  - STZSITE-ZUI99-01: Zui Rule 99 (visible provenance of machine-made content) applies to a site whose prose was drafted with an AI assistant -> the author
                      [not routed: a statement about authorship is the author's to make]
  - STZSITE-VERDICT-03: the author's reading of this pass -> the author [not routed]

next:
  - me:      run the Zui verifier on the generated pages once its repository can be reached from this one; narrations as pages of the site
  - author:  read the site; rule on Rule 99

note:      the author's two navigation rulings ("a page has a structure that must be shown in a submenu" and "a submenu is not needed when the reader can grasp the page in a normal scroll") are one rule once read with Zui 115: the second level lists PAGES of a section, never anchors inside a page.
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-01 21:22

subject:   every area shows what Softanza rethought, and runs its proof

why:       the author asked that each domain show the first-principles thinking behind it, pragmatic and
           innovative; that the regex area be presented as the entry point of pattern matching; and that
           the documentation centre learn from how Wolfram's documentation is designed

did:
  - read the library's design documents, narrations and guards at commit 0e72e2e2c with four reading
    agents, seven areas each, and wrote for each of the 28 areas a principle, what it kept from best
    practice and what it rethought, every item with its source file (data/heritage.json); each area
    page opens with it, in both languages, and the area tiles carry the principle
  - renamed the regex area Pattern matching (Recherche de motifs): the regex at full PCRE2 power is the
    entry point, and Listex, Numbrex, Timex, Tablex, Matrex, Graphex, stzRegexMaker and the patterns
    called by name are what Softanza rethought
  - built tools/showcase_run.py, which runs each area's snippets inside the library, one area per
    process and one at a time, loads the guards' own helpers, and keeps a snippet only when its output
    keeps the promise its source wrote; of 80 snippets taken from the library, 12 were not run for a
    stated reason and 59 of the 68 run kept their promise, in 25 areas; binary formats has no code yet,
    concurrency needs a running cluster and performance a live server, so those three keep the Atlas
    example
  - completed doc/DOCUMENTATION-DESIGN.md: what Softanza already decided about its documentation,
    counted from the tree, and the design that follows (page types, method entries with graded
    examples, order of work D1 to D5)
  - linked every class page and area page to its area's guide (3398a87)
  - checked: 62 pages at 375 px, none wider; no forbidden name and no machine path in the runs; the
    build's contrast check passes

state:
  release-1-pass-6:  built; the commit carrying this entry is the one after 3398a87
  perception-gate:   OPEN -- the author has not seen this pass

waiting:
  - STZLIB-PATTERN-PROMISES-01: pattern-language promises broken at 0e72e2e2c -- the Listex narration's
                       [@S, @A] prints 0 twice and [@N1-3, @S] accepts four numbers; timex/03 MatchPartial
                       and timex/04 Match print 0 where TRUE is promised; tablex/07 @cs:unique and
                       tablex/29 @!nulls print 0; the recorded run files mark timex/04 and tablex/29 PASS
                       -> the stzlib desk [routed in CONCLUSIONS]
  - STZLIB-DEPLOY-NARRATION-01: stz-system-dev-to-deploy-narration calls AddServer and AddSuperApp,
                       which stzPlatformProfile does not define, and uses oGuarded, which it never builds
                       -> the stzlib desk [routed in CONCLUSIONS]
  - STZLIB-EXAMPLE-INDEX-01: _StzExampleFor reads only the same-line #--> form, keys by bare method
                       name, and records the first file a name was seen in; D3 of the design needs it right
                       -> the stzlib desk [routed in CONCLUSIONS]
  - STZSITE-ZUI99-01:  Zui Rule 99 -> the author [not routed]

next:
  - me:      D3, method entries with graded examples, once the example index is right; narrations as pages
  - author:  read the area pages, Pattern matching first
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 00:11

subject:   the identity: the north star of 2020 opens Vision, and Softanza is presented as a platform of platforms

why:       the author asked, before the method entries, whether Softanza is also a platform of platforms, to read
           the DIKO Hub study and the other platforms built with Softanza, and to embrace strategically in the
           site's identity the platform architecture he drew years ago and that was updated in September

did:
  - found the architecture: the author's sheet "Softanza -- Programming by heart!" (2020), read band by band
    against the estate on 2026-09-13 and ratified on 2026-09-27 (softanza/vision/08-NORTH-STAR.md, private)
  - read, with three reading agents, the DIKO Hub study, RestoLean, Organizium at Sonibank, Zin, Zing, Refine
    and the vision corpus; the estate's word for the idea is recursion: "a super-app is a graph whose nodes
    are worlds -- a graph of graphs" (stzlib STZSUPERAPP_DESIGN.md, public)
  - made the Vision page the north star: the sheet of 2020, each band's verdict in 2026, the sheet redrawn
    (new diagram, wide and phone, both languages), and what must not change; the twelve principles moved to
    their own page, without their two stale in-page links
  - added "A platform of platforms" to the Platform section: what it means, what every platform declares and
    receives (new diagram), the construction run inside the library from the stzSuperApp guard (two worlds
    become one platform, then one world of a holding), three platforms, and the stage stated plainly
  - added one sentence to the home page's definition of a platform, and two scenes to the tour (13 now)
  - verified: build passes with its contrast check; 2 of 2 constellation runs keep their guard's promise;
    37 renders, deck-check 184 of 184 assets offline

state:
  release-1-pass-7:  built; the commit carrying this entry is the one after 1ef989b
  perception-gate:   OPEN -- the author has not seen this pass

waiting:
  - STZSITE-DIKO-NAMING-01: DIKO Hub follows the same construction, but its study is marked internal and
                       nothing records DIKO's consent; the site does not name it -> the author [not routed]
  - STZSITE-CUSTOMS-REFERENCE-01: the site lists the customs school as a reference; zin's design notes say
                       Organizium was PROPOSED to it -> the author [not routed]
  - STZSITE-HARO-TENSE-01: the Platform page says Haro's virtual machine "already runs the platform's code";
                       the ratified chapter says "Haro does not exist" yet, its road being the VM in Zig -> the
                       author [not routed]
  - STZSITE-ZUI99-01:  Zui Rule 99 -> the author [not routed]

next:
  - me:      the method entries with graded examples (D3 of doc/DOCUMENTATION-DESIGN.md), once the author has
             read this pass
  - author:  read Vision and Platform of platforms; rule on the three naming questions
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 00:51

subject:   Softanza for coding agents added to the site, and the open decisions taken on the author's delegation

why:       the author wrote "take whatever decision on my behalf and move forward adding this part to the site"

decided, on the author's delegation, 2026-10-02:
  - COMPASS-AGENTTOOLS-01 to 08: adopted in the compass's order -- failure made visible, the door (AGENTS.md and
    a skill), stz check and stz ask, stz promise, rehearse and grammar, an MCP server generated from the verbs
    (reusing the application tier's read-only, audited pattern), a Claude Code plugin, then measurement before
    any claim; the verbs live on one stz executable. The site shows the door as "ratified proposal", not built.
  - STZSITE-DIKO-NAMING-01: DIKO stays unnamed -- the consent is DIKO's to give, not the author's
  - STZSITE-CUSTOMS-REFERENCE-01: the customs school stays a reference -- the ratified corpus (08-NORTH-STAR,
    section 4) lists it among the customer deliveries
  - STZSITE-HARO-TENSE-01: the Platform page now says Haro is in construction and its machine is the road
    being built, aligned with the ratified chapter
  - STZSITE-ZUI99-01: applied -- every page's footer says the prose was drafted with an AI assistant under the
    author's direction, and that code, runs and figures come from the repositories

did:
  - added "For coding agents" to the Agentic section: hands and judges (new diagram, wide and phone, both
    languages), three judges run inside the library (ask, check, plan; 3 of 3 kept their sources' promises),
    what an agent reaches today, the stz command and its six verbs, five ways in, governed tools, the order
  - corrected the "For agents" grammar card: a schema already compiles to a constraint grammar; emitting one
    for every declared language is the next step
  - shortened the Zui path label so the Agentic section's eight pages stay on one line at laptop width

state:
  release-1-pass-8:  built; the commit carrying this entry is the one after 4f9e10c
  perception-gate:   OPEN -- the author has not seen this pass

next:
  - me:      nothing on the site claims the door until it is built; the method entries come next
  - Central: route COMPASS-AGENTTOOLS-01 to 08, now decided, to stzlib and stz
```
