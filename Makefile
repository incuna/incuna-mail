SHELL := /bin/bash

help:
	echo "release: publish package to the PyPI"

release:
	python setup.py regsiter sdist upload
	python setup.py regsiter bdist_wheel upload
