---
title: Le code
title_html: Le <i>code</i>
kicker: À côté de Python et de JavaScript
lede: Une plateforme se juge à ce que son code a l'air et à ce qu'il répond. Quatre courtes comparaisons, chaque côté exécuté le soir de la publication, chaque sortie telle qu'elle est sortie. Python et JavaScript sont d'excellents langages ; la question n'est pas qu'ils échouent, c'est ce qu'une ligne coûte et ce qu'elle répond.
description: Quatre courtes comparaisons entre Softanza et Python ou JavaScript, chaque côté exécuté le soir de la publication.
---

## Exact par défaut

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q(2).Power(64)</pre><pre class="o">18446744073709551616</pre></div>
<div class="side other"><div class="lbl">JavaScript, Node 22</div><pre>console.log(2 ** 64);</pre><pre class="o">18446744073709552000</pre></div>
</div>
<p class="ran">Exact par défaut : un entier est exact à toute taille. Le nombre de JavaScript est un flottant 64 bits, donc les derniers chiffres sont arrondis ; <code>9007199254740993</code> s'affiche <code>9007199254740992</code>. Exécuté le 2026-10-01 à 09:26.</p>

## Trouver d'abord, agir ensuite

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
<p class="ran">Trouver d'abord, agir ensuite. La question se dit comme elle se pense : trouver tout, retirer les doublons. Les réponses de Python sont justes aussi ; elles sont construites avec des mécanismes (enumerate, les clés d'un dictionnaire) que le lecteur doit décoder. Exécuté le 2026-10-01 à 09:26.</p>

## L'écriture d'un texte

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? Q("مرحبا بالعالم").Script()</pre><pre class="o">arabic</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre>import unicodedata
s = "مرحبا بالعالم"
print({unicodedata.name(c).split()[0] for c in s if not c.isspace()})</pre><pre class="o">{'ARABIC'}</pre></div>
</div>
<p class="ran">L'écriture d'un texte est une question à laquelle la plateforme répond directement. En Python on l'assemble à partir des noms Unicode de chaque caractère. Exécuté le 2026-10-01 à 09:26.</p>

## Une instruction dans votre langue

<div class="vs">
<div class="side stz"><div class="lbl">Softanza</div><pre>? @@( Naturally("Create a list with [ 5, 3, 5, 1 ] and remove its duplicates").Result() )</pre><pre class="o">[ 5, 3, 1 ]</pre></div>
<div class="side other"><div class="lbl">Python 3.13</div><pre># pas d'équivalent sans un modèle de langage externe</pre><pre class="o"></pre></div>
</div>
<p class="ran">Une instruction en anglais, français, arabe ou haoussa s'exécute. La couche naturelle est fondée sur un dictionnaire et locale : pas de réseau, pas de modèle, pas de clé d'API. Exécuté le 2026-10-01 à 09:26.</p>
