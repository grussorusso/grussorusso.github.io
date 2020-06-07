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
<h2 class="homesection">Selected publications</h2>
{% for paper in site.publications %}
{% if paper.selected %}
<span class="publist-authors">{{ paper.authors }}</span><br/>
<span class="publist-title">{{ paper.title }}</span><br/>
<span class="publist-info">{{ paper.info }}</span><br/>
[abstract]({{ site.baseurl}}{{ paper.url }}){: .btn .btn--verysmall .btn--inverse} {% if paper.doi %} [doi]({{ paper.doi }}){: .btn .btn--verysmall .btn--inverse} {% endif %} {% if paper.pdf %} [pdf]({{ paper.pdf }}){: .btn .btn--verysmall .btn--info} {% endif %}
{% endif %}
{% endfor %}

You can find [here]({{ site.baseurl }}/publications.html) a list of all my publications.
{: .notice--info}


