.PHONY: build serve clean

build:
	ablog build

serve:
	sphinx-autobuild . _website -b dirhtml --open-browser

clean:
	rm -rf _website .doctrees
