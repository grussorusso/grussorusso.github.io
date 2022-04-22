BUILDDIR=_site

all:
	hugo -b "http://127.0.0.1/" -d $(BUILDDIR) --cleanDestinationDir
serve:
	hugo server --port 4000 -D
