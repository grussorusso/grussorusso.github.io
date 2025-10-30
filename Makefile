all: update_pubs
	hugo -b "http://www.ce.uniroma2.it/~russorusso/" --cleanDestinationDir
update_pubs:
	python update_publications.py
serve:
	hugo server --port 4000 -D --disableFastRender
