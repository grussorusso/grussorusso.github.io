---
layout: single
classes: wide 
author_profile: false
title: Publications
permalink: /publications.html
---

{% assign years = "2019,2018,2017" | split: "," %}

{% for year in years %}
<h2>{{ year }}</h2>
{% for paper in site.publications %}
{% if year contains paper.year %}
<span class="publist-authors">{{ paper.authors }}</span><br/>
<span class="publist-title">{{ paper.title }}</span><br/>
<span class="publist-info">{{ paper.info }}</span><br/>
<a class="btn btn--verysmall btn--inverse" href="{{ site.baseurl }}{{ paper.url }}">abstract</a>	
{% if paper.doi %} <a class="btn btn--verysmall btn--inverse" href="{{ paper.doi }}">doi</a>	{% endif %}
{% if paper.pdf %} <a class="btn btn--verysmall btn--info" href="{{ paper.pdf }}">pdf</a>	{% endif %}
{% endif %}
{% endfor %}
{% endfor %}


<br>
