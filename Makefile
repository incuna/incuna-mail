SHELL := /bin/bash

help:
	echo "release: publish package to the PyPI"
	echo "test: run unit tests"

release:
	python setup.py register sdist bdist_wheel
	twine upload dist/*

test:
	@python -Wmodule -m coverage run tests/run.py
	@coverage report --show-missing
	@flake8
