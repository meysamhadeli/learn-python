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

The official tutorial introduces assignment very early because it is one of the main differences beginners notice when coming from other languages: you do not write a declaration like `string name;` or `let name;` first. You simply bind a name to a value.

```python
language = "Python"
year = 1991
```

After that assignment, the names `language` and `year` can be reused anywhere in the current scope.

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

This reference model explains a lot of Python behavior:

- assigning one list to another name does **not** make a copy
- changing a mutable object through one name is visible through every name pointing to it
- rebinding a name does not change the old object; it only changes what the name points to

```python
items = [1, 2, 3]
other = items
items = [10, 20, 30]

print(other)  # [1, 2, 3]
```

Here, `other` still points to the original list. Reassigning `items` did not rewrite that old list.

## Multiple Assignment

Python lets you assign multiple variables in one line using **tuple unpacking**:

```python
x, y, z = 1, 2.5, "three"  # types can differ
a = b = c = 0               # all three point to the same object

# Swap without a temporary variable — a Python idiom
x, y = y, x
```

This works because Python evaluates the full right-hand side first, then performs the assignments. That is why swapping values is safe and does not overwrite one side too early.

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

For course code and small scripts, the naming convention is usually enough. In larger codebases, `Final` helps readers and type checkers understand your intent.

## Deleting Variables

Use `del` to remove a variable name from the current scope:

```python
temp = 42
del temp
# print(temp)  # NameError: name 'temp' is not defined
```

This does not necessarily destroy the object — Python's garbage collector reclaims memory when an object has no more references pointing to it.

Most beginners do not need `del` often. It appears more in cases like:

- removing items from containers
- cleaning up names in a narrow scope
- demonstrating how references work

The main lesson is that names and objects are related, but they are not the same thing.
