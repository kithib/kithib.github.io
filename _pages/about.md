---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently a Ph.D. student at **The University of Hong Kong (HKU)**, advised by Prof. [Difan Zou](https://difanzou.github.io/).

My research interests primarily lie in the **post-training of Large Language Models (LLMs)**, including Supervised Fine-Tuning (SFT), Prompt Optimization, and Reinforcement Learning (RL). Additionally, I am interested in the **theory of pre-training** and learning theories, such as Machine Learning Theory, Optimization Theory, and Reinforcement Learning Theory. Recently, I have been working on **Self-Evolving Agents and Agentic Reinforcement Learning**, with a focus on solving harder problems, generating more human-readable and preference-aligned outputs, improving token efficiency, and developing theoretically grounded algorithms with optimization guarantees.

My English proficiency is demonstrated by an **IELTS overall band score of 7.0**.

<span id="scholar-citation-summary">My publications have received <strong><span id="total_cit" aria-live="polite">411</span> citations</strong> on <a href="https://scholar.google.com/citations?user=Dv8hrakAAAAJ">Google Scholar</a>.</span>

If you are interested in my research, please feel free to contact me via [![Email](https://img.shields.io/badge/Email-Contact_Me-blue?style=flat&logo=gmail&logoColor=white)](mailto:weichenxing2023@email.szu.edu.cn).

<br/>

# 🔥 News


<div style="max-height: 200px; overflow-y: auto;">
<ul>

  <li><em>2026.08:</em> 🎉🎉 <a href="https://arxiv.org/abs/2603.01563">LFPO</a> is accepted by <strong>EMNLP 2026 Main Conference</strong>.</li>

  <li><em>2026.05:</em> 🎉🎉 <a href="https://arxiv.org/abs/2603.01375">ROSA2</a> is accepted by <strong>ICML 2026</strong>.</li>

  <li><em>2026.05:</em> We propose <a href="https://arxiv.org/abs/2605.02469">BOLT</a>, an offline training framework that mathematically aligns static SFT with the optimal Boltzmann policy in online RLVR, revealing that iterative BOLT strictly functions as Policy Mirror Descent (PMD). </li>

  <li><em>2026.04:</em> 🎉🎉 <a href="https://arxiv.org/abs/2510.21830">GAPO</a> is accepted by <strong>ACL 2026 Findings</strong>.</li>

  <li><em>2026.03:</em> We propose <a href="https://arxiv.org/abs/2603.15255">SAGE</a>, a method that enhances multi-step reasoning in LLMs through a closed-loop, self-evolving framework of four agents (Challenger, Planner, Solver, and Critic) that autonomously generate, plan, solve, and verify tasks using minimal human-labeled data. </li>

  <li><em>2026.03:</em> We propose <a href="https://arxiv.org/abs/2603.01563">LFPO</a>, which overcomes the likelihood intractability in Diffusion LLMs by directly optimizing denoising logits via contrastive positive/negative trajectories, achieving SOTA performance with significantly faster inference.  Check our <a href="https://github.com/kithib/LFPO"> Github</a>. </li>

  <li><em>2026.03:</em> We propose <a href="https://arxiv.org/abs/2603.01375">ROSA2</a>, which reformulates test-time adaptation as a co-adaptation framework that jointly optimizes interaction context and model parameters to significantly accelerate convergence speed. Check our <a href="https://github.com/kithib/ROSA2"> Github</a>. </li>

  <li><em>2026.01:</em> 🎉🎉 <a href="https://openreview.net/forum?id=V4zln7XiJj">R-Score</a> is accepted by <strong>ICLR 2026</strong>.</li>

  <li><em>2025.12:</em> 🎉🎉 <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/115973">ReDit</a> is accepted by <strong>NeurIPS 2025</strong>.</li>

  <li><em>2025.11:</em> 🎉🎉 <a href="https://dl.acm.org/doi/abs/10.1145/3746027.3758269">UniSVG</a> is accepted by <strong>ACM MM 2025 Dataset Track</strong>.</li>

  <li><em>2025.11:</em> 🎉🎉 <a href="https://aclanthology.org/2025.emnlp-main.37/">PAFT</a> is accepted by <strong>EMNLP 2025 Main Conference</strong>, and wins the <strong>SAC Highlights Award</strong> (TOP 2%) at <strong>EMNLP 2025!</strong> </li>

  <li><em>2025.10:</em> I serve as a reviewer for <strong>ICLR 2026</strong>.</li>

  <li><em>2025.10:</em> We propose <a href="https://arxiv.org/abs/2510.21830">GAPO</a>, a method that robustly handles skewed reward distributions with outliers in code-editing RL by adaptively computing advantages, leading to consistent performance improvements. Check our <a href="https://github.com/TsingZ0/verl-GAPO"> Github</a>.</li>

  <li><em>2025.10:</em> We propose <a href="https://arxiv.org/abs/2510.24832">R-Score</a>, a novel metric to quantify the learnability of queries in RL to enhenced the curriculum learning method. Check our <a href="https://github.com/zz-haooo/Re-Schedule"> Github</a>.</li>

  <li><em>2025.09:</em> We propose <a href="https://arxiv.org/abs/2509.23166">ROSA</a>, a lightweight algorithm for our test-time adaptation paradigm that enables LLMs to perform efficient in-conversation self-correction by updating parameters online using real-time user feedback. Check our <a href="https://github.com/kithib/ROSA"> Github</a>.</li>

  <li><em>2025.08:</em> We propose <a href="https://arxiv.org/abs/2508.07766">UniSVG</a>, a SVG dataset for improving MLLM SVG generate performance. Check our <a href="https://ryanlijinke.github.io/"> Project Page</a> and <a href="https://huggingface.co/datasets/lili24/UniSVG"> Hugging Face</a>.</li>

  <li><em>2025.06:</em> We propose <a href="https://arxiv.org/abs/2506.18631">ReDit</a>, a technique that enhances reinforcement learning in large language models by adding random perturbations to reward signals, improving training efficiency and convergence speed while maintaining performance. Check our <a href="https://github.com/kithib/ReDit"> Github</a>.</li>

  <li><em>2025.06:</em> 🎉🎉 <a href="https://aclanthology.org/2025.acl-long.713/">Flexora</a> is accepted by <strong>ACL 2025 Main Conference</strong>.</li>

  <li><em>2025.02:</em> We propose <a href="https://arxiv.org/abs/2502.12859">PAFT</a>, which dynamically adjusts prompts during training, improving robustness, generalization, and even inference speed. Check our <a href="https://github.com/kithib/PAFT"> Github</a>.</li>

  <li><em>2024.08:</em> We propose <a href="https://arxiv.org/abs/2408.10774">Flexora</a>, a novel method that enhances Large Language Model fine-tuning efficiency by selectively adapting only the most critical layers. Check our <a href="https://github.com/kithib/Flexora"> Github</a>.</li>

  <li><em>2024.02:</em> We propose <a href="https://arxiv.org/abs/2402.18679">Data Interpreter</a>, an LLM agent for solving data science problems. Check our <a href=" https://github.com/geekan/MetaGPT"> Github</a>.</li>
  
</ul>
</div>

<br/>

# 📝 Publications 
**&dagger; Equal Contribution**   

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2026</div><img src='images/LFPO.png' alt="LFPO" width="100%" style="display: block;"></div></div>
<div class='paper-box-text' markdown="1">

LFPO: Likelihood-Free Policy Optimization for Masked Diffusion Models

<strong>Chenxing Wei</strong>, Jiazhen Kang, Hong Wang, Jianqing Zhang, Hao Jiang, Xiaolong Xu, Ningyuan Sun, Ying He, F. Richard Yu, Yao Shu, Bo Jiang

[**Paper**](https://arxiv.org/abs/2603.01563)  |  [**GitHub** ](https://github.com/kithib/LFPO) 
- <strong>Algorithm (LFPO):</strong> Introduces **LFPO**, which overcomes the likelihood intractability in Diffusion LLMs by directly optimizing denoising logits via contrastive positive/negative trajectories, achieving SOTA performance with significantly faster inference
- <strong>Theory:</strong> Proves the theoretical equivalence of continuous Flow Matching and discrete Masked Diffusion, justifying efficient trajectory rectification beyond policy gradients

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/ROSA2.png' alt="ROSA2" width="100%" style="display: block;"></div></div>
<div class='paper-box-text' markdown="1">

Words & Weights: Streamlining Multi-Turn Interactions via Co-Adaptation

<strong>Chenxing Wei</strong>, Hong Wang, Ying He, Zhongxiang Dai, Bo Jiang, F. Richard Yu, Yao Shu

[**Paper**](https://arxiv.org/abs/2603.01375)  |  [**GitHub** ](https://github.com/kithib/ROSA2) 
- <strong>Algorithm (ROSA2):</strong> Introduces **ROSA2**, which reformulates test-time adaptation as a co-adaptation framework that jointly optimizes interaction context and model parameters to significantly accelerate convergence speed
- <strong>Theory:</strong> Rigorously proves that semantic refinement acts as a pre-conditioner to strictly reduce parameter shift and guarantee faster convergence to the optimal policy

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Workshop MTI-LLM</div><img src='images/ROSA.png' alt="ROSA" width="100%" style="display: block;"></div></div>
<div class='paper-box-text' markdown="1">

Test-Time Policy Adaptation for Enhanced Multi-Turn Interactions with LLMs


<strong>Chenxing Wei</strong>, Hong Wang, Ying He, Yao Shu, Fei Yu 

[**Paper**](https://arxiv.org/abs/2509.23166)  |  [**GitHub** ](https://github.com/kithib/ROSA) 
- <strong>Paradigm (T2PAM):</strong> Proposes a paradigm shifting alignment from offline training to test-time inference, utilizing conversational feedback for real-time policy updates
- <strong>Algorithm (ROSA):</strong> Introduces **ROSA**, a lightweight algorithm that performs single-step, analytical parameter updates for efficient in-conversation self-correction
- <strong>Theory:</strong> Proves monotonic error reduction at each turn and guarantees cumulative convergence to the user's optimal preference

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/ReDit.png' alt="ReDit" width="100%" style="display: block;"></div></div>
<div class='paper-box-text' markdown="1">

ReDit: Reward Dithering for Improved LLM Policy Optimization


<strong>Chenxing Wei</strong>, Jiarui Yu, Ying Tiffany He, Hande Dong, Yao Shu, Fei Yu

[**Paper**](https://arxiv.org/abs/2506.18631)  | [**OpenReview**](https://openreview.net/forum?id=pG1Y63MqHm) |  [**GitHub** ](https://github.com/kithib/ReDit) 
- <strong>Algorithm (ReDit):</strong> a method that injects zero-mean random noise into rewards to smoothen the landscape, enabling continuous and stable gradient estimation.
- <strong>Theory:</strong> proves that reward dithering effectively mitigates gradient anomalies (vanishing/exploding) and significantly accelerates convergence.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025</div><img src='images/PAFT.png' alt="PAFT" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

PAFT: Prompt-Agnostic Fine-Tuning


<strong>Chenxing Wei</strong>, Mingwen Ou, Ying Tiffany He, Yao Shu, Fei Richard Yu

[**Paper**](https://arxiv.org/abs/2502.12859)  |  [**GitHub** ](https://github.com/kithib/PAFT) 
- <strong>Algorithm (PAFT):</strong> Introduces **PAFT**, which minimizes the divergence between predictions from full prompts and "pattern-free" inputs, effectively decoupling task reasoning from specific instruction syntax.
- <strong>Theory:</strong> Theoretically guarantees reduced generalization error under prompt distribution shifts and empirically achieves state-of-the-art robustness.

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025</div><img src='images/Flexora.png' alt="Flexora" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Flexora: Flexible Low-Rank Adaptation for Large Language Models


<strong>Chenxing Wei&dagger;</strong>, Yao Shu&dagger;, Ying Tiffany He, Fei Yu

[**Paper** ](https://arxiv.org/abs/2408.10774)  |  [**GitHub** ](https://github.com/kithib/Flexora) 
- <strong>Algorithm (Flexora):</strong> Introduces Flexora, a framework that treats layer selection as a Hyperparameter Optimization (HPO) problem. It employs unrolled differentiation to automatically learn a policy that identifies and adapts only the most critical layers for specific downstream tasks.
- <strong>Theory:</strong> Provides theoretical insights into how automated, flexible layer selection effectively mitigates overfitting and enhances generalization compared to uniform adaptation.

</div>
</div>

<br>


# 🎡 Service
- Reviewer for ICLR 2026
- Reviewer for NeurIPS 2026
- Reviewer for EMNLP 2026

<br>


# 🎖 Honors and Awards

- *2026.06* Outstanding Graduation Thesis Awards, *Shenzhen University*
- *2026.06* Outstanding Graduates, *Shenzhen University*
- *2025.11* Senior Area Chair Highlights Award, *EMNLP 2025*
- *2025.10* National Scholarship, *Shenzhen University*
- *2025.09* First-Class Academic Scholarship, *Shenzhen University*
- *2023.09* Second-Class Academic Scholarship, *Shenzhen University*
- *2022.06* First Prize in the TI Cup National Undergraduate Electronics Design Contest, *Nanjing University of Aeronautics and Astronautics*
- *2021.06* First Prize in the Contemporary Undergraduate Mathematical Contest in Modeling, *Nanjing University of Aeronautics and Astronautics*

<br>

# 📖 Education
- The University of Hong Kong<img src="images/hku.jpg" alt="HKU Insignia" class="education-logo"/>

  Ph.D. Student, 2026.09 - Present

  Advisor: Prof. [Difan Zou](https://difanzou.github.io/)

<div class="education-separator"></div>


- Shenzhen University<img src="images/szu.jpg" alt="SZU Insignia" class="education-logo"/>

  Master, Computer Science, 2023.09 - 2026.06,

  Advisor: Prof. [Fei Richard Yu](https://scholar.google.com/citations?user=zuGMGBoAAAAJ), 
  Co-Advisor: Prof. [Yao Shu](https://yao.notion.site/)


<div class="education-separator"></div>


- Nanjing University of Aeronautics and Astronautics<img src="images/nuaa.png" alt="NUAA Insignia" class="education-logo"/>
  
  Undergraduate, 2019.09 - 2023.06, 
  
  Advisor: Prof. [Hanlin Sheng](https://ieeexplore.ieee.org/author/37088579434)

<div class="education-separator"></div>

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)
-->

# 💻 Internships


- ByteDance<img src="images/bytedance.png" alt="ByteDance Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, Trae Team, 2025.10 - 2026.06,

  Main contributions: 
  - Research on reinforcement learning for DLLM in code modification and proposes LFPO. 
  - Research on integrating browser-use agents with code generation agents for harness-guided web code improvement.
  


<br>


- Tencent<img src="images/tencent.png" alt="Tencent Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, CSIG, 2025.02 - 2025.09, 

  Main contributions: Research on self-play reinforcement learning framework for GUI agents.
  


<br>


- Tencent<img src="images/tencent.png" alt="Tencent Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, AI LAB, 2024.06 - 2024.12, 
  
  Main contributions: Research on emotion and action prediction model of the game NPC.

<br>

# 👾 Misc

<div style="max-width: 300px; margin: 0 auto; text-align: center;">
  <script type="text/javascript" id="mapmyvisitors" src="https://mapmyvisitors.com/map.js?d=wKqgeh-N90xIj8eybW-CQnEiRLxwelgkHx7ekkOyQL0&amp;cl=ffffff&amp;w=300"></script>
  <noscript>
    <a href="https://mapmyvisitors.com/web/1c7ya" title="Visit tracker">
      <img src="https://mapmyvisitors.com/map.png?d=wKqgeh-N90xIj8eybW-CQnEiRLxwelgkHx7ekkOyQL0&amp;cl=ffffff" alt="Visitor map" width="300" style="max-width: 100%; height: auto;" loading="lazy"/>
    </a>
  </noscript>
</div>
