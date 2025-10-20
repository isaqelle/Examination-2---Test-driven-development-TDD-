.PHONY: test coverage install

install:
	pip install -r requirements.txt

test:
	pytest -v

coverage:
	PYTHONPATH=. python -m coverage run -m pytest

flake8:
	flake8 src/

docstring:
	pdoc --html src