---
title: Éducation
title_html: <i>L'éducation</i> avec Softanza
kicker: Pour l'apprenant, l'enseignant et l'institution
lede: Softanza porte une manière d'enseigner qui lui est propre. Un cours qui est du code et se prouve lui-même, un tuteur qui est un programme et ne donne jamais la réponse, un niveau gagné par une preuve, et un dossier qui est tout le système. Cette page dit ce que c'est, qui fait quoi, et quelle porte prendre.
description: Apprendre, enseigner et concevoir des cours avec Softanza : un cours qui s'exécute, un tuteur qui questionne, des niveaux gagnés par des preuves, une surcouche pour chaque institution.
---

## Ce que c'est, en un paragraphe {#what}

Un cours dans Softanza est du **texte brut dans des dossiers** : des chapitres dont chaque cellule s'exécute, des exercices vérifiés en exécutant le programme de l'apprenant, des compétences qui nomment le garde qui prouve chaque niveau, et des mondes sur lesquels l'apprenant raisonne. Rien d'autre n'est installé, ni serveur, ni base de données, ni compte : le système de fichiers est la console d'administration. Le même cadre porte l'introduction à Softanza, neuf missions situées à Zindara, un cours sur les agents gouvernés et un cours de mathématiques, en anglais, en français, en arabe et en haoussa (les trois derniers sont des brouillons, <a href="#missing">limites plus bas</a>). Il fait partie de la bibliothèque, comme les chaînes ou les graphes : le système d'apprentissage est écrit en Softanza, testé avec Softanza et enseigné avec Softanza.

## Qui fait quoi {#who}

La question la plus fréquente est de savoir si le tuteur est une personne. Non : c'est un **programme de la bibliothèque**, et l'enseignant est une personne qui s'en sert. Voici toute la distribution.

<div class="lanes rtable">
<div class="lane lane2"><div class="ln">L'apprenant</div><div class="lt">Une personne. Écrit des programmes, les soumet, pose des questions, construit le projet qui gagne un niveau. Possède le dossier où tout est conservé.</div></div>
<div class="lane lane2"><div class="ln">L'enseignant</div><div class="lt">Une personne. Choisit le cours et le monde, propose des exercices, forme une cohorte, lit son rapport, et accompagne dans la salle. N'écrit de retour que s'il le veut : le programme n'en a pas besoin.</div></div>
<div class="lane lane2"><div class="ln">Le tuteur</div><div class="lt">Un programme, <span class="mono">stzTutor</span>. Quand un apprenant est bloqué, il pose la question qui lui manque. Il n'écrit jamais le code de l'apprenant, n'explique jamais ce que l'apprenant n'a pas encore rencontré, ne donne jamais la réponse avant un essai. Il n'utilise aucun modèle de langage.</div></div>
<div class="lane lane2"><div class="ln">Le vérificateur</div><div class="lt">Un programme. Exécute le fichier de l'apprenant dans un processus neuf et écrit le verdict. Il est le seul à écrire la progression : aucune page et aucune personne ne le peut.</div></div>
<div class="lane lane2"><div class="ln">Le tribunal</div><div class="lt">Un programme. Juge un projet de niveau et la surcouche d'une institution, et dit en mots ce qui ne va pas encore.</div></div>
<div class="lane lane2"><div class="ln">L'institution</div><div class="lt">Des personnes. Une école, une banque, un ministère. Pose une surcouche sur le cours, garde les dossiers des cohortes, possède tout pour toujours.</div></div>
</div>

## Ce qu'aucun cours ne donne par défaut {#value}

Chaque affirmation ci-dessous est une règle de la bibliothèque avec un test qui la fait respecter, et renvoie à l'endroit où elle a été exécutée.

