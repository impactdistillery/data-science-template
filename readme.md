# Data Science Template for Cookiecutter

This repository provides a template for data-science-projects to be used with Cookiecutter.

Setup:

#. Install [cookiecutter](https://cookiecutter.readthedocs.io/) (Python package).
#. Use cookiecutter to setup your project: `cookiecutter https://github.com/impactdistillery/data-science-template`
#. Enter the new project directory: `cd [your-project-name]`
#. Install dependencies, e.g.: `pipenv install -r requirements.txt`
#. Use invoke to setup missing tools etc.: `inv setup`
#. use invoke to start jupyter, run Sphinx, etc. You can list all options with `inv -l`
