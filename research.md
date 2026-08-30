---
layout: default
title: Research
description: Research directions, network measurement and security, and Responsible AI.
---

<div class="wrap wrap-wide">
  <p class="kicker">Research</p>
  <h1>Research directions</h1>
  <p class="lede">Two threads run through my work: building data-driven systems that measure and make sense of network infrastructure, and figuring out what it costs, both environmentally and to public health, to run the AI systems we're increasingly relying on, plus adjacent work in blockchain security and machine unlearning. Titles, venues, and DOIs are on <a href="{{ '/publications/' | relative_url }}">Publications</a>; this page groups the underlying projects by what each one is actually trying to do.</p>

  <h2>Network measurement &amp; security <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Michalis Faloutsos)</span></h2>
  <p>I design data-driven systems for network-aware probing recommendation and anomaly detection, deciding what's worth measuring, rather than measuring everything.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Understanding C2 infrastructure via DNS &amp; domain history, to optimize active probing</strong>
      <p class="group-desc">Combines active and passive DNS history (aDNS, pDNS) with server-side fingerprinting to flag likely-malicious infrastructure, including C2 traffic disguised as ordinary activity. Ongoing, not public.</p>
    </li>
    <li>
      <strong class="group-title">Anomaly detection in smart autonomous systems <span class="group-note">(smart meter &amp; smart transportation)</span></strong>
      <p class="group-desc">Three projects: transportation networks, power grids, and the poisoning-robustness question underneath both.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Smart transportation incident detection</p>
          <p class="sub-note">City-scale anomaly detection at ~90% true-positive / 3% false-positive (ICCPS 2022, Best Paper Nominee), later scaled to larger city networks (TCPS 2024).</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/ICCPS22" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Smart-grid attack detection under data poisoning</p>
          <p class="sub-note">Keeps smart-grid anomaly detection reliable under active data-poisoning attacks.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/CPSS22" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Poisoning attacks against quantile-regression anomaly detectors</p>
          <p class="sub-note">Studies how poisoning attacks degrade quantile-regression anomaly detectors across CPS domains, and what makes them robust again.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/quantile-poison-iwspa25" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></h2>
  <p>Running AI systems has real environmental and public-health costs, and they aren't distributed evenly. This thread designs cost-aware, learning-based resource allocation to minimize those costs directly, and measures where careless AI deployment makes them worse.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Online learning for resource allocation</strong>
      <p class="group-desc">An online allocator for resources that replenish over time, with a learning-augmented variant that keeps most of a trained predictor's everyday performance while staying anchored to a worst-case-safe fallback (<a href="https://github.com/mohammadjaminur/replenish-opt" target="_blank" rel="noopener noreferrer">code</a>). Applied below to two data-center cost problems and one AI-deployment question.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Datacenter environmental-cost load balancing <span class="group-note">(energy, water, carbon)</span></p>
          <p class="sub-note">Shifts AI data-center workloads across time and location to cut environmental costs without concentrating the burden on one region.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/equishift-neurips2024-ccai" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Datacenter public-health &amp; energy-cost load balancing</p>
          <p class="sub-note">GRU forecasters for demand, price, water, and carbon feed a convex scheduler that shifts workload to cut water, carbon, and health costs, closing most of the gap to a perfect-foresight baseline. Under review.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/greenload-forecast" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Benchmarking LLM inference on cloud vs. edge</p>
          <p class="sub-note">Benchmarks latency, power draw, and energy cost across six generative models and GPU tiers, to show whether bigger hardware is actually the greener choice.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/LLM_benchmarking" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>More research</h2>
  <p>A couple of adjacent directions: machine unlearning, and blockchain-system security.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Ensuring the right to forget: machine unlearning under different learning setups</strong>
      <p class="group-desc">Removing a data point's influence from a trained model without retraining from scratch, and without quietly degrading accuracy elsewhere.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Correcting the hidden cost of forgetting in self-training models (PALMU)</p>
          <p class="sub-note">Machine unlearning for self-training models, correcting for the accuracy that forgetting quietly costs elsewhere in the model. Under review at NeurIPS 2026.</p>
        </li>
      </ul>
    </li>
    <li>
      <strong class="group-title">Blockchain-system security</strong>
      <p class="group-desc">Two survey papers mapping the threat landscape across blockchain layers and consensus designs.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Layer-oriented survey of blockchain security</p>
          <p class="sub-note">A layer-by-layer survey of blockchain threats, vulnerabilities, and detection methods.</p>
        </li>
        <li>
          <p class="sub-title">Survey of consensus algorithms in blockchain applications</p>
          <p class="sub-note">Surveys consensus-algorithm architecture, taxonomy, and open operational issues across blockchain applications.</p>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>
</div>
