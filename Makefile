.PHONY: test coverage

test:
	pytest -v

coverage:
	coverage run -m pytest
	coverage report -m
