# Interview

## Setup

- Install poetry

  - curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  - _-OR-_ pipx install poetry
  - poetry config virtualenvs.in-project

- git clone https://github.com/flow-labs/interview
- cd interview
- git switch -c [your name]
- poetry install
- poetry run pre-commit install -t pre-commit && poetry run pre-commit install -t pre-push
- poetry run flow
- Suggested editor: VS Code with Pylance extension
