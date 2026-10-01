---
title: The code
title_html: The <i>code</i>
kicker: Beside Python and JavaScript
lede: The platform is judged on what its code looks like and what it answers. Four short comparisons, each side run on the night of publication, each output as it came out. Python and JavaScript are excellent languages; the point is not that they fail, it is what a line costs and what it answers.
description: Four short comparisons between Softanza and Python or JavaScript, each side run on the night of publication.
---

## Exact by default

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q(2).Power(64)</pre><pre class="o">18446744073709551616</pre></div>
<div class="side other"><div class="lbl">JavaScript, Node 22</div><pre>console.log(2 ** 64);</pre><pre class="o">18446744073709552000</pre></div>
</div>
<p class="ran">Exact by default: an integer is exact at any size. JavaScript's number is a 64-bit float, so the last digits are rounded; <code>9007199254740993</code> prints as <code>9007199254740992</code>. Run 2026-10-01 at 09:26.</p>

## Find first, then apply

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? @@( o1.FindAll("tea") )
? @@( o1.DuplicatesRemoved() )</pre><pre class="o">[ 1, 3, 6 ]
[ "tea", "rice", "fish" ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>items = ["tea", "rice", "tea", "fish", "rice", "tea"]
print([i + 1 for i, x in enumerate(items) if x == "tea"])
print(list(dict.fromkeys(items)))</pre><pre class="o">[1, 3, 6]
['tea', 'rice', 'fish']</pre></div>
</div>
<p class="ran">Find first, then apply. The question is spoken as it is thought: find all, remove duplicates. The Python answers are right too; they are built from mechanics (enumerate, a dictionary's keys) that the reader must decode. Run 2026-10-01 at 09:26.</p>

## The script of a text

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q("مرحبا بالعالم").Script()</pre><pre class="o">arabic</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>import unicodedata
s = "مرحبا بالعالم"
print({unicodedata.name(c).split()[0] for c in s if not c.isspace()})</pre><pre class="o">{'ARABIC'}</pre></div>
</div>
<p class="ran">The script of a text is a question the platform answers directly. In Python it is assembled from the Unicode names of each character. Run 2026-10-01 at 09:26.</p>

## An instruction in your language

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )</pre><pre class="o">[ 5, 3, 1 ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre># no counterpart without an external language model</pre><pre class="o"></pre></div>
</div>
<p class="ran">An instruction in English, French, Arabic or Hausa runs. The natural layer is dictionary-driven and local: no network, no model, no API key. Run 2026-10-01 at 09:26.</p>
