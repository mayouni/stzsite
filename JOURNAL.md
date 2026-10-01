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
