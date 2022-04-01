export FLASK_APP=run.py
export FLASK_ENV=development

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
        
lint:
	pylint --rcfile .pylintrc model/ tests/ app/ #pylint --disable=R,C model.py

format:
	black *.py

test:
	python -m pytest -vv --disable-warnings tests/ --junitxml=junit/test-results.xml --cov=. --cov-config=.coveragerc --cov-report xml:coverage.xml --cov-report term --cov-report html:cov_html #--doctest-modules #--cov=hello test_hello.py
	
run_dev:
	flask run
	
run:
	flask run	
	
all: install lint test	

