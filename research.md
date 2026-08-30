---
layout: default
title: Research
description: Research directions, network measurement and security, and Responsible AI.
---

<div class="wrap wrap-wide">
  <p class="kicker">Research</p>
  <h1>Research directions</h1>
  <p class="lede">Two threads run through my work: building data-driven systems that measure and make sense of network infrastructure, and figuring out what it costs, both environmentally and to public health, to run the AI systems we're increasingly relying on, plus adjacent work in blockchain security and machine unlearning. Featured papers live on <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>

  <h2>Network measurement &amp; security <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Michalis Faloutsos)</span></h2>
  <p>I design data-driven systems for network-aware probing recommendation and anomaly detection, deciding what's worth measuring, rather than measuring everything. A core piece of this maps infrastructure by combining active and passive DNS (aDNS, pDNS) with server-side fingerprint analysis, to explain why a given host or service is likely malicious. One application of this pipeline is catching malware command-and-control (C2) traffic that's built to look like ordinary network activity.</p>

  <ul class="featured-list">
    <li>
      <span class="venue-tag">Ongoing</span>
      <p class="pub-title">Network-aware probing recommendation and malicious-infrastructure detection</p>
      <p class="pub-note">Combines active and passive DNS history with server-side fingerprinting to prioritize infrastructure for active probing and explain why it's likely malicious, including malware command-and-control (C2) traffic.</p>
    </li>
    <li>
      <span class="venue-tag">ACM/IEEE ICCPS 2022 · Best Paper Nominee</span>
      <p class="pub-title">Anomaly-based Incident Detection in Large Scale Smart Transportation Systems</p>
      <p class="pub-note">City-scale anomaly detection for smart transportation, reaching about 90% true-positive detection at a 3% false-positive rate.</p>
      <ul class="resource-links">
        <li><a href="https://doi.org/10.1109/ICCPS54341.2022.00026" target="_blank" rel="noopener noreferrer">Paper</a></li>
        <li><a href="https://github.com/mohammadjaminur/ICCPS22" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">ACM TCPS 2024</span>
      <p class="pub-title">Scalable Pythagorean Mean-based Incident Detection in Smart Transportation Systems</p>
      <p class="pub-note">Extends the transportation anomaly-detection work to scale across larger city networks.</p>
      <ul class="resource-links">
        <li><a href="https://doi.org/10.1145/3603381" target="_blank" rel="noopener noreferrer">Paper</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">IWSPA 2025</span>
      <p class="pub-title">Poisoning Attacks against Quantile L1 Regression in CPS Anomaly Detection Frameworks</p>
      <p class="pub-note">Studies how data-poisoning attacks degrade quantile-regression-based anomaly detectors, and what makes them robust again.</p>
      <ul class="resource-links">
        <li><a href="https://doi.org/10.1145/3716815.3729009" target="_blank" rel="noopener noreferrer">Paper</a></li>
        <li><a href="https://github.com/mohammadjaminur/quantile-poison-iwspa25" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">ACM CPSS 2022</span>
      <p class="pub-title">Robust Anomaly-based Attack Detection in Smart Grids under Data Poisoning Attacks</p>
      <p class="pub-note">Smart-grid anomaly detection that stays reliable even when an attacker is actively poisoning the training data.</p>
      <ul class="resource-links">
        <li><a href="https://doi.org/10.1145/3494107.3522778" target="_blank" rel="noopener noreferrer">Paper</a></li>
        <li><a href="https://github.com/mohammadjaminur/CPSS22" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
  </ul>

  <h2>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></h2>
  <p>Running AI systems has real environmental and public-health costs, and they aren't distributed evenly. This thread designs cost-aware spatial-temporal workload distribution, deciding when and where AI workloads run, to minimize those costs directly, alongside measuring the environmental footprint of generative-AI inference across cloud versus edge deployments.</p>

  <ul class="featured-list">
    <li>
      <span class="venue-tag">NeurIPS Climate Change AI Workshop 2024</span>
      <p class="pub-title">Equity-Aware Spatial-Temporal Workload Shifting for Sustainable AI Data Centers (EquiShift)</p>
      <p class="pub-note">Shifts AI data-center workloads across time and location to cut environmental costs without concentrating the burden on any one region.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/equishift-neurips2024-ccai" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">ACM SIGMETRICS / POMACS 2024</span>
      <p class="pub-title">Online Allocation with Replenishable Budgets: Worst Case and Beyond</p>
      <p class="pub-note">An online allocator for resources that replenish over time, plus a learning-augmented variant that keeps most of a trained predictor's everyday performance while staying anchored to a worst-case-safe strategy.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/replenish-opt" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">ACM SIGMETRICS AI Crossroads Workshop 2025</span>
      <p class="pub-title">A Case Study of Environmental Footprints for Generative AI Inference: Cloud versus Edge</p>
      <p class="pub-note">Benchmarks the latency, power draw, and energy cost of six generative models (text, image, audio, OCR) across GPU tiers, to see whether faster hardware is actually greener.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/LLM_benchmarking" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">IEEE Trans. Sustainable Computing · Under review</span>
      <p class="pub-title">Balancing the Public Health Impact of Data Centers via Geographical Load Shifting</p>
      <p class="pub-note">GRU forecasters for demand, price, water use, and carbon intensity feed a convex scheduler that routes datacenter workload to minimize water and carbon costs, cutting most of the gap to a perfect-foresight baseline.</p>
      <ul class="resource-links">
        <li><a href="https://github.com/mohammadjaminur/greenload-forecast" target="_blank" rel="noopener noreferrer">Code</a></li>
      </ul>
    </li>
    <li>
      <span class="venue-tag">UCR Summer Research Symposium 2023 · Mentored project</span>
      <p class="pub-title">Quantifying the Water Footprint of AI Computing</p>
      <p class="pub-note">Mentored an undergraduate researcher (Allison Hwang) building a tool that estimates the water footprint of computing from component-level energy use and regional electricity-generation water intensity.</p>
    </li>
  </ul>

  <h2>Other research</h2>
  <p>A couple of adjacent directions outside the two main threads above: machine unlearning, and blockchain-system security.</p>

  <ul class="featured-list">
    <li>
      <span class="venue-tag">NeurIPS 2026 · Under review</span>
      <p class="pub-title">PALMU: Correcting the Hidden Cost of Forgetting in Self-Training Models</p>
      <p class="pub-note">Machine unlearning for self-training models, correcting for the accuracy that forgetting quietly costs elsewhere in the model.</p>
    </li>
    <li>
      <span class="venue-tag">Future Internet 2025</span>
      <p class="pub-title">Securing Blockchain Systems: A Layer-Oriented Survey of Threats, Vulnerability Taxonomy, and Detection Methods</p>
      <p class="pub-note">A layer-by-layer survey of blockchain threats, vulnerabilities, and detection methods.</p>
    </li>
    <li>
      <span class="venue-tag">IEEE Access 2023</span>
      <p class="pub-title">A Survey on Consensus Algorithms in Blockchain-Based Applications</p>
      <p class="pub-note">Surveys consensus-algorithm architecture, taxonomy, and open operational issues across blockchain applications.</p>
      <ul class="resource-links">
        <li><a href="https://doi.org/10.1109/ACCESS.2023.3267047" target="_blank" rel="noopener noreferrer">Paper</a></li>
      </ul>
    </li>
  </ul>
</div>
