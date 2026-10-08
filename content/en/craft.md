---
title: How Softanza is written
title_html: How Softanza is <i>written</i>
kicker: The craft of Softanza code
lede: Softanza is written so that a name tells you what a call does, a condition can travel inside an argument, a loop gives way to a metaphor, and the library can explain itself. These are conventions held across thousands of methods. This page shows each one running.
description: How Softanza code is written: the grammar of its names, the small languages inside its arguments, the four metaphors that replace loops, its conventions, and a library that explains itself.
---

## A name is a sentence {#names}

A method's name is read like a short sentence: the verb says what happens, and the form of the word says how. `Remove()` changes the object. `Removed()` returns a changed copy and keeps the original. `RemoveQ()` changes it and hands it back, so the sentence can go on. Suffixes add meaning the same way in every class: a case dial, a condition, extended options, positions or sections, a start position.

<figure class="diagram"><img src="../assets/img/diagrams/forms-en.png" alt="Left, emphasised: the forms of Remove. Remove() changes the string; Removed() returns a changed copy; RemoveQ() changes it, and chains; RemoveCS() with a case dial; RemoveW() where a condition holds; RemoveXT() with extended options. Right: suffixes are words. ed, a copy, the original kept; Q, keep chaining; CS, case sensitivity; W, a condition written inline; XT, extended; Z and ZZ, positions and sections; ST, from a start position." width="1376" height="640"><figcaption>The eight forms of Remove in the string class, read from the reference this site generates from the library.</figcaption></figure>

The forms are a system, not a habit: the library reads its own names with a grammar, and an audit lists every verb that lacks one of its three main forms. That is why the string class holds 2,117 methods of its own and the list class 1,583, and why a reader who knows one verb already knows its family.

<!--SHOWCASE:craft:1,2-->

- **A verb, never a bare noun.** A name says what the call does: `AddCircle()`, not `Circle()`.
- **Calm verbs.** Remove, Clear, Close; never Kill or Destroy.
- **Data or object, said by the name.** A plain form returns data; the `Q` form returns the object, so a chain never guesses what it holds.
- **A parameter's name says its type.** `pc` for text, `pn` for a number, `pa` for a list, `pb` for a yes or no.

## Small languages inside the arguments {#languages}

Some arguments are not values but sentences in a small language. A condition such as `"{ @item > 5 }"` is compiled by the engine and checked against every item, without ever evaluating code: it is safe even when it comes from a user or a file. A named parameter such as `:With = "coffee"` or `:StartingAt = 3` makes a call read like a sentence. Patterns over lists, numbers, tables and time follow the same idea, and near-natural chains let a line of code read as English.

<!--SHOWCASE:craft:3,4,6-->

<p class="way"><span>The Softanza way</span> A small language inside an argument says what you want, and the library decides how to get it. The loop, the index and the temporary variable disappear from the page.</p>

## Four metaphors instead of loops {#metaphors}

A loop hides which move it is making. Softanza names the four moves, and a task is decomposed into them instead.

<div class="cards">
<div class="card"><h3>The walker</h3><p>Moves through positions: it knows its whole route before it moves, which steps it will visit, which it will skip, and where it stands. It lives in the max layer.</p></div>
<div class="card"><h3>The checker</h3><p>Asks yes or no questions about the items: all of them, any of them, none of them, where a condition holds.</p></div>
<div class="card"><h3>The yielder</h3><p>Produces new data from the old: it filters, transforms and reduces, and its core runs in the engine.</p></div>
<div class="card"><h3>The performer</h3><p>Acts in place: it changes the items it is told to change, where a condition holds.</p></div>
</div>

<!--SHOWCASE:craft:5-->

## Fourteen rules of writing {#rules}

Everything above is one grammar. Written out as rules, it is fourteen, and a line of code that follows them reads as the thinking behind it. These are readings of the library's own code and articles, stated as rules. Each rule's sample is written below it, not run; the runs that follow show several of them working.

<!--RULES-->

<!--SHOWCASE:craft:8,9,10,11-->

<p class="way"><span>The Softanza way</span> The same rules serve the seven steps of the mental model, one rule or two at each step. <a href="way.html">The next page</a> sets the two side by side.</p>

## Conventions {#conventions}

- **Positions start at 1, and 0 means not found.** People count from one; so does every layer, the engine included.
- **Characters, not bytes.** A length or a position counts the letters a person reads, in any script.
- **The engine first.** Substance goes into the engine, written once, and the language above it is its face.
- **`Q()` turns a value into an object.** A plain value stays data; `Q("text")` becomes a string object with its thousands of methods.
- **Find first, then apply.** Where is it, and what do I do there: the same two steps in every area.
- **The same verbs for every structure.** What works on a string generally works on a list.
- **A printed true is 1.** The console prints a true answer as 1 and a false one as 0, which is why the outputs on this site read that way.

## A library that explains itself {#selfdoc}

Each method carries, right above its definition, one line saying what it does in the user's words, and optional tags: other names a reader might use, the shape of the answer, an example, related methods. A real one, from the text class:

<pre># The overall tone/mood of the text as "positive", "negative", or "neutral".
#@ aka  mood, emotion, feeling, attitude, opinion, how positive or negative
#@ out  string: "positive" | "negative" | "neutral"
#@ eg   Q("The food was terrible.").Text().Sentiment()   #--> "negative"
#@ see  SentimentScore, IsPositive, IsNegative
def Sentiment()</pre>

A harvester reads these lines, the section titles and the examples promised in the tests. Every object then answers `Ask()`, `HowTo()` and `ExplainMethod()` from them, without any model: the answer is the library's own, and a method that does not exist is refused by name.

<!--SHOWCASE:craft:7-->

<p class="proof"><b>in construction</b> The convention is fully used on few methods so far: 106 lines name other words for a method, and the harvester does not yet read the example and answer-shape tags. The reference on this site is generated from what exists.</p>

<p class="proof">Sources: the forms are described in the narration <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-functions-as-linguistic-expressions.md">stz-functions-as-linguistic-expressions.md</a>; the condition language is compiled by <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/engine/src/expr.zig">engine/src/expr.zig</a>; the doc-comment convention is set in <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/design/stz-information-tagging-strategy.md">stz-information-tagging-strategy.md</a>. Method counts read from the library at commit 010743cce.</p>
