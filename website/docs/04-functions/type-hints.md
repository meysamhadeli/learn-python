## Type Hints

Type hints let you document expected types in your code. They're optional - Python doesn't enforce them at runtime - but they help IDEs, type checkers, and other developers understand your code better.

### Basic Syntax

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def log(message: str) -> None:  # Returns nothing
    print(message)
```

### Common Types

```python
# Basic types
def process(value: int | str) -> str:  # Python 3.10+ union syntax
    return str(value)

# Optional values (can be None)
def find_user(id: int) -> dict | None:  # Or Optional[dict]
    return {"id": id} if id > 0 else None

# Collections
def first(items: list[int]) -> int:
    return items[0]

def get_config() -> dict[str, str]:
    return {"host": "localhost", "port": "8080"}

def coordinates() -> tuple[float, float]:
    return (10.5, 20.3)
```

### Generics

Generics let you write type-safe code that works with different types while preserving type information.

#### Collection Generics

Specify what types your collections contain:

```python
# Lists, dicts, tuples, sets
def process_users(users: list[dict[str, int | str]]) -> list[str]:
    return [str(user["id"]) for user in users]

def stats(data: list[float]) -> tuple[float, float, float]:
    return min(data), max(data), sum(data) / len(data)

# Nested collections
def flatten(matrix: list[list[float]]) -> list[float]:
    return [x for row in matrix for x in row]
```

**Note:** Python 3.9+ uses built-in types (`list`, `dict`, `tuple`). Older code may use `List`, `Dict` from `typing`.

#### Type Variables (Generic Parameters)

When the return type relates to the input type:

```python
from typing import TypeVar

T = TypeVar('T')

def first(items: list[T]) -> T | None:
    return items[0] if items else None

# Type is preserved
value = first([1, 2, 3])     # value is int | None
text = first(["a", "b"])     # text is str | None
```

#### Generic Classes

```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T | None:
        return self._items.pop() if self._items else None

# Usage - type is preserved
int_stack = Stack[int]()
int_stack.push(1)
value = int_stack.pop()  # value is int

str_stack = Stack[str]()
str_stack.push("hello")
text = str_stack.pop()   # text is str
```

#### Constraining Generic Types

Restrict what types can be used:

```python
# T must be int or float
Number = TypeVar('Number', int, float)

def average(numbers: list[Number]) -> float:
    return sum(numbers) / len(numbers)

# Works with ints, floats, or mixed
avg = average([1, 2, 3.5, 4])
```

### Type Aliases

Simplify complex or repeated types:

```python
from typing import TypeAlias

UserID: TypeAlias = int
Vector: TypeAlias = list[float]
JSONValue: TypeAlias = str | int | float | bool | None | dict | list

def get_user(id: UserID) -> dict:
    return {"id": id}

def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))
```

### Function Types (Callable)

When a parameter accepts a function:

```python
from collections.abc import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Callable that takes two strings and returns a string
def combine(func: Callable[[str, str], str], a: str, b: str) -> str:
    return func(a, b)

apply(lambda x: x * 2, 5)        # 10
combine(lambda a, b: a + b, "Hello", "World")  # "HelloWorld"
```

### Type Checking with mypy

Type hints are validated by tools like `mypy`:

```bash
pip install mypy
mypy your_script.py
```

This catches type errors before runtime:
```python
def add(a: int, b: int) -> int:
    return a + b

add("1", "2")  # mypy will complain: Argument 1 to "add" has incompatible type "str"
```