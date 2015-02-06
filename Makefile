SHELL := /bin/bash

help:
	echo "release: publish package to the PyPI"
	echo "test: run unit tests"

release:
	python setup.py register sdist upload
	python setup.py register bdist_wheel upload

test:
	@python -Wmodule -m coverage run tests/run.py
	@coverage report --show-missing
	@flake8
