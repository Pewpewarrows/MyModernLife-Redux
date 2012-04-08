all: build

build:
	pelican -s conf/settings.py src

develop:
	mkvirtualenv mml_redux
	~/.virtualenvs/mml_redux/bin/pip install -r conf/requirements.txt

freeze:
	pip freeze -l | sort > conf/requirements.txt