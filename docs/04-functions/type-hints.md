# Type Hints

Type hints add structure to Python code without changing Python into a statically typed language. They are best understood as communication tools for readers, editors, and type checkers rather than runtime enforcement.

This page is about learning what hints express well, where they help maintainability, and why they remain optional in normal Python execution.

## What Are Type Hints?

Introduced in PEP 484, **type hints** are optional annotations that document the expected types of function parameters and return values. Python **does not enforce them at runtime** — they are purely informational for developers and static analysis tools like `mypy`, `pyright`, and IDEs.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

The `->` annotation on the function signature declares the return type. Both annotations are accessible via `add.__annotations__`.

## Common Annotations

```python
from typing import Optional, Union, Any

# Optional — the value can be the type or None
def find(items: list, target: int) -> Optional[int]:
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

# Python 3.10+ shorthand (preferred for new code)
def find2(items: list, target: int) -> int | None:
    ...

# Union — multiple possible types
def process(value: int | str | None) -> str:
    return str(value) if value is not None else ""

# Any — opt out of checking (use sparingly)
def debug(value: Any) -> None:
    print(repr(value))
```

## Generic Collections (Python 3.9+)

Before Python 3.9, you had to import generics from `typing`. Since 3.9, built-in types support subscripting directly:

```python
# Python 3.9+
def first(items: list[int]) -> int:
    return items[0]

def merge(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    return {**a, **b}

def flatten(matrix: list[list[float]]) -> list[float]:
    return [x for row in matrix for x in row]

# Tuple with specific element types
def stats(data: list[float]) -> tuple[float, float, float]:
    return min(data), max(data), sum(data) / len(data)
```

## Type Aliases

Give a meaningful name to a complex type to improve readability:

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
JSONValue: TypeAlias = str | int | float | bool | None | dict | list

def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))
```

## Callable Types

When a parameter is a function, annotate it with `Callable`:

```python
from collections.abc import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def apply_all(
    funcs: list[Callable[[str], str]],
    text: str,
) -> str:
    for fn in funcs:
        text = fn(text)
    return text
```

## Running `mypy`

Type hints are most useful when checked with a static type checker:

```bash
pip install mypy
mypy my_script.py
```

`mypy` will report type errors — arguments passed with the wrong type, return values that don't match, and missing annotations — before you even run the code.
