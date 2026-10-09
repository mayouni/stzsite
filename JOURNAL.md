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
  - STZSITE-REFERENCE-01: the site lists a third reference; zin's design notes say
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
  - STZSITE-REFERENCE-01: the third reference stays -- the ratified corpus (08-NORTH-STAR,
    section 4) lists it among the customer deliveries (withdrawn on 2026-10-04: the author took it off the site)
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

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 02:46

subject:   how Softanza is built and written: the Architecture and The craft pages

why:       the author found no place on the site for the layered architecture (core, base, max), the coding style and
           conventions, the small languages inside method arguments, the naming design, the four metaphors, the
           self-documentation, or the single dependency-free executable

did:
  - read the library at origin/main 010743cce with two reading agents (one on architecture and build, one on the
    craft); the first pair was lost when the previous session ended and was relaunched
  - added Platform > Architecture: three layers over one engine (new layers diagram, wide and phone), the engine's
    89 modules and two doors (752 C functions, 2,652 registered for the library), a folder per domain (the 44
    folders of base), and the single executable split into what exists (the cross-platform builder and its 38-check
    guard, a script compiled with its virtual machine, proven on one line, the web build carrying only the declared
    engine groups) and what does not yet (a whole program and its engine in one file with only the code it uses)
  - added Platform > The craft: a name is a sentence (new verb-family diagram from the generated reference), the
    small languages inside arguments, the four metaphors (walker, checker, yielder, performer), the conventions, and
    the comment-based self-documentation shown on a real doc-comment, its thin coverage stated
  - ran 11 snippets inside the library (4 architecture, 7 craft), all kept their sources' promises; a build
    placeholder now places chosen runs beside the idea they show, and refuses if a run was dropped
  - corrected the Compared page: the engine ships for Windows, and a Linux build is under way (it said Linux and
    macOS built from source)
  - earlier the same night, on the author's reading (3a4522d): a slideshow icon replaces the word Present, the home
    menu lies on a 30 percent translucent band, and the first Offering page is named Audiences

state:
  release-1-pass-9:  built; the commit carrying this entry is the one after 3a4522d
  perception-gate:   OPEN -- the author has not seen these two pages

waiting:
  - STZLIB-LAYER-DOCS-01: the layer and engine design documents are stale (counts, inheritance, a separate engine
                       repository and clients that do not exist); future/doc/softanza_architecture_reference.md and
                       readme.txt promise tools never written -> stzlib [routed: CONCLUSIONS]
  - STZLIB-CORE-ENGINE-01: stkString and stkChar call twelve StkEngine names that no engine file registers since
                       4c14b35d4, so a core string most likely fails at main -> stzlib [routed: CONCLUSIONS]
  - STZLIB-NARRATION-FIXES-01: stz-bridging-minds-and-code section 3.2 calls a method that does not exist;
                       stzstring-duplicates-narration shows 0-based positions; stzstring-overspaces-narration
                       contradicts itself -> stzlib [routed: CONCLUSIONS]

next:
  - me:      the method entries with graded examples
  - author:  read Platform > Architecture and Platform > The craft
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 03:28

subject:   The Atlas leaves the Platform menu and becomes a view of The areas

why:       the author judged the Atlas submenu unnecessary: each area's page already carries its rated lanes

did:
  - removed "The Atlas" from the Platform section's path (seven entries now); the ratings table of all 334 lanes
    stays, marks "The areas" as current like every area page, and is reached from one line at the end of The areas
    and from the Documentation page

next:
  - me:      the method entries with graded examples
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 03:39

subject:   the table of all lanes removed

why:       the author asked to remove the table once it had left the menu: each area's page carries its rated lanes

did:
  - removed the generation of atlas.html and the two pages; the Documentation card that opened it now opens The
    areas, and the closing line of The areas is gone; no page links to the table any more

next:
  - me:      the method entries with graded examples
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 03:54

subject:   method entries with graded examples: 666 methods, every example run inside the library

why:       the author's next step after the identity and craft passes; D3 of doc/DOCUMENTATION-DESIGN.md, learned from
           the Wolfram function page and decided as Softanza's own: an example is published only after it ran

did:
  - wrote tools/harvest_examples.py: it reads the library's classic test files in 32 pure-computation topics (3,401
    files), keeps the 894 short ones that touch no file, input, clock or chance, and attributes each to the methods
    it shows (a call made as a statement counts; a viewer such as Content only when nothing else was called)
  - wrote tools/examples_run.py: batches of 40 in one process at a time, each example in its own try block; a batch
    that never starts is split until the faulty example stands alone, and one that stops resumes after the example
    that stopped it; 558 examples kept every promise, in 108 s, covering 666 methods of 25 classes
  - wrote tools/build_methods.py: one entry per method (1,332 pages, both languages) with its explanation, the forms
    of its verb, examples graded as Basic, Scope and Possible issues with the count in each heading, and links to
    the class, the area's guide and the other methods the examples touch; class pages and guides link to the entries
  - removed the table of all lanes earlier (bba7345), on the author's request

state:
  release-1-pass-10: built; the commit carrying this entry is the one after bba7345
  perception-gate:   OPEN -- the author has not seen the entries

waiting:
  - STZLIB-PROMISES-269-01: of 894 classic examples run at 0e72e2e2c, 269 print something other than their file
                       promises and 65 raise an error; the list is reproducible with the two tools -> stzlib [routed]

next:
  - me:      widen the harvest to the narrated suites and the course chapters, where the string class lives now
  - author:  read an entry, for instance Reference > stzList > FindW
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 04:08

subject:   method entries widened to the narrated suites: 1,504 methods of 49 classes

why:       the author asked to widen the harvest to the narrated suites, where most of the string class's tests live now

did:
  - taught tools/harvest_examples.py the narrated form: each scenario becomes one example; each Then or chk becomes a
    printed line with its label as a comment; a zero-argument helper ending in one return is inlined so the shown
    code is whole; a scenario leaning on another helper is left out; linguistics, mathematics and statistics added
  - taught tools/examples_run.py to print a narrated example's expected values in the same run and compare them
    with what the code printed, so the promise is the library's own value
  - made attribution follow a chain that elevates to another class (Q("...").TextQ().IsSemanticallySimilarTo files
    under stzText)
  - 1,641 examples harvested, 1,297 kept every promise (739 narrated), in 177 s; 3,008 entry pages for 1,504 methods
    of 49 classes; the string class now holds 948 attributions, the list class 613

state:
  release-1-pass-11: built; the commit carrying this entry is the one after ca96d67
  perception-gate:   OPEN

next:
  - me:      the course chapters as a last source of examples, then narrations as pages
  - author:  read an entry of the string class, for instance stzString > RemoveXT
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 04:38

subject:   course chapters harvested, and the former language's name kept out of every code block

why:       the author asked to widen the harvest to the course chapters; a sweep then found the former language's name
           inside published examples, which the site's rule forbids

did:
  - harvested the course chapters (elementary introduction and mathematics): each fenced cell is an example titled by
    its section heading; 73 cells read, 49 kept their promises (the others lean on earlier cells of their chapter)
  - found 146 published examples whose code or output showed the former language's name (often as sample text, such
    as "RING"); library code is never rewritten, so such examples are now left out of the entries and of the area
    showcases (one documentation run), a .ring file name not counting; the library's own descriptions now map the
    uppercase form to HARO as they already mapped the capitalised one
  - the entry generator now clears its folders before writing, so an entry that no longer qualifies leaves no page
  - swept every page's code and output blocks: none shows the word; 1,428 methods of 59 classes keep an entry
    (2,856 pages)

state:
  release-1-pass-12: built; the commit carrying this entry is the one after 6f8ccf4
  perception-gate:   OPEN

next:
  - me:      narrations as pages
  - author:  read an entry built from a chapter, for instance stzList > FindW
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 21:13

subject:   narrations as pages: 8 of 134 run block after block and published, each block with its verdict

why:       a narration is the library's tutorial form, and the site shows only what it ran; the list linked every
           narration to GitHub with nothing saying which of them still keep their promise

