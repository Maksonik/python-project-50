
lint:
	poetry run flake8 . && poetry run isort . --check --diff


test:
	poetry run pytest


install:
	poetry install
