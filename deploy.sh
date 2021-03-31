#!/bin/sh
rsync -avz --delete --exclude=./software _site/* russorusso@claudius.ce.uniroma2.it:public_html/
