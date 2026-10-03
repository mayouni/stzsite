# The Softanza documentation centre: what we learn from Wolfram, and what we do

*Asked by the author on 2026-10-01: "in the documentation centre of the domains and the
foundation features you need to learn from how Wolfram's documentation system is designed
(there are reference pages that are example driven, tutorial driven, etc.)". This file
records the study and the design that follows from it. Written by the stzsite desk.*

## 1. How the Wolfram documentation is built

Read on 2026-10-01 from reference.wolfram.com: the function pages for Select, StringReplace
and Plot; the guides String Manipulation, List Manipulation, String Patterns and Language
Overview; the tutorials Working with String Patterns and Lists; two workflow pages and one
workflow guide; the documentation front page; two version summaries. Described here in our
own words.

### Page types, each answering one question

| Page type | The reader's question | What it holds, in order |
|---|---|---|
| Function reference | What exactly does X do, in every form? | usage lines (one per calling form, code then one sentence) · details and options · examples · see also · tech notes · related guides · related workflows · history · cite |
| Guide | What exists for this area, and which one do I want? | one-paragraph pitch · 9 to 14 group headings, some linking to narrower guides · featured functions with a phrase each, then a run of further names · related tutorials, workflows, guides |
| Tutorial (tech note) | How does this mechanism work as a whole? | outline · prose interleaved with small tables and live input/output pairs · related links |
| Workflow guide | What tasks can I do in this domain? | headings, then task titles in the imperative |
| Workflow | How do I do this task? | imperative title and one-line purpose · 3 to 9 steps, each a sentence, code and its output · related workflows, functions, guides |
| Front page | What is the whole territory? | search · about 23 area tiles, each opening 12 to 18 guides · fast introductions · workflow guides · function index |
| Version summary | What changed in version N? | the functions new or improved, chained back to earlier versions |

### The examples of a function page

