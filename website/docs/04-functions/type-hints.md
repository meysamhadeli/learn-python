## Type Hints

Type hints document expected types. Python does not enforce them at runtime, but editors and type checkers use them.

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

Built-in collection types can include their element types in brackets. For example, `list[int]` means "a list of integers" and `dict[str, str]` means "a dictionary with string keys and string values."

```python
def process(value: int | str) -> str:  # Python 3.10+ union syntax
    return str(value)

def find_user(id: int) -> dict | None:  # Or Optional[dict]
    return {"id": id} if id > 0 else None

def first(items: list[int]) -> int:
    return items[0]

def get_config() -> dict[str, str]:
    return {"host": "localhost", "port": "8080"}

def coordinates() -> tuple[float, float]:
    return (10.5, 20.3)
```

### Generics

Generic types let you write reusable code while keeping type information consistent. Define a `TypeVar` when a value can be many concrete types, but those types should stay linked across parameters, return values, or class members.

```python
from typing import TypeVar

T = TypeVar('T')

# T is only used for the input type here
def log_value(value: T) -> None:
    print(value)

# T is used for both input and output here
def first(items: list[T]) -> T | None:
    return items[0] if items else None

# Input can be any type that fills T
log_value(123)
log_value("hello")

# Returned value keeps the element type from the input list
value = first([1, 2, 3])     # value is int | None
text = first(["a", "b"])     # text is str | None
```

### Generic Classes

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

### Type Aliases

Use aliases to simplify repeated types:

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

Use `Callable` when a parameter accepts a function:

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

Validate hints with `mypy`:

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

For API clients, AI agents, and backend code, type hints pay off quickly because function boundaries stay clearer.