---
title: Sécurité
title_html: Les chiffres <i>de la sécurité</i>
kicker: Mesurés, avec leurs limites
lede: Trente-huit garanties, chacune liée à un garde, et un exercice d'attaque rejoué le soir de la publication : ce qui a été mesuré, et où la mesure s'arrête.
description: Les chiffres de la sécurité de Softanza : 38 garanties avec leurs gardes, détection en 395 ms et confinement en 50 ms.
---

<div class="figures">
<div class="figure"><b>38</b><span>garanties, chacune liée à un garde</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/security/SOFTANZA_THREAT_MODEL.md">SOFTANZA_THREAT_MODEL.md</a></div>
<div class="figure"><b>395 ms</b><span>pour détecter un bourrage d'identifiants sur du vrai HTTP</span><a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/security/containment_drill_narrated.ring">containment_drill_narrated</a></div>
<div class="figure"><b>50 ms</b><span>pour le confiner : compte verrouillé, sessions terminées, vérifié de l'extérieur</span></div>
<div class="figure"><b>27 / 27</b><span>assertions de l'exercice de confinement</span></div>
</div>

L'exercice a été rejoué le 2026-10-01 à 00:41. Un modèle de langage joue l'enquêteur, propose le bon plan, et ne commet rien ; l'humain d'astreinte commet le même plan, et le confinement tient. Limites, énoncées par le modèle de menace lui-même : une seule forme d'attaque, en boucle locale, sur une seule machine ; la détection tourne à la demande, pas en continu.

<pre>WHEN  five bad passwords are sent over real HTTP
THEN  credential stuffing was detected                        [PASS]
WHEN  an LLM investigator tries to contain
THEN  it commits nothing                                       [PASS]
THEN  and the victim can still log in                          [PASS]
WHEN  the on-call human contains
THEN  the lock and the session revocation were committed       [PASS]
THEN  containment holds, verified from outside the target      [PASS]
>> TIME TO DETECT : 395 ms  (first bad password -> detection on verified evidence)
>> TIME TO CONTAIN: 50 ms   (detection -> account locked + sessions ended, verified)
TOTAL: 27 assertions, 27 pass, 0 fail      real 0m7.079s</pre>

<p class="proof">La narration complète : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/doc/narrations/stz-agents-that-cannot-hurt-you-narration.md">stz-agents-that-cannot-hurt-you-narration.md</a> · le garde de l'atelier : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/agentic/safeworld_narrated.ring">safeworld_narrated</a> (76 assertions) · la traversée gouvernée : <a href="https://github.com/mayouni/stzlib/blob/main/libraries/stzlib/base/test/system/governance_crossing_narrated.ring">governance_crossing_narrated</a> · les domaines dans l'Atlas : doctrine de gouvernance, agents et conversation, sécurité.</p>