A fixed order, and a section with nothing to say is left out: Basic Examples, Scope,
Generalizations & Extensions, Options, Applications, Properties & Relations, Possible Issues,
Interactive Examples, Neat Examples. The count is printed in each heading ("Basic Examples
(6)"). Each example opens with one sentence saying what it shows, then the input and the
output it really produced. Typical counts: 3 to 6 basic examples, 13 to 33 for scope,
about 2 possible issues, about 1 neat example. Properties & Relations sets the function
against its siblings with runnable comparisons; Possible Issues documents the system's own
traps.

### Five principles

1. **Prove, do not assert.** Every claim about behaviour is a runnable example with its real
   output, and the pitfalls have their own section.
2. **One fixed anatomy per page type.** Same sections in the same order, empty ones left out,
   counts printed: the reader learns once where everything is.
3. **Examples grow in ambition and are labelled by purpose**, so each reader stops at the depth
   they need.
4. **Separate the reader's questions into page types, and link them in every direction**: a
   graph laid over a tree.
5. **Each page is a record with a history and a citation.**

## 2. What Softanza already has, and what it decided

Read on 2026-10-01 from the library at commit 0e72e2e2c, the softanza repository at aceb7fb,
stznarrations at 11c4529 and this site at 49bb866. No earlier document designs a
documentation centre on Wolfram's model; what exists is a set of decisions, each made for its
own reason, that together already answer most of section 1.

### Decisions already taken

| Decision | Where it is written | What it means for the centre |
|---|---|---|
| The docs are run, not written | the Atlas page *Documentation System*; `base/doc/narrations` | an example without its real output is not documentation |
| A narration stores no output | stznarrations `STUDY.md` and `POSITIONING.md`; `base/education/stzChapter.ring` | outputs are produced at publication, never pasted and left to rot |
| Five doors for five readers | `base/doc/stz-doc-system-overview.md` (2025-06): quickers, narrations, references, deep dives, FAQs | the page types exist in the library's own vocabulary |
| Examples for free, from the tests | `base/doc/design/stz-information-tagging-strategy.md` (2026-07), Layer 3 | every `#-->` line and every narrated `Then()` is an example waiting to be linked to its method |
| The library explains itself | `base/meta/stzSelfDoc.ring`: `Ask`, `HowTo`, `ExplainMethod` | the reference and the runtime answer come from ONE source, the doc-comments |
| Method names follow a grammar | `Verb()` mutates, `Verbed()` copies, `VerbQ()` chains, `CS` takes the case dial | Wolfram's *Properties & Relations* is mechanical here: the forms of one verb are its relations |

### What exists, counted

| Source | Count | Shape |
|---|---|---|
| test files with promised outputs | 7,653 `#-->` lines in 2,872 files | `? expr` then `#--> value`, mostly on the next line |
| narrated assertions | 9,660 `Then()` in 2,765 scenarios | label, actual, expected; prints PASS or FAIL |
| narrations | 1,436 `#-->` lines in 71 of 134 files | code fences, two output conventions |
| quickers (recipes) | 30 with an `# Intent:` line, 144 `#-->` lines | a task and its code: Wolfram's *workflow* |
| distinct methods with at least one example | 1,693 (1,347 of them in the site's reference) | scanned from tests and narrations, last call of each `?` line |
| `#@ eg` doc-comment examples | 1 | the tag exists; the parser ignores it |

### What does not exist yet

- **No committed index from a method to its examples.** `_StzExampleFor` builds one at
  runtime, but it reads only the same-line `code #--> output` form, so it skips the
  dominant two-line form; it keys by bare method name, so `Name()` of one class shows
  another's example; and it records where a name was first seen, not where the snippet came
  from. Fixing it is library work, routed to the stzlib desk.
- **No method page carries an example.** `data/reference.json` holds name, aliases and
  description only.
- **No page answers "how do I…?"** The quickers are that answer and are not published.

## 3. The design for Softanza

### Principles, kept and rethought

Kept from section 1: prove, do not assert; one anatomy per page type; examples graded by
purpose; page types linked in every direction.

Rethought, because Softanza already decided differently:

1. **An example is published only after it ran.** Wolfram ships outputs stored in its
   notebooks. Here every output on the site is produced by running the snippet inside the
   library at a named commit, and a snippet whose output differs from what its source file
   promised is left out, not corrected by hand. `tools/showcase_run.py` is the first
   instrument that does this.
2. **The pitfalls section is the library's refusals.** Wolfram's *Possible Issues* lists
   traps. Softanza's equivalent is stronger: what it refuses, and why (the empty string is
   never found; a model cannot act; an unsourced number is refused in a data story). Each
   area page shows them under "Rethought".
3. **Properties & Relations comes from the name grammar.** The forms of one verb (`Remove`,
   `Removed`, `RemoveQ`, `RemoveCS`) are listed together, folded under the base verb, as the
   guides already do.
4. **The site and the runtime answer from one source.** A method's explanation on the site is
   the doc-comment that `ExplainMethod` prints. Improving one improves the other; they can
   never disagree.
5. **Every area says what it kept and what it rethought.** No documentation system presents
   a domain this way; it is the reason the area pages open with the Softanza way.

### Page types

| Page type | The reader's question | Built from | State on 2026-10-01 |
|---|---|---|---|
| Documentation front (Learn › Documentation) | What is the whole territory? | the 28 areas, by theme | built |
| Area page (Platform › Areas › one area) | What did Softanza rethink here, and what does it look like run? | `data/heritage.json`, `data/showcase.json`, the Atlas ratings | built: heritage on 28 areas; runs where the snippets ran |
| Guide (one per area) | What exists here, and which function do I want? | the reference, grouped by leading verb, suffix forms folded | built, 28 × 2 languages |
| Class reference | What exactly does this class offer? | the doc-comments | built, 618 classes |
| Method entry with examples | What does this method do, shown? | the library's classic test files, harvested by the site and run before publishing | built 2026-10-02 for 1,254 methods (1,428 before the extension rule below) |
| How-to (workflow) | How do I do this task? | the recipes of `base/doc/quickers/recipes`, their `# Intent:` line as the title, run in one process (`tools/howto_run.py`) | built 2026-10-02: 28 of 30 published, each kept its promise; 2 show the former name |
| Narration (tutorial) | How does this idea work as a whole? | `base/doc/narrations`, run block after block in one process (`tools/narrations_run.py`) | built 2026-10-02: 8 narrations are pages, each block with its verdict; the other 126 are listed with the reason they stay on GitHub |
| Book (course) | Teach me, from the start | the Learning System chapters, run | linked |
| For agents (Learn › Ask the library) | How does a program ask the library? | `Ask`, `HowTo`, `ExplainMethod`, run and measured on the 28 recipes' intents (`tools/ask_run.py`); `llms.txt` and `agents/index.json` for an agent reading the site | built 2026-10-02 |

### The method entry, when it is built

Usage (each calling form, then its one-line description) · its forms (the suffix family) ·
**Examples (n)**, graded: *Basic* from narrations and quickers, *Scope* from the guards'
positive cases, *Possible issues* from their negative siblings · see also (the same verb's
forms, the class's other families) · the guide and the area page it belongs to. Every example
is run by the same instrument as the area showcases; the count in the heading is the count
that ran.

### The extension rule (ruled by the author, 2026-10-03)

A method name can end in extensions (`Q`, `CS`, `XT`, `Z`, `ZZ`, `U`, `IB`, `W`...). The author ruled it first for `Q`, then for all of them: an extension is a syntax variation of the same method, never another method (a `Q` form does what the method does and returns the object so a call can be chained; the library's own design document says the suffix DSL "generates 15,000+ method variants through composition"). So:

- **The reference lists a method once, and says which extensions exist for it and which do not.** `tools/qforms.py` holds the catalogue: 19 extensions the library documents (`Q`, `QQ`, `QQQ`, `QC`, `QRT`, `CS`, `ST`, `IB`, `D`, `XT`, `XTT`, `Z`, `ZZ`, `W`, `WF`, `F`, `Many`, `Except`, `U`), each with what it adds, the library file that documents it, and an example run in the library with the extension's letters highlighted (`tools/ext_examples_run.py`: composed from the usage the library documents, real method names, every one run; 19 of 19 ran). `QC` is documented but no method name carries it (the library provides it through a generic dispatch), so the per-method tables leave it out; `WXT` is listed by the library's parser but no method carries it and its call does not run, so it is not in the catalogue. The authority for the grammar is the library's forms document (`stz-functions-as-linguistic-expressions.md`) and the function-name grammar that the Haro spike declared from it as data (`stzv_v12.haro`: fluent `Q`, passive `ed`, parameter suffixes `cs st xt ib d z zz s w f many except`), read by the spike against the 595 definitions of `stzString.ring`. A name that is a method plus extensions, in any order and stacking (`FindSTZZ`, `ContentCSU`), is folded into the method; the language is case-insensitive, so a remainder written `FindSt` is resolved to the method `FindST`, which is itself `Find` plus `ST`. 4,677 of 26,949 names are folded; 22,272 methods are listed. Each row of a class page ticks or strikes the standard eight (`Q CS XT Z ZZ IB W U`) and adds any other that exists; an entry page carries the table of 18 with the names that carry each, the letters of the extension highlighted in each name (`FindMany`**CS**). A method defined in an ancestor to which a class only gives extensions is listed in that class as an inherited method (8 cases).
- **Passive forms are not extensions: decided, not asked.** `Removed` beside `Remove` does not do the same thing (one changes the object, the other returns a copy), and the forms document names it a form of its own, so both stay listed; the entry of a verb shows its passive twin among its forms.
- **Only documented extensions are folded.** `S` is left (seconds in `ElapsedS`, a start position in `NthStzS`: two meanings in six names); `X`, the statement form, is left (three of its four endings are unrelated words, `IsMacOSX`); `FF` and the prefixes (`@`, `rnd`, `viz`, `Deep`) are generic mechanisms of the forms document and not name suffixes of the reference. The other endings that look like extensions and are not documented stay listed, and the reference page names them with a count and an example: `N` (103 names, calendar), `R` (7), `AP` (7), `B` (5), `SF` (5) and a few more, many of them domain words (`ShowH`, `NormalizeNFC`, `ValidateDAG`). Adding one to the catalogue folds it at the next build.
- **One suffix carries two meanings.** `F` is "takes a function" in `WF` and `UpdateNodesF`, and "future" (it defers the action) in `UppercasingFQ`. The forms document's own principle (one meaning per suffix) is the Haro spike's finding too; the catalogue states both senses.
- **An example calls a `Q` form only to use what it returns.** `Q([1, 2, 3]).FilterQ('{ @item > 1 }').Content()` is right. `o1.FilterQ('{ @item > 1 }')` alone on a line is wrong: `o1.Filter(...)` does the job. The library's own examples and guards are never rewritten, so one that does it is left out of the entries and the showcases (2 of 1,346 examples, 5 of 75 showcase runs), and a narration that does it is shown as written with a note under the block (1 of the 8 published). The finding goes to the library.
- **Entries merge a method with all its forms.** An example of `FindCS` is an example of `Find`: 1,254 methods keep an entry (1,428 before the extension rule).

### Order of work

1. **D1, done 2026-10-01.** Guides for the 28 areas; heritage on every area page; the
   showcase runner and the runs it kept.
2. **D2.** The example index, made correct in the library (two-line form, class-qualified
   keys, the right file per snippet) — routed to the stzlib desk, since this desk does not
   edit the library.
3. **D3, done 2026-10-02.** Method entries with graded examples, run before publishing. Built site-side while D2 waits: `tools/harvest_examples.py` reads 3,401 classic test files of 32 topics, keeps 894 short ones that touch no file, input, clock or chance, and attributes each to the methods it shows; `tools/examples_run.py` runs them inside the library and keeps 558 whose output kept every promise, covering 666 methods; 269 printed something other than their file promised, a finding for the library. Widened the same day to the narrated suites: each scenario becomes an example, each assertion a printed line with its label as a comment, and the expected values are printed by the library in the same run and compared; 1,297 examples kept, covering 1,504 methods of 49 classes. Widened again to the course chapters (73 cells, 49 kept), and every example that shows the former language's name in its code or output is left out, as the site never names it; 1,428 methods of 59 classes kept an entry; the Q rule of 2026-10-03 (see below) folds that to 1,386 of 58.
4. **D4.** How-to pages from the quickers.
5. **D5.** Narrations as pages, and the page for agents.