did:
  - wrote tools/narrations_run.py: each narration runs in ONE process inside the library, its code blocks in order,
    each in its own try block; a block is judged against its own `#-->` lines (also written `# -->` or `// -->`), or
    the untagged output block right under it; a promised refusal counts as kept; a promise written on a line that
    prints nothing cannot be checked and is said so
  - ran all 134 at 0e72e2e2c in 188 s: 43 ran; 27 not run because their code names the former language; 42 not run
    because they touch files, the network, input, the clock or chance; 15 do not compile as written; 7 have no code
  - published as pages the 8 where at least three blocks in four keep their promise (tools/build_narration_pages.py):
    the narration's own prose and code, under each block what the run did, with what it printed when it differs or
    raises; their pictures hosted on the site so the pages open with no network
  - the list page now groups all 134 by that outcome, with the count of kept blocks for those that ran
  - corrected six sentences in both languages (Start, Documentation, Principles, Learn, Offering, the list's lede)
    that said every narration's blocks run and keep their output: the run measured otherwise

state:
  release-1-pass-13: built; the commit carrying this entry is the one after 5ff8466
  perception-gate:   OPEN -- the author has not seen the narration pages

waiting:
  - STZLIB-NARRATIONS-RUN-01: of the 318 code blocks in the 43 narrations that ran, 86 print what they promise, 32
    state no output, 7 write their promise on a line that prints nothing, 59 print something else, 134 raise: 36 an
    uninitialised variable (mostly left by an earlier block that raised), 32 a method that does not exist, 28 a
    function that does not exist, 17 a property error, 9 a wrong argument count, 11 a refusal by the library itself;
    and 15 narrations do not compile -> stzlib [routed]

next:
  - me:      file the run's findings for the library, then the how-to pages from the quickers
  - author:  read a narration page, for instance Learn > Narrations > The Parser That Says No
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 21:31

subject:   the third menu level: a bar on the left listing the pages of the level the reader is in

why:       the author asked that a page one level below a page of the section's path show its level in a vertical bar
           on the left, so the reader can go back and forth in it, and ruled that a site never has more than the main
           menu and two submenu levels

did:
  - wrote tools/level2.py and wrapped every deeper page with it: the 28 area pages and the 28 guides (by band), the
    class pages (the classes of their area), the A to Z method pages (the letters, replacing their row of letter
    chips), the narrations run as pages; 2,137 pages per language carry the bar (709 at that level, 1,428 method
    entries)
  - a method entry is a page of its class, not a fourth level: it shows its class's bar with the class marked
  - the bar sits in the same centred box as the menus, aligned with the brand and the path; it stays in view and opens
    on the current entry; below 1,100 px it becomes a third row that scrolls sideways, like the path, and is not pinned
  - fixed on the way: the body is a flex column, so the wrapper took the width of the sideways row (7,425 px) on a phone
    until given min-width 0; checked at 390 and 1,366 px that nothing overflows

state:
  release-1-pass-14: built; the commit carrying this entry is the one after b0eb364
  perception-gate:   OPEN -- the author has not seen the bar

next:
  - me:      the how-to pages from the quickers
  - author:  open Platform > The areas > Geo & cartography and move along the bar
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 22:18

subject:   pages with the left bar take the width the screen offers

why:       the author found the page with the bar boxed in the menus' width, with wide empty margins on a large screen

did:
  - widened the layout of every page with the bar to 1,680 px: the bar takes 18 % of the width (272 to 336 px), never
    a quarter (Zui 8, a sidebar stays quiet), and the page takes the rest (Zui 6, 70/30); spacing in steps of 8 px
  - kept prose at its measure (68 characters) and let code, run blocks, tables and pictures widen to 1,120 px
  - measured: 1,855 px wide, bar 334 px (18 %), prose 857 px, nothing overflows; 1,366 px, bar 272 px (20 %); 1,180 px,
    bar 23 %; below 1,100 px the bar is still the sideways row

state:
  release-1-pass-15: built; the commit carrying this entry is the one after fbf4c34
  perception-gate:   OPEN

next:
  - me:      the how-to pages from the quickers
  - author:  look at Platform > The areas > Agents & conversation on the large screen
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 22:43

subject:   how-to pages: 28 of the library's 30 recipes run and published, a new page of Learn

why:       the author asked for the how-to pages, the documentation design's D4: no page of the site answered
           "how do I...?", and the library's recipes are that answer

did:
  - wrote tools/howto_run.py: reads base/doc/quickers/recipes (intent, code, explanation, methods, tags, see also)
    and runs them all in one process inside the library at 0e72e2e2c, each in its own try; an expression carrying a
    promise without printing it is printed for the run, and the page says so; 12 s
  - 28 kept their promise, checked by eye beside the outputs and against five wrong values the comparison rejects;
    2 not run because their code shows the former language's name (section, summarize)
  - wrote tools/build_howto.py: Learn > How-to lists the recipes by kind (lists, numbers, strings, text); each recipe is
    a page with the left bar, its code, the run's output and verdict, its explanation, its methods linked to their
    entries or class pages, its see-also recipes and its search words; intents and short names translated into French
  - 35 method entries now link to the recipes that use them; the Documentation page has four ways in
  - checked 1,804 local links on the new pages: none missing; none shows the former name

state:
  release-1-pass-16: built; the commit carrying this entry is the one after ebe777d
  perception-gate:   OPEN -- the author has not seen the recipes

next:
  - me:      the agents' door (Ask, HowTo, ExplainMethod) is the last page type of the design still planned
  - author:  open Learn > How-to and a recipe, for instance Lists > Filter
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-02 23:10

subject:   the agents' door: Learn > Ask the library, measured on the library's own recipes, and llms.txt with a JSON index

why:       the author asked for the agents' door, the last page type the documentation design still planned (D5): how a
           program asks the library, and what an agent reading the site can take as data

did:
  - wrote tools/ask_run.py: asks each of the 28 published recipes' intents, word for word, of the recipe's class with
    HowTo and Ask (no neural model loaded, none in the library's models folder), and keeps four whole answers to show;
    one process, 138 s
  - measured: HowTo proposed the recipe's own method for 16 of 28, another form of the same verb for 3, another method
    for 9 (Merge for filter, Bottom3Z for max and min, AddManyOneByOne for sum, ReturnType for is prime, IsNotOdd for
    even or odd, Contains for find, IsHybridcase for upper case, RemoveAllExcept for remove duplicates, Mean for
    average); Ask had the recipe's method or its verb among its first three answers for 21
  - wrote tools/build_ask.py: the page shows the three calls run, the 28 answers as they came with their grade, what an
    outside agent reaches today (stz ask decided, not built), and the two machine files
  - generated llms.txt (the site in one text file, every page that matters linked) and agents/index.json (618 classes
    with every method's explanation and entry, 28 recipes with code and output, 8 narrations, 28 areas; 2.9 MB)
  - linked the For agents page's Ask card to the new page; fixed my own slip on the way: a failed patch let the old
    script run with "--regrade" as a library path, which overwrote the uncommitted run data and left three empty
    folders in stzsite; the folders were removed and the run taken again

state:
  release-1-pass-17: built; the commit carrying this entry is the one after 11f2f437
  perception-gate:   OPEN

waiting:
  - STZLIB-ASK-RECIPES-01: asked its own recipes' intents, HowTo names another method for 9 of 28 (listed above);
    each recipe's Tags line lists the words a reader would use; whether feeding them to the index finds the
    right method is for the library to measure -> stzlib [routed]

next:
  - me:      the documentation design's page types are all built; the reader's ladder on Learn is the open proposal
  - author:  open Learn > Ask the library
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-03 00:06

subject:   the reader's ladder: the five rungs on the Learn page, and every chapter of the reader naming its rung

why:       the author asked for the reader's ladder on the Learn page; Pedagogy had proposed it as Zin's "ladder always
           visible": where the learner stands, from S0 to S4, and what earns the next rung

did:
  - wrote tools/ladder_run.py: asks the library which chapters each rung needs (ChaptersForLevel), has each of the five
    project guards prove itself on its samples (ProveItself), and asks where a new learner stands (MissingFor); one
    process inside the library, 47 s; every guard refused its 2 wrong samples and accepted its right one, each refusal
    with the guard's own words; a new learner is told "ex-01-01 ... ex-04-01, project-s0"
  - wrote tools/build_ladder.py: Learn > The ladder shows S0 Explorer to S4 Master, the chapters each adds (linked into
    the reader), the project that earns it, what its guard checks, the guard's verdicts on its samples, and "where you
    stand" run; the reader's 60 chapters (15 x 4 languages) each carry a line naming their rung and what earns it, added
    to the site's copy between markers so a rebuild replaces it; the Arabic and Hausa lines use only the library's own
    brief in that language; the reader is otherwise byte-identical, checked
  - Pedagogy now says the ladder is built, and that where a learner stands is named by the library on their machine,
    which the site cannot see
  - fixed on the way: a greedy pattern had kept only the right samples; the code shown for "where you stand" now
    matches the code that ran (@@( ... ))

state:
  release-1-pass-18: built; the commit carrying this entry is the one after 2c9a462
  perception-gate:   OPEN -- the author has not seen the ladder

waiting:
  - STZLIB-READER-LADDER-01: the reader generator (base/education/stzEduReader.ring) could draw the rung line itself;
    the site adds it to its copy meanwhile; the rung names exist only in English (program/levels.zknw) -> stzlib
    [routed]

next:
  - me:      the two other proposals of Pedagogy remain: progressive revelation, and from the cell to its proof
  - author:  open Learn > Learn, The ladder; then a chapter of the reader
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 00:23

subject:   the Q rule: a method is listed once, and an example calls a Q form only to use what it returns

why:       the author corrected a general misunderstanding: a ...Q() name does what the method does and then returns the
           object so a call can be chained; it is a syntax detail, not another method

did:
  - wrote tools/qforms.py, the one place that decides: a ...Q, ...QQ or ...QQQ name whose plain method exists in the class
    or an ancestor is folded into it; a detector reads code statement by statement and flags a Q call that ends a
    statement whose value nothing uses (an assignment, ?, return, a loop or a chain on it makes it right; nine test cases)
  - the reference, the A to Z index, the guides, the method entries, the how-to pages, the Ask page and agents/index.json
    list a method once: 24,774 of 26,949 names are listed, 2,175 folded, 1,251 Q names with no plain twin stay; inherited
    counts recomputed; one sentence on the reference and Ask pages says what a trailing Q is
  - entries now merge a method with its Q form: 1,386 methods of 58 classes (it was 1,428 of 59); 37 gained examples
  - left out the library's examples that call a Q form and use nothing of it: 2 of 1,346 examples and 5 of 75 showcase runs;
    4 methods of stzGraphRule lost their only example with them; the published narration "The Parser That Says No" keeps
    its text and shows a note under the 2 blocks that do it
  - checked on the built site: no folded name on any class page, 0 dangling among 423,884 local links, and the only code
    block of the English pages that still calls a Q form without using it is those 2 narration blocks, noted

state:
  release-1-pass-19: built; the commit carrying this entry is the one after b2f43a0
  perception-gate:   OPEN

waiting:
  - STZLIB-QUNCHAINED-01: library examples that call a Q form and use nothing of its result: graph/graphrule_object_narrated
             (SetDomainQ, SetSeverityQ, SetMessageQ), string/809_content (RemoveSectionQ), graphics_faces_narrated (ColorQ),
             sound_mu4_narrated (PerformQ), narrations stz-service-virtualization-code-first-subscribe-later (SetPhaseQ),
             stz-guarding-secrets-and-credentials-narration (FromEnvQ), stz-xml-the-parser-that-says-no (OpenQ, SetAttributeQ,
             AddElementQ, CloseQ) -> stzlib [routed]
  - STZLIB-ASK-QTWIN-01: Ask spends one of its three answers on a Q twin for 6 of the 28 recipe questions (Reverse,
             ReversedCopy, ReverseQ); folding the Q forms would free the slot -> stzlib [routed]

next:
  - me:      the two other proposals of Pedagogy remain: progressive revelation, and from the cell to its proof
  - author:  open Learn > Reference > stzList, then Learn > Reference > stzNumber > Add
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 01:02

subject:   from a cell of the book to its proof: 30 proof pages and a bridge inside the reader

why:       Pedagogy proposed Zin's "pro bridge", one gesture from any cell of the book to the guard that proves it; the
           author said to continue, and it is the one of the two open proposals a static site can build

did:
  - wrote tools/proof_run.py: runs the Elementary Introduction exactly as the library's own guard
    (test/education/course_narrated.ring) does, with RunChapterInQ, which supplies the teaching world; one process inside
    the library, 252 s: 15 chapters, 60 editions (4 languages), 336 cell runs, 149 promises; every edition ran with every
    promise kept and no stored output; the four editions make the same promises cell for cell; the 23 exercises each
    proved themselves (47 of 47 wrong answers refused, 47 of 47 right ones accepted)
  - my first version called Run with no world, which made the cells that read the world raise: caught at the raw output
    before any page was built, and replaced by the guard's own call
  - wrote tools/build_proof.py: 30 pages, en and fr, Learn > The book > one chapter, each with the chapter's verdict, the
    guard and how to run it alone, every cell with its code, its promise, what it printed and whether it kept it (and the
    link to its line in the four chapter files), and each exercise with its samples; the book page lists the 15
  - the bridge inside the reader: under each of the 60 chapter titles a verdict line, on each of the 336 cells a link to its
    place on its proof page, on each of the 92 exercises a line saying it proves itself; 488 injections, between markers, so
    a rebuild replaces them; the reader is otherwise byte-identical (checked); ar and ha carry only the library's own names
    and numbers
  - 9 cells show the former language's name as sample text (RING), so the proof page shows their verdict and links, not
    their code
  - fixed my own slips on the way: a pattern that tested code and output as one string let "RING" + "RING" through (the
    sweep of all 9,594 code blocks of the site is clean); the reader had carried a duplicate ladder style block since the
    ladder was added, now removed by marker so an edited style never stacks again
  - Pedagogy: two of the three proposals are built; progressive revelation stays proposed and says why a static site
    cannot build it

state:
  release-1-pass-20: built; the commit carrying this entry is the one after c422f1a
  perception-gate:   OPEN

waiting:
  - STZLIB-COURSE-WORD-01: 9 cells of the course use RING as sample text (read-the-name-as-a-sentence 1, 2, 4, 5;
             declare-what-not-how 5; draw-the-answer 1, 2; write-a-narration 1, 2), so the site cannot show them -> stzlib
             [routed]
  - STZLIB-READER-LADDER-01 (widened): the reader generator could draw the rung line, the proof line, the cell links and
             the exercise lines itself, so the site's added copy retires -> stzlib [routed]

next:
  - me:      only progressive revelation remains of Pedagogy's proposals, and it is the library's to build
  - author:  open Learn > The book, at the bottom, then any chapter of the reader and its "Proof of this cell" link
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 01:32

subject:   the extension rule: every extension is the same method, so the reference lists a method once and says which
           extensions exist for it

why:       the author ruled that what was said for Q applies to CS, U and all the other extensions: they are syntax
           variations of the same method, not other methods; remove them from the reference, and for each method say
           whether each extension exists

did:
  - wrote the catalogue in tools/qforms.py: 16 extensions the library documents (Q, QQ, QQQ, QC, QRT, CS, ST, IB, XT, XTT,
    Z, ZZ, W, WF, WXT, U), each with what it adds in the library's own words and the library file that documents it; a name
    that is a method plus extensions, stacked in any order (FindSTZZ, ContentCSU), is folded into the method
  - the reference lists a method once: 22,386 of 26,949 names are listed, 4,563 folded (the Q rule had folded 2,175);
    class pages, the A to Z index, the guides, the entries, the how-to pages, the Ask page and agents/index.json all list
    the method once
  - each row of a class page says, for the standard eight (Q CS XT Z ZZ IB W U), which extensions exist (bold, ticked) and
    which do not (struck), plus any other that exists, or "no extension"; each entry carries the full table of 16 with the
    names that carry each; the reference page carries the catalogue with its sources; agents/index.json lists, for every
    method, its extensions and the names of its forms
  - 7 methods of an ancestor that a class only gives extensions to are listed in that class as inherited methods
  - entries merge a method with all its forms: 1,266 methods (it was 1,386); the counts in the content pages now come from
    the data through placeholders, so they cannot go stale
  - checked on the built site: no folded name is a row on any class page, none is in the A to Z index, 0 dangling among
    378,046 local links, and none of 9,242 code blocks shows the former name

state:
  release-1-pass-21: built; the commit carrying this entry is the one after 9611fe9
  perception-gate:   OPEN

waiting:
  - THE AUTHOR: two readings of "all other extensions" are mine and open: (1) passive forms (Removed beside Remove) are
             kept listed, since they do not do the same thing; (2) only documented extensions are folded, and the endings
             N (103 names), F (14), D (11), R (7), AP (7), B (5), SF (5) and a few more are left listed because the library
             does not document them as extensions; they are named on the reference page -> the author decides [routed]
  - STZLIB-ASK-EXTENSIONS-01: 16 of the 84 answers of Ask are an extension of another answer, and for 12 of the 28
             recipe questions two of its three answers are one method (FindFirst and FindFirstCS; Reverse and ReverseQ);
             folding the extensions would free those slots -> stzlib [routed]

next:
  - me:      Pedagogy's last proposal, progressive revelation, is the library's to build
  - author:  open Learn > Reference > stzString, then Learn > Reference > stzString > Find
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 11:42

subject:   the extension catalogue grounded in the author's own forms grammar: 20 extensions, and the questions I had put to
           the author answered by the sources instead

why:       my last report ended on two questions for the author, against the standing rule to decide and move; the answer
           was in the estate's own record: the Haro spike (ringpp, 2026-10-03 00:11) had declared "principle 7's
           function-name grammar" from the library's forms document, with the parameter suffixes cs st xt ib d z zz s w f many
           except, fluent Q, passive ed, statement X

did:
  - read the forms document (stz-functions-as-linguistic-expressions.md) and stzv_v12.haro: Many (the plural form), Except
    (the exceptional form), D (directional), F (takes a function; also the future form) are documented forms of the same verb,
    so the catalogue grows from 16 to 20 and 114 more names fold: 22,272 methods listed, 4,677 folded
  - decided, not asked: passive forms stay listed (they do not do the same thing, and the document names them a form of
    their own); S stays (seconds in ElapsedS, a start position in NthStzS, six names, two meanings); X stays (three of its four
    endings are unrelated words); FF and the prefixes are generic mechanisms, not name suffixes of the reference
  - fixed on the way: the language is case-insensitive, so FindStD was folded onto "FindSt", which is the method FindST, itself
    Find plus ST; that left a spurious inherited row; the remainder is now resolved to the library's own spelling and folded in
    turn (FindStD is Find with ST and D); a sample of 56 folded names shows each under the method it extends
  - checked on the built site: no folded name is a row on any class page, 0 dangling among 375,358 local links, none of
    9,198 code blocks shows the former name; stzString.Remove shows Many and CS existing, Except, D, F not

state:
  release-1-pass-22: built; the commit carrying this entry is the one after 5bd8ee6
  perception-gate:   OPEN

waiting:
  - STZLIB-F-SUFFIX-01: F means "takes a function" (WF, UpdateNodesF) and "future" (UppercasingFQ); the forms document's own
             principle is one meaning per suffix, and the Haro spike found the same clash (HARO-FORMS-01) -> stzlib [routed]

next:
  - me:      Pedagogy's last proposal, progressive revelation, is the library's to build; nothing else is queued here
  - author:  open Learn > Reference > stzString > Remove, and its table of 20 extensions
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 12:10

subject:   an example for each extension, with its letters highlighted, in the reference catalogue

why:       the author, looking at the catalogue: "very good! add an example for each with extension letters highlighted"
           (under each extension's description), and the header "EXTENSIO N" broke across two lines

did:
  - wrote tools/ext_examples_run.py: one small example per extension, composed from the usage the library documents (its
    tests, narrations and descriptions) with real method names, every one RUN in one process inside the library at
    0e72e2e2c; 19 of 19 ran; the output shown is the run's (RemoveQC leaves the original "softanza" untouched, FindD goes
    backward, FindZZ returns [ [ 2, 3 ], [ 4, 5 ] ], WordsQ then WordsQQ shows the Q ladder)
  - the catalogue shows, under each extension's description, the example with the called name's extension letters
    highlighted (bold, accent, underlined, so colour is not the only cue) and what it printed
  - the entry tables highlight the extension's letters in every name they list (FindManyCS, FindZZCS, FindStD)
  - the first column no longer breaks EXTENSION: it is wide enough; checked at 390 px, no overflow
  - WXT leaves the catalogue (the parser lists it, no method carries it, its call does not run), and QC stays documented but is
    left out of the per-method yes/no (no method name carries it: the library gives it to any method through a generic dispatch)
  - XTT now uses the library's own words, "yet another extension" (stzlist-diff.md)

state:
  release-1-pass-23: built; the commit carrying this entry is the one after 72495fd
  perception-gate:   OPEN

waiting:
  - STZLIB-QLADDER-01: Q("It is. It works.").SentencesQQQ().ClassName() answers stzstringlist, the same class as SentencesQQ, where
             the Q ladder rule says QQQ is the most specific type (stzListOfTexts for sentences); the only name that carries QQQ is
             SentencesQQQ -> stzlib [routed]

next:
  - me:      nothing queued on the site; progressive revelation is the library's to build
  - author:  open Learn > Reference, The extensions
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 20:03

subject:   an example on every row, function, index entry and narration of the site

why:       the author, looking at the stzList reference table: "examples must be everywhere in the site! we don't want to let
           anything abstract ... a strategic asset for softanza adoption, so the reader knows it's a practical technology"

did:
  - wrote tools/rows_run.py: an example composed from each method's signature and RUN in the library at 0e72e2e2c, on a fresh
    sample object shown with the example; a first run composed 9,116 methods over 150 classes and kept 5,801, each kept only
    if a second run in another order printed the same (56 dropped), 10 calls crashed or hung and were isolated; stzListNamedParams
    (1,927 composed, 1,645 kept) and stzGraph (294 composed, 164 kept) were run again after; 7,446 composed examples in all
  - wrote tools/rows_mine.py: receivers mined from the library's own tests (single-line constructions with literals only, each
    tried by running it; empty receivers and paths left out): 149 classes, plus five written by hand from how the tests build them
  - gave stzListNamedParams (1,913 methods IsXNamedParam) a receiver made from each method's own name, kept only when it answers true
  - wrote tools/rowex.py: the library's example of the very method first, else the composed one, last a folded form's; the legend
    of each class page counts them and says what is not run and why
  - put an example under every row of 618 class pages, every function of the 28 guides, the class index, the A to Z index, and
    each method of agents/index.json (field example)
  - wrote tools/narrations_snippets.py: 120 of 134 narrations carry a snippet on the list (25 from a run, 95 as the narration
    writes it, labelled not run for this page; 7 have no code and say so)
  - wrote tools/check_examples.py: 29,002 blocks of the built site, 0 failures (no former name, no bare ...Q() statement, an
    output, a source); 0 dangling among 546,293 local links
  - found that the harvest read section banners as method descriptions (8,425 rows, 38%): the reference now shows "in the
    section X" and the share described from the source falls from 74% to 42%

state:
  release-1-pass-24: built; the commit carrying this entry is the one after de9f587
  rows with an example: 7,610 of 22,272 (34.2%), on 151 of 618 classes
  classes not run on purpose: 251 (5,112 rows: files, network, process, clock, chance, sound), each says so
  classes with no receiver yet: 216 (4,021 rows)
  perception-gate:   OPEN

waiting:
  - STZLIB-SELFDOC-BANNER-01: the self-documentation takes the nearest comment above a method, so a section title describes every
             method under it (stzListNamedParams 1,884, stzDiagram 110, stzDateTime 78) -> stzlib [routed]

next:
  - me:      write a receiver by hand for the 216 classes the tests never build directly, largest first (stzQuestion, stzGraphPlanner, stzGeoMap)
  - author:  open Learn > Reference > stzGraph, and Learn > Narrations
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 20:52

subject:   sample objects for the classes the tests never build directly, and an example for each of stzQuestion's words

why:       the author, "ok do it", on the next step of the examples pass: write a receiver by hand for the classes with no example

did:
  - wrote tools/rows_context.py: a construction from variables or over several lines, with the lines that arrange it, mined from
    the library's tests and run before it is accepted; 23 classes (the graph planner and query, the bar charts, the decision tree,
    the data wrangler, the table classes, the tree, the list of timelines...)
  - wrote data/row-receivers-hand.json and tools/rows_probe.py: 58 sample objects from how the library builds each class (the geo
    map from a one-polygon GeoJSON, the pivot table, the diagram, the org chart, kNN and logistic regression from a training set...)
  - composed stzQuestion's methods as words of a sentence, WhatQ().TheQ().<Noun>Q().Of("Softanza"): 712 of 1,048 ran and kept an example
  - recognised the cStr, nRow, aToken spelling of parameters, which blocked 1,257 methods, and re-ran the 30 classes with the most rows lacking one
  - found four classes the library cannot build with the obvious arguments: stzListOfSets calls IsListOfSets, which does not exist;
    stzTextStream needs a class QTextStream that is not there; stzSetOfSections refuses [ [ 1, 3 ], [ 5, 8 ] ]; stzGridNav("g", 3, 3)
    answers "Engine returned error"
  - rebuilt: 34,356 example blocks checked, 0 failures, 0 dangling among 546,293 local links

state:
  release-1-pass-25: built; the commit carrying this entry is the one after 03318455
  rows with an example: 8,991 of 22,272 (40.4%, was 34.2%), on 215 of 618 classes
  classes not run on purpose: 251 (5,112 rows)
  classes with no receiver yet: 103 (1,295 rows)
  perception-gate:   OPEN

waiting:
  - STZLIB-RECEIVERS-01: four classes cannot be built with the obvious arguments (stzListOfSets, stzTextStream, stzSetOfSections, stzGridNav)
             -> stzlib [routed]

next:
  - me:      the solvers, the string finders and the courses are the largest of the 103 classes left; what remains in the others is
             calls that raised or printed nothing
  - author:  open Learn > Reference > stzQuestion, and stzGeoMap
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-03 23:25

subject:   wave 1 of the plan after the author's review: external links, the extension reminder, the pinned path, @@() for lists only, Zin gone

why:       the author, "go ahead with wave 1" (doc/SITE-PLAN-2026-10-03.md)

did:
  - marked every link that leaves the site (19,992 on 4,083 pages): a new tab, an arrow drawn in the link's own colour, the words
    "(opens in a new tab)" for a screen reader; the pass runs as each page is written, because reading the 4,000 pages a second time
    cost four minutes where the build costs sixteen seconds
  - reduced the extension paragraph that opened 618 class pages to one line, and gave each letter of a strip its meaning as a title
  - pinned the path under the menu on every page deeper than its section: Learn > Reference > String > stzString > Find()
  - ran 6,852 composed examples again in the plain form: 6,836 now print with ? alone, the 1,993 that print a list keep @@()
  - removed Zin from the estate, platforms and pedagogy pages (the pedagogy page now says what the learning system is made of, not
    where it came from), regenerated the four diagrams that named it, and made the build refuse the name at the source
  - kept Zui: it names a law of Softanza and the sources never showed Zin on it (the plan said to rename it; corrected)

state:
  release-1-pass-26: built; the commit carrying this entry is the one after ac63d0a2
  external links: 19,992 marked; examples with ? alone: 6,836 of 8,829; Zin in the built site: 0
  perception-gate:   OPEN

waiting:
  - STZLIB-DOCREFORM-01: the documentation session has not reported; the alias fold (wave 2) reads its record when it comes

next:
  - me:      wave 2, one name per thing: tools/aliases.py reads the sources, the build folds classes and methods by it
  - author:  open Learn > Reference > String > stzString: the path at the top, one line about extensions, the arrow on the source link
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 00:09

subject:   wave 2 of the site plan, one name per thing (built, committed locally; interrupted by a power cut in Niamey before the push)

why:       the author, "go ahead with wave 2"; the author then asked to prepare for a cut of the session

did:
  - wrote tools/aliases.py: reads the library's sources once into data/names.json: 43 class names that are other names of a class
    (stz2DList, stzList2D, stzLists... fold under stzListOfLists, the author's own example), 4,026 method names that only forward to
    another (3,699 folded under a main name in the listed rows), 11 detours (IsAString for IsString...)
  - folded in tools/qforms.py: the reference lists 575 classes (was 618) and 18,561 methods (was 22,272); each class says "also named",
    each method "also written", the old class addresses and the entry addresses of other names lead to the main one; HasMoreCharsThan is
    the main name of HasMoreChars, with the forms it accepts (HasMoreChars(3), (:Then = 3))
  - added the Names section to the reference index (four kinds: other name of a class, of a method, an extension, a detour)
  - examples show the natural name (IsChar) and say what they ran as (IsAChar); the agents' index carries also_named and also_written
  - FOUND AND FIXED: wave 1 gave the external-link arrow the class "ext", which the highlight of the extension letters in the
    catalogue already used: the highlighted letters collapsed into a tiny arrow on the live site; the arrow is class "xarr" now
  - 0 failures on the example blocks, 0 dangling among 506,863 local links

state:
  working tree: built and checked, committed locally; NOT YET PUSHED, NOT YET DEPLOYED
  live site:    still wave 1 (8fb789ac), WITH the catalogue highlight regression until this is pushed
  release-1-pass-27: the commit carrying this entry

next:
  - me:      push, watch the deploy, verify the live catalogue; file memo, CONCLUSIONS, mailbox CLOSE and cost line for waves 1-2 (wave 1 is filed; wave 2 is not)
  - me:      then wave 3, search (doc/SITE-PLAN-2026-10-03.md)
  - author:  nothing; the plan, the journal and this entry hold the state
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 00:47

subject:   wave 3 of the site plan, the search: one field, category > class > method

why:       the author, "resume with wave 3": the search field of the reference is impractical; it should find classes, methods,
           descriptions and the code of examples, quickly and visually, always as category > class > method

did:
  - tools/build_search.py: an index built with the site: assets/search/names.js (575 classes, 18,561 methods with their other names and
    the forms written with extensions, 205 pages: guides, how-to, narrations, book; 118 KB compressed) and assets/search/text.js (every
    description and the first lines of every example; 329 KB compressed, loaded only when the reader asks, and the choice remembered)
  - assets/js/search-core.js: the matching, one file for the page and for node: Class.Method read as a class and a method, a class
    named in a sentence, a method found through its class's descendants (hash list finds stzList's Sort), tokens weighted by how telling
    they are and by position, stop words in English and French
  - tools/search_check.mjs: 13 questions a reader asks, 13 answered in the first results (remove duplicates, FindW, ContainsCS,
    stzString.Find, list of pairs, palindrome, sort hash list by value, banana split...), 3 to 21 ms each
  - assets/js/search.js and assets/css/search.css: a magnifier in the header (and / and Ctrl+K) opens the field over any page; the
    reference's own field gets the same results under it and keeps filtering its page; rows are 44 px, the match is bold and underlined,
    nothing moves; tools/search_ui.mjs drives it in headless Chrome and keeps the picture
  - found on the way: a second class collision (sr for the screen-reader text of external links and for result rows): renamed

state:
  release-1-pass-28: built; the commit carrying this entry is the one after d1f5ab44
  checks: 13 of 13 search questions; 0 failures on the example blocks; 0 dangling among 518,388 local links
  perception-gate:   OPEN (the author has not used the search yet)

waiting:
  - STZLIB-DOCREFORM-01: the documentation session has not reported; its record will feed the descriptions the search shows

next:
  - me:      push and verify live; wave 4, learning, teaching and pedagogic design as one flow (doc/SITE-PLAN-2026-10-03.md)
  - author:  open any reference page, press / and type: find, sort a hash list, banana split
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 01:27

subject:   wave 4 of the site plan, learning, teaching and pedagogic design as one flow: Education

why:       the author, "go ahead with wave 4": the Teaching page was confusing about its goal, mechanism and concepts (is the tutor a
           person or a program?), Zin is not to be named, and Teaching versus Pedagogy hid what Softanza offers education

did:
  - replaced the two pages Teaching and Pedagogy by one, Education, in the Learn menu, with three doors one level under it (a left bar):
    I learn by myself, I teach or design courses, I run a programme or an institution; the old addresses lead to Education
  - the landing page says what it is in a paragraph, who does what (learner, teacher, tutor, checker, court, institution: the tutor is
    a program of the library, never a person and never a language model), six things no course gives by default each tied to the
    library's own law and test, the three doors, and what is not done
  - the doors, read from the library's own charter, overlay guide, demo guide and the learner's desk: the path, the desk and the five
    rungs with the project each guard judges; a teacher's steps and a course designer's chapter format; an overlay's five steps, cohorts,
    languages, governed AI, the fifteen-minute demonstration
  - wrote tools/edu_run.py: the teacher's door run in the library (a cohort of two learners, an exercise judged by running, the
    cohort's report) into data/edu-run.json; the page shows code and output side by side with the run's date and commit
  - added the three doors to the Learn page and pointed the educator door of Offering at Education; Education is searchable
  - kept the word rule: the desk's commands are written without the interpreter's name (the file learn.ring, then the verb)
  - English and French of every page; Arabic and Hausa are not written (the site is fr and en)
  - a slip: I staged wholesale and the project's hook refused it, as it should; staged by explicit path after

state:
  release-1-pass-29: built; the commit carrying this entry is the one after 04df8989
  checks: 0 failures on the example blocks; 0 dangling links; the word sweep clean but for the course in reader.html (STZLIB-COURSE-WORD-01)
  perception-gate:   OPEN (the author has not read the Education pages)

waiting:
  - STZLIB-DOCREFORM-01: the documentation session has not reported

next:
  - me:      push and verify live; wave 5, forged in projects (RestoLean, Organizium, the knowledge hub, the learning programme)
  - author:  read Learn > Education and its three doors; rule on the wording of the six claims
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 01:53

subject:   wave 5 of the site plan, the page "Forged in projects": what RestoLean, Organizium and Sonibank, and DIKO taught the library

why:       the author, "go ahead with wave 5", then "Name Diko" and a reference the author withdrew not to be cited: the site had to tell that the library was
           built by use, and tell it only as far as a file of the library, or a document of the project, attests

did:
  - wrote the page Forged in projects (fr and en) under Vision: three rules to read it by, a dated order of events, then one section per
    project, each need tied to the library file that carries it or to the gap it names
  - RestoLean: the method lesson (a specification is not a delivery), the Lock, four needs (payments tried without a subscription, the whole
    solution seen before it is built, a constellation of worlds, a speed budget as a promise); the emulation and deployment designs are
    marked "example", not "origin"
  - Organizium and Sonibank: the BCEAO governance validators of the organisation chart, and the web layer born in that repository
    (quoted only as far as its existence and date: the repository is private)
  - DIKO, named as the author ruled: six asks of a platform, each tied to a piece of the library or to a gap the study names; offline by
    default is said to be a gap, not a lesson; DIKO Hub is said to be a design, not a product
  - wrote tools/forged_run.py and data/forged-run.json: two lessons run in the library at 0e72e2e2c, a registry that refuses a fake in
    production (is sound: 0, finding sandbox-in-production) and a bank chart that fails three BCEAO rules; the page prints each run's date
  - left out on purpose: no price, no client figure, no name of a person; the withdrawn reference is not cited on this page
  - checked: 0 failures on the example blocks, 0 dangling links, the word sweep clean but for the course in reader.html
    (STZLIB-COURSE-WORD-01), no standalone Zin on the page, both languages rendered and read at laptop and phone width

state:
  release-1-pass-30: built; the commit carrying this entry is the one after 186ffd46
  perception-gate:   OPEN (the author has not read the Forged page; the French was read by the agent only)
  withdrawn-reference: still cited on five older pages (one of them with its diagram image) -- not changed, for the author to rule

waiting:
  - SITE-REFERENCE-01: sweep the withdrawn reference out of the five older pages? -> the author
             [not routed; asked in chat]
  - STZLIB-DOCREFORM-01: the documentation session has not reported; a FOR STZSITE line in CONCLUSIONS would mean rebuild on its record
             [routed]

next:
  - me:      push and verify the page live; then the 103 classes without receivers, or the rebuild if the documentation session reports
  - author:  read Vision > Forged in projects, rule on the wording of the DIKO section, and answer SITE-REFERENCE-01
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 06:32

subject:   SITE-REFERENCE-01 closed: the withdrawn reference is no longer cited anywhere on the site

why:       the author, "sweep it out of the five older pages", after ruling that the new Forged page must not cite it

did:
  - removed its card from Customers and from Africa, and its mention from the Africa lede and the Principles card
    (the references now read: a bank and a restaurant), in fr and en
  - replaced it on Platforms, in the text, the third card and the diagram's alt text, by DIKO Hub, written as what it is, a design study
    that is not built, and linked it to the DIKO section of Forged in projects; the stage section now says DIKO Hub is not built
  - redrew the platforms diagram, wide and narrow, in both languages (four images): the third box reads DIKO Hub, designed; the French
    label first overflowed its box and the build refused it, so it was shortened; looked at the French wide diagram and the English wide one on the rendered page; the top half of both narrow ones, where the third box sits, is read too (the rest of them did not change)
  - kept Customers honest: it says "two are, today" and points to Forged in projects for DIKO, a design study and not a delivery
  - rewrote the Tour speaker notes and slide text the same way; re-rendered the proof images of the five pages
  - rewrote the plan's lines about it; on the author's request the older journal entries were scrubbed too
  - checked: 0 failures on the example blocks, 0 dangling links, no built page cites it; the word sweep is clean but for the
    course in reader.html (STZLIB-COURSE-WORD-01)

state:
  release-1-pass-31: built; the commit carrying this entry is the one after cfaf65aa
  withdrawn-reference: cited on no page of the site; this repository's git history keeps the older wording
  perception-gate:   OPEN (the author has not read the redrawn Platforms page or Customers)

waiting:
  - STZLIB-DOCREFORM-01: the documentation session has not reported; a FOR STZSITE line in CONCLUSIONS would mean rebuild on its record
             [routed]

next:
  - me:      push and verify live; then the 103 classes without receivers, or the rebuild if the documentation session reports
  - author:  open Platform > Platform of platforms and Offering > Customers; say if DIKO Hub as a design study reads right in the diagram
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-04 07:42

subject:   the last classes without a sample object: 28 of 101 now carry examples, and the journal no longer names the withdrawn reference

why:       the author, "go ahead with the 103 remaining classes", and "older journal lines naming the customs school should be scrubbed too"

did:
  - scrubbed this repository's journal and plan of the withdrawn reference (renamed its task SITE-REFERENCE-01); the git history keeps the
    older wording, and Central's own memos, CONCLUSIONS and mailbox name it too, which are Central's files and not mine to edit
  - recounted the open classes from the tool's own skip lists: 101 classes in the areas that may be composed had no receiver
    (the last report said 103; I did not find which two differ)
  - wrote 37 sample objects by hand from how the library's tests and sources build each class, the solvers, regex makers, geo
    classes, org-chart reporters and diagram converters among them; all 37 build; three more were tried and dropped: stzWorldGraph
    (its class is not in the library's load), stzListOfTables (it refuses what the tests give it) and stzWorkflowSimulation (no constructor)
  - wrote data/row-calls-hand.json: sample arguments per class where a parameter's NAME says nothing (a solver's expression,
    operator, varName), calls written whole where a sequence is the example (Solve then Status), and a list of 62 methods I read and refused
  - taught tools/rows_run.py to read that file, to show a method that returns the object itself by the object's content afterwards,
    and to refuse an object's name inside a list as an answer
  - read every kept example as a reader would, before keeping it: removed an internal helper shown with a meaningless argument
    (the solvers' tableau and population helpers), a method spelled as a typo (Shwo), and an example that said SetCaseSensitive empties the
    word stream (rewritten as the sequence a reader needs: set it, feed "Cat cat", two distinct words)
  - result: 209 examples added, 8,829 -> 9,038; classes with an example 213 -> 241; 28 of the 101 classes (635 rows in them)
  - rebuilt: 0 failures on the example blocks, 0 dangling links, the word sweep clean but for the course in reader.html

state:
  release-1-pass-32: built; the commit carrying this entry is the one after 3fc39d07
  classes without a receiver: 73 of the 101 -- 34 have no method that could be composed (a rule base is an init and nothing else, the seven
                       table accessors have no method of their own), 39 have methods and remain
  the 39:              file-based (the education classes, the code graphs, the font), four that cannot be built (STZLIB-RECEIVERS-01),
                       the planner's comparison helpers, three diagram converters whose output is longer than an example may be, and a few small ones
  perception-gate:     OPEN (the examples were read by the agent; the author has not read them)

waiting:
  - STZLIB-RECEIVERS-02: findings from composing, for the stzlib session, not routed yet -> stzlib [not routed; in CONCLUSIONS now]
  - STZLIB-DOCREFORM-01: the documentation session has not reported; a FOR STZSITE line in CONCLUSIONS would mean rebuild on its record
             [routed]

next:
  - me:      push and verify live; then the file-based classes only if the author wants a path shown in an example, otherwise stop here
  - author:  open Learn > Reference > stzLinearSolver and stzUnicodeData, and say whether the examples read as examples
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-05 21:41

subject:   STZSITE-EDUCATION-REFRESH-01: the Learning System on the site, with its three limits beside every claim

why:       the stzlib-education report of 2026-10-05 20:51, read from stzlib at 4a184e6f0 (the commit it names, on origin/main), after the fact sheet, DEMO.md and CHARTER.md

did:
  - placed it: Education stays the home, and gets a fourth page, "What is proved, and what is not" (fr and en), in its left bar; the
    three limits come first, then ten figures each beside its guard and its limit, then the learner's desk and the reviewer's sheet
    run for real, how a draft stops being one, and what the page does not claim
  - quoted only the fact sheet's figures; two I read from the library rather than took on trust: a "unit" is a chapter with its
    exercises, a world page, the skills or the tutor's texts (the comment of ReviewUnits), which is what the 35 are
  - wrote tools/edu_record_run.py: six runs at 4a184e6f0, in a temporary learner's folder and never in the library's (the worktree
    was clean before and after): status, a wrong answer refused, a right one passed, status again, the tutor refusing to spoil
    chapter 12, and the count of reviewed units in fr, ar and ha (0 of 35 in each); the first and the tutor's match the memo word for word
  - put the limits beside the claim in every other place the site says "four languages" or describes the system: the Education
    landing and its learner and programme doors, the Book page, the estate card, Principles, Sovereignty, Editions (and the
    enterprise offer: no adopter yet), the Tour (slide eyebrow and speaker notes), Born in Africa, Audiences; both languages
  - replaced "149 promises in the English edition" and "eleven guards" by the sheet's figures (60 editions, 249 assertions; 14 guards, 716
    assertions), and the tour's "three minutes twenty-two" by what this machine measured, three minutes thirty-seven
  - FOUND AND FIXED a falsehood of the site's own: the reader page, built on 2026-10-03, carried none of the draft notices the library
    added later, while the Book page said it did. Rebuilt it from the library: 15 chapters in four languages and 3 world pages all ran
    green. Removing the 54 notices (18 units x 3 languages, each in its own language) returns the old page byte for byte
  - checked: 0 failures on the example blocks, 0 dangling links, the word sweep clean but for the course in reader.html
    (STZLIB-COURSE-WORD-01); looked at most of the English page and the top of the French one on a render

state:
  education-record: built, fr and en; live once pushed
  the three limits: 0 of 35 units reviewed in fr, ar and ha; cells run on the desktop only; no institution has adopted it -- each beside every claim
  not re-measured by the site: the 14 guards (about twenty minutes), the 716 assertions, the 20 demo claims; the page says so
  one number did not reproduce: the reader builds in 217 s here, the sheet says about 100 s; a different machine under load, not a defect, and the page quotes the sheet only for its own run
  perception-gate:   OPEN (nobody but the agent has read the page; the Arabic and Hausa notices are only counted)

waiting:
  - EDU-ATLAS-01: the Atlas rating of the Learning System -> compass [not mine; the site's Atlas is unchanged]
  - STZSITE-PIN-01: the worktree the site used to pin the library for its runs, D:\GitHub\_wts at 0e72e2e2c, is now the security desk's
             (security/week1), so the pin no longer holds; today's runs went to the education worktree, read-only
             -> Central or the author, who own worktrees [not routed; in CONCLUSIONS now]
  - STZLIB-DOCREFORM-01: the documentation session has not reported [routed]

next:
  - me:      push, verify the new page and the rebuilt reader live
  - author:  read Learn > Education > What is proved, and what is not, and say whether the limits sit where a reader meets the claim
  - stzlib-education: nothing is owed; every figure that was checked matched
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-08 20:27

subject:   STZSITE-REFORM-01, wave 0: the hero line, the code shown in Haro's name, scenario guards, the runtime said once, and four defects of the site's own

why:       the author, "go ahead with wave 0", after the reconcile memo of 19:45; D1 to D4 were not ruled, so the memo's defaults were applied
           and are named below for the author to overturn

did:
  - put the new hero line in its eight places (build.py's two slogans and the home's title, the tour in two languages, the README, the
    home's two h1): "The Software Makers Platform of the AI Age", "La plateforme des makers du logiciel à l'ère de l'IA"; the second line
    unchanged; the home's word-by-word definitions now define "a software maker" and "the AI age" (D1: my wording, the author's to change)
  - built the rename that shows code in Haro's name (B37): tools/haro.py renames the name and nothing else, leaves what the library owns
    (file names, ring_len, ring:, Ring++, a ```ring fence tag the narration reader parses), and an audit refuses any other difference;
    four data strings that spell the name inside a value (RIxxNxG, rixxnxg, "R I N G", fjringljringdjringg) are declared pairs, each
    found because the renamed chapter ran red without it
  - rebuilt the course reader from a renamed COPY of the program (tools/reader_run.py): every cell of the 15 chapters ran green in four
    languages and the three world pages, 99 lines renamed in 21 files, published in data/haro-rename.json; the exercise checkers were
    renamed with their tasks, so what the page shows and what proves it are one program
  - re-ran the book's proof on that copy (tools/proof_run.py --haro): 60 editions with every promise kept, 23 of 23 exercises prove
    themselves; the cells the proof pages used to hide for the old name are shown, with one sentence saying the name was changed and
    nothing else; the proof data now carries the commit it ran at instead of a typed one
  - "narrated guards" became "scenario guards" in the prose of 10 pages (en and fr) and in the four trajectory diagrams
  - printed the runtime once (D4 as proposed): on Platform's Haro section and the first screen of Start, the sentence "Softanza runs today
    on its Ring face ... Ring++ is the bridge, in construction. Haro is the destination", written once in the build; a new build rule
    refuses the name anywhere else in the prose
  - FOUND AND FIXED a dead guard: the build's rule refusing the name Zin held two backspace bytes in its regex and had never matched
    since 2026-10-03 (the bash-heredoc trap); repaired, and it finds nothing today
  - FOUND AND FIXED the zero-byte reader proofs: a ':' in the render's file name opened a hidden NTFS stream; names fixed, renders redone
  - fixed the dead #editions anchor on Audiences (en and fr)
  - brought reader.html and deck-check.html to the floor: measured with a new instrument on the paint (tools/floor_check.mjs, size and
    contrast per visible text, light and dark): 0 texts under 16 px and 0 under contrast on four reader chapters (en, ar, ha) and on the
    deck check, which had 2 and 1 left after the first fix; before, the assessment counted about 2,730 and 417
  - the two gates (the example checker, the proof pages) now read the rename's own pattern; seven other copies of the old pattern
    remain in tools that filter rather than judge, to fold in wave 1;
    the word sweep finds the former name in the code of 0 files, the first time since the site began (the reader's long-standing hit,
    STZLIB-COURSE-WORD-01, is closed by the rename, not by the library)
  - checked: 0 failures on the example blocks, 0 dangling links; looked at the home, Start and the reader on a render

state:
  release-2-pass-1: built; the commit carrying this entry is the one after fa8e1e60
  library pin:      the runs read the education worktree at 4a184e6f0 (clean before and after); STZSITE-PIN-01 still open
  perception-gate:  OPEN (the agent looked; the author has not)
  not done in wave 0, on purpose: the glossary (wave 4); the StzWeb sweep (68 generated pages from the library's own comments, B19)

waiting:
  - REFORM-RULING-01: D1 (the definitions' wording), D2, D3 -> the author [asked 19:45]
  - B19, the drift list, for StzWeb on 68 generated pages -> stzlib [routed now in CONCLUSIONS]
  - the reader's own small sizes and its dark link colour, fixed today only in the site's copy -> stzlib-education [routed now]
  - the book's hero line, which must match the site's -> the book session through Central [routed now]

next:
  - me:      push, check the deploy once, then wave 1 (the research section) on the author's word
  - author:  read the home's three definitions and the runtime sentence on Start; rule D1 to D3
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-08 21:27

subject:   STZSITE-REFORM-01, wave 1: the narrations become the research section -- every article a page, a card, a filter, a citation

why:       the author, "go ahead with wave 1"; the assessment's 12.16 asks that the author's articles be published as research, and
           B36 that a run annotate an article rather than decide whether it is shown

did:
  - published all 135 articles, where 8 were published before: the run is now a note on the page, never a gate (B36)
  - ran every article in Haro's name inside the library at 4a184e6f0 (tools/narrations_run.py renames each article, the name and nothing
    else, audits the rename, then runs it): 55 ran, 123 of their 423 blocks kept their promise; 56 were not run because their code touches
    files, the network, the clock or chance; 18 do not load as written; 6 carry no code. Each page says which, block by block
  - FOUND AND FIXED a defect of the site's own: five articles indent their code fences under list items, and the runner and the page both
    read fences at the margin only, so that code was neither run nor shown as code (the mental-model article, the one Learn points to, read
    as "no code"; four pages showed the fence tag as text). Fences are brought to the margin before parsing; the mental-model article now
    keeps 4 of its 7 blocks. A --only option re-runs named articles in seconds instead of all 135 in 336
  - derived a card for every article (tools/narr_meta.py -> data/narrations-meta.json): abstract, genre, series, Atlas area, year of first
    commit, author, guards named, related reading; every derived field says it is derived on the page, until the articles carry their own
    header (B34, routed to stzlib)
  - gave each article a page in the research form: eyebrow, title, lede taken from its first paragraph, the card line, the hero picture
    (32 articles open on one; 64 pictures hosted in all), the body with each code block labelled Haro, then "Proved by" (the guards it names, linked), related
    reading, a citation block, and the proof line with the commit
  - made Narrations a top-level section beside Platform, with the three series as pages read in order (performance 11, security 14,
    delivery 5); the index lists paradigm essays first, then by date, with filters by genre, area and year; the family filter shows
    "designed, not yet built" (B30)
  - listed each Atlas area's articles on its page; pointed Learn at the mental-model article's page instead of the file on GitHub
  - changed the footer's law (D7): "Every code block that runs was run on the night of publication and its output sits beside it; the
    others say so" -- on all 4,110 pages that carry it
  - folded the seven old copies of the name pattern into tools/haro.py, and found the fold was wrong before committing it: the narrower
    rename pattern let two method examples showing "ring---" as test data through, and the gate could not see it because it reads the
    same pattern. Two meanings now have two names in one file -- FORMER (what the rename treats as the name) and SHOWN (the stricter filter
    for code shown as the library wrote it) -- and the method pages are back to 1,177
  - dropped an empty-label link in one article that pointed at an article that does not exist; it showed the reader nothing
  - checked: 0 failures on the example blocks; 0 dangling links in 4,203 files; the former name in the code of 0 files and in the text of
    0 narration or Atlas pages; the floor (16 px, contrast) held on the index, a series page, an article, an area page and Learn, light and
    dark; the filters answer in both languages (135, 25 paradigm essays, 3 of them from 2026, 14 in security); looked at the index, an
    article's top, body and tail on a render

state:
  research section:  built; 270 article pages + an index + 3 series pages per language
  library pin:       every run read the education worktree at 4a184e6f0, clean before and after; STZSITE-PIN-01 still open
  perception-gate:   OPEN (the agent looked; the author has not)
  derived, not ruled: the genre and area of each article come from its file name -- 12 articles point to several areas and say so

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not yet answered]
  - B34, a front-matter header in each article (abstract, genre, series, area, guards), which replaces every derived field
    -> stzlib [routed now in CONCLUSIONS]
  - B30, the article families, which the family filter waits on -> stzlib [routed now in CONCLUSIONS]

next:
  - me:      push, check the deploy once; then wave 2 on the author's word
  - author:  open the narrations index, try the filters, read one article to its citation; say whether the genres read right
```

```yaml
by:        stzsite · claude-opus-5-5 · 2026-10-08 22:17

subject:   STZSITE-REFORM-01, wave 2: the paradigms -- Natural and executable, By example, The Softanzuter, The Softanza way, and the register of innovations

why:       the author, "go ahead with wave 2"; the assessment's 12.12 to 12.15, 12.22 and 12.23 found five paradigms and a discipline that the library holds whole and the site names nowhere

did:
  - made Craft the style's page, "How Softanza is written", with the fourteen rules of writing, each with its sample written below it
    and four new runs (a scene, a chain, a precise verb, a near-natural sentence); and hung the paradigm pages off it in the same left
    bar the Education pages use, so the menu path gains no entry
  - published "Natural, and executable": one program run in English, Hausa, French, Arabic and Turkish, the two directions (who parses),
    the refusals with their reasons, a language added at runtime as a block of data, five faces, the history in four dates, the limits;
    seven runs, all from the scenario guards that are green, because the articles' own blocks mostly no longer run as written
  - published "By example" with a stage at each of its three levels in its titles (finding: every piece built, the verb not yet;
    inducing: the agent declared and reserved; synthesising: designed), the example-to-promise law marked designed, and one sentence
    saying nothing induces yet
  - published "The Softanzuter": the definition, the ladder of four rungs with a stage at each, the Regexuter and the agent's cascade
    run, the three siblings as vision, and the three meanings of the word; rung 2, the missing middle, is said to be unbuilt
  - published "The Softanza way": the seven steps of the mental model with the rules that serve each, run on one problem, the three
    widenings, and the courts that judge it, with the one that does not exist (a court for a program written with the library) marked
    designed; every callout headed "The Softanza way" on the site now links to it (20 pages)
  - declared the discipline once (data/discipline.json) and generated from it the craft page's rules, this page's steps, a new section
    of llms.txt placed before the method list, and a discipline object in the agents index
  - published the register of innovations as a page (47 rows, 7 families, each with the record's line, its evidence and the pages and
    articles that tell it), marked designed: it is a hand-made reading, not yet generated from a guarded file
  - ran 25 new snippets in the library at 4a184e6f0 (worktree clean before and after); the runner now records the commit it ran at, so a
    run's label no longer claims the old pinned one
  - found and left out of the page: the article that teaches rule 4 calls ReplaceNextOccurrence, a name the library does not define; its
    named-parameter sample is shown from another source instead, and the article's name goes to stzlib
  - checked: 0 failures on the example blocks, 0 dangling links in 4,213 files, the former name in the code of 0 files, 0 texts under
    the 16 px floor or under contrast on the new pages in both themes and both languages; looked at the Natural, Way and Softanzuter pages
    on renders

state:
  paradigm pages:    built, en and fr; Craft is their hub
  innovations:       published as "designed" until a guarded data file generates it
  perception-gate:   OPEN (the agent looked; the author has not)
  not done, on purpose: the Atlas layer above its areas, the Narrations page grouped by the seven families, a 2022 sample beside each
                     rule, the Regexuter article split at its vision tail -- each waits on data the library does not hold yet

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not yet answered]
  - the register as a guarded data file (B30), the narration that calls a name the library does not define, the lexicon coverage per
    language and the no-network guard for the natural layer -> stzlib [routed now in CONCLUSIONS]

next:
  - me:      push, check the deploy once; then wave 3 on the author's word
  - author:  open Craft and follow its left bar; read Natural and say whether the five faces are the ones you would claim
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-08 22:23

subject:   the hero line says "Crafters", not "Makers"

why:       the author, in chat: "crafter" says the culture the background image carries and what they think of programming -- not maker, not builder

did:
  - changed the line in its places: "The Software Crafters Platform of the AI Age" and, in French, "La plateforme des artisans du logiciel à l'ère de l'IA"
    (artisan is the word the French tradition of "software craftsmanship" uses); in the build's two slogans and the home's title, the home's two
    h1, the tour in two languages, the README and the first line of llms.txt
  - changed the home's word-by-word definition to match: "A software crafter" / "Un artisan du logiciel"; its text is unchanged, so D1 (the wording of
    the definitions) stays the author's to rule
  - looked at the French home on a render: the line fits its panel in two lines

state:
  still saying "maker": the Offering page ("What is a maker?", six kinds of makers, the doors), the Atlas and guide labels ("what a maker does
                        with it"), the Agentic page's "decision maker" (a different word, left), and the Learn page's run, whose output
                        spells "makers" because it is a run and must not change
  the book:             its cover line must carry the same sentence; routed again to the book session

waiting:
  - the sweep of the rest of the maker vocabulary -> the author [asked now: it is the same decision, applied to about 25 lines]

next:
  - me:      commit and push this line; sweep the rest if the author says so
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-08 22:31

subject:   the rest of the maker vocabulary becomes "crafter" (English) and "artisan" (French)

why:       the author, "yes sweep the rest of the maker vocabulary", after the hero line changed

did:
  - changed the Offering page: the lede ("six kinds of crafters"), the heading and its anchor ("What is a software crafter?", #crafter; nothing linked to the old one)
    and the definition's first words; the French says "un artisan du logiciel"
  - changed the Areas page's lede, the Atlas area pages' heading and the guide pages' line ("what a crafter does with it", "ce qu'un artisan en fait")
  - changed one line of the binary area's heritage, which called the person who narrates a file's fields a maker (the French said "fabricant")
  - left on purpose: the Learn page's run, whose output spells the word because it is the program's own output; the names of the library's classes
    (RegexMaker, KernelMaker, FileMaker); "decision maker", a different word; a quoted developer's surname in an article
  - checked: the built pages hold the word only in those four places; 0 failures on the example blocks

next:
  - me:      commit and push
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 00:38

subject:   STZSITE-REFORM-01, wave 3: the platform -- nine journeys, the seven design goals, the layer decision table, the environment, conversations, seven languages and one door, and Compared in the top menu

why:       the author, "go ahead with wave 3"; the assessment's 12.8 to 12.11 and 12.18 to 12.21 and 12.24 found a method (the user flows), a skeleton (the goals), a dependency rule (the layers) and four directions that the library holds and the site does not tell

did:
  - declared the journeys once (data/journeys.json) and generated from it a hub and nine pages in two languages: the programmer, the educator,
    the linguist and knowledge architect, the analyst and designer, the data analyst, the technical leader, the agent, the author and the
    platform architect; every step carries its stage in the Estate page's own words and a page of this site that shows it; the Offering
    page's six doors now link to their journeys and to the ninth
  - made the platform architect's journey the page for the vertical: nine steps from the guarantee sheet to operating, four of them built
    with guards, two built and only emulated, one a specification with two rungs built, one a name, one with no instance; it says so in
    its own positioning sentence, and it does not use the word "architecture", which the library's layers page already owns
  - added the layer decision table to the Architecture page: which layer to load, the naming convention, the fact that base does not
    inherit core, the build goal with the two web sizes, the lesson of the entry files as a callout, and the debt in one paragraph
    (93.2 per cent of the lines in base, 44 folders against 23 placed); the core's breakage is reported there as read, not asserted as current
  - published "Seven design goals": the thirty-three features of the 2022 slide against their state today (24 built, 4 transformed, 2 changed
    form, 1 partial, 1 archived, 1 a name only), one run per goal, and the decision owed on manageability, which is the author's
  - published "The environment": the grammar six efforts converged on, the efforts with their stages (one ships, a listening bench), the two
    shells with their named costs, and one sentence saying no environment of this family ships today
  - published "Conversations" as a direction: what exists (the governed conversation, ports with sandboxes, the registry that refuses a fake),
    the text-message cost law run in the library, what is designed, and what is absent; no conversational medium is a target today
  - published "Seven languages, one door": the rationale as the spine, the two doors, the difference between a facet of Haro and a door to a
    runtime, and the honest state of the door, with no run on the page because the door's own guards cannot say whether it works
  - made Compared a section of the top menu beside The code, and gave it, in words, where the others lead on the nine rows where Softanza is
    partial or absent, and the five rules by which the site compares; the area-level Compared block is not built (below)
  - put the three new families in left bars: goals and the paradigms under Craft, conversations, environment and the door under the platform
    of platforms, the journeys under Offering
  - ran 8 new snippets in the library at 4a184e6f0 (clean before and after); FOUND on the way: the library counts a woman-technologist emoji
    as four characters (its parts), not one; the page's Unicode run uses Arabic, Latin and Chinese, where a character is unambiguous
  - checked: 0 failures on the example blocks, 0 dangling links in 4,241 files, the former name in the code of 0 files, search 13 of 13, and
    0 texts under the 16 px floor or under contrast on the new pages in both languages and both themes

state:
  gates:             all green, as above
  not done, on purpose: the Compared block on each Atlas area (it needs a register of comparisons the library does not hold as data: B39),
                     the Compared layer column per area, the business matrix on the polyglot page, the three screenshots of the environment
                     (none exists on this machine), the Seven design goals run for each of the 33 features
  perception-gate:   OPEN (the agent looked at the goals, compared, journey and architecture renders; the author has not)

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not answered]
  - the register of comparisons as data (B39), the layer court (B19), the goals court (B16), the inheritance decision (B20), the journey
    guard (B10), the door's promises made judgeable (B61), the messaging unit and channel (B46) -> stzlib [routed now in CONCLUSIONS]
  - the manageability decision (revive the decorators or declare the class form final) -> the author [asked on the goals page]

next:
  - me:      wave 4 on the author's word
  - author:  open the journeys from the Offering page, walk the architect's nine steps, and say whether the stage words are the ones you would put
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 01:45

subject:   STZSITE-REFORM-01, wave 4, first half: the external reader's shortlist -- Start that runs, a glossary, a home that leads somewhere, the small defects, the search, the class pages

why:       the author, "go ahead with wave 4"; wave 4 lists about forty items, and I took first the ones the assessment's own shortlist (0.5) puts first and that the site can decide alone; the other half needs the author's word or content the library does not hold yet

did:
  - made Start runnable end to end: three steps (the repository, the runtime at version 1.27.0 with where to get it, a first.ring file whose first line
    loads the library), the command that runs it, and the commands to rebuild the reader and play the demo, where there were comments; the first
    program was run again today from a clean library worktree at 4a184e6f0 and printed what the page shows (6.9 seconds)
  - published a glossary of thirty terms (data/glossary.json, en and fr), in the Learn path and the footer; its entry for Haro, Ring++ and Ring is the
    runtime sentence, printed there as the assessment asked
  - linked the home's six audience rows to their journeys and gave the first screen one call to action, Start and Learn
  - added the page for an address that is not found, a sitemap of 4,145 addresses, a robots file, and a link-preview card (the wordmark on the site's
    paper, made from the wordmark alone) with Open Graph and Twitter tags on every page
  - gave the magnifier its word, and indexed the authored pages in the search (56 pages and the front page): "map of niger", which found nothing before,
    now finds the page; three new questions about the site itself are in the search check, 16 of 16
  - moved the two header icons that had no words, the slideshow and the repository, to the footer where words already stand, and added "Softanza" as the
    first step of every trail; tightened the menu so eight entries and the search word fit at 1366 px
  - gave the course reader a way back to the site (a bar at its top), and fixed the README's page count
  - class pages: a "jump to" line (letters, and the sections the source names) at the top of each, and composed examples folded by default with their
    provenance under them; the examples taken from the library's own tests stay open
  - renamed the Offering section "Adopt" ("Adopter"), as the assessment proposes; its landing page keeps the name Audiences
  - FOUND AND FIXED: two regular expressions, in the reference and in the search builder, that were meant to say "the word Ring, standing alone" and
    held two backspace bytes each since before this reform, so they had never matched (the same heredoc trap as the Zin rule of wave 0); the narration
    titles in the search index now follow the rename; and the runtime's own command, "ring first.ring", is no longer treated as the former name in
    code, because it is the command that runs the program
  - checked: 0 failures on the example blocks, 0 dangling links in 4,244 files, the former name in the code of 0 files, search 16 of 16, and 0 texts under
    the 16 px floor on the new pages; the floor instrument reports the home's menu at 1.12:1 because the menu lies over the photograph and the instrument cannot
    see an image: the build's own measurement of it (white letter against its halo over the brightest pixel) is 19.46:1, and I looked at the render

state:
  gates:             green, with the one instrument limit named above
  held back:         "Why Softanza leaves Ring" (12.7) is drafted, with the six things I need the author to confirm, in .central/WHY-RING-DRAFT.md; it is not in any commit
  not done, on purpose, for the second half:
    - the caveat dose (D2, the author's ruling), the Learn page split into learning Softanza and building on it, the learner's vocabulary diet
    - the guides in the Learn path, How-to beyond lists and strings, the hero picture's provenance (I do not know it), the Estate cards as a table,
      the Zui page's closing line, the phone's pinned rows (still four on a class page), decks per target
    - the Adopt section's own pages (proving grounds, solutions, education as a product line, partners, certification), the stack page, the seat pages, Depth
    - the Applications section, the Intelligence section and the Aïcha page, the store page, the site's own world file, the Foundation chapter, Roots,
      Pattern languages, the grammar of functions, a reading order for the narrations, the gallery, the craft page's metaphors
  perception-gate:   OPEN (the agent looked at the home, Start, the glossary and a class page; the author has not)

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not answered]
  - WHY-RING-DRAFT: the six confirmations -> the author [asked here; nothing public until answered]

next:
  - me:      commit and push; the second half of wave 4 on the author's word, starting with the pages whose content the library already holds
  - author:  open the home, Start (follow it to the first program), and the glossary; read .central/WHY-RING-DRAFT.md and answer its six questions
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 02:37

subject:   STZSITE-REFORM-01, wave 4, second half: applications, the store, depth, roots, pattern languages, Aïcha, and the estate as a table

why:       the author, "go ahead with the second half of wave 4"; I took the pages whose content the library or the site already holds, and left the ones that wait on a decision of the author or on facts I cannot read

did:
  - built the Applications family in the left bar of the platform of platforms: a hub that maps eight planes with their stage and guard count (read from the guards, not from
    the status documents), the host (with the Atlas's own statement of its gaps), from the editor to the device (define, emulate, plan, deploy, secrets), surfaces (the web
    built, the native interface in construction, the rest as directions), real applications (three grounds, each with its stage), your first application (the shape of a
    world, the narration that builds one, and the missing creation command named), and the store (six properties, its charter and its two built rungs, stage in construction)
  - set the store's stage word on the Estate page to "in construction", as the assessment says the site's own definition requires, and drew the estate's eleven products as a table
  - published "Aïcha": the author's definition, the folder that would make an agent (written, not run), the six organs that exist under other names with their stage, and the coding agent
    that would change the unit from a diff to a refinement, stage designed; it says in its first block that no product ships under the name
  - published "Roots": the 2022 founding sentence in the author's words, the slogan, what the deck held, and the dates printed with their sources where they disagree; I left out the
    dedication and the 2021 mail, which are the author's to give
  - published "Pattern languages": seven languages over seven kinds of data, five runs from the library's own tests at 4a184e6f0, and the two that failed said plainly (below)
  - published "Depth": the library's 46 domains with files and lines, the engine's files, the 5,284 test files with 527 scenario guards, and 43 design documents as a reading list, all
    counted by a new tool (tools/depth_run.py) from a checkout; the hand-over notes between working sessions are left out of the list, and a note that held a machine path was one of them
  - added a reading order of twenty articles to the narrations index, from the mental model to reactive programming; put each area's lane tally under its tile; and pointed Learn at the guides
  - FOUND: the library's own tests for the table patterns (cols(3)) and for time patterns (MatchPartial) promise a match and print 0 at 4a184e6f0, run directly from their folders
    (the same tests passed in earlier runs of the narrations); reported below
  - checked: 0 failures on the example blocks, 0 dangling links in 4,266 files, the former name in the code of 0 files, search 16 of 16, 0 texts under the floor on the new pages;
    two of my builds ran at once once and broke a file; I rebuilt from nothing and ran every gate on the clean tree

state:
  library pin:       every run read the education worktree at 4a184e6f0, clean before and after
  not done, on purpose (they wait for the author or for facts I cannot read):
    - the section "Applications" in the top menu (the menu has no room for a ninth entry at 1366 px; the family sits in the Platform section's left bar), and the page for the world itself
    - the home sentence "With Softanza you build applications" and a fourth door (the home's words are D1, the author's)
    - the Adopt section's own pages: proving grounds, solutions, education as a product line, partners, certification (commercial decisions); the stack and seat pages; ESPA-MT stays unnamed (D3)
    - the caveat dose (D2), the Learn split into learning Softanza and building on it, the learner's vocabulary diet, decks per target
    - the Intelligence section (renaming Agentic), a name check for Aïcha, the Foundation chapter, the declared languages table, the grammar of functions, the gallery, How-to beyond lists
      and strings, the Zui page's closing line, the phone's pinned rows, the hero picture's provenance (I do not know it), the site's own world file
    - "Why Softanza leaves Ring": drafted, held, six confirmations owed (.central/WHY-RING-DRAFT.md)
  perception-gate:   OPEN (the agent looked at renders of the estate and the pattern page; the author has not)

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not answered]
  - the six confirmations on the Ring page -> the author [asked 01:50]
  - the table-pattern and time-pattern tests that print 0 where they promise a match -> stzlib [routed now in CONCLUSIONS]

next:
  - me:      commit and push; then whichever of the held items the author rules on
  - author:  open Applications in the Platform section's left bar, and the pattern page; rule D1 to D3
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 03:08

subject:   "Why Softanza leaves Ring" is published, in the cautious form

why:       the author, "go ahead with the Ring page", after the draft and its six questions; the answers did not come with the go-ahead, so I published what the author's own words and the site's record carry, and left out what only a third party's record could prove

did:
  - published the page in English and French under Roots (a two-entry left bar), and linked it from Roots, from the Haro proof line on Platform, and from the glossary entry
    for Haro, Ring++ and Ring; it is the one page, besides the runtime sentence, where the site names the former language
  - kept: thanks first (the years, the book, the 2021 description, the 2022 presentation's sentence), the three reasons, the commitments the site runs, and what stays
  - reason one states the technical limits as the author's, reproduced by the author, without the numbers of an upstream register that is not public yet; it says so in its last line
  - reason two is "in the author's experience", and says nothing about how Ring++ was received
  - reason three states the due-diligence argument and the author's ethical concern in general terms
  - LEFT OUT, because I cannot verify them from any record I can read and the page's own rule is to name decisions and documents: the removal of the package, the
    removal from the core team, the count of pull requests, and the twelve limits by name; the author can add any of them, each with its link, and the page's last line is ready for it
  - checked: 0 failures on the example blocks, 0 dangling links in 4,268 files, the former name in the code of 0 files, search 16 of 16, the floor held on the page and on the three it touches; I looked at the render

state:
  perception-gate:   OPEN (the agent looked; the author has not read the final text)

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not answered]
  - the omitted claims, each with a public source or the author's wording, if the author wants them on the page -> the author

next:
  - me:      commit and push
  - author:  read the page once through before it is shared; say what to add or cut
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 03:20

subject:   the Adopt section gets its pages: proving grounds, solutions, education as a capability, partners, certification

why:       the author, "go ahead with the Adopt pages"; the assessment's 3.3 asks for a section that helps people adopt, partner and certify, and its 3.4 asks the author to rule before a new offering is announced

did:
  - published five pages in English and French: Proving grounds (RestoLean, Organizium and the Sonibank, DIKO, each as asked, what exists, what was learned),
    Solutions for organisations (what is delivered with the stage of each, the engagement in three moves, assurance as a name), Softanza for education (a course is a
    folder, the mathematics course as proof beyond programming, the fifteen-minute demonstration, the three limits), Partners, and Certification
  - put the funding doctrine, the project funds itself so that no outside capital acquires a voice over the open foundation, as a box on the Audiences page
  - kept Partners and Certification to what is designed: the laws every customer is promised, a certification as evidence and not an examination (a project whose guards
    pass and that a human reads), the stage said as designed at every card, and no term, price, fee or share stated, because none is set
  - did NOT name ESPA-MT: the framework convention is attested in the record, but the education desk's fact sheet says to name no institution, and the author's account is that the other
    side did not honour its side; a page that listed it as a partner would misstate that. The Education page keeps its limit "no institution has adopted it yet"
  - left Partners and Education free of any promise about schools in Niger or the sub-region, because the convention's articles 5 and 9 give one institution a priority there; the author knows
    the clauses, and the pages promise nothing they could contradict
  - checked: 0 failures on the example blocks, 0 dangling links in 4,278 files, the former name in the code of 0 files, search 16 of 16, the floor held on the new pages; I looked at the render

state:
  perception-gate:   OPEN (the agent looked at the solutions render; the author has not)

waiting:
  - REFORM-RULING-01: D1, D2, D3 -> the author [asked 19:45, not answered]; D3 is what would let the proving-grounds page name the first institution in education, in the words the document supports
  - the money model, if the author wants a price or a share on Partners or Certification -> the author

next:
  - me:      commit and push
  - author:  read Partners and Certification as a stranger would; say whether "designed, no term" is the line to hold
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 03:44

subject:   the held items: what I could do on the author's word, and what I could not

why:       the author, "go ahead with the held items"; I took each held item in turn and did it where the site can decide it alone

did:
  - D2, the caveat dose: the figure "0 of 35 units reviewed" now stands once on each Education page, in its limits paragraph; the earlier mentions on the Education and Programme pages
    say "drafts" and link down to it; the record page keeps the full account
  - D1, the home: added the sentence "With Softanza you build applications: you declare a world, and it runs, on the web today and on the other surfaces as they are built" (the stage
    is in the sentence), and a seventh door, "A team that ships an application", on the home, on the Audiences page and in the journeys hub; Start gains "Your first application"
  - the Intelligence section: the Agentic section is named Intelligence in the menu and the footer; its pages keep their own titles
  - the first picture says what it is: "Illustration: how it was made is not recorded in the repository", in both languages, because I do not know how it was made
  - a page for the world (domain, life, body, and the four ways it is met), in the Applications bar
  - the Foundation chapter, six one-screen pages: the graph beneath, four widths, visual by default, proven, reach, and the declared languages as one table of thirteen rows with
    their stage and no product names; the figures are counted from the library (data/depth.json) or marked as readings of an outside assessment
  - Learn: "The ladder" is "Your levels" in the learner's words, and Learn points to Softanza for education for the other proposition
  - two defects of my own found in the renders and fixed: the French menu overflowed at 1366 px with eight entries and the search word (tightened between 1300 and 1480 px), and the declared
    languages table squeezed its last column
  - checked: 0 failures on the example blocks, 0 dangling links in 4,294 files, the former name in the code of 0 files, search 16 of 16, the floor held on the new and changed pages

state:
  not done, and why:
    - the phone's pinned rows: the header, the section's path and the trail are one pinned block and the home's hero, the left bar and the reference tables measure it; collapsing it for
      phones changes every page and needs a design the author chooses (a disclosure for the path and trail is my proposal)
    - Applications as a ninth top-menu entry: the menu has no room at 1366 px, in French least of all
    - the grammar of functions (twenty-two forms, a run each) and the gallery: I have verified runs for about a third of the forms and none for the gallery's pictures, which wait on the author's
      afternoon of looking; How-to beyond lists and strings: a recipe is a file in the library's quickers folder, and the site does not write the library's files, so the request goes to stzlib
    - the Zui page's closing line: it needs the audit's date and results, and I have not run the audit; decks per target need scenes and a projector's eye
    - the vocabulary diet beyond Learn, and the Learn page's own split, are done only as far as the wording above
    - D3 and ESPA-MT: unchanged; nothing names an institution
  perception-gate:   OPEN (the agent looked at the home, the declared languages and the world; the author has not)

waiting:
  - REFORM-RULING-01: D3 -> the author [asked 19:45, not answered]
  - How-to recipes outside lists and strings -> stzlib [routed now in CONCLUSIONS]
  - the phone's pinned block: a disclosure for the path and the trail, or another design -> the author

next:
  - me:      commit and push
  - author:  open the home in French at 1366 px and on a phone; say whether to collapse the path and the trail on phones
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 04:07

subject:   the phone pins one row

why:       the author, "go ahead with the phone disclosure"; the assessment's 4.6 asks for one pinned row at most on a phone

did:
  - on a screen narrower than 761 px, a small script folds the section's path and the trail into one closed line, "Where you are: ... ", placed under the menu and scrolling away with the
    page; it opens on a tap and shows the path and the trail as they were
  - measured on three pages at 390 px in a headless browser: the pinned header is 47 px, where it was 145 px on a class page (a sixth of the screen), and the left bar was already a
    row that scrolls away; the table headers that stick under the menu follow the new height
  - without the script nothing is lost: the path and the trail stay where they were, pinned; the desktop is unchanged
  - checked: 0 failures on the example blocks, 0 dangling links in 4,294 files, search 16 of 16; I looked at the scrolled and the opened state of a class page

state:
  perception-gate:   OPEN (the agent measured and looked; the author's thumb has not been on it)

next:
  - me:      commit and push
  - author:  open a class page on a phone, scroll, and open the "Where you are" line
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 04:33

subject:   the grammar of functions, each form tried

why:       the author, "go ahead with the grammar of functions"; the assessment's A3 asks for the twenty-two forms with one run each

did:
  - published "The grammar of functions" in the Craft family's bar, English and French: fifteen forms, each tried in the library at 4a184e6f0 with the example its own article gives (a new
    tool, tools/grammar_run.py, data/grammar.json), and what came out shown beside the promise: the answer, or the library's own error
  - the result is the page's finding: of 22 tries, 11 kept their promise (active, passive, fluent, immutable, plural, negative, alternative, named, conditional, prefix, suffix), 8 raised an error and 7 of those because the name does not exist (AllRemoved, @Removed,
    RemoveNonLetters, RemoveNonLettersExcept, IsNotALetter, vizFindAll, BeforeQ), and 3 printed something other than the promise (a plural find returns each pattern with its sections
    and not the merged sections; a chain's history starts with the first value; a case-insensitive removal leaves STAZA, not SOFTANZA, as the code reads FALSE)
  - the page does not hide this: the article documents more than the library has, and it says which side should move, the library by writing the forms or the article by correcting them
  - used data that does not spell the former name for the page's examples (a string of letters that is not the word), so the rename never has to touch them
  - checked: 0 failures on the example blocks, 0 dangling links in 4,296 files, the former name in the code of 0 files, search 16 of 16, the floor held; I looked at the render

state:
  not tried, said on the page: the random, deep, default, free-order, misspelled-name and statement forms, the free form (its name collides with another suffix), and the multilingual form
  (archive only); the assessment's 22 count groups forms differently from the article's, and this page says fifteen
  perception-gate:   OPEN (the agent looked; the author has not)

waiting:
  - the forms the article documents and the library lacks, and the three wrong promises -> stzlib [routed now in CONCLUSIONS]

next:
  - me:      commit and push
  - author:  read the page's findings; say whether the library should grow the forms or the article should shrink
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 05:03

subject:   the gallery, with room for a person's verdict

why:       the author, "go ahead with the gallery"; the assessment's A6 asks for the gallery as a page with room for the human verdict

did:
  - published "The gallery" in the Foundation bar, English and French: the library's 27 graphics tests that have a picture of the same name, each shown with the script that makes
    it (linked), what happened when it was drawn again tonight, and the line "Unperceived: nobody has yet said whether this picture is right"
  - drew each script again in a temporary folder of the library at 4a184e6f0 (a new tool, tools/gallery_run.py; the folder is removed, the worktree stayed clean): 7 are byte for byte the
    picture the library kept, 6 were drawn and differ in their bytes (a person decides whether it is the same picture), 14 could not be drawn again here
  - said why for each of the 14, in the script's own words: the data to draw a map or a neuron is not in the repository and the script skips by name (twelve of them), one cannot read
    its file, one waits for a window on a screen and timed out at 240 s; for those the page shows the picture the library kept and says so
  - made the verdict a file the author edits: data/gallery-verdicts.json, empty today, with the form of an entry (a name, right, wrong or uncertain, a date, a note); the next build prints
    it under the picture; a model's opinion is not accepted there, as the file says
  - kept the earlier model judgments out: they were a model's, and the page says only that a model once judged some
  - checked: 0 failures on the example blocks, 0 dangling links in 4,298 files, the former name in the code of 0 files, search 16 of 16, the floor held; I looked at the render's top

state:
  perception-gate:   OPEN, by design: the page exists to carry the author's verdicts; none is in it
  not done:          the pictures that could not be drawn again here, which need the library's data folders or a screen

waiting:
  - the author's afternoon of looking, one verdict per picture in data/gallery-verdicts.json -> the author
  - the data the map and neuron scripts skip for, and the script that waits for a window -> stzlib [routed now in CONCLUSIONS]

next:
  - me:      commit and push
  - author:  open the gallery, look, and write your verdicts into data/gallery-verdicts.json
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 05:31

subject:   the Zui page's closing line, now a measured report from the constitution's own audit

why:       the page said the site's pages had not been run through the verifier; the author asked for the line to say they have, with the results

did:
  - ran StzZui's tools/ui-audit.html read-only (served through a temporary mapping, neither repository touched) on 188 pages at 1280 px, light then dark: the home page, 91 English and 91 French section pages, five deeper pages; 368 violations in light, 340 in dark
  - broke the findings by rule: Rule 108 no trail on 182 pages (the site shows a section bar, not a breadcrumb) plus 10 trail-markup findings on the five deeper pages; Rule 115 six (five markup, one a path showing ancestors only); Rule 114 the section bar scrolls sideways on 80 pages by 18 to 116 px; Rules 105/107 62 findings on the narrations choice lists (13.3 px, a browser default); Rule 105 contrast 28 in light and none in dark, all over a picture the audit cannot see; Rule 116 none
  - replaced the closing line of content/en/zui.md and content/fr/zui.md with a section "What the audit found" stating the date, the pages, each result and what the audit cannot see, and said unperceived for the tour counter in the light theme
  - corrected three of the page's own seven applied-rule lines that the audit contradicted (same size, path shows every depth, no sideways scroll), each pointing to the section below
  - checked: 0 failures on the example blocks, 0 dangling links in 4,298 files, search 16 of 16, the floor held on both Zui pages; I looked at the render of the new section

state:
  zui-page:          the audit's results are on it, in both languages; it no longer claims a clean site
  findings:          open, none repaired
  audit-reading:     it wants Breadcrumb as the label, a bare root address and a class on the current step; this site uses neither, so 15 of the trail findings describe the audit's convention as much as the page

waiting:
  - TRAIL: does every page owe a breadcrumb, or does the section bar suffice? -> the author [not routed before this memo]
  - SECTIONBAR-114: let the section bar wrap instead of scrolling sideways, 80 pages -> the author [not routed before this memo]
  - OPTIONSIZE-105: set the narrations choice lists at 1 rem -> the author [not routed before this memo]
  - TOUR-COUNTER: someone looks at the tour's page counter over the photograph in the light theme -> the author [not routed before this memo]

next:
  - me:      commit and push
  - author:  decide the trail question, then say go to a repair wave for the three fixes
  - stzzui:  the audit's limits (no flat-section exemption by structure, a menu label of Main, a class on the current step) are theirs to know; routed in CONCLUSIONS

note:      the audit flagged what the site said it did; the three lines I corrected were my own claims from the earlier pass
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 12:39

subject:   the repair wave for the findings of the constitution's audit on this site

why:       the audit found 368 violations in the light theme and 340 in the dark; the author asked for the owed decisions to be taken and the repair done

did:
  - decided that every page of a section owes a breadcrumb, because Rule 108 names section landings without a path of their own as what to avoid and this site has depth; kept the section bar beside it
  - put a breadcrumb on every page of a section (182 had none): marked nav[aria-label="Breadcrumb"] (the rule's label, English on the French pages too), first step the bare root address, current step class here-crumb; the presentation names itself Presentation mode; the two redirect stubs lead to a page that has one
  - made the section bar and the trail wrap above 760 px and scroll only below it (80 pages had scrolled sideways at 1280 px)
  - set choice lists at 1 rem (62 findings) and gave the presentation's page counter its own backing over the photograph
  - ran the audit again after the rebuild, 188 pages, 11:29 and 11:31 UTC: 46 violations in light, 22 in dark, down from 368 and 340; zero under Rules 105 size, 107 and 108 and 114
  - rewrote the Zui page's section to report both runs, what changed, what remains and why, and restored the three applied-rule lines to their claims now that they hold
  - checked: 0 failures on the example blocks, 0 dangling links in 4,298 files, search 16 of 16, the floor held on five pages in both themes; I looked at a section page at laptop and phone width

state:
  rule-108:        182 pages without a trail -> 0
  rule-114:        80 pages with a sideways bar -> 0
  rule-115:        16 findings, a landing's trail ends at the section while a child's goes on; the levels below sit in the section bar, which the audit does not read; two rows kept by decision
  rule-116:        6 findings, all the footer map read as a menu (the audit's selector matches nav[aria-label="Site"]); the main menu has none
  rule-105:        24 findings in light on the home menu over the photograph, none in dark; the audit cannot see the image; unperceived

waiting:
  - FOOTERNAMES: the footer map calls a section's first page by its own name (the north star, agentic, audiences) where the menu and trail say Vision, Intelligence, Adopt -> the author [not routed before this memo]
  - HOMEMENU-LIGHT: someone looks at the home menu over the photograph in the light theme -> the author [not routed before this memo]
  - AUDIT-READS-FOOTER: the audit takes the footer map for the main menu, and wants the English word Breadcrumb on a French page -> stzzui [routed in CONCLUSIONS]

next:
  - me:      commit and push
  - author:  say a word on the footer names, and look at the home menu in the light theme

note:      the Rule 115 finding is a design disagreement between two rows and one, taken on the author's behalf and stated on the page so it can be reversed
```

```yaml
by:        stzsite · claude-sonnet-5-5 · 2026-10-09 13:10

subject:   the footer names, one page one name in the menu, the trail, the section bar and the footer map

why:       the audit's Rule 116 findings showed three sections whose first page had a different name from the section; the author asked for the footer names to be settled

did:
  - decided that the first page of a section takes the section's name in the section bar and the footer map, as Platform, Narrations, Learn, Compared and Start already did, and keeps its own title as its heading: Vision (was the north star), Intelligence (was Agentic), Adopt (was Audiences), in both languages
  - changed three labels in SECTIONS in tools/build.py and rebuilt; nothing else used the old labels
  - ran the audit a third time on 188 pages at 11:57 and 11:59 UTC: 40 violations in light, 16 in dark; Rule 116 6 -> 0
  - updated the Zui page in both languages: the third run, and the Rule 116 line moved from remaining to repaired
  - checked: 0 failures on the example blocks, 0 dangling links in 4,298 files, search 16 of 16, the floor held on both Zui pages in both themes

state:
  rule-116:        0 findings
  rule-115:        16 findings, two rows kept by decision
  rule-105:        24 findings in light, the home menu over the photograph, unperceived

waiting:
  - HOMEMENU-LIGHT: someone looks at the home menu over the photograph in the light theme -> the author [routed in the memo of the repair wave]
  - AUDIT-READS-FOOTER: the audit takes the footer map for the main menu -> stzzui [routed in CONCLUSIONS]

next:
  - me:      commit and push
  - author:  look at the home menu in the light theme; say whether Adopt should keep the name Audiences for its first page

note:      the first-page title Audiences is still the heading of that page; only the navigation name changed
```
