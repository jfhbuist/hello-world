[![Build Status](https://github.com/jfhbuist/hello-world/actions/workflows/CI.yml/badge.svg?event=push)](https://github.com/jfhbuist/hello-world/actions)
[![codecov](https://codecov.io/gh/jfhbuist/hello-world/branch/master/graph/badge.svg?token=JKZUS5AVBP)](https://codecov.io/gh/jfhbuist/hello-world)

# hello-world

This is a simple template for a collection of python scripts with testing (not a package).
It uses pip for installation, flake8 for linting, pytest for testing, and coverage for monitoring test coverage.

To use it, first create a virtual environment, and install flake8, pytest, and coverage using pip.
The following works on Windows: 
```
py -3 -m venv .venv
.venv\scripts\activate
python -m pip install --upgrade pip
pip install flake8 pytest coverage
```

Then, install the dependencies:
```
pip install -r requirements.txt
```

The scripts can now be run and tested:
```
python src/main.py
flake8
coverage run -m pytest
coverage report
```

When done, deactivate the virtual environment:
```
deactivate
```