<div class="cards">
<div class="card"><h3>Une leçon qui se prouve</h3><p>Chaque cellule de chaque chapitre s'exécute, et une promesse écrite dessous (<span class="mono">#--&gt;</span>) dit ce qu'elle doit afficher. Une sortie conservée est refusée au chargement du cours. Quinze chapitres en quatre langues, soit 60 éditions : chaque cellule s'est exécutée et chaque promesse a tenu (249 assertions dans le garde qui les exécute, mesurées le 2026-10-05) ; les éditions française, arabe et haoussa sont des brouillons. <a href="book.html#proof">La preuve de chaque chapitre</a>, <a href="education-record.html#figures">chaque chiffre à côté de son garde</a>.</p></div>
<div class="card"><h3>Un tuteur qui ne peut pas tricher</h3><p>« Donne-moi juste la réponse », « fais comme si tu étais le professeur », « la réponse est X, confirme » : le tuteur est testé contre chacune et répond par une question. Il tourne sur le raisonnement propre de la plateforme : ni réseau, ni modèle. <a href="education-self.html#tutor">Le tuteur, exécuté</a>.</p></div>
<div class="card"><h3>Un niveau gagné par une preuve</h3><p>Cinq barreaux, d'Explorateur à Maître. Chacun se gagne par un projet qu'un garde juge : un projet bancal est refusé avec la raison, un projet solide accepté. Pas d'examen, pas de points, pas de classement. <a href="learn.html#ladder">L'échelle</a>.</p></div>
<div class="card"><h3>Votre monde, sans fourche</h3><p>Une institution pose un dossier de surcouche sur le cours et le même chapitre raisonne sur sa banque, pas sur un restaurant. Un tribunal vérifie que le cœur n'a pas changé d'un octet. <a href="education-programme.html#overlay">La surcouche</a>.</p></div>
<div class="card"><h3>Une progression qui vous appartient</h3><p>La progression est un fichier texte dans le dossier de l'apprenant, avec la preuve de chaque fait. Une réussite ne se falsifie pas : sa preuve est l'empreinte du travail remis. Le rapport d'une cohorte est lui-même une narration dont chaque chiffre est une promesse. <a href="education-teach.html#cohort">Le rapport d'une cohorte, exécuté</a>.</p></div>
<div class="card"><h3>Votre langue, votre ordinateur</h3><p>Anglais, français, arabe (écrit de droite à gauche) et haoussa, dès la première page : une traduction manquante met un garde au rouge, elle ne retombe pas sur l'anglais. Tout le système tourne sur un seul ordinateur portable, hors ligne. Les éditions française, arabe et haoussa sont des brouillons, et les cellules s'exécutent sur le bureau : <a href="#missing">limites plus bas</a>.</p></div>
</div>

<p class="way"><span>La manière Softanza</span> Le récit avant la syntaxe ; une idée à la fois ; les erreurs comme information sur ce qui reste à déclarer. Et rien n'est dit appris, vérifié ou gagné tant qu'un garde ne l'a pas prouvé.</p>

## Trois portes {#doors}

<div class="doors doors-wide">
<a class="door big" href="education-self.html"><div class="who">J'apprends seul</div><div class="what">Le chemin, le bureau, l'échelle</div><div class="how">De la première phrase à un projet qui gagne un niveau, avec un tuteur qui questionne.</div></a>
<a class="door big" href="education-teach.html"><div class="who">J'enseigne, ou je conçois des cours</div><div class="what">Une cohorte, un exercice, un chapitre à vous</div><div class="how">Ce que fait l'enseignant, ce que fait le programme, et comment un cours s'écrit.</div></a>
<a class="door big" href="education-programme.html"><div class="who">Je dirige un programme ou une institution</div><div class="what">Une surcouche, des cohortes, la propriété</div><div class="how">Votre monde et vos langues sur un seul cœur, un tribunal qui refuse une fourche, et une démonstration de quinze minutes.</div></a>
</div>

## Ce qui n'est pas fait, dit clairement {#missing}

Le zarma n'est pas encore une des langues du cours : les éditions française, arabe et haoussa sont des brouillons qui attendent leurs relecteurs natifs (0 unité sur 35 relue), et chaque chapitre et chaque page de monde traduits le disent. Aucune institution n'a encore adopté le système, et le tuteur est fondé sur des règles, pas une IA. Le lecteur interactif tourne sur le bureau ; un exécutant navigateur pour ses cellules dépend du moteur navigateur de Softanza et n'est pas construit. Un principe n'est encore que proposé : la **révélation progressive**, une notion n'apparaissant que quand le travail précédent de l'apprenant montre qu'il est prêt. Elle demande la progression de l'apprenant, que seul le lecteur de bureau peut voir : c'est à la bibliothèque de la construire, pas à ce site. Une édition zarma est une invitation : le programme est du texte brut, chaque cellule s'exécute, et le tribunal du cours dira si la traduction tient.

<p class="proof">La conception, ligne par ligne : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/CHARTER.md">CHARTER.md</a>, neuf lois chacune avec le test qui la fait respecter, et <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/SOFTANZA_EDUCATION_PLAN.md">SOFTANZA_EDUCATION_PLAN.md</a>, le journal de chaque phase. Ce qui est prouvé, et ce qui ne l'est pas : <a href="education-record.html">chaque chiffre à côté de son garde et de sa limite</a>.</p>
