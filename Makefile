.PHONY: run test lint format check-all coverage

# Проверки: mypy
typing:
	poetry run mypy basic/ intermediate/

# Форматирование: black + isort
format:
	poetry run isort .

# Синхронизация poetry
sync:
	poetry lock && poetry install
