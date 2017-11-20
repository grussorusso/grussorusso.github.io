#!/bin/sh
docker run -it --rm --label=jekyll -p 127.0.0.1:4000:4000 --volume=$(pwd):/srv/jekyll jekyll/jekyll:pages jekyll build
