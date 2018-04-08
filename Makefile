.PHONY: test

test:
	py.test -vv --cov=hmsite --cov=polls tests/
