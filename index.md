---
layout: default
title: Home
layout_class: home
description: Mohammad Jaminur Islam is a UC Riverside Ph.D. student studying network measurement, security, and anomaly detection.
---

<div class="wrap wrap-wide">
  <section class="hero-card">
    <p class="job-banner">I am seeking academic and industry research positions starting in 2027, including postdoctoral, <strong>AI Engineer</strong>, and <strong>Applied Scientist</strong> roles. My main areas are network measurement, security, and trustworthy AI. <a href="{{ site.cv_url }}" target="_blank" rel="noopener noreferrer">CV</a> · <a href="mailto:{{ site.email }}">Get in touch</a></p>

    <div class="profile">
    <img class="avatar avatar-lg" src="{{ '/profile.jpg' | relative_url }}" alt="Portrait of Mohammad Jaminur Islam" width="160" height="160">
    <div>
      <h1 class="profile-name">Mohammad Jaminur Islam</h1>
      <p class="profile-pitch">I use DNS history, server fingerprints, and anomaly detection to find suspicious network infrastructure without scanning everything.</p>
      <p class="profile-role">Ph.D. Student · Computer Science · UC Riverside</p>

      <p class="profile-bio">My current Ph.D. research, advised by Dr.&nbsp;Michalis Faloutsos, combines active and passive DNS history with server fingerprints to identify likely malware command-and-control (C2) infrastructure and choose hosts for active probing. During my M.S. at Western Michigan University, I worked with Dr.&nbsp;Shameek Bhattacharjee on anomaly detection in transportation and smart-grid systems. I have also worked with Dr.&nbsp;Shaolei Ren on schedulers that account for the energy, water, carbon, and public-health costs of AI data centers.</p>
      <p class="tag-row">
        <span class="tag">Network Measurement</span>
        <span class="tag">DNS &amp; Fingerprinting</span>
        <span class="tag">Anomaly Detection</span>
        <span class="tag">Responsible &amp; Sustainable AI</span>
      </p>
    </div>
    </div>
  </section>

  <h2>Research highlights</h2>
  <ul class="highlight-list">
    <li>
      <strong>Network measurement &amp; security</strong>
      <p>Scanning every host is expensive. I use active and passive DNS history and server fingerprints to rank hosts, so active probes focus on infrastructure most likely to reveal malware C2 activity.</p>
    </li>
    <li>
      <strong>Anomaly detection in cyber-physical systems <span style="font-weight:500;color:var(--muted)">(M.S. research with Dr.&nbsp;Shameek Bhattacharjee)</span></strong>
      <p>At Western Michigan University, I developed and evaluated incident and attack detectors for transportation and smart-grid data, including settings where an attacker poisons the detector's training data.</p>
    </li>
    <li>
      <strong>Responsible AI <span style="font-weight:500;color:var(--muted)">(with Dr.&nbsp;Shaolei Ren)</span></strong>
      <p>Where and when an AI job runs changes its energy, water, carbon, and public-health costs. I have developed schedulers that use those differences and measured the cost of generative-AI inference in cloud and edge settings.</p>
    </li>
  </ul>
  <a class="more-link" href="{{ '/research/' | relative_url }}">Research directions →</a>

  <h2>Selected publications</h2>
  <ul class="featured-list">
    <li>
      <span class="venue-tag">ICCPS 2022 · Best Paper Nominee</span>
      <p class="pub-title">Anomaly-based Incident Detection in Large Scale Smart Transportation Systems</p>
      <p class="pub-note">A city-scale traffic detector that achieved about a 90% true-positive rate with a 3% false-positive rate.</p>
    </li>
    <li>
      <span class="venue-tag">NeurIPS 2024 · CCAI Workshop</span>
      <p class="pub-title">Equity-Aware Spatial-Temporal Workload Shifting for Sustainable AI Data Centers</p>
      <p class="pub-note">A scheduler that shifts AI workloads across time and location without placing most of the environmental burden on one region.</p>
    </li>
    <li>
      <span class="venue-tag">ACM SIGMETRICS 2024</span>
      <p class="pub-title">Online Allocation with Replenishable Budgets: Worst Case and Beyond</p>
      <p class="pub-note">Algorithms for allocating a resource whose budget is replenished over time when future demand is unknown.</p>
    </li>
  </ul>
  <a class="more-link" href="{{ '/publications/' | relative_url }}">All publications →</a>

  <h2>News</h2>
  <table class="news-table">
    <tbody>
      <tr>
        <td class="news-date">Ongoing</td>
        <td class="news-body">Developing a system that combines DNS history and server fingerprints to prioritize active probes for likely C2 infrastructure.</td>
      </tr>
      <tr>
        <td class="news-date">2026</td>
        <td class="news-body">Two manuscripts are under review: one on the public-health cost of data-center load shifting and one on machine unlearning for self-training models.</td>
      </tr>
      <tr>
        <td class="news-date">2025</td>
        <td class="news-body">Our comparison of generative-AI inference in cloud and edge settings was accepted at the ACM SIGMETRICS AI Crossroads workshop.</td>
      </tr>
      <tr>
        <td class="news-date">2024</td>
        <td class="news-body">Our work on equity-aware workload shifting for AI data centers was accepted at the NeurIPS Climate Change AI workshop.</td>
      </tr>
      <tr>
        <td class="news-date">2024</td>
        <td class="news-body">Our paper <em>Online Allocation with Replenishable Budgets</em> was published at ACM SIGMETRICS 2024.</td>
      </tr>
    </tbody>
  </table>
  <a class="more-link" href="{{ '/news/' | relative_url }}">All news &amp; timeline →</a>

  <h2>Teaching</h2>
  <ul class="highlight-list">
    <li>
      <strong>Discussion sections &amp; lab instruction</strong>
      <p>For <span class="course-code">CS 170</span> (Introduction to Artificial Intelligence), I led discussions on search and optimization, adversarial games, constraint satisfaction, Markov decision processes, reinforcement learning, and probabilistic reasoning. The Summer 2026 course focused on reinforcement learning, where I also gave a guest lecture on deep neural networks. For <span class="course-code">CS 105</span>, I led applied data-analysis labs and guest lectures on deep neural networks and generative models, including GANs and autoencoders.</p>
    </li>
  </ul>
  <a class="more-link" href="{{ '/teaching/' | relative_url }}">Teaching experience →</a>
</div>
