# Build & Packaging

## `pyproject.toml` — The Modern Standard

`pyproject.toml` is the single file that defines a Python project's metadata, dependencies, and build configuration. It replaced the older `setup.py` / `setup.cfg` approach.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my-package"
version = "1.0.0"
description = "A sample Python package"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.9"
authors = [{ name = "Alice", email = "alice@example.com" }]
keywords = ["python", "example"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff"]
docs = ["mkdocs", "mkdocs-material"]

[project.urls]
Homepage = "https://github.com/user/my-package"
Issues = "https://github.com/user/my-package/issues"

[project.scripts]
my-tool = "my_package.cli:main"   # creates a command-line entry point
```

## Building a Distribution

A **wheel** (`.whl`) is a binary distribution — fast to install. A **source distribution** (`.tar.gz`, sdist) contains raw source files.

```bash
# Install the build frontend
pip install build

# Build both wheel and sdist
python -m build
# Creates: dist/my_package-1.0.0-py3-none-any.whl
#          dist/my_package-1.0.0.tar.gz
```

## Publishing to PyPI

```bash
# Install twine (the upload tool)
pip install twine

# Check the distribution files for errors
twine check dist/*

# Upload to the test PyPI (safe to experiment)
twine upload --repository testpypi dist/*

# Upload to the real PyPI
twine upload dist/*
```

You will need a PyPI account and an API token. Set the token as an environment variable or store it in `~/.pypirc`.

## Development Install

During development, install your package in **editable mode** so changes take effect immediately without reinstalling:

```bash
pip install -e .            # installs in editable mode
pip install -e ".[dev]"     # also installs optional dev dependencies
```

## Project Layout Reference

```
my-package/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
└── tests/
    ├── test_core.py
    └── conftest.py
```
