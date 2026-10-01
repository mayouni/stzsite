---
title: Les domaines de la plateforme
title_html: Les domaines <i>de la plateforme</i>
kicker: La plateforme
lede: Un seul moteur écrit en Zig, une seule langue, Haro, et vingt-huit domaines de calcul, des chaînes de caractères aux cartes, du son aux agents gouvernés, conçus pour fonctionner ensemble. Tout ce qui est ici tourne ; ce qui ne tourne pas encore porte sa note.
description: Les vingt-huit domaines de la plateforme Softanza : un moteur Zig, la langue Haro, et chaque domaine noté honnêtement contre les meilleurs de sa catégorie.
---

## Une plateforme de calcul unifiée

Softanza est une plateforme de calcul : un moteur, écrit en Zig, qui sait traiter des chaînes de caractères correctes au point de code, des nombres exacts à toute taille, des tables, des graphes, des cartes sur l'ellipsoïde, des images, du son, des réseaux de neurones, des agents gouvernés et la sécurité qui les tient ; une langue, Haro, qui se lit comme une phrase et met tout cela à portée d'une ligne ; et une loi, tout est jugé en s'exécutant, qui fait que ce que vous lisez ici a tourné.

<div class="figures">
<div class="figure"><b>28</b><span>domaines, 334 couloirs notés</span><a href="atlas.html">l'Atlas</a></div>
<div class="figure"><b>401</b><span>fichiers source Zig dans le moteur</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>5 384</b><span>méthodes sur une seule chaîne de caractères</span><a href="atlas/meta.html">atlas/meta</a></div>
<div class="figure"><b>134</b><span>narrations vérifiées par exécution</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/doc/narrations">doc/narrations</a></div>
<div class="figure"><b>5 822</b><span>commits sur la branche principale</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

## Les vingt-huit domaines

Chaque domaine a sa page : ce qu'un maker en fait, un exemple exécuté, ses couloirs notés contre les meilleurs de sa catégorie, ce qui se distingue et ce qui est dû. Les barres disent la note : <span class="chip strong">Strong</span> <span class="chip solid">Solid</span> <span class="chip partial">Partial</span> <span class="chip emerging">Emerging</span>.

<!--ATLAS-TALLY-->
<!--ATLAS-COMPACT-->

<p class="proof">Atlas version 21, relu le 2026-09-30 sur le commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> ; <a href="atlas.html">l'Atlas complet, avec ses cartes</a>.</p>

## La langue : Haro

<div class="cards">
<div class="card"><h3>Haro <span class="pill charter">en construction</span></h3><p>La langue de la plateforme : conçue pour qu'un agent l'écrive et qu'un humain la gouverne, sur une machine virtuelle à registres et un compilateur écrits en Zig, souverains. Sa charte est un brouillon v0.1 du 2026-09-26 qui attend la ratification de l'auteur ; la machine virtuelle et le compilateur existent et exécutent le code de la plateforme d'aujourd'hui. Ce site ne présentera jamais Haro comme disponible avant qu'il le soit.</p></div>
<div class="card"><h3>Le code de ce site</h3><p>Chaque bloc de code de ce site est du code Softanza tel qu'il tourne aujourd'hui sur la plateforme, exécuté le soir de la publication, sa sortie à côté. Il se lit comme une phrase : on trouve d'abord, on agit ensuite.</p></div>
<div class="card"><h3>Le moteur</h3><p>Quatorze modules GPU, neuf modules géographiques, six neuronaux, sept sonores, et les chaînes, les tables, les graphes, la cryptographie, la base de données, HTTP, les expressions régulières, les statistiques, l'algèbre linéaire, la transformée de Fourier : les familles se lisent dans les noms de fichiers du moteur, et c'est là qu'on les compte.</p><p class="proof"><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></p></div>
</div>

## Ce que « moteur » veut dire ici

Un exemple minuscule et réel : le moteur compte des caractères, pas des octets. Le mot arabe « سلام » fait huit octets et quatre lettres.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len("سلام")
? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q("SOFTANZA").BoxedXT([ :Rounded = TRUE ])</pre></div><div class="out"><div class="lbl">Sortie</div><pre>8
4
arabic
╭──────────╮
│ SOFTANZA │
╰──────────╯</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:11, Softanza au commit 0e72e2e2c</p>
