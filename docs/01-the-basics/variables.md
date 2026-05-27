# Variables

## Assignment and Naming

In Python you create a variable simply by assigning a value to a name — no type declaration is needed. A variable name must start with a letter or underscore, can contain letters, digits, and underscores, and is case-sensitive (`count` and `Count` are different variables).

```python
name = "Python"
version = 3.13
is_awesome = True
_private = "convention only"
```

Python follows **snake_case** for variable and function names (e.g. `user_name`, `total_price`), as specified in [PEP 8](https://peps.python.org/pep-0008/).

## Variables Are References

This is one of Python's most important concepts: a variable is **not a box that holds a value** — it is a **label that points to an object** in memory. When you write `x = 42`, Python creates the integer object `42` in memory and makes `x` point to it.

```python
x = [1, 2, 3]
y = x           # y points to the SAME list object
y.append(4)
print(x)        # [1, 2, 3, 4] — modifying via y also affects x
```

Use `id()` to see the memory address an object lives at:

```python
a = "hello"
b = "hello"
print(id(a) == id(b))  # Often True — Python interns short strings
```

If you want an independent copy of a mutable object, use `copy()` or slicing:

```python
y = x.copy()    # or: y = x[:]
y.append(99)
print(x)        # unaffected
```

## Multiple Assignment

Python lets you assign multiple variables in one line using **tuple unpacking**:

```python
x, y, z = 1, 2.5, "three"  # types can differ
a = b = c = 0               # all three point to the same object

# Swap without a temporary variable — a Python idiom
x, y = y, x
```

## Constants

Python has no built-in constant mechanism. The convention is to name constants in **UPPER_CASE** to signal they should not be reassigned:

```python
MAX_CONNECTIONS = 100
PI = 3.14159
DATABASE_URL = "postgresql://localhost/mydb"
```

Nothing prevents another part of the code from reassigning these — it is a social convention, not a language feature. For stricter enforcement, use `typing.Final`:

```python
from typing import Final
MAX_RETRIES: Final = 3
```

## Deleting Variables

Use `del` to remove a variable name from the current scope:

```python
temp = 42
del temp
# print(temp)  # NameError: name 'temp' is not defined
```

This does not necessarily destroy the object — Python's garbage collector reclaims memory when an object has no more references pointing to it.
