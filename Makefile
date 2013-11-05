SHELL := /bin/bash

help:
	echo "release: publish package to Incuna's internal PyPI"

release:
	python setup.py regsiter -r incuna sdist upload -r incuna
	python setup.py regsiter -r incuna bdist_wheel upload -r incuna
