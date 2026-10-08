---
title: From first principles
title_html: From <i>first principles</i>
kicker: On GitHub since 12 March 2022
lede: Softanza did not start as a wrapper around existing libraries. It started from the question of what programming should feel like when the human is the parser, and it rebuilt text, numbers, lists, tables, errors and documentation from there. The mission has not moved since 2018; the repository has been public since 12 March 2022.
description: Softanza's years of work from first principles, counted in the repository.
---

<figure class="diagram"><img src="../assets/img/diagrams/trajectory-en.png" alt="Commits per year on the main branch: 136 in 2022, 390 in 2023, 1,171 in 2024, 935 in 2025, 3,192 in 2026 up to 1 October. End of 2024: 348,000 lines of library, 63,000 of tests, 1,697 commits, no engine yet. On 2026-10-01: 531,000 lines of library, 179,000 lines of engine in Zig, 306,000 lines of tests, 501 scenario guards." width="1376" height="768"><figcaption>Counted in the repository on 2026-10-01: commits per calendar year on the main branch, and the tree as it stood on 31 December 2024 against the tree at commit 0e72e2e2c.</figcaption></figure>

By the end of 2024, after 1,697 commits by one author, the library held 348 thousand lines of code and 63 thousand lines of tests, all in the host language, with no engine yet. The author states that these lines were written by hand, before coding agents. Since then the Zig engine was written (179 thousand lines), the library grew to 531 thousand lines, the tests to 306 thousand, and the pace of commits tripled: that is what building with agents under a harness looks like, when the harness is Takamba and the law is that everything is judged by running.

<p class="proof">The counts: <code>git rev-list --count</code> at the last commit of each year on the main branch; lines counted over <code>*.ring</code> files outside <code>archive</code> folders, split between <code>base/test</code> and the rest, in the tree of <a href="https://github.com/mayouni/stzlib/commit/a395d09cd59a3439154ff1b899db04acce2dfb27">a395d09c</a> (2024-12-31) and of <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> (2026-09-30). The "written by hand" statement is the author's; the dates and sizes are the repository's.</p>

<p class="way"><span>The Softanza way</span> A platform written from first principles can obey one set of laws everywhere. A platform assembled from a hundred libraries cannot, because each library already chose its own.</p>
