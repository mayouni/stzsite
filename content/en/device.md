---
title: From the editor to the device
title_html: From the editor <i>to the device</i>
kicker: Delivery, rehearsed before it is real
lede: A solution's definition becomes a running system on real targets as one continuous program: defined, emulated, deployed, provisioned. Between your editor and a customer's machine there is a twin that holds no reference to reality.
description: The Softanza delivery plane: define the solution and its targets, emulate on a twin, deploy through a plan with rollback by an actor that may commit, and provision, with the stage of each step.
---

## The road, in five steps {#road}

<ol class="steps">
<li value="1"><b>Define.</b> The solution and its targets are declared as artefacts before any feature code. Feature code is written in a deployment scope that the target can refuse. <span class="rx-src">built · see <a href="narrations/stz-system-dev-to-deploy-narration.html">from dev to deploy</a></span></li>
<li value="2"><b>Emulate.</b> The whole solution runs on a twin, a copy of the system that holds no reference to the real one. <span class="rx-src">built · see <a href="narrations/stz-emulating-the-whole-solution-narration.html">emulating the whole solution</a></span></li>
<li value="3"><b>Plan and provision.</b> The plan says what each target needs and in what order. <span class="rx-src">built · see <a href="narrations/stz-planning-and-provisioning-a-deployment-narration.html">planning and provisioning</a></span></li>
<li value="4"><b>Deploy.</b> Provision, then store, then launch, then verify, with rollback, by an actor that may commit. A build can be deployed to emulation freely and to production only through the plan. <span class="rx-src">built · see <a href="narrations/stz-deploying-to-target-sites-narration.html">deploying to target sites</a></span></li>
<li value="5"><b>Hold the secrets.</b> Credentials are held in a store that redacts itself, and the governance crossing is the only road to production. <span class="rx-src">built · see <a href="narrations/stz-guarding-secrets-and-credentials-narration.html">secrets and credentials</a></span></li>
</ol>

<p class="way"><span>The Softanza way</span> A solution is rehearsed before it is committed, and a fake dependency is allowed on the twin and refused in production. What you see work in emulation is the same program that is deployed, and the court that judges it does not change between the two.</p>

<p class="proof"><b>in construction</b> The deployment guard passes 45 assertions of 45, read from the library's files. Live hosts are gated by infrastructure: the plane has been exercised against emulated targets, and a real customer host is where the remaining work is. The articles above run in this site's runner where they can, and their pages say which blocks kept their promise.</p>
