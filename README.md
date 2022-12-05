# cloack

A Python package to truncate dates and times.

## References

- [Wolt Python Package Cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter)

## Development

- `poetry install`
- `poetry run isort .` or `poetry run isort . --verbose`
- `poetry run black .` or `poetry run black . --verbose`

## Notes

- [cruft](https://cruft.github.io/cruft/):
  - Alternative to Cookiecutter
  - cruft uses Cookiecutter as the template engine
- [pytest-github-actions-annotate-failures](https://github.com/utgwkk/pytest-github-actions-annotate-failures)
- Poetry:
  - `poetry --version`
  - Update Poetry: `poetry self update` or `curl -sSL https://install.python-poetry.org | python3 - --uninstall` + `curl -sSL https://install.python-poetry.org | python3 -`
  - `curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0`
  - Check the current configuration: `poetry config --list`
  - `poetry config virtualenvs.in-project true --local`
  - `poetry config virtualenvs.in-project --unset`
  - `poetry new cloack`
  - Check `poetry-core` version: `poetry about`
  - `poetry shell`
  - `poetry run black --help`
- https://python-poetry.org/docs/configuration/#local-configuration
