# FILE_1 = $(shell find ./tests -name "*.py" -type f)
# FILE_1 = $(shell find ./locators -name "*.py" -type f)
# FILE_1 = $(shell find ./pages -name "*.py" -type f)
# FILE_1 = data.py
FILE_1 = conftest.py

lint:
	python3 -m flake8 $(FILE_1)

fix:
	python3 -m autopep8 --in-place --aggressive --aggressive $(FILE_1)

test:
	pytest -v -s $(FILE_1) --alluredir=report

report:
	allure serve report

cov:
	pytest --cov=main

cov-html:
	pytest --cov=main --cov-branch --cov-report=html