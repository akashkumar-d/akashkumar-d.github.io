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

- <b> Is Interpretability at Odds with Accuracy? Inapproximability of Decision Trees by Shallow Networks </b> <br>
**Akash Kumar** <br>
<i>In submission.</i><br>
[[Arxiv Coming Soon]()]

- <b> Learning Smooth Distance Functions via Queries </b> <br>
**Akash Kumar**, Sanjoy Dasgupta <br>
<i>In submission to a conference.</i><br>
[[ArXiv 2024](https://arxiv.org/pdf/2412.01290)]

- <b> Convergence of Nearest Neighbor Selective Classification </b> <br>
**Akash Kumar**, Sanjoy Dasgupta<br>
<i>Manuscript on request.</i>

- <b> Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries </b> <br>
**Akash Kumar**, <a href="https://machineteaching.mpi-sws.org/adishsingla.html">Adish Singla</a>, <a href="http://www.yisongyue.com/">Yisong Yue</a>, <a href="https://yuxinchen.org/">Yuxin Chen</a>.<br>
[[ArXiv 2020](https://arxiv.org/abs/2006.14677)]

---

## Publications

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
