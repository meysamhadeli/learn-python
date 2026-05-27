# Packages

Packages are how Python scales module organization from a few files to larger codebases. They give related modules a shared namespace and let projects grow without collapsing into import chaos.

If modules organize code by file, packages organize it by folder and public API.

## What is a Package?

A **package** is a directory that contains a special file called `__init__.py`. This file (which can be empty) marks the directory as a Python package, allowing its modules to be imported with dot notation.

```
my_package/
├── __init__.py        # makes this directory a package
├── auth.py
├── database.py
└── utils/
    ├── __init__.py    # nested package
    └── helpers.py
```

## Importing from a Package

```python
# Import a module from the package
import my_package.auth

# Import a specific name
from my_package.auth import login, logout

# Import from a nested package
from my_package.utils.helpers import format_date
```

## `__init__.py` — Defining the Public API

The `__init__.py` runs when the package is first imported. Use it to expose a clean public API and hide internal structure:

```python
# my_package/__init__.py
from .auth import login, logout, User
from .database import connect, disconnect
from .utils.helpers import format_date

__version__ = "1.2.0"
__all__ = ["login", "logout", "User", "connect", "disconnect"]
```

With this setup, users can write `from my_package import login` instead of `from my_package.auth import login`.

## Relative Imports

Inside a package, use **relative imports** (prefixed with `.`) to import from sibling modules:

```python
# my_package/auth.py
from .database import connect      # sibling module
from .utils.helpers import hash_pw # subpackage
from . import config               # the package itself
```

Relative imports only work inside packages — not in scripts run directly.

## Namespace Packages (Python 3.3+)

Python 3.3+ supports **namespace packages** — directories without `__init__.py` that still act as packages. This is useful for splitting a package across multiple directories or repositories, but regular packages with `__init__.py` are still the norm for most projects.

## Practical Package Layout

A typical small project:

```
myproject/
├── pyproject.toml          # project metadata and build config
├── README.md
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
└── tests/
    ├── __init__.py
    ├── test_core.py
    └── test_utils.py
```

Placing the package under `src/` (the "src layout") prevents accidental imports of the development version instead of the installed version, which makes testing more reliable.
