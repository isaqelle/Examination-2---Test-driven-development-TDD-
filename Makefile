.PHONY: test coverage install

install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. pytest -v

coverage:
	PYTHONPATH=. python -m coverage run -m pytest
	PYTHONPATH=. python -m coverage report -m

flake8:
	flake8 proj test

# RUN MANUAL:
# make install  --- intalls packages from req.txt
# make test	    --- runs pytest
# make coverage --- runs coverage
# make flake8