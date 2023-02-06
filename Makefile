setup:
	# Create python virtualenv & source
	# source ~/.devops/bin/activate
	python3 -m venv ~/.devops

install:
	# run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt 

test:
	# Additional, optional, tests could go here
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	# See the local hadolint install instructions:   https://github.com/hadolint/hadolint
	# The linter for Dockerfiles
	# Install hadolint steps:
        # command : wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 &&\
        # commmand: chmod +x /bin/hadolint
	hadolint Dockerfile

	# The linter for Python source code linter: https://www.pylint.org/
	# run from inside a virtualenv
	pylint --disable=R,C,W1203 app.py

all: install lint test
