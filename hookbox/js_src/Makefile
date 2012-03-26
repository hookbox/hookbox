.PHONY: help all clean 

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all 	    compile/minify hookbox. Make sure pyjsiocompile is installed or do pip install pyjsiocompile first"
	@echo "  clean	    to remove minified hookbox"

all:
	jsio_compile hookbox.pkg -j jsio-3.2 -o ../static/hookbox.js -d
	jsio_compile hookbox.pkg -j jsio-3.2 -o ../static/hookbox.min.js -g --v
	cp ../static/hookbox.min.js ../static/hookbox.min.js.bak
	gzip -f ../static/hookbox.min.js
	mv ../static/hookbox.min.js.bak ../static/hookbox.min.js
clean:
	rm ../static/*.js
	rm ../static/*.js.gz
