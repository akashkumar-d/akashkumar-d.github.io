---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Preprints and Manuscripts

<ul>
  <li>
    <b>Is Interpretability at Odds with Accuracy? Inapproximability of Decision Trees by Shallow Networks</b><br>
  <span class="author-self">A Kumar</span><br>
    <i>In submission.</i><br>
    ArXiv (coming soon) · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">Abstract forthcoming.</div></details>
  </li>
  <li>
    <b>Learning Smooth Distance Functions via Queries</b><br>
  <span class="author-self">A Kumar</span>, S Dasgupta<br>
    <a href="https://arxiv.org/abs/2412.01290">ArXiv</a>
    {% assign preprint_queries = site.publications | where: "title", "Learning Smooth Distance Functions via Queries" | first %}
    {% if preprint_queries and preprint_queries.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ preprint_queries.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Convergence of Nearest Neighbor Selective Classification</b><br>
  <span class="author-self">A Kumar</span>, S Dasgupta<br>
    <i>Manuscript on request.</i>
    {% assign preprint_convergence = site.publications | where: "title", "Convergence of Nearest Neighbor Selective Classification" | first %}
    {% if preprint_convergence and preprint_convergence.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ preprint_convergence.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries</b><br>
  <span class="author-self">A Kumar</span>, A Singla, Y Yue, Y Chen<br>
    <a href="https://arxiv.org/abs/2006.14677">ArXiv</a>
    {% assign preprint_avg = site.publications | where: "title", "Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries" | first %}
    {% if preprint_avg and preprint_avg.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ preprint_avg.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Deletion to Induced Matching</b><br>
  <span class="author-self">A Kumar</span>, M Kumar<br>
    <a href="https://arxiv.org/abs/2008.09660">ArXiv</a>
    {% assign preprint_dim = site.publications | where: "title", "Deletion to Induced Matching" | first %}
    {% if preprint_dim and preprint_dim.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ preprint_dim.abstract }}</div></details>{% endif %}
  </li>
</ul>

---

## Publications

<!-- Manual list as requested -->
<ul>
  <li>
    <b>A Gap Between the Gaussian RKHS and Neural Networks: An Infinite-Center Asymptotic Analysis</b><br>
  <span class="author-self">A Kumar</span>, R Parhi, M Belkin<br>
    <i>The 38th Annual Conference on Learning Theory (COLT 2025)</i><br>
    <a href="https://proceedings.mlr.press/v291/kumar25b.html">Proceedings</a> · <a href="https://arxiv.org/abs/2502.16331">ArXiv</a>
    {% assign pub_gap = site.publications | where: "title", "A Gap Between the Gaussian RKHS and Neural Networks: An Infinite-Center Asymptotic Analysis" | first %}
    {% if pub_gap and pub_gap.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_gap.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Mirror Descent on Reproducing Kernel Banach Space (RKBS)</b><br>
  <span class="author-self">A Kumar</span>, M Belkin, P Pandit<br>
    <i>Journal of Machine Learning Research (JMLR), 2025 (To appear)</i><br>
    <a href="https://arxiv.org/abs/2411.11242">ArXiv</a>
    {% assign pub_rkbs = site.publications | where: "title", "Mirror Descent on Reproducing Kernel Banach Space (RKBS)" | first %}
    {% if pub_rkbs and pub_rkbs.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_rkbs.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>The Complexity of Learning Sparse Superposed Features with Feedback</b><br>
  <span class="author-self">A Kumar</span><br>
    <i>The 42nd International Conference on Machine Learning (ICML 2025)</i><br>
    <a href="https://proceedings.mlr.press/v267/kumar25b.html">Proceedings</a> · <a href="https://arxiv.org/abs/2502.05407">ArXiv</a>
    {% assign pub_sparse = site.publications | where: "title", "The Complexity of Learning Sparse Superposed Features with Feedback" | first %}
    {% if pub_sparse and pub_sparse.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_sparse.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Robust Empirical Risk Minimization with Tolerance</b><br>
  R Bhattacharjee, K Chaudhuri, M Hopkins, <span class="author-self">A Kumar</span>, H Yu<br>
    <i>The 34th International Conference on Algorithmic Learning Theory (ALT'23)</i><br>
    <a href="https://proceedings.mlr.press/v201/bhattacharjee23a">Proceedings</a> · <a href="https://arxiv.org/abs/2210.00635">ArXiv</a>
    {% assign pub_alt = site.publications | where: "title", "Robust Empirical Risk Minimization with Tolerance" | first %}
    {% if pub_alt and pub_alt.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_alt.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>Teaching via Best-Case Counterexamples in the Learning-with-Equivalence-Queries Paradigm</b><br>
  <span class="author-self">A Kumar</span>, Y Chen, A Singla<br>
    <i>The 35th Conference on Neural Information Processing Systems (NeurIPS 2021)</i><br>
    <a href="https://proceedings.neurips.cc/paper/2021/hash/e22dd5dabde45eda5a1a67772c8e25dd-Abstract.html">Proceedings</a>
    {% assign pub_neurips = site.publications | where: "title", "Teaching via Best-Case Counterexamples in the Learning-with-Equivalence-Queries Paradigm" | first %}
    {% if pub_neurips and pub_neurips.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_neurips.abstract }}</div></details>{% endif %}
  </li>
  <li>
    <b>The Teaching Dimension of Kernel Perceptron</b><br>
  <span class="author-self">A Kumar</span>, H Zhang, A Singla, Y Chen<br>
  <i>The 24th International Conference on Artificial Intelligence and Statistics (AISTATS 2021)</i>
    <br><a href="https://proceedings.mlr.press/v130/kumar21a.html">Proceedings</a> · <a href="https://arxiv.org/abs/2010.14043">ArXiv</a>
    {% assign pub_aistats = site.publications | where: "title", "The Teaching Dimension of Kernel Perceptron" | first %}
    {% if pub_aistats and pub_aistats.abstract %} · <details class="inline-abstract"><summary>Abstract</summary><div class="abstract-text">{{ pub_aistats.abstract }}</div></details>{% endif %}
  </li>
</ul>
