.PHONY: test coverage install

install:
	pip install -r requirements.txt

test:
	pytest -v

coverage:
	PYTHONPATH=. python -m coverage run -m pytest



# RUN WITH:
# make test
# make coverage
