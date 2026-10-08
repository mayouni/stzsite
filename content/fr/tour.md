---
title: Présentation
description: Le site en mode présentation : chaque scène est une page, en plein écran.
help: → ou clic : suivant · ← : précédent · n : notes · h : menu · Échap : ouvrir la page
---

<<< scene id="onboarding" page="../index.html" label="Accueil" class="scene-image" >>>
<img class="bg" src="../assets/img/onboarding-elder.webp" alt="Un ancien en turban blanc lit une feuille de code dans une cour ; le mot SOFTANZA est peint sur le mur derrière lui.">
<div class="caption">
<div class="eyebrow">Softanza</div>
<p><b>La plateforme des artisans du logiciel à l'ère de l'IA.</b></p>
<p>Née en Afrique. Utile au monde !</p>
</div>
```notes
Laisser l'image parler dix secondes. Puis une phrase : « Cet homme lit du code. Le mur derrière lui dit déjà Softanza. Tout ce que je vais montrer ce soir tient dans cette image : la connaissance, le lieu, et une langue que l'on peut lire. »
```

<<< scene id="northstar" page="vision.html" label="L'étoile polaire" >>>
<div class="eyebrow">L'architecture depuis 2020 · relue bande par bande face à ce qui existe, septembre 2026</div>
<figure class="diagram"><img src="../assets/img/diagrams/northstar-fr.png" alt="Six bandes : pour qui, solutions, systèmes, langues, la fondation Softanza, et en dessous ; à côté, le tribunal." width="1376" height="820"></figure>
```notes
« En 2020, l'auteur a dessiné Softanza sur une seule feuille. Lisez-la depuis le haut : pour qui, les solutions, les cinq systèmes auxquels une solution répond, les langues, la fondation, ce qui est en dessous. » En septembre 2026, chaque bande a été vérifiée dans les dépôts. Le but n'a pas bougé. Deux choses sont nouvelles : les agents dans la première bande, et les étages en dessous. À côté de tout, le tribunal : rien n'est cru.
```

<<< scene id="vision" page="principles.html" label="Vision" >>>
<div class="eyebrow">L'approche de Softanza pour programmer à l'ère agentique</div>
## Déclarez <i>une langue</i>
<p>Avec Softanza, on n'écrit plus des logiciels.</p>
<p>On <b>déclare des mondes</b> dans des langues faites pour leur domaine, et on <b>gouverne</b> la manière dont ces mondes changent.</p>
<p>Ce n'est pas la pratique d'aujourd'hui. C'est la proposition de Softanza : <b>une plateforme qui connaît votre monde.</b></p>
```notes
Trois idées, une par ligne. Ne pas lire la page. L'exemple parlé : une banque déclare ses entités, ses règles et ses acteurs ; le système répond « quels flux touchent le compte de dépôt, et qu'est-ce qui casse si j'ajoute un champ ». Aucun outil général ne peut répondre à cela : on ne lui a jamais donné votre banque. Le dire comme l'approche de Softanza, jamais comme ce que fait l'industrie.
```

<<< scene id="platform" page="platform.html" label="Plateforme" >>>
<div class="eyebrow">Un moteur, vingt-huit domaines</div>
## Un moteur en Zig, <i>une langue pour visage</i>
<div class="figures">
<div class="figure"><b>401</b><span>fichiers source Zig, 179 000 lignes</span></div>
<div class="figure"><b>531 000</b><span>lignes de bibliothèque, 306 000 de tests</span></div>
<div class="figure"><b>334</b><span>couloirs notés dans l'Atlas</span></div>
<div class="figure"><b>5 824</b><span>commits depuis le 12 mars 2022</span></div>
</div>
<p>Un moteur en Zig · une langue, <b>Haro</b>, en construction · vingt-huit domaines, chacun noté honnêtement contre .NET, Python, Wolfram et la JVM.</p>
```notes
Dire le stade tel qu'il est : Haro est la langue de la plateforme, sa machine virtuelle et son compilateur existent et tournent, sa charte attend ma ratification ; je ne la dirai pas disponible avant qu'elle le soit. La crédibilité de la plateforme, c'est que l'Atlas montre ses 36 couloirs « Emerging » à côté de ses 101 « Strong ».
```

