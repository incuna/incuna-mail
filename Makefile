SHELL := /bin/bash

help:
	echo "release: publish package to the PyPI"

release:
	python setup.py register sdist upload
	python setup.py register bdist_wheel upload
