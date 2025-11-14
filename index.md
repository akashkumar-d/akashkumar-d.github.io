---
permalink: /
title: ""
excerpt: ""
author_profile: true
---
<div align="center">
  <p style="
      font-family: 'Cinzel', serif;
      font-size: 14px;
      font-weight: bold;
      border: 2px solid #FFD700; 
      padding: 10px; 
      display: inline-block;
      border-radius: 10px;
      background: linear-gradient(135deg, #1E1E1E, #3A3A3A);
      color: #FFD700;
      text-shadow: 1px 1px 3px #b8860b;
  ">
    तद्वनः मम हृदये वसति। <br>
    <i style="font-family: serif; font-weight: normal; text-transform: none;">Tadvanaḥ mama hṛdaye vasati.</i> <br>
  </p>
</div>

<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap" rel="stylesheet">


# About Me
I am a 5th-year doctoral candidate in the [Computer Science department](https://cse.ucsd.edu/) at the University of California-San Diego where I am co-advised by Prof. [Sanjoy Dasgupta](https://cseweb.ucsd.edu/~dasgupta/) and Prof. [Misha Belkin](http://misha.belkin-wang.org/). Previously, I was a research fellow at Max Planck Institute (Saarbruecken, Germany) under Dr. [Adish Singla](https://machineteaching.mpi-sws.org/adishsingla.html). I completed a BSc in Mathematics and Computer Science, followed by an MSc in Computer Science at Chennai Mathematical Institute (CMI, India). 

In the past, I have been fortunate to be supported by the following fellowships: **Jacobs School of Engineering Fellowship** (at UCSD), the **Crerar Fellowship** (awarded by UChicago CS, declined), the **Max Planck Institute Fellowship**, and the **Chennai Mathematical Institute Scholastic Fellowship**.

I am broadly interested in advancing both the theoretical foundations and practical applications of machine learning. Specifically, my focus lies in statistical machine learning, algorithm design, interactive learning, optimization, and the theoretical aspects of deep learning. I am particularly enthusiastic about leveraging tools from probability theory, analysis, differential geometry, and statistics to rigorously study the computational and statistical efficiency of learning algorithms. My goal is to deepen our understanding of the principles underlying data-driven learning and the capabilities of machines to extract meaningful insights from complex datasets.
  
**Email**: akk002 at ucsd dot edu

# Recent News
<div class="recent-news-scroll" markdown="1">

 - [<span class="news-date">August, 2025</span>] Presented my recent work at Princeton University and Yale University (Theory Seminar).
 - [<span class="news-date">May, 2025</span>] Selected for the [Summer School](https://mlschool.princeton.edu/) on machine learning theory at Princeton University. 
 - [<span class="news-date">May, 2025</span>] One paper to appear in JMLR 2025.
 - [<span class="news-date">May, 2025</span>] Two papers accepted, one each in ICML 2025 and COLT 2025.
 - [<span class="news-date">Feb, 2025</span>] Presenting my recent work at ITA'25 (San Diego) and reviewing for COLT'25.
 - [<span class="news-date">Dec, 2024</span>] Attended [Unknown Futures of Generalization workshop](https://simons.berkeley.edu/workshops/unknown-futures-generalization) at Simons Institute, UC Berkeley.
 - [<span class="news-date">Summer, 2023</span>] I was a research scientist intern at Adobe Research (San Jose, CA).
 - [<span class="news-date">Aug, 2022</span>] Attended the [Deep learning theory workshop](https://simons.berkeley.edu/workshops/deep-learning-theory-workshop) at Simons Institute, UC Berkeley.
 - [<span class="news-date">July, 2022</span>] Attended a summer school on Discrete Mathematics at Charles University, Prague (CZK).

</div>


## Publications

<div class="pub-tabs" role="tablist" aria-label="Publications tabs">
  <!-- Radio controls (hidden) -->
  <input type="radio" name="pubtabs" id="tab-selected" class="pub-tab-control" checked>
  <label for="tab-selected" class="pub-tab-label" role="tab" aria-controls="panel-selected" aria-selected="true">Selected Work</label>

  <input type="radio" name="pubtabs" id="tab-all" class="pub-tab-control">
  <label for="tab-all" class="pub-tab-label" role="tab" aria-controls="panel-all" aria-selected="false">All Publications</label>

  <input type="radio" name="pubtabs" id="tab-topic" class="pub-tab-control">
  <label for="tab-topic" class="pub-tab-label" role="tab" aria-controls="panel-topic" aria-selected="false">Topic-Wise</label>

  <div class="pub-tab-panels">
    <!-- Selected Work Panel -->
    <section id="panel-selected" class="pub-tab-panel" role="tabpanel" aria-labelledby="tab-selected">
      {% assign selected_pubs = site.publications | where_exp: "p", "p.selected" | sort: "date" | reverse %}
      {% if selected_pubs.size == 0 %}
        {%- assign selected_titles = "A Gap Between the Gaussian RKHS and Neural Networks: An Infinite-Center Asymptotic Analysis|Mirror Descent on Reproducing Kernel Banach Space (RKBS)|Learning Smooth Distance Functions via Queries|Robust Empirical Risk Minimization with Tolerance|The Teaching Dimension of Kernel Perceptron" | split: "|" -%}
        {%- assign _fallback = "" | split: "" -%}
        {%- for t in selected_titles -%}
          {%- assign found = site.publications | where: "title", t | first -%}
          {%- if found -%}{%- assign _fallback = _fallback | push: found -%}{%- endif -%}
        {%- endfor -%}
        {%- assign selected_pubs = _fallback -%}
      {% endif %}
      {% if selected_pubs and selected_pubs.size > 0 %}
      <ul>
      {% for pub in selected_pubs %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}
            {% assign primary_link = pub.paperurl %}
          {% elsif pub.arxiv %}
            {% assign primary_link = pub.arxiv %}
          {% elsif pub.paperurl %}
            {% assign primary_link = pub.paperurl %}
          {% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
        {% if pub.authors %}
          {% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}
          {{ authors_text }}<br>
        {% endif %}
        {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
        {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}
          {% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}
            {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}
              {% assign show_proceedings = true %}
            {% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}
              {% if pub.venue %}
                {% assign v = pub.venue | downcase %}
                {% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}
                {% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}
                {% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}
                {% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}
                {% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}
                {% endif %}
              {% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
            {% if pub.abstract %} · <details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
          {% endif %}
        </li>
      {% endfor %}
      </ul>
      {% else %}
      <p><i>No selected publications to show right now.</i></p>
      {% endif %}
    </section>

    <!-- All Publications Panel -->
    <section id="panel-all" class="pub-tab-panel" role="tabpanel" aria-labelledby="tab-all" hidden>
      {% assign all_pubs = site.publications | sort: "date" | reverse %}
      {% if all_pubs and all_pubs.size > 0 %}
      <ul>
      {% assign conv_pub = site.publications | where: "title", "Convergence of Nearest Neighbor Selective Classification" | first %}
      {% assign alt_pub = site.publications | where: "title", "Robust Empirical Risk Minimization with Tolerance" | first %}
      {% assign conv_rendered = false %}
      {% for pub in all_pubs %}
        {% if conv_pub and pub.title == conv_pub.title %}
          {% continue %}
        {% endif %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}
            {% assign primary_link = pub.paperurl %}
          {% elsif pub.arxiv %}
            {% assign primary_link = pub.arxiv %}
          {% elsif pub.paperurl %}
            {% assign primary_link = pub.paperurl %}
          {% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
        {% if pub.authors %}
          {% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}
          {{ authors_text }}<br>
        {% endif %}
        {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
        {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}
          {% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}
            {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}
              {% assign show_proceedings = true %}
            {% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}
              {% if pub.venue %}
                {% assign v = pub.venue | downcase %}
                {% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}
                {% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}
                {% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}
                {% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}
                {% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}
                {% endif %}
              {% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>
        {% if alt_pub and pub.title == alt_pub.title and conv_pub and conv_rendered == false %}
        <li>
          {% assign primary_link = nil %}
          {% if conv_pub.paperurl and (conv_pub.paperurl contains 'proceedings.mlr.press' or conv_pub.paperurl contains 'proceedings.neurips.cc') %}
            {% assign primary_link = conv_pub.paperurl %}
          {% elsif conv_pub.arxiv %}
            {% assign primary_link = conv_pub.arxiv %}
          {% elsif conv_pub.paperurl %}
            {% assign primary_link = conv_pub.paperurl %}
          {% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ conv_pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
        {% if conv_pub.authors %}
          {% assign authors_text = conv_pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}
          {{ authors_text }}<br>
        {% endif %}
        {% if conv_pub.authors_note %}<i>{{ conv_pub.authors_note }}</i><br>{% endif %}
        {% if conv_pub.venue %}<span class="pub-venue"><i>{{ conv_pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = conv_pub.paperurl %}
          {% assign has_arxiv = conv_pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}
            {% if conv_pub.paperurl and (conv_pub.paperurl contains 'proceedings.mlr.press' or conv_pub.paperurl contains 'proceedings.neurips.cc') %}
              {% assign show_proceedings = true %}
            {% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}
              {% if conv_pub.venue %}
                {% assign v = conv_pub.venue | downcase %}
                {% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}
                {% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}
                {% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}
                {% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}
                {% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}
                {% endif %}
              {% endif %}
              <a class="pub-link pub-link-primary" href="{{ conv_pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ conv_pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ conv_pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ conv_pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if conv_pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ conv_pub.abstract }}</div></details>{% endif %}
        </li>
        {% assign conv_rendered = true %}
        {% endif %}
      {% endfor %}
      {% if conv_pub and conv_rendered == false %}
        <li>
          {% assign primary_link = nil %}
          {% if conv_pub.paperurl and (conv_pub.paperurl contains 'proceedings.mlr.press' or conv_pub.paperurl contains 'proceedings.neurips.cc') %}
            {% assign primary_link = conv_pub.paperurl %}
          {% elsif conv_pub.arxiv %}
            {% assign primary_link = conv_pub.arxiv %}
          {% elsif conv_pub.paperurl %}
            {% assign primary_link = conv_pub.paperurl %}
          {% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ conv_pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
        {% if conv_pub.authors %}
          {% assign authors_text = conv_pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}
          {{ authors_text }}<br>
        {% endif %}
        {% if conv_pub.authors_note %}<i>{{ conv_pub.authors_note }}</i><br>{% endif %}
        {% if conv_pub.venue %}<span class="pub-venue"><i>{{ conv_pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = conv_pub.paperurl %}
          {% assign has_arxiv = conv_pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}
            {% if conv_pub.paperurl and (conv_pub.paperurl contains 'proceedings.mlr.press' or conv_pub.paperurl contains 'proceedings.neurips.cc') %}
              {% assign show_proceedings = true %}
            {% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}
              {% if conv_pub.venue %}
                {% assign v = conv_pub.venue | downcase %}
                {% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}
                {% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}
                {% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}
                {% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}
                {% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}
                {% endif %}
              {% endif %}
              <a class="pub-link pub-link-primary" href="{{ conv_pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ conv_pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ conv_pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ conv_pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if conv_pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ conv_pub.abstract }}</div></details>{% endif %}
        </li>
      {% endif %}
      </ul>
      {% else %}
      <p><i>No publications found.</i></p>
      {% endif %}
    </section>

    <!-- Topic-Wise Panel -->
    <section id="panel-topic" class="pub-tab-panel" role="tabpanel" aria-labelledby="tab-topic" hidden>
      <!-- Learning theory -->
      <h3>Learning theory</h3>
      <ul>
        {% assign lt1 = site.publications | where: "title", "Robust Empirical Risk Minimization with Tolerance" | first %}
        {% assign lt2 = site.publications | where: "title", "Learning Smooth Distance Functions via Queries" | first %}
        {% assign lt3 = site.publications | where: "title", "Convergence of Nearest Neighbor Selective Classification" | first %}
        {% for tgt in lt1 | split: "|" %}{% endfor %}
        {% if lt2 %}{% assign pub = lt2 %}{% include base_path %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
        {% if lt1 %}{% assign pub = lt1 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
        {% if lt3 %}{% assign pub = lt3 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
      </ul>

  <!-- Optimization and Approximation with Kernel Machines -->
  <h3>Optimization and Approximation with Kernel Machines</h3>
      <ul>
        {% assign ok1 = site.publications | where: "title", "Mirror Descent on Reproducing Kernel Banach Space (RKBS)" | first %}
        {% assign ok2 = site.publications | where: "title", "A Gap Between the Gaussian RKHS and Neural Networks: An Infinite-Center Asymptotic Analysis" | first %}
        {% if ok1 %}{% assign pub = ok1 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
        {% if ok2 %}{% assign pub = ok2 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% elsif v contains 'alt' %}{% assign proceedings_label = 'alt' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
      </ul>

      <!-- Interpretability / Feature learning -->
      <h3>Interpretability / Feature learning</h3>
      <ul>
        <!-- Interpretability preprint (not in collection yet) -->
        <li>
          <b>Is Interpretability at Odds with Accuracy? Inapproximability of Decision Trees by Shallow Networks</b><br>
          <span class="author-self">A Kumar</span><br>
          <i>In submission.</i><br>
          ArXiv (coming soon)
        </li>
        {% assign ifl2 = site.publications | where: "title", "The Complexity of Learning Sparse Superposed Features with Feedback" | first %}
        {% if ifl2 %}{% assign pub = ifl2 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
      </ul>

      <!-- Interactive learning -->
      <h3>Interactive learning</h3>
      <ul>
        {% assign il1 = site.publications | where: "title", "Teaching via Best-Case Counterexamples in the Learning-with-Equivalence-Queries Paradigm" | first %}
        {% assign il2 = site.publications | where: "title", "The Teaching Dimension of Kernel Perceptron" | first %}
        {% assign il3 = site.publications | where: "title", "Average-case Complexity of Teaching Convex Polytopes via Halfspace Queries" | first %}
        {% if il1 %}{% assign pub = il1 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
        {% if il2 %}{% assign pub = il2 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
        {% if il3 %}{% assign pub = il3 %}
        <li>
          {% assign primary_link = nil %}
          {% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign primary_link = pub.paperurl %}{% elsif pub.arxiv %}{% assign primary_link = pub.arxiv %}{% elsif pub.paperurl %}{% assign primary_link = pub.paperurl %}{% endif %}
          {% if primary_link %}<a href="{{ primary_link }}">{% endif %}<b>{{ pub.title }}</b>{% if primary_link %}</a>{% endif %}<br>
          {% if pub.authors %}{% assign authors_text = pub.authors | replace: 'A Kumar', '<span class="author-self">A Kumar</span>' | replace: 'Akash Kumar', '<span class="author-self">Akash Kumar</span>' %}{{ authors_text }}<br>{% endif %}
          {% if pub.authors_note %}<i>{{ pub.authors_note }}</i><br>{% endif %}
          {% if pub.venue %}<span class="pub-venue"><i>{{ pub.venue }}</i></span><br>{% endif %}
          {% assign has_paperurl = pub.paperurl %}{% assign has_arxiv = pub.arxiv %}
          {% if has_paperurl or has_arxiv %}
            {% assign show_proceedings = false %}{% if pub.paperurl and (pub.paperurl contains 'proceedings.mlr.press' or pub.paperurl contains 'proceedings.neurips.cc') %}{% assign show_proceedings = true %}{% endif %}
            {% if show_proceedings %}
              {% assign proceedings_label = 'proceedings' %}{% if pub.venue %}{% assign v = pub.venue | downcase %}{% if v contains 'colt' %}{% assign proceedings_label = 'colt' %}{% elsif v contains 'icml' %}{% assign proceedings_label = 'icml' %}{% elsif v contains 'neurips' or v contains 'nips' %}{% assign proceedings_label = 'neurips' %}{% elsif v contains 'aistats' %}{% assign proceedings_label = 'aistats' %}{% endif %}{% endif %}
              <a class="pub-link pub-link-primary" href="{{ pub.paperurl }}">{{ proceedings_label }}</a>{% if has_arxiv %} · <a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% endif %}
            {% else %}
              {% if has_arxiv %}<a class="pub-link pub-link-arxiv" href="{{ pub.arxiv }}">arxiv</a>{% elsif has_paperurl %}<a class="pub-link" href="{{ pub.paperurl }}">link</a>{% endif %}
            {% endif %}
          {% endif %}
          {% if pub.abstract %}{% if has_paperurl or has_arxiv %} · {% endif %}<details class="inline-abstract"><summary>abstract</summary><div class="abstract-text">{{ pub.abstract }}</div></details>{% endif %}
        </li>{% endif %}
      </ul>
    </section>

  </div>
</div>



# Recent talks

<ul class="talk-list">
  <li>
    <b>Learning Smooth Distance Functions via Queries</b> (<a href="https://drive.google.com/file/d/1vmprFyvcK6mb9zrEU9-55ZWij04WqkOz/view?usp=drive_link">slides</a>)<br>
    <span class="talk-venues">Yale Student Theory Seminar; Princeton ML Theory Summer School; UCSD CSE</span>
  </li>
  <li>
    <b>A Gap Between Gaussian Kernel Machine and Neural Networks</b><br>
    <span class="talk-venues">COLT 2025; UCSD CSE Thesis Proposal</span>
  </li>
  <li>
    <b>Feature Learning in Large Language Models</b><br>
    <span class="talk-venues">Adobe Research, San Jose</span>
  </li>
</ul>

  
# Some notes
<b> [Improved Certified Adversarial Lower Bound Using Adaptive Relaxations](https://drive.google.com/file/d/1lZmiU3NnEhWHOtVuGhURxeFS4DWaYP_n/view?usp=sharing) </b> <br>
<i>Ongoing project on adversarial deep learning.</i>

<b> [Escaping Saddle Points and Tensor Decomposition](https://drive.google.com/file/d/1MAcwvvqGJCmr4VCnvE0kCFSTUB8w4mSA/view?usp=sharing) </b> <br>
<i>Master's Thesis under the guidance of Dr. K V Subrahmanyam. [[Slides](https://drive.google.com/file/d/1X4wGdlJvXqvzu-4C4qRFSEkSxy3ZF4Bg/view?usp=sharing)]</i>

<b> [Natural Proofs Vs Derandomization](https://drive.google.com/file/d/1TeHXyLIIUfp0p4iPqRqgNKwUx92ZO0Qn/view?usp=sharing) </b> <br>
<i>Project report completed as part of the Advanced Complexity course at Chennai Mathematical Institute.</i>
