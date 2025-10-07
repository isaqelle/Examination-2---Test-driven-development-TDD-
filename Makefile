.PHONY: test coverage

test:
	PYTHONPATH=. pytest -v

coverage:
	PYTHONPATH=. coverage run -m pytest
	PYTHONPATH=. coverage report -m

# RUN WITH:
# make test
# make coverage