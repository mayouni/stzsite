---
title: Quatre largeurs
title_html: Quatre <i>largeurs</i>
kicker: Une fonction, quatre largeurs
lede: Une fonction peut tourner sur des voies, sur des cœurs, sur la carte graphique ou à travers des nœuds. Le moteur choisit par la mesure, et la personne ne voit que la vitesse.
description: Les quatre largeurs du calcul Softanza : voies, cœurs, carte graphique et nœuds sous un seul aiguillage mesuré, chaque largeur identique au bit près ou justifiée par écrit, avec l'étape de chacune.
---

<ol class="steps">
<li value="1"><b>Voies.</b> La même instruction sur plusieurs valeurs à la fois, à l'intérieur des boucles du moteur. <span class="rx-src">construit</span></li>
<li value="2"><b>Cœurs.</b> Le même travail sur les cœurs de la machine, utilisés seulement là où un seuil mesuré dit que cela paie. <span class="rx-src">construit</span></li>
<li value="3"><b>La carte graphique.</b> Du calcul sur la carte, la carte étant réveillée avant que rien soit chronométré. <span class="rx-src">construit · voir <a href="atlas/gpu.html">le domaine GPU</a></span></li>
<li value="4"><b>Les nœuds.</b> Le même travail sur plusieurs machines, supervisé. <span class="rx-src">construit · voir <a href="host.html">l'hôte</a></span></li>
</ol>

La règle qui tient les quatre ensemble : une voie n'est prise que là où une mesure montre qu'elle gagne, et sa réponse est identique au bit près à celle de la voie simple ou la différence est justifiée par écrit. Le travail élément par élément sur de petites données a été mesuré et laissé sur la voie simple, parce qu'il ne gagnait pas.

<p class="proof"><b>en construction</b> Les largeurs sont construites. Un vocabulaire qui laisserait un programmeur dire en mots simples quelle largeur il veut est spécifié et n'a pas de code. Les mesures derrière chaque seuil sont dans les propres registres de la bibliothèque et ne sont pas reproduites ici.</p>