<<< scene id="platforms" page="platforms.html" label="Plateforme de plateformes" >>>
<div class="eyebrow">La langue des langues, et la plateforme des plateformes · la construction tourne dans la bibliothèque</div>
<figure class="diagram"><img src="../assets/img/diagrams/platforms-fr.png" alt="RestoLean, Organizium, DIKO Hub, et la vôtre : chacune déclare sa plateforme dans ses propres mots ; Softanza donne à chacune la plateforme." width="1376" height="700"></figure>
```notes
« Haro est la langue des langues. Softanza est la plateforme des plateformes. » Un réseau de restaurants, une banque, une organisation au Niger : chacun déclare sa propre plateforme dans ses propres mots, un socle commun, un monde par personne et appareil, des liens, des règles, des rôles. Softanza donne à chacune une grammaire et son tribunal, tous les écrans, des données avec retour arrière, et des agents tenus aux mêmes règles. Dire le stade : la construction tourne dans la bibliothèque ; les plateformes des clients tournent aujourd'hui sur des piles web ordinaires, et les passer sur le moteur est un changement de moteur, pas de plan.
```

<<< scene id="atlas" page="areas.html" label="Les domaines" >>>
<div class="eyebrow">Vingt-huit domaines, un seul moteur · chaque image produite par la plateforme elle-même</div>
<!--ATLAS-WALL-->
```notes
Laisser le mur d'images parler. « Chaque image a été rendue par la plateforme : une carte, une onde, un diagramme, une table. Aucun concurrent ne couvre toutes ces lignes sur un seul moteur, et la page de l'Atlas montre les notes, les basses à côté des hautes. » Cliquer un domaine si on le demande : chaque page a ses couloirs et un exemple exécuté.
```

