# cloack

A Python package to truncate dates and times.

## References

- [Wolt Python Package Cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) repo
- [Delorean](https://delorean.readthedocs.io/en/latest/) package

## Development

- `poetry install`
- `poetry run isort .` or `poetry run isort . --verbose`
- `poetry run black .` or `poetry run black . --verbose`
- [Add an entry](https://github.com/mschmieder/python-kacl#add-an-entry-to-an-unreleased-section) to the `CHANGELOG.md` file and manually save it in VS Code to format it.
- `poetry run kacl-cli verify` or `poetry run kacl-cli verify --json`

## Deployment

- `poetry version patch` or `poetry version minor`
- `poetry run kacl-cli release $(poetry version --short) --modify`

## Notes

- [cruft](https://cruft.github.io/cruft/):
  - Alternative to Cookiecutter
  - cruft uses Cookiecutter as the template engine
- [pytest-github-actions-annotate-failures](https://github.com/utgwkk/pytest-github-actions-annotate-failures)
- [flake8-logging-format](https://github.com/globality-corp/flake8-logging-format)
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
- `poetry run kacl-cli --help`
- `poetry run kacl-cli add --help`
- `poetry run kacl-cli add added 'Boilerplate to create a Python package.' --modify`
- `poetry run kacl-cli new` or `poetry run kacl-cli new | pbcopy`
  - https://github.com/mschmieder/python-kacl/blob/v0.2.24/kacl/document.py#L426
- https://python-poetry.org/docs/configuration/#local-configuration
