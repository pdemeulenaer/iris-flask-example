export FLASK_APP=run.py
export FLASK_ENV=development

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
        
lint:
	pylint --rcfile .pylintrc model.py #pylint --disable=R,C model.py

format:
	black *.py

test:
	python -m pytest -vv #--cov=hello test_hello.py
	
run_dev:
	flask run
	
run:
	flask run	
	
all: install lint test	

