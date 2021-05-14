
<div class="home_author__avatar">
<img src="{{ site.baseurl}}/assets/images/me.jpg" alt="Gabriele Russo Russo" itemprop="image">
</div>

I am a Research Associate at the 
University of Rome Tor Vergata, in Italy, where I received my PhD degree in
May 2021.

My research interests span the area of distributed computing systems with emphasis on
performance optimization and run-time self-adaptation.
As a PhD student, I investigated auto-scaling solutions for data stream processing 
applications, combining Reinforcement Learning techniques and traditional
performance modeling tools.

Here is my [CV]({{ site.baseurl }}/assets/cv.pdf) and 
a list of [publications]({{ site.baseurl }}/publications.html) (also
available in [DBLP](https://dblp.org/pid/214/1442.html)).

<!--<hr class="sectionbar"/>-->
<a name ="contact"></a>
<h2 class="homesection">Contact information</h2>
Dipartimento di Ingegneria Civile e Ingegneria Informatica<br/>
Università di Roma "Tor Vergata"<br/>
Via del Politecnico 1, 00133 Roma, Italy<br/>
&#114;usso.&#114;usso (&#97;&#116;) ing.uniroma2.it
<!--
![]({{ site.baseurl }}/assets/images/email_addr.png)
-->

<h2 class="homesection">News</h2>

- I have
  presented *MEAD: Model-based Vertical Auto-Scaling for Data Stream Processing*
at [CCGRID 2021](http://cloudbus.org/ccgrid2021/mainpage.html). [Video](https://www.youtube.com/watch?v=R66RqVWIMtE&list=PLQV187VBTU9eXuko4_hmFNXo0V0VwWYF3&index=3){: .btn .btn--verysmall .btn--success}

- New book chapter [Towards a Security-aware Deployment of Data Streaming
  Applications in Fog Computing](https://doi.org/10.1007/978-3-030-57328-7_14)


<!--<hr class="sectionbar"/>-->
<h2 class="homesection">Recent publications</h2>
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


