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

I am currently a third-year Master's student at the School of Computer and Software, **Shenzhen University**, supervised by Prof. [Fei Richard Yu](https://scholar.google.com/citations?user=zuGMGBoAAAAJ). I am also fortunate to be advised by Prof. [Yao Shu](https://yao.notion.site/). 

My research interests primarily lie in the post-training of Large Language Models (LLMs), including Supervised Fine-Tuning (SFT), Prompt Optimization, and Reinforcement Learning. Additionally, I am interested in learning theories, such as machine learning theory and reinforcement learning theory. 

If you are interested in my research, please feel free to contact me via [![Email](https://img.shields.io/badge/Email-Contact_Me-blue?style=flat&logo=gmail&logoColor=white)](mailto:weichenxing2023@email.szu.edu.cn).

<br/>
# 🔥 News


<div style="max-height: 200px; overflow-y: auto;">
<ul>

  <li><em>2025.12:</em> 🎉🎉 <a href="https://neurips.cc/virtual/2025/loc/san-diego/poster/115973">ReDit</a> is accepted by <strong>NeurIPS 2025</strong>.</li>

  <li><em>2025.11:</em> 🎉🎉 <a href="https://dl.acm.org/doi/abs/10.1145/3746027.3758269">UniSVG</a> is accepted by <strong>ACM MM 2025 Dataset Track</strong>.</li>

  <li><em>2025.11:</em> 🎉🎉 <a href="https://aclanthology.org/2025.emnlp-main.37/">PAFT</a> is accepted by <strong>EMNLP 2025</strong>, and wins the <strong>SAC Highlights Award</strong> (TOP 2%) at <strong>EMNLP 2025!</strong> </li>

  <li><em>2025.10:</em> I serve as a reviewer for <strong>ICLR 2026</strong>.</li>

  <li><em>2025.10:</em> We propose <a href="https://arxiv.org/abs/2510.21830">GAPO</a>, a method that robustly handles skewed reward distributions with outliers in code-editing RL by adaptively computing advantages, leading to consistent performance improvements. Check our <a href="https://github.com/TsingZ0/verl-GAPO"> Github</a>.</li>

  <li><em>2025.10:</em> We propose <a href="https://arxiv.org/abs/2510.24832">R-Score</a>, a novel metric to quantify the learnability of queries in RL to enhenced the curriculum learning method. Check our <a href="https://github.com/zz-haooo/Re-Schedule"> Github</a>.</li>

  <li><em>2025.09:</em> We propose <a href="https://arxiv.org/abs/2509.23166">ROSA</a>, a lightweight algorithm for our test-time adaptation paradigm that enables LLMs to perform efficient in-conversation self-correction by updating parameters online using real-time user feedback. Check our <a href="https://github.com/kithib/ROSA"> Github</a>.</li>

  <li><em>2025.08:</em> We propose <a href="https://arxiv.org/abs/2508.07766">UniSVG</a>, a SVG dataset for improving MLLM SVG generate performance. Check our <a href="https://ryanlijinke.github.io/"> Project Page</a> and <a href="https://huggingface.co/datasets/lili24/UniSVG"> Hugging Face</a>.</li>


  <li><em>2025.06:</em> We propose <a href="https://arxiv.org/abs/2506.18631">ReDit</a>, a technique that enhances reinforcement learning in large language models by adding random perturbations to reward signals, improving training efficiency and convergence speed while maintaining performance. Check our <a href="https://github.com/kithib/ReDit"> Github</a>.</li>

  <li><em>2025.06:</em> 🎉🎉 <a href="https://aclanthology.org/2025.acl-long.713/">Flexora</a> is accepted by <strong>ACL 2025</strong>.</li>

  <li><em>2025.02:</em> We propose <a href="https://arxiv.org/abs/2502.12859">PAFT</a>, which dynamically adjusts prompts during training, improving robustness, generalization, and even inference speed. Check our <a href="https://github.com/kithib/PAFT"> Github</a>.</li>

  <li><em>2024.08:</em> We propose <a href="https://arxiv.org/abs/2408.10774">Flexora</a>, a novel method that enhances Large Language Model fine-tuning efficiency by selectively adapting only the most critical layers. Check our <a href="https://github.com/kithib/Flexora"> Github</a>.</li>

  <li><em>2024.02:</em> We propose <a href="https://arxiv.org/abs/2402.18679">Data Interpreter</a>, an LLM agent for solving data science problems. Check our <a href=" https://github.com/geekan/MetaGPT"> Github</a>.</li>
  
</ul>
</div>

<br/>
# 📝 Publications 
**&dagger; Equal Contribution**   

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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS2025</div><img src='images/ReDit.png' alt="ReDit" width="100%" style="display: block;"></div></div>
<div class='paper-box-text' markdown="1">

ReDit: Reward Dithering for Improved LLM Policy Optimization


<strong>Chenxing Wei</strong>, Jiarui Yu, Ying Tiffany He, Hande Dong, Yao Shu, Fei Yu

[**Paper**](https://arxiv.org/abs/2506.18631)  | [**OpenReview**](https://openreview.net/forum?id=pG1Y63MqHm) |  [**GitHub** ](https://github.com/kithib/ReDit) 
- <strong>Algorithm (ReDit):</strong> a method that injects zero-mean random noise into rewards to smoothen the landscape, enabling continuous and stable gradient estimation.
- <strong>Theory:</strong> proves that reward dithering effectively mitigates gradient anomalies (vanishing/exploding) and significantly accelerates convergence.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP2025</div><img src='images/PAFT.png' alt="PAFT" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

PAFT: Prompt-Agnostic Fine-Tuning


<strong>Chenxing Wei</strong>, Yao Shu, Mingwen Ou, Ying Tiffany He, Fei Richard Yu

[**Paper**](https://arxiv.org/abs/2502.12859)  |  [**GitHub** ](https://github.com/kithib/PAFT) 
- <strong>Algorithm (PAFT):</strong> Introduces **PAFT**, which minimizes the divergence between predictions from full prompts and "pattern-free" inputs, effectively decoupling task reasoning from specific instruction syntax.
- <strong>Theory:</strong> Theoretically guarantees reduced generalization error under prompt distribution shifts and empirically achieves state-of-the-art robustness.

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL2025</div><img src='images/Flexora.png' alt="Flexora" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Flexora: Flexible Low-Rank Adaptation for Large Language Models


<strong>Chenxing Wei&dagger;</strong>, Yao Shu&dagger;, Ying Tiffany He, Fei Yu

[**Paper** ](https://arxiv.org/abs/2408.10774)  |  [**GitHub** ](https://github.com/kithib/Flexora) 
- <strong>Algorithm (Flexora):</strong> Introduces Flexora, a framework that treats layer selection as a Hyperparameter Optimization (HPO) problem. It employs unrolled differentiation to automatically learn a policy that identifies and adapts only the most critical layers for specific downstream tasks.
- <strong>Theory:</strong> Provides theoretical insights into how automated, flexible layer selection effectively mitigates overfitting and enhances generalization compared to uniform adaptation.

</div>
</div>


# 🎖 Honors and Awards
- *2025.11* Senior Area Chair Highlights Award of EMNLP 2025.
- *2025.10* National Scholarship *Shenzhen University*
- *2025.09* First-Class Academic Scholarship *Shenzhen University*
- *2023.09* Second-Class Academic Scholarship Shenzhen University*
- *2022.06* First Prize in the TI Cup National Undergraduate Electronics Design Contest *Nanjing University of Aeronautics and Astronautics*
- *2021.06* First Prize in the Contemporary Undergraduate Mathematical Contest in Modeling *Nanjing University of Aeronautics and Astronautics*

<br>

# 📖 Educations
- Shenzhen University<img src="images/insignia/szu.png" alt="SZU Insignia" style="float: right; width: 90px;"/>

  Master, Computer Science, 2023.09 - (now), 

  Advisor: Prof. [Fei Richard Yu](https://scholar.google.com/citations?user=zuGMGBoAAAAJ), 
  Co-Advisor: Prof. [Yao Shu](https://yao.notion.site/)


<br>


- Nanjing University of Aeronautics and Astronautics<img src="images/insignia/nuaa.png" alt="NUAA Insignia" style="float: right; width: 100px;"/>
  
  Undergraduate, 2019.09 - 2023.06, 
  
  Advisor: Prof. [Hanlin Sheng](https://ieeexplore.ieee.org/author/37088579434)

<br>

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)
-->

# 💻 Internships


- ByteDance<img src="images/insignia/bytedance.png" alt="ByteDance Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, MarsCode Trae Team, 2025.10 - (now), 

  Main contributions: Research on reinforcement learning for diffusion language models in code modification
  


<br>


- Tencent<img src="images/insignia/tencent.png" alt="Tencent Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, CSIG CodeBuddy Team, 2025.02 - 2025.09, 

  Main contributions: Research on self-play reinforcement learning framework for GUI agents.
  


<br>


- Tencent<img src="images/insignia/tencent.png" alt="Tencent Insignia" style="float: right; width: 100px;"/>

  Algorithm Intern, AI LAB, 2024.06 - 2024.12, 
  
  Main contributions: Research on emotion and action prediction model of the game NPC and Scaling Law.

<br>

