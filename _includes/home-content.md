I am a third-year PhD student in *Computer Science* at the 
[University of Rome Tor Vergata](http://web.uniroma2.it), in Italy.

My research interests span the area of Distributed Systems with emphasis on performance optimization.
I am currently investigating decentralized solutions for
self-adaptive data processing systems deployed in geographically distributed and heterogeneous environments (e.g., Fog/Edge).

Here is my [CV]({{ site.baseurl }}/assets/cv.pdf).

<hr class="sectionbar"/>
<a name ="contact"></a>
<h2 class="homesection">Contact information</h2>
Dipartimento di Ingegneria Civile e Ingegneria Informatica<br/>
Università di Roma "Tor Vergata"<br/>
Via del Politecnico 1, 00133 Roma, Italy<br/>
&#114;usso.&#114;usso (&#97;&#116;) ing.uniroma2.it
<!--
![]({{ site.baseurl }}/assets/images/email_addr.png)
-->

<hr class="sectionbar"/>
<h2 class="homesection">Recent publications</h2>
{% for y in site.data.publications limit: 2 %}
  {% for paper in y.papers limit: 2 %}
{{ paper.authors }}<br/>
**{{paper.title}}**&nbsp;{% if paper.link %}\[[{{ paper.link_title }}]({{ paper.link }})\]{% endif %}{% if paper.pdf %}&nbsp;[\[pdf]({{ paper.pdf }})\]{% endif %}<br/>
<span class="publications-info">{{paper.info}}</span>
  {% endfor %}
{% endfor %}

You can find [here]({{ site.baseurl }}/publications.html) a list of all my publications.
{: .notice--info}


