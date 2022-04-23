all:
	hugo -b "http://www.ce.uniroma2.it/~russorusso/" --cleanDestinationDir
serve:
	hugo server --port 4000 -Dv --disableFastRender
