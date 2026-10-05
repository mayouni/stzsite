---
title: Diriger un programme
title_html: <i>Je dirige</i> un programme ou une institution
kicker: Éducation · une surcouche, des cohortes, la propriété
lede: Une école, une banque, un ministère pose un dossier de surcouche sur le cours. Les mêmes chapitres raisonnent alors sur son monde, dans ses langues, sous ses règles, et le cœur n'a pas changé d'un octet. Les cohortes, la progression et les rapports sont des dossiers que l'institution garde pour toujours.
description: Adapter le système d'apprentissage Softanza à une institution : une surcouche, des cohortes, les langues, la gouvernance, et une démonstration de quinze minutes.
---

## Ce qu'une institution possède {#own}

Tout est un dossier de texte brut : le programme, ses cours, sa surcouche, ses cohortes, le travail et la progression de chaque apprenant. Il n'y a pas de base de données à sauvegarder, pas de serveur à maintenir en marche, pas de compte à renouveler ; copier le dossier copie tout le système d'apprentissage de l'institution, et un système de gestion de versions en lit l'historique. Le système demande la bibliothèque et un ordinateur portable, et il tourne hors ligne.

## Une surcouche, jamais une fourche {#overlay}

Vous ne changez pas le cours. Vous posez votre **surcouche** dessus : un dossier qui donne aux mêmes chapitres votre monde, vos exercices, vos langues, votre nom et vos règles.

<pre>Programme de base, le restaurant :        Avec la surcouche de la banque posée (un fichier) :
    bella-cucina (restaurant)                sahel-savings (banque)
    [ "margherita", "tiramisu", "lasagna" ]  [ "transfer", "loan", "deposit" ]
PROUVÉ   la même cellule répond au sujet de la banque
PROUVÉ   le fichier du chapitre n'a pas changé d'un octet</pre>
<p class="ran">exécuté le 2026-09-30, la démonstration d'éducation</p>

Une surcouche peut ajouter un chapitre, un exercice, une compétence ou un monde ; remplacer un monde par son nom, ce qui fait que le même chapitre raisonne sur une banque ; faire correspondre ses compétences à celles du cœur ; ajouter une cinquième langue comme un paquet de données seulement ; et gouverner, avec des règles que les agents de ses apprenants doivent respecter. Elle **ne peut pas** modifier ni supprimer un fichier du cœur : elle ne peut qu'en masquer un, et chaque masquage est listé, si bien qu'une institution voit toujours ce qui diffère du cœur.

Les étapes du guide, lequel est lui-même vérifié par un garde qui les suit à la lettre :

<ol>
<li><b>Copiez le gabarit</b>, et donnez-lui un nom court : <span class="mono">bank</span>, <span class="mono">university</span>, <span class="mono">ministry</span>.</li>
<li><b>Remplissez les emplacements</b> : le nom, l'institution, le monde, deux choses qu'on y demande.</li>
<li><b>Écrivez votre monde</b> : un fichier de faits, trois mots par ligne, <span class="mono">ministry-of-education | is-a | ministry</span>, <span class="mono">request-1 | requested | transcript</span>. Le chapitre 1 demande à ce monde ce qui a été demandé, compte les répétitions et les retire.</li>
<li><b>Ajoutez un exercice à vous</b> si vous le voulez : une tâche dans chaque langue, une promesse, une réponse qui doit échouer et une réponse qui doit passer.</li>
<li><b>Lancez le tribunal.</b> Il vous dit, par son nom et en mots, ce qui ne va pas encore : une espace dans un mot d'un monde, un fichier qui remplacerait un chapitre du cœur.</li>
</ol>

<p class="proof">Le guide : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/OVERLAY_GUIDE.md">OVERLAY_GUIDE.md</a>. Deux surcouches de référence, une banque et une université, sont dans <a href="https://github.com/mayouni/stzlib/tree/main/libraries/stzlib/base/education/overlays">education/overlays</a> ; la cinquième loi de la charte (une surcouche ne fait jamais de fourche) est tenue par un garde qui échange deux surcouches sous un même chapitre et vérifie que l'empreinte du cœur n'a pas changé.</p>

## Cohortes, rapports, propriété {#cohorts}

Une cohorte est un dossier d'apprenants qui suivent un cours sous une surcouche. Son rapport de progression est une narration dont chaque chiffre est une promesse, si bien qu'il dit de lui-même quand il est périmé : la porte de l'enseignant en montre une <a href="education-teach.html#cohort">exécution</a>. La progression de chaque apprenant est un fichier texte dans son propre dossier, écrit seulement par le vérificateur et portant la preuve de chaque fait ; une réussite ne se falsifie pas, parce que sa preuve est l'empreinte du travail remis. À la fin d'une année l'institution détient, comme fichiers, qui a fait quoi et ce qui a été prouvé.

