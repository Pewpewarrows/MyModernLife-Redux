all: build_site

build_site:
	pelican -s conf/settings.py src

build_live:
	pelican -r -s conf/settings.py src

develop:
	mkvirtualenv mml_redux
	~/.virtualenvs/mml_redux/bin/pip install -r conf/requirements.txt

run:
	cd bin && python -m SimpleHTTPServer 8001

deploy:
	git push --all

freeze:
	pip freeze -l | sort > conf/requirements.txt

clean:
	git clean -f
	rm -rf bin/