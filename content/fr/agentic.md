---
title: Agentique
title_html: L'agent propose. <i>Il ne commet pas.</i>
kicker: Le paradigme agentique, à la manière Softanza
lede: Les machines écrivent et agissent désormais. La réponse de Softanza n'est pas de leur faire confiance avec plus de soin ; c'est de changer l'endroit où elles ont le droit de se tenir. Un agent parle une langue déclarée, répète dans un atelier, fait face à un tribunal, et ne détient jamais la capacité de commettre.
description: Le paradigme agentique de Softanza : l'agent propose, un atelier répète, un tribunal juge, seul un acteur gouverné commet.
---

Une langue Softanza a six lecteurs : le programmeur, l'analyste, le designer, le décideur, l'éducateur, et l'agent. L'agent est celui pour qui elle a été conçue en dernier, et celui qui la parle le plus. Quatre choses rendent cette rencontre sûre.

<figure class="diagram"><img src="../assets/img/diagrams/govern-fr.png" alt="Un flux vertical : l'agent propose un plan ; l'atelier le répète sur un jumeau du système ; le tribunal juge le périmètre, la capacité et la réversibilité ; un acteur gouverné commet. À côté du tribunal, un refus : un modèle de langage ne détient jamais la capacité d'agir, même quand on le trompe. En dessous, un humain lit le plan et peut refuser une étape." width="1376" height="768"><figcaption>La boucle, telle que les gardes l'exercent. Mesuré le 2026-10-01 : 610 suppressions proposées par un agent, aucune commise ; l'exercice de confinement 27 sur 27.</figcaption></figure>

<div class="cards">
<div class="card"><h3>1 · La grammaire contraint</h3><p>Chaque langue déclarée émet sa grammaire de contrainte, et le décodeur du moteur rend impossible l'émission d'un jeton qui la viole. L'agent ne peut prononcer que des phrases valides. La malformation meurt par construction ; la fausseté fait toujours face au tribunal.</p></div>
<div class="card"><h3>2 · L'atelier répète</h3><p>Chaque écriture de fichier, chaque suppression, chaque mise à jour de mémoire va dans un jumeau virtuel qui ne tient aucune référence au réel. Le vrai fichier existe toujours ; l'atelier tient la version proposée. La seule sortie de l'agent est un plan, lisible opération par opération.</p></div>
<div class="card"><h3>3 · Le tribunal juge</h3><p>Un acteur qui ne dit pas ce qu'il couvre, ni si ses actes sont réversibles, est refusé avant son premier pas. Le plan passe le périmètre, les capacités, la gouvernance. Le risque et l'irréversibilité sont deux axes séparés : un petit acte qu'on ne peut défaire mérite plus de cérémonie qu'un grand acte qu'on peut défaire.</p></div>
<div class="card"><h3>4 · Un acteur gouverné commet</h3><p>Un modèle de langage ne détient jamais la capacité « à effet » : il ne commet rien, même trompé. Un humain, ou un acteur habilité, commet ; un humain peut rejeter une seule étape, et le refus est consigné.</p></div>
</div>

<div class="run"><div><div class="lbl">Ce que l'agent a proposé</div><pre>What it WOULD have done (610 operations):
  Update plan (610 of 610 operations to commit):
  * 1. delete file '…/courses/elementary-introduction/course.zknw'
  * 2. delete file '…/courses/elementary-introduction/curriculum.zknw'
  * 3. delete file '…/chapters/01-find-then-apply.ar.md'
  ...</pre></div><div class="out"><div class="lbl">Ce qui s'est passé</div><pre>An AI helper asks to commit the plan:
  actor 'amina-helper-llm' cannot commit
  -- it lacks the 'effectful' capability
     (required by operation 1)
PROVED  the court admitted the declaration
PROVED  the agent rehearsed every deletion
PROVED  the course folder still holds all 610 files
PROVED  an AI cannot commit what the agent proposed</pre></div></div>
<p class="ran">exécuté le 2026-09-30 à 23:10 par <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/education/demo/demo.ring">la démonstration pour décideurs</a>, scène 6 ; le même mécanisme avec un relecteur humain qui rejette une étape est le garde <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/virtual_system_twin_narrated.ring">virtual_system_twin_narrated</a>, scène 5</p>

<p class="way"><span>La manière Softanza</span> La sécurité n'est pas une consigne qui demande au modèle d'être prudent. C'est une architecture dans laquelle le modèle n'a rien avec quoi être prudent.</p>

<p>Ce qui rend l'esprit d'un agent programmatique et non un modèle dans une boucle, c'est une échelle de motifs, de facultés et d'agents : <a href="softanzuter.html">le Softanzuter</a>.</p>
