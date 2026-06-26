# Modules

Modules are how Python code is organized into files and reusable namespaces.

## What is a Module?

A module is any `.py` file. Importing it runs the file once and makes its names available.

## Importing Modules

```python
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
from math import pi, sqrt, ceil
print(pi)          # 3.14159...
print(sqrt(25))    # 5.0

from math import *
```

Avoid `from module import *` in real code.

## Aliases

```python
import numpy as np         # de facto standard
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt
now = dt.now()
```

## Module Search Path

Python looks for imports in `sys.modules`, built-ins, and directories from `sys.path`.

```python
import sys
print(sys.path)   # list of directories Python searches
```

## The Standard Library

Python ships with a large standard library. Useful modules include:

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

Use the `__name__ == "__main__"` guard when a file should be both importable and runnable:

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

`__all__` controls what `from module import *` exports:

```python
# utils.py
__all__ = ["public_func", "PublicClass"]

def public_func():
    ...

def _internal():    # _ prefix also signals non-public, but __all__ is authoritative
    ...
```
