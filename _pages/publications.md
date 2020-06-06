---
layout: single
classes: wide 
author_profile: false
title: Publications
permalink: /publications.html
---

{% for y in site.data.publications %}
  <h2>{{ y.year }}</h2>
  {% for paper in y.papers %}
{{ paper.authors }}<br/>
**{{paper.title}}**&nbsp;{% if paper.link %}\[[{{ paper.link_title }}]({{ paper.link }})\]{% endif %}{% if paper.pdf %}&nbsp;[\[pdf]({{ paper.pdf }})\]{% endif %}<br/>
<span class="publications-info">{{paper.info}}</span><br/>
{% if paper.link %}[{{ paper.link_title }}]({{ paper.link }}){: .btn .btn--verysmall .btn--inverse} {% endif %}{% if paper.pdf %} [pdf]({{ paper.pdf }}){: .btn .btn--verysmall .btn--danger} {% endif %}<br/>
  {% endfor %}
{% endfor %}



<br>
