---
title: The Atelier
title_html: The <i>Atelier</i>
kicker: The library's own checks, recorded
lede: The Atelier is a program that runs the library's own tests, one assertion at a time, and records the verdict of each. This page explains it and links its static edition, a set of read-only pages that show what was recorded at one commit of the library. Nothing on them runs.
description: The Softanza Atelier and its static edition: the library's own assertions, judged and recorded at one commit, the five states of a test line shown apart, and every check citable by commit and identity.
---

## What the Atelier is {#what}

The Atelier is a program that runs the tests of the Softanza library and records what each one found. Each test file of the library tells a short story: a few calls, each followed by a line that states what the library must answer. The tests call such a line a *Then line*. A **check** is one of these lines taken whole: its description, the two values it compares and the helpers its file defines for it. The expected value is always the one written by the author of the test, never one chosen by the Atelier.

To judge a check, the Atelier loads the library in a running program, calls the code of the check, and compares the answer with the expected value. The verdict is one of three: the check passed; it failed, with what was expected and what came; or it ended in an error.

On a machine that has the library, the Atelier can also run live. It answers only to the address 127.0.0.1, which is that machine alone. This site cannot run it, and no page of the site runs code. What a site can show is what was recorded.

## The static edition {#edition}

An edition is a folder of pages built from the data that one commit of the library carries: the checks grouped by domain, with a search box; the coverage of whole test files; and one page for each check, found by its identity. Everything is static, so reading it needs no server and fetches nothing.

The figures below are the edition's. Each is a statement about the commit named under them and about no other, and the edition itself says the same.

<!--ATELIER:counts-->

## Two different counts {#counts}

The first four figures count checks: the Then lines that the Atelier runs one by one in a live program. The next five count every Then line of the narrated test files, which the Atelier runs whole: a file goes from its first line to its last, and a judge compares what it printed with the claims found in it.

Each Then line ends in one of five states. They are shown apart and never added together:

- **kept**: the line was judged, and the answer was the expected one.
- **diverged**: the line was judged, and the answer was different.
- **unreached**: the file broke, or never started, before the line.
- **unjudged**: the file finished without walking through the line.
- **unperceived**: the line concerns something a person must see or hear, and nobody has yet said what they perceived.

Adding these into "pass" and "fail" would hide the lines that were never reached, which are not failures and are not successes either.

## Citing a check {#cite}

Every check has an identity: its test file, a `#`, and eight hexadecimal digits taken from its text. Joined to the commit at which it was recorded, it makes a citation, written `commit:identity`. A citation without its commit is not a citation, because a verdict is true of one commit only. The resolver refuses a citation whose commit is not the one that was recorded.

Where a page of this site says something that the library's own tests also say, it cites the check. The example below is a check of the string class: the page [Proven](proven.html#checks) cites three more.

<!--CITE:string/00_string_narrated#87ed4de2-->

## What this page does not do {#limits}

- It runs nothing: no playground and no button that runs code. A hosted playground needs a sandbox, and none exists yet.
- It does not change a page's stage. A citation says that a check passed at a commit; it does not say that a page is finished.
- It does not hide what is not known. A line that nobody has reached or perceived stays in its own state.
