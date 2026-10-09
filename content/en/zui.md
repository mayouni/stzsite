---
title: Zui constitution
title_html: The Zui <i>constitution</i>
kicker: A law a machine can refuse to violate
lede: Interfaces are decaying in the agentic age, and not for lack of capable generators: the generators reproduce, at machine speed, every inherited assumption of the corpus they learned from. Softanza's answer is Zui, a constitution for interfaces: **122 rules** in 31 sets under 7 articles, **22 verbs** in 6 families, 6 operator rights, and a verifier that checks a page against the law.
description: The Zui constitution: 122 rules and 22 verbs for interfaces, against the chaos of vibe-coded applications.
---

## The chaos it answers {#chaos}

Machines now generate interfaces faster than anyone can review them, and a generator reproduces every habit of the pages it learned from: a menu that hides its entries, a button labelled with a state instead of an action, text set small to look elegant, a page that glides when you asked to jump, an error that blames the person who met it. Each habit looks harmless alone.

Together they make the chaos of vibe-coded applications, where every screen behaves differently and nobody can say why. Guidelines did not stop it, because a guideline asks for taste and a generator has none. Zui is written as law instead: every rule names what to avoid, what to do, why, and who enforces it, and a verifier refuses a page that breaks a rule a machine can check.

## The law {#law}

<div class="cards">
<div class="card"><h3>The seven articles</h3><p>Calm · Intent over mechanics · Visible state · Reversibility · Predictable authority · Operator primacy and vibes · Amendment. Every rule records who enforces it: a judgment, a tool, or a machine.</p></div>
<div class="card"><h3>The twenty-two verbs</h3><p>Orienting: discover, understand, locate. Attention: focus, filter, compare. Information: read, scan, scroll, zoom. Selection: select, highlight, preview, mark. Action: act, confirm, cancel, undo. Continuity: pause, resume, retry, exit. Every element of an interface must trace to at least one; an element that traces to none is a structural error. The grammar is closed: a new medium adds renderings, never verbs.</p></div>
<div class="card"><h3>Five rules, as written</h3><p><b>Cognitive mercy:</b> the interface must never compete with the user's thinking. <b>Non-accusatory pathfinding:</b> every error message contains a verb that tells the user how to fix it. <b>The undo covenant:</b> every destructive action has an instant, one-click undo for ten seconds. <b>The legibility floor:</b> main reading text is at least one rem, never lighter than 4.5:1 against its background; secondary text may be quieter, never less legible. <b>The verb on the button:</b> every action control states the action it performs.</p></div>
<div class="card"><h3>Born from defects</h3><p>Every rule numbered above 104 was canonised from a defect an agent produced while building a real site, under explicit instruction to be careful. Without a machine-checkable law, the defects regenerate endlessly. Article V: an intelligent agent is an actor under this law, never an authority above it.</p></div>
</div>

<p class="proof">Constitution version 3.11 of 2026-08-16; the verifier passes 50 of 50 conformance fixtures and conforms at level 4; two consuming products are pinned to it. Read in the constitution's repository on 2026-10-01; that repository is not public yet, and this site will link it the day it is. This site itself follows the legibility floor: its reading text is 19 pixels, and nothing is set small to say it matters less.</p>

<p class="way"><span>The Softanza way</span> Someone has to write the principles down in a form a machine can refuse to violate. Guidelines did not stop the decay of interfaces. A law can.</p>

## This site, under the law {#site}

This site is built under the constitution, and its build checks what a machine can check. The rules it applies, each one where you can see it:

- **One reading size (Rule 107).** Every text you read here is set at the same size, except the choice lists of the narrations page, which the audit found smaller (below); a title is larger, and nothing is set smaller to say it matters less.
- **The legibility floor (Rule 105).** Every pair of text and background colours is measured by the build, which stops if one falls below its threshold; the words over the photograph on the home page are measured over its brightest part.
- **Motion reports, it never decorates (Rules 112 and 17).** Nothing glides, fades or bounces: a link takes you where you asked, at once.
- **The path shows every depth (Rules 108 and 115).** Under the main menu, every page of the current section is listed and the one you are on is marked; both stay on screen while you read. It is a section bar, not the breadcrumb the audit looks for, and the audit faults it (below).
- **Nothing floats over the reading (Rule 110).** The bars hold their own space; nothing hovers over the text or the pictures.
- **No sideways scroll (Rules 14 and 95).** Code wraps inside its block, tables stay tables at every width, and every diagram has a second drawing made for a phone. The section bar under the menu is the exception: it scrolls sideways on 80 pages at 1280 pixels (below).
- **The verb on the button (Rule 106).** The display buttons at the foot of every page say what they do.

## What the audit found {#audit}

<p class="proof"><b>in construction</b> The constitution's own audit, the tool that measures Rules 105, 107, 108, 114, 115 and 116 on the rendered page, was run on this site on 2026-10-09, at 04:18 UTC in the light theme and 04:21 UTC in the dark one, at 1280 pixels. It read 188 pages: the home page, all 91 English and all 91 French section pages, and five deeper ones (a narration, two reference pages, a guide and an atlas page), not the thousands of reference and narration pages in between. It found <b>368 violations in the light theme and 340 in the dark one. This site is not clean.</b></p>

- **Rule 108, a trail from the root: 182 pages have none.** They carry the section bar under the menu, which lists every page of the section and marks the one you are on, and not a breadcrumb. The constitution exempts a flat site, and this one is not flat: a section, a page, then narrations and reference pages that do carry a trail. The five deeper pages carry one, and the audit faults it too: it wants the trail labelled as a breadcrumb, the first step to be the bare root address and the current step to carry its own class, where this site labels it "You are here", links the root with its language and marks the current step with the standard attribute. Those are fifteen findings, ten here and five under Rule 115, that say as much about the audit's reading as about the page, and they are counted, not hidden. Whether the section bar is enough, or every page owes a trail, is the author's to decide.
- **Rule 114, room before scrollbars: the section bar scrolls sideways on 80 pages.** At 1280 pixels it overflows by 18 to 116 pixels while up to 98 pixels of page sit free beside it. The line above on sideways scroll holds for code, tables and diagrams, not for this bar.
- **Rules 105 and 107, the floor: the choice lists of the narrations page are set at 13.3 pixels** in both languages, the size a browser gives a list of choices, which is 62 findings. The reading text everywhere else cleared 16 pixels.
- **Rule 105, contrast: 28 findings in the light theme, none in the dark one, all on text laid over a picture:** the menu over the photograph on the home page and the page counter over the photograph on the tour. The audit cannot see an image. It measured the colour beneath the picture, so its 2.22 to 1 and 1.12 to 1 are not what a reader sees. No person has yet looked at the counter on the tour in the light theme: that is unperceived, not passed.
- **Rule 115, the path reads the same at every step: 6 findings,** five of them the trail markup described above and one a path that shows its ancestors and not what lies beneath it. **Rule 116, the menu against the tree: no finding.**

What this audit cannot see: an image, a state that needs a hand (hover, focus, a menu opened), any width but 1280 pixels, and any page it was not given. A model read its report and wrote this; a clean report would still prove agreement with a rule, not that a person finds the page right. The findings are open, none is repaired yet, and the audit is run again on the day they are.
