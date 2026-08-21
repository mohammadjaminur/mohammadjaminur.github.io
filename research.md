---
layout: default
title: Research
description: Research themes — network measurement and security, and Responsible AI.
---

<div class="wrap">
  <p class="kicker">Research</p>
  <h1>Research themes</h1>
  <p class="lede">Two threads run through my work: building data-driven systems that measure and make sense of network infrastructure, and figuring out what it costs — environmentally, and to public health — to run the AI systems we're increasingly relying on. Featured papers live on <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>

  <ul class="highlight-list">
    <li>
      <strong>Network measurement &amp; security <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Michalis Faloutsos)</span></strong>
      <p>I design data-driven systems for network-aware probing recommendation and anomaly detection — deciding what's worth measuring, rather than measuring everything. A core piece of this maps infrastructure by combining active and passive DNS (aDNS, pDNS) with server-side fingerprint analysis, to explain why a given host or service is likely malicious. One application of this pipeline: catching malware command-and-control (C2) traffic that's built to look like ordinary network activity.</p>
    </li>
    <li>
      <strong>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></strong>
      <p>Running AI systems has real environmental and public-health costs, and they aren't distributed evenly. This thread designs cost-aware spatial-temporal workload distribution — deciding when and where AI workloads run — to minimize those costs directly, alongside measuring the environmental footprint of generative-AI inference across cloud versus edge deployments.</p>
    </li>
  </ul>
</div>