## Les langues {#languages}

Le cours tourne en anglais, en français, en arabe (écrit de droite à gauche) et en haoussa, dès la première page ; le garde de chaque chapitre s'exécute dans les quatre, et une traduction manquante est un garde en échec, pas un repli sur l'anglais. Les éditions française, arabe et haoussa sont des brouillons qui attendent leurs relecteurs natifs (<a href="education-record.html#limits">0 unité sur 35 relue</a>), et chaque chapitre et chaque page de monde traduits le disent. Une cinquième langue est un paquet de données seulement, et les mots propres de l'institution vont dans sa surcouche.

## L'IA gouvernée pour les apprenants {#governed}

L'agent d'un apprenant propose ; seule une porte valide. Les exercices sur les agents s'exécutent dans un monde sûr : un garde vérifie que l'arbre réel est inchangé après que l'agent d'un étudiant a « tout supprimé ». Le tuteur lui-même n'utilise aucun modèle de langage et n'a besoin d'aucun réseau.

## Une démonstration de quinze minutes pour les décideurs {#demo}

Le guide du présentateur donne une scène par minute, tourne sur un seul ordinateur portable hors ligne, et calcule chaque scène pendant qu'elle est montrée. Avant une réunion, sa répétition doit se terminer par la ligne <span class="mono">DEMO: 20 proved, 0 not proved</span> : si une ligne dit NOT PROVED, la démonstration dit qu'il serait faux de la présenter, et le dirait aussi devant le public.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">0 à 2</div><div class="lt"><b>Zéro installation.</b> Un dossier de texte brut. Softanza est la seule chose que cet ordinateur exécute.</div></div>
<div class="lane lane2"><div class="ln">2 à 4</div><div class="lt"><b>Leur langue.</b> Le même chapitre, exécuté en direct en anglais, en français, en arabe et en haoussa.</div></div>
<div class="lane lane2"><div class="ln">4 à 6</div><div class="lt"><b>Leur monde.</b> Un fichier de l'institution, et le chapitre raisonne sur sa banque, pas sur un restaurant.</div></div>
<div class="lane lane2"><div class="ln">6 à 8</div><div class="lt"><b>Rien de truqué.</b> Une mauvaise réponse échoue et une bonne passe, parce que le programme a été exécuté, pas lu.</div></div>
<div class="lane lane2"><div class="ln">8 à 10</div><div class="lt"><b>Le tuteur.</b> Il ne donnera pas la réponse ; il pose la question qui manque à l'apprenant.</div></div>
<div class="lane lane2"><div class="ln">10 à 12</div><div class="lt"><b>IA sûre.</b> L'agent d'un étudiant a tenté de supprimer tout le cours ; il n'a pu que proposer.</div></div>
<div class="lane lane2"><div class="ln">12 à 14</div><div class="lt"><b>Tous les niveaux.</b> La mission d'un enfant de neuf ans en haoussa et l'exercice de gouvernance d'un analyste de banque, sur le même moteur.</div></div>
<div class="lane lane2"><div class="ln">14 à 15</div><div class="lt"><b>La propriété.</b> La progression est un fichier texte que l'institution garde pour toujours, et une réussite ne se falsifie pas.</div></div>
</div>

<p class="proof">Le guide du présentateur : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/DEMO.md">demo/DEMO.md</a>. Son garde exécute la démonstration deux fois depuis un dossier propre et vérifie que les deux exécutions disent la même chose mot pour mot.</p>

## Ce qu'une institution doit savoir avant de commencer {#honest}

Le lecteur interactif tourne sur le bureau ; un exécutant navigateur pour les cellules n'est pas encore construit, et la page le dit sur chaque cellule. Les éditions française, arabe et haoussa attendent des relecteurs natifs (0 unité sur 35 relue) ; le zarma n'est pas encore une langue du cours. Aucune institution n'a encore adopté le système : les surcouches de la banque et de l'université dans la bibliothèque sont des références écrites pour montrer ce qu'est une surcouche. Le tuteur est fondé sur des règles, pas une IA. Il n'y a aucun modèle de langage dans la boucle et aucun n'est requis : on pourra en ajouter un plus tard comme option, jamais comme l'esprit du tuteur.
