---
title: De l'éditeur à l'appareil
title_html: De l'éditeur <i>à l'appareil</i>
kicker: La livraison, répétée avant d'être réelle
lede: La définition d'une solution devient un système qui tourne sur de vraies cibles comme un seul programme continu : défini, émulé, déployé, approvisionné. Entre votre éditeur et la machine d'un client, il y a un jumeau qui ne garde aucune référence à la réalité.
description: Le plan de livraison de Softanza : définir la solution et ses cibles, émuler sur un jumeau, déployer par un plan avec retour arrière par un acteur qui peut engager, et approvisionner, avec l'étape de chaque pas.
---

## La route, en cinq pas {#road}

<ol class="steps">
<li value="1"><b>Définir.</b> La solution et ses cibles sont déclarées comme artefacts avant tout code de fonction. Le code de fonction s'écrit dans une portée de déploiement que la cible peut refuser. <span class="rx-src">construit · voir <a href="narrations/stz-system-dev-to-deploy-narration.html">du développement au déploiement</a></span></li>
<li value="2"><b>Émuler.</b> Toute la solution tourne sur un jumeau, une copie du système qui ne garde aucune référence au vrai. <span class="rx-src">construit · voir <a href="narrations/stz-emulating-the-whole-solution-narration.html">émuler toute la solution</a></span></li>
<li value="3"><b>Planifier et approvisionner.</b> Le plan dit ce dont chaque cible a besoin et dans quel ordre. <span class="rx-src">construit · voir <a href="narrations/stz-planning-and-provisioning-a-deployment-narration.html">planifier et approvisionner</a></span></li>
<li value="4"><b>Déployer.</b> Approvisionner, puis stocker, puis lancer, puis vérifier, avec retour arrière, par un acteur qui peut engager. Une construction se déploie librement en émulation et en production seulement par le plan. <span class="rx-src">construit · voir <a href="narrations/stz-deploying-to-target-sites-narration.html">déployer sur les sites cibles</a></span></li>
<li value="5"><b>Tenir les secrets.</b> Les identifiants sont tenus dans un coffre qui se masque lui-même, et le passage de gouvernance est la seule route vers la production. <span class="rx-src">construit · voir <a href="narrations/stz-guarding-secrets-and-credentials-narration.html">secrets et identifiants</a></span></li>
</ol>

<p class="way"><span>La manière Softanza</span> Une solution est répétée avant d'être engagée, et une dépendance factice est permise sur le jumeau et refusée en production. Ce que vous voyez marcher en émulation est le même programme que celui qui est déployé, et le tribunal qui le juge ne change pas entre les deux.</p>

<p class="proof"><b>en construction</b> Le garde du déploiement passe 45 assertions sur 45, lu dans les fichiers de la bibliothèque. Les hôtes réels dépendent de l'infrastructure : le plan a été exercé sur des cibles émulées, et c'est sur l'hôte réel d'un client que reste le travail. Les articles ci-dessus s'exécutent dans l'exécuteur de ce site quand ils le peuvent, et leurs pages disent quels blocs ont tenu leur promesse.</p>
