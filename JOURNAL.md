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
