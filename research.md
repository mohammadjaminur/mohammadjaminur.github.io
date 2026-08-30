---
layout: default
title: Research
description: Research on selective network probing, C2 infrastructure, anomaly detection, sustainable AI systems, and machine unlearning.
---

<div class="wrap wrap-wide">
  <p class="kicker">Research</p>
  <h1>Research directions</h1>
  <p class="lede">My current Ph.D. research focuses on network measurement and security: I use DNS history and server fingerprints to choose targets for active probing and identify likely C2 infrastructure. During my M.S., I worked on anomaly detection in transportation and power systems. I have also studied the environmental and public-health costs of AI infrastructure. Paper titles, venues, and DOIs are listed on <a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>

  <h2>Network measurement &amp; security <span style="font-weight:500;color:var(--muted)">(current Ph.D. research with Dr.&nbsp;Michalis Faloutsos)</span></h2>
  <p>The goal is to collect useful evidence without probing every host. I develop methods that rank network infrastructure for follow-up measurements.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Using DNS history to prioritize probes for C2 infrastructure</strong>
      <p class="group-desc">I combine active and passive DNS history (aDNS and pDNS) with server-side fingerprints to rank hosts for follow-up probing. The system also records which DNS and fingerprint signals made each host suspicious. The aim is to find malware C2 infrastructure that blends into ordinary network activity. This project is ongoing, and the code is private.</p>
    </li>
  </ul>

  <h2>Anomaly detection in cyber-physical systems <span style="font-weight:500;color:var(--muted)">(M.S. research with Dr.&nbsp;Shameek Bhattacharjee, Western Michigan University)</span></h2>
  <p>During my M.S., I worked on detectors that distinguish attacks and operational incidents from normal changes in transportation and power-system data. We also studied whether those detectors remain reliable when an attacker poisons their training data.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Anomaly detection in smart systems <span class="group-note">(smart meters &amp; transportation)</span></strong>
      <p class="group-desc">This work covers two detection settings—transportation networks and power grids—and a shared security problem: whether the detectors still work after an attacker poisons their training data.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Smart transportation incident detection</p>
          <p class="sub-note">Our detector found incidents in city-scale traffic data with about a 90% true-positive rate and a 3% false-positive rate. The ICCPS 2022 paper was nominated for Best Paper, and a TCPS 2024 follow-up scaled the method to larger city networks.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/ICCPS22" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Smart-grid attack detection under data poisoning</p>
          <p class="sub-note">We designed a detector for smart-grid measurements and tested whether it remained accurate when an attacker deliberately corrupted part of its training data.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/CPSS22" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Poisoning attacks against quantile-regression anomaly detectors</p>
          <p class="sub-note">We measured how poisoned training data reduced the accuracy of quantile-regression anomaly detectors across cyber-physical systems, then evaluated defenses that restored detection accuracy.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/quantile-poison-iwspa25" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></h2>
  <p>The location and timing of an AI workload affect its electricity and water use, as well as the carbon emissions and local air pollution associated with its power supply. I have worked on schedulers that consider those costs and on measurements of generative-AI inference in cloud and edge settings.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Online learning for resource allocation</strong>
      <p class="group-desc">Online allocation requires each decision to be made before future demand is known. We developed an algorithm for a limited resource whose budget is replenished over time. A learning-augmented version follows a trained predictor when its advice is useful and falls back to an algorithm with a worst-case guarantee when it is not (<a href="https://github.com/mohammadjaminur/replenish-opt" target="_blank" rel="noopener noreferrer">code</a>).</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Data-center workload scheduling <span class="group-note">(energy, water &amp; carbon)</span></p>
          <p class="sub-note">The scheduler moves AI workloads across time and location to reduce energy, water, and carbon costs without placing most of the burden on one region.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/equishift-neurips2024-ccai" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Forecast-guided scheduling for environmental and public-health costs</p>
          <p class="sub-note">GRU models forecast demand, electricity price, water use, and carbon intensity. A convex scheduler uses those forecasts to place workloads while reducing energy, water, carbon, and public-health costs. It closes most of the performance gap with a scheduler that knows the future perfectly. Under review.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/greenload-forecast" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
        <li>
          <p class="sub-title">Comparing generative-AI inference in the cloud and at the edge</p>
          <p class="sub-note">We measured latency, power draw, and energy use for six generative models across several GPU tiers. The comparison shows when cloud hardware is more efficient and when edge hardware uses less energy.</p>
          <ul class="resource-links">
            <li><a href="https://github.com/mohammadjaminur/LLM_benchmarking" target="_blank" rel="noopener noreferrer">Code</a></li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>

  <h2>More research</h2>
  <p>I have also worked on machine unlearning and two surveys of blockchain security.</p>

  <ul class="project-groups">
    <li>
      <strong class="group-title">Machine unlearning for self-training models</strong>
      <p class="group-desc">Machine unlearning removes the influence of selected training examples from a trained model without retraining it from scratch. The challenge is to forget those examples without reducing accuracy on the data that remains.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Correcting the hidden cost of forgetting in self-training models (PALMU)</p>
          <p class="sub-note">PALMU measures and corrects the accuracy loss that unlearning can cause elsewhere in a self-training model. The paper is under review at NeurIPS 2026.</p>
        </li>
      </ul>
    </li>
    <li>
      <strong class="group-title">Blockchain-system security</strong>
      <p class="group-desc">I contributed to two surveys: one organizes blockchain threats by system layer, and the other compares consensus designs.</p>
      <ul class="sub-projects">
        <li>
          <p class="sub-title">Layer-oriented survey of blockchain security</p>
          <p class="sub-note">This survey connects threats and vulnerabilities at each layer of a blockchain system with the methods used to detect them.</p>
        </li>
        <li>
          <p class="sub-title">Survey of consensus algorithms in blockchain applications</p>
          <p class="sub-note">This survey compares consensus architectures, organizes the major algorithm families, and identifies unresolved deployment problems.</p>
        </li>
      </ul>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">Full papers &amp; venues on Publications →</a>
</div>
