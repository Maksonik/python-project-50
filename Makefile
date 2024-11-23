
lint:
	poetry run flake8 . && poetry run isort . --check --diff


test:
	poetry run pytest


test-coverage:
	poetry run pytest --cov=hexlet-code --cov-report=xml

install:
	poetry install


