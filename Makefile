
lint:
	poetry run flake8 . && poetry run isort . --check --diff