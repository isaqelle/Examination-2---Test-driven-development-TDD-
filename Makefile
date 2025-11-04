.PHONY: test coverage install

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest -v

flake8:
	python -m flake8 src/

docstring:
	python -m pdoc --html src
