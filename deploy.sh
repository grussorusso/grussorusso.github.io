#!/bin/sh
rsync -avz --delete --exclude=./software public/* russorusso@claudius.ce.uniroma2.it:public_html/
