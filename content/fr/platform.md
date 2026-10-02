---
title: Plateforme
title_html: La <i>plateforme</i>
kicker: Un moteur, vingt-huit domaines
lede: Softanza est une seule plateforme de calcul. Un moteur, écrit en Zig, traite le texte, les nombres exacts, les tables, les graphes, les cartes, les images, le son, les réseaux de neurones, les agents gouvernés et la sécurité qui les entoure. Une langue, Haro, en construction, doit mettre tout cela dans une phrase. Tout ce qui est sur cette page a été exécuté le soir de la publication.
description: La plateforme Softanza en mots simples : ce qu'elle est, ce que fait le moteur, et la langue, Haro.
---

## Ce que c'est, en mots simples {#what}

La plupart des logiciels sont assemblés à partir de nombreuses bibliothèques séparées, écrites par des gens différents, chacune avec ses règles et son calendrier de versions. Softanza prend l'autre route. C'est **un seul** corps de code où chaque domaine, du comptage des lettres d'un mot arabe au dessin d'une carte du Niger ou à un agent qui propose un changement, obéit aux mêmes lois.

<p class="way"><span>La manière Softanza</span> Tout est déclaré, tout est jugé en s'exécutant, et rien n'est cru. Une page de ce site, un chapitre du cours, un garde dans le dépôt : chacun exécute son code quand on le lit ou quand on le construit. Ce qui n'a pas tourné n'est pas montré.</p>

<div class="figures">
<div class="figure"><b>28</b><span>domaines de calcul, 334 couloirs notés</span></div>
<div class="figure"><b>401</b><span>fichiers source du moteur Zig, 179 000 lignes</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/engine/src">engine/src</a></div>
<div class="figure"><b>531 000</b><span>lignes de bibliothèque, 1 227 fichiers, hors tests et archives</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base">base/</a></div>
<div class="figure"><b>501</b><span>gardes narrés, 306 000 lignes de tests</span><a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/test">base/test</a></div>
<div class="figure"><b>618</b><span>classes, 24 774 méthodes, chacune expliquée par la bibliothèque elle-même</span></div>
<div class="figure"><b>5 824</b><span>commits sur la branche principale depuis le 12 mars 2022</span><a href="https://github.com/mayouni/stzlib/commits/main">commits/main</a></div>
</div>

<p class="proof">Compté le 2026-10-01 dans le dépôt au commit <a href="https://github.com/mayouni/stzlib/commit/0e72e2e2c">0e72e2e2c</a> : les fichiers <code>*.ring</code> sous <code>libraries/stzlib</code> hors dossiers <code>archive</code>, séparés entre <code>base/test</code> et le reste ; les fichiers <code>*.zig</code> sous <code>engine/src</code> ; les gardes sont les fichiers de test dont le nom finit par <code>_narrated.ring</code>. Le nombre de commits est lu sur la branche principale le même jour.</p>

## Ce que « moteur » veut dire ici {#engine}

Sous la langue, il y a un programme écrit en Zig, un langage système, compilé en code machine. Il fait le travail lourd : il compte des caractères et non des octets, garde les entiers exacts à toute taille, dessine les images au pixel, exécute l'inférence neuronale et surveille l'horloge. La langue que vous écrivez est son visage.

Un exemple petit et réel. Le mot arabe « سلام » fait huit octets et quatre lettres. Beaucoup d'outils répondent huit. Le moteur répond quatre, et connaît l'écriture.

<div class="run"><div><div class="lbl">Softanza</div><pre>? Q("سلام").NumberOfChars()
? Q("مرحبا بالعالم").Script()
? Q(2).Power(64)
? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>4
arabic
18446744073709551616
┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26 depuis <code>libraries/stzlib</code>, Softanza au commit 0e72e2e2c, en 6,6 secondes chargement de la bibliothèque compris</p>

<p class="way"><span>La manière Softanza</span> La substance vit dans le moteur, et la langue en est un visage. Une seconde langue, ou une seconde machine, partage le même moteur par une seule interface C : rien n'est écrit deux fois et rien ne diverge.</p>

## La langue : Haro {#haro}

Haro est la langue de la plateforme. Elle est conçue pour qu'un humain la lise comme une phrase et qu'un agent l'écrive sous une grammaire qui interdit les phrases malformées. Elle n'est pas achevée : sa route est une machine virtuelle à registres et un compilateur écrits en Zig, vers lesquels le code de la plateforme est en train de passer. Sa charte, un brouillon du 26 septembre 2026, attend la ratification de l'auteur.

<p class="proof"><b>en construction</b> Ce site ne dira pas que Haro est disponible avant qu'il le soit. Chaque bloc de code de ce site est du code Softanza tel qu'il tourne sur la plateforme aujourd'hui.</p>

La bibliothèque se documente elle-même : un objet connaît ses méthodes et peut expliquer chacune. Une chaîne seule répond avec 5 384 méthodes. C'est ainsi que la référence de ce site a été générée, à partir des explications de la bibliothèque et non d'un manuel écrit à la main.

<div class="run"><div><div class="lbl">Softanza</div><pre>? len( Q("Softanza").Methods() )
? Q([ 1, 2, 2 ]).Ask("how do I remove duplicates")</pre></div><div class="out"><div class="lbl">Sortie</div><pre>5384
Unique
1.10
remove duplicates / unique (engine-backed)
UniqueCS
...
RemoveDuplicates</pre></div></div>
<p class="ran">exécuté le 2026-10-01 à 09:26 et à 01:40</p>
