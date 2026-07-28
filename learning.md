---
layout: default
title: Learning
description: Explorations in RL, machine unlearning, and agentic system security.
---

<div class="wrap wrap-wide">
  <p class="kicker">Learning</p>
  <h1>Things I’m exploring</h1>
  <p class="lede">Side threads beyond core research — hands-on experiments and topics I’m actively reading into. Starter links below; notes and demos will grow here.</p>

  <ul class="learning-list">
    <li>
      <h3>Reinforcement learning playground</h3>
      <p class="meta">Small interactive agents for intuition: car racing (continuous control), walking / locomotion, and road-crossing games (timing and risk). A way to feel policies, rewards, and credit assignment before scaling to research settings.</p>
      <ul class="resource-links">
        <li><a href="https://spinningup.openai.com/" target="_blank" rel="noopener noreferrer">OpenAI Spinning Up in Deep RL</a></li>
        <li><a href="https://gymnasium.farama.org/" target="_blank" rel="noopener noreferrer">Gymnasium</a> — standard RL environments</li>
        <li><a href="https://stable-baselines3.readthedocs.io/" target="_blank" rel="noopener noreferrer">Stable-Baselines3</a> — practical RL algorithms</li>
      </ul>
    </li>
    <li>
      <h3>Machine unlearning</h3>
      <p class="meta">How to make models <em>forget</em> training data on request — exact vs. approximate unlearning, evaluation of residual memorization, and ties to privacy, compliance, and responsible deployment.</p>
      <ul class="resource-links">
        <li><a href="https://arxiv.org/abs/1912.03817" target="_blank" rel="noopener noreferrer">Eternal Sunshine of the Spotless Net</a> — early machine unlearning survey framing</li>
        <li><a href="https://arxiv.org/abs/2201.09334" target="_blank" rel="noopener noreferrer">Machine Unlearning survey</a> (Nguyen et al.)</li>
        <li><a href="https://unlearning-challenge.github.io/" target="_blank" rel="noopener noreferrer">NeurIPS Machine Unlearning Challenge</a></li>
        <li><a href="https://blog.research.google/2023/06/announcing-first-machine-unlearning.html" target="_blank" rel="noopener noreferrer">Google Research — Machine Unlearning Challenge</a></li>
      </ul>
    </li>
    <li>
      <h3>Agentic systems &amp; coding-environment access</h3>
      <p class="meta">Analyzing LLM agents that write and run code — what they can read, write, and execute; sandboxing; tool permissions; and failure modes when access rights are too broad or poorly scoped. Intersects security review with how coding agents operate in real developer workflows.</p>
      <ul class="resource-links">
        <li><a href="https://owasp.org/www-project-top-10-for-large-language-model-applications/" target="_blank" rel="noopener noreferrer">OWASP Top 10 for LLM Applications</a></li>
        <li><a href="https://arxiv.org/abs/2402.06664" target="_blank" rel="noopener noreferrer">LLM Agents can Autonomously Hack Websites</a></li>
        <li><a href="https://arxiv.org/abs/2403.02691" target="_blank" rel="noopener noreferrer">InjecAgent</a> — tool-integrated agent security benchmark</li>
        <li><a href="https://docs.anthropic.com/en/docs/agents-and-tools/computer-use" target="_blank" rel="noopener noreferrer">Computer use / agent tool access</a> (Anthropic)</li>
      </ul>
    </li>
  </ul>
</div>
