
all: install

install:
	@ echo "installing package ..."
	@ python3 setup.py install

test: install
	@ echo "starting unit tests ..."
	@ python3 ./tests/run_test.py
