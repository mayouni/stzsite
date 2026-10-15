# The structure of the site, rethought from the reader's side — 2026-10-15

The author, on a screenshot of the Adopt section (a main menu, a second horizontal row of nine pages that
wraps, a breadcrumb row): "This kind of deep menu options is not good for readability and for the reader to
make a knowledgeable mental model of the site content … radically rethink the information structure and menus
depth for all the site and documentation … put yourself instead of a reader (per profile), read the site and
identify any structural or ergonomic enhancement necessary."

Six readers went through the built site on 2026-10-15, read-only, each with one question: a newcomer tech
lead with ten minutes, a programmer trying it for an afternoon, the French-speaking CTO of a bank in Niamey,
a French-speaking teacher in Niamey, a functional and data analyst who designs screens, and an AI coding
agent reading the site as a machine. Their full reports are summarised in the memo of 2026-10-15
(`softanza\memos\2026-10-15.md`). This file is the decision that comes out of them.

## What the six found, in one table

| finding | readers who hit it | the rule it breaks |
|---|---|---|
| three stacked horizontal rows (menu, section bar, trail) plus a left bar on some pages; the section bar wraps | all six | Zui 120, 27 |
| the trail never names the page you are on, and on family pages names the wrong parent | 5 | Zui 108, 115 |
| one page, several names (Adopt / Who it is for / Audiences / Offering page; Vision / The north star; The craft / How Softanza is written …) | 5 | Zui 116 |
| a family's head stands in its own left bar as a child of its child (Platform of platforms, Applications) | 3 | Zui 116 |
| the decisive facts sit far from the reader who needs them (the CTO's proof in Vision and Intelligence, the teacher's machine needs only on Start, the analyst's "how to declare" seven pages deep under The foundation) | 4 | Zui 116 |
| the same thing told three or four times (the three projects; the audience grid; the education doors and ladder; the same example on several pages) | 5 | Zui 123 |
| seven surfaces answer "how do I do X" and none says which to use when; the site's own search is never named | 2 | — |
| each area is two pages in two sections (atlas under Platform, guide under Learn) that disagree | 3 | Zui 116 |
| contradictions between pages (Narrations "under Learn"; 134 vs 135; a book "with no public address" beside a linked one; the reader opening in English from French pages; contacts that disagree) | 5 | — |
| machine readers: no runtime line in llms.txt, no signatures, global functions not indexed | 1 | — |

## The decision

**Two navigation levels on screen, never more: a short horizontal main menu, and a vertical rail beside the
page.** The second level turns vertical (Zui 120). The rail shows the section's pages, and under the page you
are in, its own pages nested: the whole branch is visible from anywhere in it (Zui 115), and nothing scrolls
sideways (Zui 27, 114). The trail sits at the top of the page itself, not in the sticky header, and always ends
on the page you are on (Zui 108). On a narrow screen the rail folds into the "Where you are" line under the
menu.

**Seven sections, cut by the reader's question, not by the topic of origin:**

| menu | the question it answers | pages (addresses unchanged) |
|---|---|---|
| Platform | what is it? | Platform · The areas · Build an application (the world, many worlds as one platform, the host, from the editor to the device, surfaces, your first application, the store, conversations, the environment, seven languages) · Pictures and data (visual by default, the gallery, four widths, the graph beneath) · Agents that cannot hurt you (security, Aïcha, coding agents) · How it is built (architecture, depth, the code, the foundation, reach, the declared languages) |
| Proof | is it real? | What is built (proven) · The estate, stage by stage · Forged in projects · Proving grounds · Real applications · Customers · Compared |
| Vision | why does it exist? | The north star · Twelve principles · From first principles (roots, why Softanza leaves Ring, born in Africa) · Sovereignty · Wise coding · Language of languages · Refinement · Zui constitution · The Softanza book |
| Learn | how do I learn it? | Learn · How Softanza is written (seven design goals, pattern languages, the grammar of functions, the Softanza way, natural and executable, by example, the Softanzuter, innovations) · The interactive course · Narrations (the three series) · Education (learn by yourself, teach, run a programme, for institutions, what is proved) · Glossary |
| Reference | how do I do this exact thing? | Reference · How-to · Documentation (the area guides) · Ask the library · For agents |
| Organisations | should my organisation use it? | Audiences · Journeys · Solutions · Editions · Partners · Certification |
| Start | how do I begin? | Start |

**One name per page**: the rail, the trail and the footer call a page by its title; the first page of a section
is called by the section's name.

**Every address stays.** Pages move between sections, never between addresses; the AYOUNI Press readers link
here by relative address, and a page that disappears in a later wave leaves a redirect, as `pedagogy.html` and
`teaching.html` already do. The press desk is told before any address changes.

## The waves

1. **The chrome and the tree** (this commit): the rail, the trail in the page, the seven sections, the stale
   contradictions the readers named (the narrations pointer, the counts, the book's address, the reader's
   language from French pages).
2. **Merges, with redirects**: one page per area (atlas and guide); the three projects told once; one
   Education hub (Education and For institutions); one page for organisations ordered by the CTO's five
   questions; How Softanza is written cut to what runs; the home page opening on one sentence and its stage.
3. **The machine face**: a runtime block at the top of llms.txt, a signature per method and the global
   functions in agents/index.json, a stable address for every method.
4. **Labels that say what is inside**: rename the pages whose titles tell a reader nothing (The code, Depth,
   Reach, Four widths, The craft), each with its redirect.

## The style of the examples, while the pages are rewritten

The author's ruling relayed by the Softanza book session, 2026-10-15: the declarative scene with braces is the basis
of the style (`Q(value) { Method() ... }`, `oObject { ... }`), used for three or more calls on one object; a chain
where the thought is one sentence; the classic `o1.Method()` form shown too; the natural form `Naturally(...)` where it
runs (on text, not on numbers, at library commit 93d7a39bd). `@@()` stays in every example until the Ring++ session
reports that the expressive print is Haro's default (PRINT-EXPRESSIVE): the site's blocks are run and judged, and
without `@@()` the former host prints a list one item per line. The Softanza book's chapter 5 shows the four forms
side by side. Every example a wave rewrites follows this, and is run again before it is shown.
