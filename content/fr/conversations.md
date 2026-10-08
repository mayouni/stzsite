---
title: Conversations
title_html: <i>Conversations</i>
kicker: Une direction, avec ses étapes
lede: Vos utilisateurs gardent leur medium. Un monde déclaré une fois pourrait les atteindre dans l'application de messagerie de leur téléphone, dans un menu texte sur n'importe quel téléphone, ou par la voix, avec le même juge pour chaque phrase. Cette page dit ce qui existe pour cela, ce qui est conçu, et ce qui est absent.
description: Les conversations comme interface de premier rang dans Softanza : la conversation gouvernée qui existe, la loi du coût d'un SMS exécutée dans la bibliothèque, et les canaux de messagerie, sessions et modèles qui sont conçus ou absents.
---

## Pourquoi {#why}

La messagerie est un trou deux fois : comme unité de calcul, le message, et comme medium, l'application qu'une personne utilise déjà. Les gens que Softanza sert ont déjà un medium. Les outils d'un restaurateur étaient sa mémoire, un carnet de papier, un tableur et quelques applications, dont une messagerie, et son exigence était une interface en français, simple comme une messagerie, jamais plus de deux gestes. La première démonstration de ce projet a tourné sur un vrai téléphone, par le restaurateur lui-même, par une messagerie, en août 2026.

Le but est des conversations qui se font de façon programmatique par défaut, pour qu'un concepteur les ait comme interface de premier rang sans obliger les utilisateurs à changer d'habitudes.

## Ce qui existe {#built}

<div class="cards">
<div class="card"><h3>La conversation gouvernée <b>(construit)</b></h3><p>Un échange à plusieurs tours avec un état, dans un espace de connaissance. L'écart entre la forme dont la connaissance a besoin et ce qu'elle tient génère la question suivante. Le socle est déterministe et n'a pas besoin de modèle. Elle s'exécute sur la <a href="wise.html">page du wise coding</a>.</p></div>
<div class="card"><h3>La transcription et le but <b>(construit)</b></h3><p>Chaque ligne a un locuteur, un texte et une certitude. Un but est l'écart qui génère les questions.</p></div>
<div class="card"><h3>Des ports avec bacs à sable <b>(construit)</b></h3><p>Un port de SMS est tout objet qui sait envoyer un numéro et un texte. Son bac à sable enregistre ce qui aurait été envoyé et ne livre rien, de sorte que la boîte d'envoi devient quelque chose qu'un test peut vérifier. Le port de courriel a la même forme.</p></div>
<div class="card"><h3>Un registre qui refuse un faux <b>(construit)</b></h3><p>Un service est déclaré, un bac à sable lui est lié en développement, le service réel au déploiement, et la production refuse le faux.</p></div>
<div class="card"><h3>Langage naturel et voix <b>(construit)</b></h3><p>La couche naturelle lit l'anglais, le français, l'arabe, le haoussa et le turc. La synthèse vocale existe dans le moteur.</p></div>
</div>

## La facture, exécutée {#bill}

Un SMS se facture par segment, et le nombre de segments n'est pas le nombre de caractères : il dépend de l'alphabet. Le bac à sable compte la facture et nomme l'encodage, pour qu'un défaut caché dans un modèle apparaisse avant qu'une campagne soit payée.

<!--SHOWCASE:conversations-->

## Le pont {#bridge}

La loi d'interface de ce site énonce que sa grammaire est fermée : un nouveau medium ajoute des rendus, jamais des verbes. Une conversation rend les mêmes verbes que l'interface. Découvrir est un menu. Choisir est « répondre 2 ». Confirmer est « répondre OUI ». Annuler est « répondre ANNULER ». Défiler est « répondre SUITE ». Un fil de messagerie, un écran de menu texte et une invite vocale sont des media, et un monde déclaré une fois s'y projetterait comme il se projette sur le web et le téléphone.

<div class="cards">
<div class="card"><h3>Le service du fonds commun <b>(conçu)</b></h3><p>La conception de la constellation range la messagerie parmi les communs : identité, registre, paiements, messagerie. C'est une ligne dans une conception, et aucun code ne porte encore le mot.</p></div>
<div class="card"><h3>Une facette par medium <b>(conçu)</b></h3><p>Chaque medium est une cible du monde, avec une matrice pour juge : un verbe qu'un medium ne sait pas rendre est une case rouge qui exige un repli, jamais une omission silencieuse.</p></div>
<div class="card"><h3>Le juge de ce qui se dit <b>(conçu)</b></h3><p>Des modèles approuvés comme grammaire fermée, un agent autorisé à n'émettre que des phrases admises, et la transcription gardée comme preuve dans le registre.</p></div>
</div>

## Ce qui est absent {#absent}

- Le message comme unité : ses parties, sa réponse, son medium, son état.
- Les ports de canal et leurs bacs à sable pour une messagerie, un menu texte sur n'importe quel téléphone, la voix et le clavardage web. Un menu texte est une session de courts écrans avec un délai, ce qu'un SMS n'est pas.
- Une session avec sa fenêtre et son délai comme états, le consentement comme donnée, et des modèles approuvés.
- La reconnaissance vocale et la téléphonie.
- Le zarma et le peul dans la couche naturelle.

<p class="proof"><b>en construction</b> Aucun medium de conversation n'est une cible aujourd'hui : la couche applicative cible le mobile, le bureau et le web. Cette page est une direction et le dit. L'inventaire a été lu dans les fichiers de la bibliothèque par une évaluation extérieure le 2026-10-07 et compté par nom ; seule la loi du coût d'un SMS ci-dessus a été exécutée.</p>

<p class="proof">Sources : le garde-scénario <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/sms_port_narrated.ring">sms_port_narrated.ring</a> ; la conversation sur la <a href="wise.html">page du wise coding</a> ; la constellation sur <a href="platforms.html">la page de la plateforme de plateformes</a>.</p>
