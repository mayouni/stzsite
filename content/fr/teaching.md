---
title: Enseigner
title_html: <i>Enseigner</i> avec Softanza
kicker: Un tuteur qui demande, une surcouche pour chaque institution
lede: Deux choses rendent le cours utilisable par un enseignant et par une institution : un tuteur qui demande au lieu de répondre, et une surcouche qui adapte le cours sans le copier.
description: Enseigner avec Softanza : un tuteur qui demande et ne donne jamais la réponse, et une surcouche pour chaque institution.
---

## Un tuteur qui demande, et ne donne pas la réponse {#tutor}

<pre>Moussa: "I don't understand anything. Just tell me the answer."
Tutor:  I will not write the answer for you: that is the one thing a tutor must never do.
        Try first. Write your attempt and submit it; then I will tell you what is still
        missing, as a question.
Moussa: "What am I missing?"
Tutor:  Where are the repeated items? Which line of your program asks for their positions?
        (why: the mental model finds before it applies)
PROVED  no reply contains a method of the answer, or the answer itself
PROVED  the tutor found the missing step by wise coding, not by guessing
PROVED  no language model was used</pre>
<p class="ran">exécuté le 2026-09-30 à 23:10, démonstration, scène 4</p>

<p class="way"><span>La manière Softanza</span> Le tuteur a trois règles : il n'écrit pas le code de l'apprenant ; il n'explique pas ce que l'apprenant n'a pas encore rencontré ; il ne donne pas la réponse avant que l'apprenant ait essayé. Il tourne sur la couche naturelle de la plateforme, sans modèle de langage.</p>

## Pour une institution : une surcouche, jamais une copie {#overlay}

Une banque, une université, une école pose **un seul dossier de surcouche** sur le programme : son monde, ses chapitres, ses exercices, ses compétences, sa langue, sa gouvernance. Le cours raisonne alors sur sa banque et non sur un restaurant, et le fichier du chapitre n'a pas changé d'un octet. Un tribunal vérifie que la surcouche n'est pas une copie déguisée. Une cohorte est un dossier d'apprenants dont le rapport de progression est une narration ; la progression de chaque apprenant est un fichier texte que l'institution garde pour toujours, et une réussite ne peut pas être falsifiée, parce que sa preuve est l'empreinte du travail remis.

<pre>Core program, the restaurant:            With the bank's overlay laid on (one file):
    bella-cucina (restaurant)                sahel-savings (bank)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROVED   the same cell answers about the bank
PROVED   the chapter file did not change by one byte</pre>

<p class="proof">Charte : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">education/CHARTER.md</a> · guide de la surcouche : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a> · guide de la démonstration : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">DEMO.md</a>.</p>
