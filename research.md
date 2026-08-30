---
layout: default
title: Research
description: Research directions, network measurement and security, and Responsible AI.
---

<div class="wrap wrap-wide">
  <p class="kicker">Research</p>
  <h1>Research directions</h1>
  <p class="lede">Two threads run through my work: building data-driven systems that measure and make sense of network infrastructure, and figuring out what it costs, both environmentally and to public health, to run the AI systems we're increasingly relying on, plus adjacent work in blockchain security and machine unlearning. Titles, venues, and DOIs are on <a href="{{ '/publications/' | relative_url }}">Publications</a>; this page is about what each project actually does.</p>

  <h2>Network measurement &amp; security <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Michalis Faloutsos)</span></h2>
  <p>I design data-driven systems for network-aware probing recommendation and anomaly detection, deciding what's worth measuring, rather than measuring everything. A core piece of this maps infrastructure by combining active and passive DNS (aDNS, pDNS) with server-side fingerprint analysis, to explain why a given host or service is likely malicious. One application of this pipeline is catching malware command-and-control (C2) traffic that's built to look like ordinary network activity.</p>

  <ul class="highlight-list">
    <li>
      <strong>Network-aware probing recommendation &amp; malicious-infrastructure detection</strong>
      <p>Combines active and passive DNS history with server-side fingerprinting to prioritize infrastructure for active probing and explain why it's likely malicious, including malware C2 traffic disguised as ordinary activity. Ongoing; the codebase isn't public.</p>
    </li>
    <li>
      <strong>Anomaly-based incident detection in large-scale smart transportation systems</strong>
      <p>City-scale anomaly detection reaching about 90% true-positive detection at a 3% false-positive rate, nominated for Best Paper at ACM/IEEE ICCPS 2022.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/ICCPS22" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Scalable version of that transportation anomaly detector</strong>
      <p>Extends the same approach to scale across much larger city networks without losing detection accuracy.</p>
    </li>
    <li>
      <strong>Poisoning attacks against quantile-regression anomaly detectors</strong>
      <p>Studies how data-poisoning attacks degrade quantile-regression-based anomaly detection in cyber-physical systems, and what makes a detector robust again.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/quantile-poison-iwspa25" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Robust attack detection in smart grids under data poisoning</strong>
      <p>Keeps smart-grid anomaly detection reliable even when an attacker is actively poisoning the training data.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/CPSS22" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></h2>
  <p>Running AI systems has real environmental and public-health costs, and they aren't distributed evenly. This thread designs cost-aware spatial-temporal workload distribution, deciding when and where AI workloads run, to minimize those costs directly, alongside measuring the environmental footprint of generative-AI inference across cloud versus edge deployments.</p>

  <ul class="highlight-list">
    <li>
      <strong>Equity-aware spatial-temporal workload shifting (EquiShift)</strong>
      <p>Shifts AI data-center workloads across time and location to cut environmental costs without concentrating the burden on any one region.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/equishift-neurips2024-ccai" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Online allocation with replenishable budgets</strong>
      <p>An online allocator for resources that replenish over time, paired with a learning-augmented variant that keeps most of a trained predictor's everyday performance while staying anchored to a worst-case-safe strategy.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/replenish-opt" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Environmental footprints of generative AI inference, cloud vs. edge</strong>
      <p>Benchmarks the latency, power draw, and energy cost of six generative models (text, image, audio, OCR) across GPU tiers, to see whether faster hardware is actually greener.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/LLM_benchmarking" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Health-aware datacenter load shifting</strong>
      <p>GRU forecasters for demand, price, water use, and carbon intensity feed a convex scheduler that routes datacenter workload to minimize water and carbon costs, closing most of the gap to a perfect-foresight baseline. Under review.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/greenload-forecast" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <strong>Quantifying the water footprint of AI computing</strong>
      <p>Mentored an undergraduate researcher (Allison Hwang) building a tool that estimates the water footprint of computing from component-level energy use and regional electricity-generation water intensity. Presented at the UCR Summer Research Symposium, 2023.</p>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>More research</h2>
  <p>A couple of adjacent directions: machine unlearning, and blockchain-system security.</p>

  <ul class="highlight-list">
    <li>
      <strong>Correcting the hidden cost of forgetting in self-training models (PALMU)</strong>
      <p>Machine unlearning for self-training models, correcting for the accuracy that forgetting quietly costs elsewhere in the model. Under review at NeurIPS 2026.</p>
    </li>
    <li>
      <strong>Layer-oriented survey of blockchain security</strong>
      <p>A layer-by-layer survey of blockchain threats, vulnerabilities, and detection methods.</p>
    </li>
    <li>
      <strong>Survey of consensus algorithms in blockchain applications</strong>
      <p>Surveys consensus-algorithm architecture, taxonomy, and open operational issues across blockchain applications.</p>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>
</div>
