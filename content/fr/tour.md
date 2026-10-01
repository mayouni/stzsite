---
title: Présentation
description: Le site en mode présentation : chaque scène est une page, en plein écran.
help: → ou clic : suivant · ← : précédent · n : notes · h : menu · Échap : ouvrir la page
---

<<< scene id="onboarding" page="../index.html" label="Accueil" class="scene-image" >>>
<img class="bg" src="../assets/img/onboarding-elder.webp" alt="Un ancien en turban blanc lit une feuille de code dans une cour ; le mot SOFTANZA est peint sur le mur derrière lui.">
<div class="caption">
<div class="eyebrow">Softanza</div>
<p><b>La plateforme des makers à l'ère agentique.</b></p>
<p>Née en Afrique. Utile au monde !</p>
</div>
```notes
Laisser l'image parler dix secondes. Puis une phrase : « Cet homme lit du code. Le mur derrière lui dit déjà Softanza. Tout ce que je vais montrer ce soir tient dans cette image : la connaissance, le lieu, et une langue que l'on peut lire. »
```

<<< scene id="why" page="why.html" label="Pourquoi" >>>
<div class="eyebrow">L'acte fondateur</div>
# Déclarez <i>une langue</i>
<p>À l'ère agentique, on n'écrit plus des logiciels.</p>
<p>On <b>déclare des mondes</b> dans des langues faites pour leur domaine, et on <b>gouverne</b> la manière dont ces mondes changent.</p>
<p>Wolfram connaît les faits du monde. <b>Softanza connaît votre monde.</b></p>
```notes
Trois idées, une par ligne. Ne pas lire la page. L'exemple à donner à l'oral : une banque déclare ses entités, ses règles, ses acteurs ; le système répond « quels flux touchent le compte de dépôt, et que casse-t-on si j'ajoute un champ ». Wolfram ne peut pas répondre à cela : on ne lui a jamais donné votre banque.
```

<<< scene id="platform" page="platform.html" label="Plateforme" >>>
<div class="eyebrow">Le moteur et ses visages</div>
# Un moteur en Zig, <i>des langages pour visages</i>
<div class="figures">
<div class="figure"><b>401</b><span>fichiers source Zig</span></div>
<div class="figure"><b>134</b><span>narrations exécutées</span></div>
<div class="figure"><b>334</b><span>couloirs notés dans l'Atlas</span></div>
<div class="figure"><b>101 / 129 / 68 / 36</b><span>Strong / Solid / Partial / Emerging</span></div>
</div>
<p><b>Ring</b> est le visage d'aujourd'hui · <b>Ring++</b> est le pont · <b>Haro</b> est la langue d'après, au stade de la charte.</p>
```notes
Dire les stades tels quels : Ring on l'écrit aujourd'hui ; Ring++ existe et tourne, il arrive publiquement quand je l'annonce ; Haro n'est qu'une charte, rien n'est construit. La crédibilité de la plateforme, c'est que l'Atlas montre ses 36 couloirs « Emerging » à côté de ses 101 « Strong ».
```

<<< scene id="learn" page="learn.html" label="Apprendre" >>>
<div class="eyebrow">Le Système d'apprentissage · construit cette nuit, 15 chapitres × 4 langues</div>
<div class="embed"><div class="embed-bar"><a href="../reader.html">Plein écran</a><span>en · fr · ar · ha — chaque cellule s'est exécutée ; aucune sortie stockée</span></div><iframe src="../reader.html" title="Le lecteur du cours Softanza" loading="lazy"></iframe></div>
```notes
Ouvrir le menu du lecteur, passer en haoussa, puis en arabe (droite à gauche). Dire : « Ce lecteur a été construit cette nuit en trois minutes vingt-deux : chaque cellule de chaque chapitre dans chaque langue a été exécutée, et la construction serait rouge si une seule avait échoué. » Puis : « Le zarma n'y est pas. C'est votre invitation. »
```

