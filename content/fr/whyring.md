---
title: Pourquoi Softanza quitte Ring
title_html: Pourquoi Softanza <i>quitte Ring</i>
kicker: L'histoire, racontée une fois
lede: Softanza est née sur Ring et le quitte. Cette page dit pourquoi, en trois raisons, et ce qui reste. Elle nomme des décisions et des documents et jamais le caractère d'une personne, et elle commence par dire merci.
description: Pourquoi Softanza quitte Ring : merci d'abord, puis trois raisons, les limites rencontrées à l'échelle de la production, une direction qu'on n'a pas pu influencer, et la gouvernance comme propriété de conception, et ce qui reste.
---

## Merci d'abord {#thanks}

Softanza est née sur Ring. Pendant des années son auteur a écrit la bibliothèque en Ring, enseigné le langage, l'a promu sur le terrain, et en a écrit le livre, <i>Beginning Ring Programming</i> (Apress, 2020). En 2021 la bibliothèque a été décrite pour la première fois à la communauté Ring, et la première présentation de Softanza, en 2022, l'appelait un meilleur ami des programmeurs Ring existants.

La simplicité de Ring et son expressivité multiparadigme sont les deux choses que Softanza garde, parce qu'elles n'ont jamais été le problème.

## Trois raisons {#reasons}

<ol class="steps">
<li value="1"><b>Les limites ont été rencontrées à l'échelle de la production.</b> Un scalaire coûte des centaines d'octets, et un élément de liste sept fois un double, selon l'arithmétique de l'auteur même du langage. Les chaînes sont copiées à chaque frontière d'appel. Il n'y a ni tri stable, ni moteur d'expressions régulières, ni mode strict, et Unicode est laissé à une boîte à outils graphique. L'auteur a reproduit chacune de ces limites en écrivant une bibliothèque de cette taille.</li>
<li value="2"><b>La direction n'a pas pu être influencée.</b> Selon l'expérience de l'auteur, les défauts ponctuels étaient corrigés vite et avec remerciements, tandis que les questions sur la direction du langage recevaient, au fil des années, le même conseil : garder le noyau simple, et faire le reste dans des extensions C ou dans le pont graphique. Ring++ a été fait pour répondre à trois points douloureux, la performance, le typage et la construction, sans quitter Ring.</li>
<li value="3"><b>La gouvernance est une propriété de conception.</b> Une dépendance dont la direction ne peut pas être influencée et dont le comportement ne peut pas être borné ne passe pas la diligence raisonnable pour les domaines réglementés que sert Softanza, une banque ou un ministère. La préoccupation de l'auteur est aussi éthique : là où une seule personne décide de la destination du travail des autres, les autres n'ont rien sur quoi s'appuyer.</li>
</ol>

## Ce que fait Softanza {#commitments}

La réponse n'est pas l'indépendance pour elle-même. C'est l'indépendance pour ceux qui construisent sur Softanza, et elle prend la forme de choses que ce site exécute, pas de promesses.

<ul class="narr">
<li><b>Un moteur sans dépendance tierce</b>, écrit en Zig depuis 2025. <span class="rx-src">construit · voir <a href="architecture.html">l'architecture</a></span></li>
<li><b>Une machine virtuelle et un compilateur souverains</b>, pour Haro. <span class="rx-src">en construction · voir <a href="platform.html">la plateforme</a></span></li>
<li><b>Un noyau ouvert</b> sous licence MIT, public depuis le 12 mars 2022. <span class="rx-src">construit · voir <a href="start.html">Démarrer</a></span></li>
<li><b>Des décisions datées et des preuves.</b> Chaque affirmation de ce site renvoie au fichier, au garde ou au rendu qui la prouve. <span class="rx-src">construit · voir <a href="goals.html">les buts de conception</a></span></li>
<li><b>Une écriture est une proposition.</b> Rien ne change un monde sans un acteur gouverné. <span class="rx-src">construit pour les fichiers, en construction pour les données · voir <a href="store.html">le magasin</a></span></li>
<li><b>Le droit d'une personne de joindre une personne.</b> <span class="rx-src">conçu, pas construit · voir <a href="agentic.html">agentique</a></span></li>
</ul>

## Ce qui reste {#stays}

<!--RUNTIME-->

Les gardes-scénario sont le test de la promesse que le code déjà écrit continue de fonctionner. Softanza dit merci au langage qui l'a vue grandir, et va là où la souveraineté de ses utilisateurs l'exige.

<p class="proof"><b>en construction</b> Cette page nomme des décisions et des documents, jamais le caractère d'une personne. Les limites de la première raison sont les mesures de l'auteur ; leurs reproductions ne sont pas encore publiques, et quand elles le seront, chaque limite renverra à la sienne. Rien ici ne cite un document privé. La façon dont l'histoire est datée est sur <a href="roots.html#dates">la page des racines</a>.</p>
