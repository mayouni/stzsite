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

*(completed from the library's own documents: see section 2 below once filled)*

## 3. The design for Softanza

*(see section 3 below once filled)*
