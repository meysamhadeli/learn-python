# Modules

## What is a Module?

A **module** is any Python file (`.py`). When you `import` a module, Python executes its code once and makes its names available under the module's namespace. Subsequent imports of the same module reuse the cached version from `sys.modules` — the code is not re-executed.

## Importing Modules

```python
# Import the whole module — access names via dot notation
import math
import os
import sys

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(os.getcwd())      # current directory
print(sys.version)      # Python version string
```

## Selective Imports

```python
# Import specific names into the current namespace
from math import pi, sqrt, ceil
print(pi)          # 3.14159...
print(sqrt(25))    # 5.0

# Import all public names (avoid — pollutes namespace, hides where names come from)
from math import *
```

## Aliases

```python
# Give a module a shorter alias
import numpy as np         # de facto standard
import pandas as pd
import matplotlib.pyplot as plt

# Alias an imported name
from datetime import datetime as dt
now = dt.now()
```

## Module Search Path

When you `import foo`, Python looks for `foo` in this order:

1. `sys.modules` (already-imported modules)
2. Built-in modules (compiled into the interpreter)
3. Directories in `sys.path` — which includes the script's directory, `PYTHONPATH`, and site-packages

```python
import sys
print(sys.path)   # list of directories Python searches
```

## The Standard Library

Python ships with an extensive standard library. Key modules:

| Module | Purpose |
|--------|---------|
| `os` | OS interaction, file system |
| `sys` | Interpreter internals, exit, argv |
| `pathlib` | Modern path manipulation |
| `json` | JSON encoding/decoding |
| `re` | Regular expressions |
| `datetime` | Dates and times |
| `collections` | Specialized containers |
| `itertools` | Iterator utilities |
| `functools` | Higher-order functions |
| `logging` | Structured logging |
| `threading` | Thread-based concurrency |
| `asyncio` | Async/await event loop |

## Writing Your Own Module

Any `.py` file is a module. Use the `__name__ == "__main__"` guard to separate code that runs when the file is a script from code that runs when imported:

```python
# greetings.py
def hello(name: str) -> str:
    return f"Hello, {name}!"

def goodbye(name: str) -> str:
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    # Only runs when executed directly: python3 greetings.py
    print(hello("World"))
```

```python
# main.py
from greetings import hello
print(hello("Alice"))
```

## `__all__` — Controlling Public API

Define `__all__` in a module to specify which names are exported when someone does `from module import *`:

```python
# utils.py
__all__ = ["public_func", "PublicClass"]

def public_func():
    ...

def _internal():    # _ prefix also signals non-public, but __all__ is authoritative
    ...
```
