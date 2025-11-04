.PHONY: test coverage install

install:
	python -m pip install -r requirements.txt

run:
	python -m src.main
test:
	python -m pytest -v

flake8:
	python -m flake8 src/

coverage:
	python -m pytest --cov=src --cov-report=term-missing -v

docstring:
	python -m pdoc --html src
