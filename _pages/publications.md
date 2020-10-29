---
layout: single
classes: wide 
author_profile: false
title: Publications
permalink: /publications.html
---

{% assign years = "2020,2019,2018,2017" | split: "," %}

{% for year in years %}
<h2>{{ year }}</h2>
{% for paper in site.publications %}
{% if year contains paper.year %}
<span class="publist-authors">{{ paper.authors }}</span><br/>
<span class="publist-title">{{ paper.title }}</span><br/>
<span class="publist-info">{{ paper.info }}</span><br/>
[abstract]({{ site.baseurl}}{{ paper.url }}){: .btn .btn--verysmall .btn--inverse} {% if paper.doi %} [doi]({{ paper.doi }}){: .btn .btn--verysmall .btn--inverse} {% endif %} {% if paper.pdf %} [pdf]({{ paper.pdf }}){: .btn .btn--verysmall .btn--info} {% endif %}
{% endif %}
{% endfor %}
{% endfor %}


<br>