<<< scene id="code" page="code.html" label="Le code" >>>
<div class="eyebrow">Le code, à côté de JavaScript · chaque côté exécuté</div>
<div class="run"><div><div class="lbl">Softanza</div><pre>? Q(2).Power(64)
? Q("مرحبا بالعالم").Script()
? @@( Naturally("Create a list with [ 5, 3, 5, 1 ]
                 and remove its duplicates").Result() )</pre></div><div class="out"><div class="lbl">Sortie</div><pre>18446744073709551616
arabic
[ 5, 3, 1 ]</pre></div></div>
<p>JavaScript répond <b>18446744073709552000</b> à la première ligne. La troisième n'a pas d'équivalent sans un modèle de langage externe.</p>
```notes
Trois lignes, trois points : exact par défaut ; le moteur connaît l'écriture d'un texte ; une instruction en anglais, en haoussa ou en arabe s'exécute, en local, sans modèle. Dire que chaque bloc du site a été exécuté ce soir et que la sortie est à côté.
```

<<< scene id="agentic" page="agentic.html" label="Agentique" >>>
<div class="eyebrow">Des agents qui ne peuvent pas vous nuire</div>
## L'agent propose. <i>Il ne commet pas.</i>
<div class="run"><div><div class="lbl">Une étudiante lâche un agent qui « range » le cours</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">Le tribunal répond</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
PROVED  the course folder still holds all 610 files</pre></div></div>
<div class="figures">
<div class="figure"><b>38</b><span>garanties, chacune avec son garde</span></div>
<div class="figure"><b>395 ms</b><span>pour détecter une attaque, mesuré</span></div>
<div class="figure"><b>50 ms</b><span>pour la confiner, vérifié de l'extérieur</span></div>
</div>
```notes
L'histoire à raconter : Amina écrit un agent qui « range » le cours. Il propose de supprimer les 610 fichiers. Il ne peut pas : il ne détient pas la capacité d'agir, il ne l'a jamais eue. Un humain lit le plan et refuse. Puis les deux chiffres : un bourrage d'identifiants détecté en 395 millisecondes et confiné en 50, ce soir, sur ce portable, et le modèle de langage qui enquêtait n'a rien pu commettre.
```

<<< scene id="wise" page="wise.html" label="Wise coding" >>>
<div class="eyebrow">Wise coding, contre vibe coding · prouvé par deux gardes, 13 sur 13 et 52 sur 52</div>
<figure class="diagram"><img src="../assets/img/diagrams/wise-fr.png" alt="Vibe coding : l'humain souffle une consigne, la machine devine ; wise coding : Softanza demande, l'écart est mesuré, chaque réponse est jugée, la base de connaissances est écrite." width="1376" height="768"></figure>
```notes
« En vibe coding, l'humain souffle une consigne et la machine devine. En wise coding, c'est Softanza qui demande : elle sait ce qu'un modèle complet de votre monde exige, mesure l'écart, et transforme chaque écart en la question suivante. La session finit par une base de connaissances écrite, pas par un code qu'il faut croire. » Deux gardes le prouvent, exécutés ce soir.
```

<<< scene id="estate" page="estate.html" label="Le domaine" >>>
<div class="eyebrow">Où se tient la plateforme · stades lus dans les dépôts aujourd'hui</div>
<figure class="diagram"><img src="../assets/img/diagrams/technology-fr.png" alt="Le domaine : applications, Aïcha, Softanza, Haro, Harobanda, matériel ; à côté, Takamba, le harnais." width="1376" height="768"></figure>
```notes
Lire la pile de bas en haut : du matériel ordinaire ; Harobanda, la machine déclarée, construite ; Haro, la langue des langues, en construction ; Softanza, la fondation, construite, le sujet de ce soir ; Aïcha, nommée, rien d'autre encore ; les applications au-dessus. Takamba à côté : comment tout cela se construit. Dire chaque stade à voix haute ; ne jamais dire que Haro est disponible.
```

<<< scene id="learn" page="book.html" label="Apprendre" >>>
<div class="eyebrow">Le système d'apprentissage · 15 chapitres × 4 langues, chaque cellule a tourné · fr, ar, ha : brouillons · bureau seulement · aucun adoptant</div>
## Trois étapes : <i>introduction, livre, documentation</i>
<div class="pair">
<div><h4>Haoussa · Nemo, sannan ka aiwatar</h4><p>Kowane wurin aiki yana karɓar buƙatu: gidan abinci yana karɓar oda, banki yana karɓar tikiti.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre></div>
<div><h4>Français · Trouver, puis agir</h4><p>Tout lieu de travail reçoit des demandes : un restaurant reçoit des commandes, une banque reçoit des tickets.</p><pre>o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.NumberOfItems()
#--> 6</pre></div>
</div>
<p><a href="../reader.html">Ouvrir le lecteur</a> · en · fr · ar · ha · construit en 3 minutes 22 secondes, chaque cellule verte</p>
```notes
Ouvrir le lecteur par le lien, passer en haoussa, puis en arabe (de droite à gauche). Dire : « Ce lecteur a été construit en trois minutes trente-sept : chaque cellule de chaque chapitre dans chaque langue a été exécutée, et la construction serait rouge si une seule avait échoué. » Puis : « Le zarma n'y est pas. C'est votre invitation. » Dire les limites avant les questions : le français, l'arabe et le haoussa sont des brouillons, aucune de leurs 35 unités n'est encore relue par un locuteur natif ; les cellules s'exécutent sur le bureau, pas dans le navigateur ; aucune institution ne l'a adopté.
```

<<< scene id="africa" page="africa.html" label="Afrique" >>>
<div class="eyebrow">Née en Afrique</div>
<figure><img src="../assets/img/niger-density.png" alt="Carte de densité de population du Niger par région, rendue par le moteur." width="1500" height="1240"><figcaption>« Où vit le Niger » : rendue par le moteur en 5,9 secondes à partir des frontières officielles et du recensement de 2012 ; les superficies sont mesurées par la routine géodésique de Softanza.</figcaption></figure>
```notes
« Agadez, c'est 52 % du territoire et 2,8 % des habitants. Ce chiffre n'a pas été copié d'une table : la bibliothèque a mesuré la superficie de chaque région sur l'ellipsoïde. » Puis les racines : Sonibank, RestoLean, l'étude DIKO ; le cours en haoussa ; Harobanda, le nom du pont de Niamey.
```

<<< scene id="start" page="start.html" label="Démarrer" >>>
<div class="eyebrow">Démarrer, en une heure</div>
## Un dépôt public. <i>Un dossier, copié.</i>
<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib</pre>
<div class="run"><div><div class="lbl">premier</div><pre>? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie</div><pre>┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p>github.com/mayouni/stzlib · édition ouverte, MIT · édition entreprise : le même code, plus les personnes qui l'ont écrit</p>
```notes
Clore par l'invitation : le cours en zarma, la relecture native du haoussa, et les premiers « Softanza Architects ». Tout ce qui a été montré ce soir est un fichier que l'on peut ouvrir, et chaque chiffre renvoie au fichier qui le prouve.
```
