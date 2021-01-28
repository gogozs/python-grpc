install:
	pip install -r requirements.txt

upload:
	twine upload dist/*

build:
	rm -f dist/*
	python setup.py sdist bdist_wheel
