---
title: Le moteur et ses visages
title_html: Le moteur <i>et ses visages</i>
kicker: La plateforme
lede: La substance vit dans un moteur écrit en Zig. Les langages sont ses visages : Ring est celui que l'on écrit aujourd'hui, Ring++ est le pont, Haro est la langue d'après, au stade de la charte.
description: L'architecture Softanza : un moteur Zig de centaines de modules, Ring comme visage d'aujourd'hui, Ring++ comme pont, Haro au stade de la charte, et l'Atlas qui note chaque domaine.
---

## Le moteur est le produit

Chaînes de caractères, tables, graphes, géographie, GPU, son, réseaux de neurones, cryptographie, base de données, HTTP, expressions régulières, statistiques, algèbre linéaire, transformée de Fourier : tout cela est écrit en Zig, dans un seul moteur, et exposé aux langages par une interface C. Le langage que vous tapez est un visage ; ce qui calcule est le moteur.

<div class="figures">
<div class="figure"><b>401</b><span>fichiers source Zig dans le moteur</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>5 822</b><span>commits sur la branche principale</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
<div class="figure"><b>134</b><span>narrations vérifiées par exécution</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations">doc/narrations</a></div>
<div class="figure"><b>2</b><span>dépôts publics, GitHub et Codeberg</span><a href="https://codeberg.org/MAyouni/stzlib">codeberg.org/MAyouni/stzlib</a></div>
</div>

Quatorze modules GPU, neuf modules géographiques, six neuronaux, sept sonores : ces familles se lisent dans les noms de fichiers du dossier lié ci-dessus, et c'est là qu'on les compte.

## Ring, Ring++, Haro

<div class="cards">
<div class="card"><h3>Ring <span class="pill built">aujourd'hui</span></h3><p>Le visage que l'on écrit aujourd'hui. Un langage petit, lisible, multiparadigme, dont la bibliothèque Softanza fait une phrase : <code>o1.ContainsDuplicates()</code> se lit comme il s'écrit. Ring n'est pas emporté comme exécutant ni comme gouvernance ; sa simplicité et son expressivité, oui.</p></div>
<div class="card"><h3>Ring++ <span class="pill built">le pont</span></h3><p>Une machine virtuelle à registres et un compilateur, en Zig, « souverains, pas nouveaux », qui exécutent le code Ring existant. Ils sont jugés contre la machine de Ring 1.27, prise pour oracle. La bibliothèque Softanza, plus de trois cent mille lignes, en est la spécification de compatibilité.</p><p class="proof"><a href="https://github.com/mayouni/ringpp">github.com/mayouni/ringpp</a></p></div>
<div class="card"><h3>Haro <span class="pill charter">charte</span></h3><p>La langue d'après Ring, conçue pour qu'un agent l'écrive et qu'un humain la gouverne, sur la machine virtuelle de Ring++. Sa charte est un brouillon v0.1 du 2026-09-26 qui attend la ratification de l'auteur. Rien n'est construit : ni analyseur, ni compilateur. Ce site ne présentera jamais Haro comme disponible.</p></div>
</div>

## L'Atlas : chaque domaine noté, honnêtement

L'Atlas Softanza est le relevé de ce que la bibliothèque sait faire, groupe par groupe, couloir par couloir, avec quatre notes : <span class="chip strong">Strong</span> <span class="chip solid">Solid</span> <span class="chip partial">Partial</span> <span class="chip emerging">Emerging</span>. Il montre ses lacunes ; c'est ce qui rend ses forces crédibles.

<div class="figures">
<div class="figure"><b>28</b><span>groupes : 25 groupes de modules et 3 systèmes transversaux</span></div>
<div class="figure"><b>334</b><span>couloirs notés</span></div>
<div class="figure"><b>101 · 129</b><span>Strong · Solid</span></div>
<div class="figure"><b>68 · 36</b><span>Partial · Emerging</span></div>
</div>

<p class="proof">Atlas version 21, relu le 2026-09-30 sur le commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> : <a href="https://claude.ai/artifact/FCeuCNfcZepUDJLxsynwFB">l'Atlas en ligne</a>. Les pages de l'Atlas seront portées sur ce site dans la version suivante.</p>

## Ce que « moteur » veut dire ici

Un exemple minuscule et réel : Ring compte des octets, le moteur compte des caractères. Le mot arabe « سلام » fait huit octets et quatre lettres.

<div class="run"><div><div class="lbl">Ring</div><pre>? len("سلام")
? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q("SOFTANZA").BoxedXT([ :Rounded = TRUE ])</pre></div><div class="out"><div class="lbl">Sortie</div><pre>8
4
arabic
╭──────────╮
│ SOFTANZA │
╰──────────╯</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:11, Ring 1.27, Softanza au commit 0e72e2e2c</p>
