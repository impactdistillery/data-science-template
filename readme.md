# Data Science Template for Cookiecutter

This repository provides a template for data-science-projects to be used with Cookiecutter.

Setup:

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/) (Python package).
2. Use cookiecutter to setup your project: `cookiecutter https://github.com/impactdistillery/data-science-template`
3. Enter the new project directory: `cd [your-project-name]`
4. Install dependencies, e.g.: `pipenv install -r requirements.txt`
5. Use invoke to setup missing tools etc.: `inv setup`
6. use invoke to start jupyter, run Sphinx, etc. You can list all options with `inv -l`