<<< scene id="govern" page="govern.html" label="Gouverner" >>>
<div class="eyebrow">Des agents qui ne peuvent pas vous nuire</div>
# L'agent propose. <i>Il ne commet pas.</i>
<div class="run"><div><div class="lbl">Une étudiante lâche un agent qui « range » le cours</div><pre>Update plan (610 of 610 operations to commit):
* 1. delete file '…/course.zknw'
* 2. delete file '…/curriculum.zknw'
...</pre></div><div class="out"><div class="lbl">Le tribunal, cette nuit</div><pre>actor 'amina-helper-llm' cannot commit
-- it lacks the 'effectful' capability
PROVED  the course folder still holds all 610 files</pre></div></div>
<div class="figures">
<div class="figure"><b>38</b><span>garanties, chacune avec son garde</span></div>
<div class="figure"><b>395 ms</b><span>pour détecter une attaque, cette nuit</span></div>
<div class="figure"><b>50 ms</b><span>pour la contenir, vérifié de l'extérieur</span></div>
</div>
```notes
L'histoire à raconter : Amina écrit un agent qui « range » le cours. Il propose de supprimer les 610 fichiers. Il ne peut pas : il ne détient pas la capacité d'agir, il ne l'a jamais détenue. Un humain relit le plan et refuse. Puis les deux chiffres : l'attaque par bourrage d'identifiants a été détectée en 395 millisecondes et contenue en 50, cette nuit, sur ce portable, et le modèle de langage qui enquêtait n'a rien pu commettre.
```

<<< scene id="africa" page="africa.html" label="Afrique" >>>
<div class="eyebrow">Née en Afrique</div>
<figure><img src="../assets/img/niger-density.png" alt="Carte de densité de population du Niger par région, rendue par le moteur." width="1500" height="1240"><figcaption>« Where Niger lives » : rendue cette nuit par le moteur, en 5,9 secondes, à partir des frontières officielles et du recensement 2012 ; les surfaces sont mesurées par la routine géodésique de Softanza.</figcaption></figure>
```notes
« Agadez est 52 % du territoire et 2,8 % des habitants. Ce nombre n'a pas été copié d'une table : la bibliothèque a mesuré la surface de chaque région sur l'ellipsoïde. » Puis les racines : Sonibank, l'école des douanes, RestoLean ; le cours en haoussa ; Harobanda, le nom du pont de Niamey.
```

<<< scene id="products" page="products.html" label="Produits" >>>
<div class="eyebrow">La famille, avec ses stades</div>
<div class="cards">
<div class="card"><h3>Softanza <span class="pill built">construit</span></h3><p>La fondation et son moteur, publics.</p></div>
<div class="card"><h3>Le Système d'apprentissage <span class="pill built">construit</span></h3><p>Deux cours, quatre langues, onze gardes.</p></div>
<div class="card"><h3>Ring++ <span class="pill built">en chantier</span></h3><p>Le pont : machine virtuelle et compilateur en Zig.</p></div>
<div class="card"><h3>Haro <span class="pill charter">charte</span></h3><p>La langue d'après. Rien n'est construit.</p></div>
<div class="card"><h3>Harobanda <span class="pill built">construit</span></h3><p>La machine déclarée, MIT, démarre en émulateur.</p></div>
<div class="card"><h3>Aïcha <span class="pill named">nommée</span></h3><p>Le visage à venir du palier neuronal.</p></div>
<div class="card"><h3>Zin · Refine · Studio</h3><p><span class="pill built">construit</span> <span class="pill spec">spécification</span> <span class="pill spec">spécification</span></p></div>
<div class="card"><h3>HaroBase · Bangalo · COBOL</h3><p><span class="pill spec">spécification</span> <span class="pill built">construit</span> <span class="pill proposal">proposition</span></p></div>
</div>
```notes
Un mot par carte, et le stade à voix haute. Aïcha : « c'est le nom que je donne au modèle de langage de Softanza ; aucun produit ne porte ce nom aujourd'hui ». Ne jamais dire que Haro est disponible, ni que Ring est mort.
```

<<< scene id="start" page="start.html" label="Commencer" >>>
<div class="eyebrow">Commencer, en une heure</div>
# Deux dépôts publics. <i>Un dossier, copié.</i>
<pre>git clone https://github.com/mayouni/stzlib.git
cd stzlib/libraries/stzlib
ring premier.ring</pre>
<div class="run"><div><div class="lbl">premier.ring</div><pre>load "stzlib.ring"
? Q("Softanza").Boxed()</pre></div><div class="out"><div class="lbl">Sortie, cette nuit</div><pre>┌──────────┐
│ Softanza │
└──────────┘</pre></div></div>
<p>github.com/mayouni/stzlib · codeberg.org/MAyouni/stzlib · ce site : github.com/mayouni/stzsite</p>
```notes
Terminer par l'invitation : le cours en zarma, la relecture native du haoussa, et les premières « Architectes Softanza ». Tout ce qui a été montré ce soir est un fichier que l'on peut ouvrir, et chaque chiffre renvoie au fichier qui le prouve.
```
