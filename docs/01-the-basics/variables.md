# Variables

## Assignment and Naming

In Python, a variable is created by assignment. There is no separate declaration step.

```python
name = "Python"
version = 3.13
is_awesome = True
_private = "convention only"
```

Use `snake_case` for variable and function names.

## Variables Are References

Variables are references to objects, not typed boxes.

```python
x = [1, 2, 3]
y = x           # y points to the SAME list object
y.append(4)
print(x)        # [1, 2, 3, 4] — modifying via y also affects x
```

If you need an independent copy of a mutable object, copy it:

```python
y = x.copy()    # or: y = x[:]
y.append(99)
print(x)        # unaffected
```

## Multiple Assignment

Python supports unpacking:

```python
x, y, z = 1, 2.5, "three"  # types can differ
a = b = c = 0               # all three point to the same object

# Swap without a temporary variable — a Python idiom
x, y = y, x
```

## Constants

Python has no hard constants. Use `UPPER_CASE` by convention:

```python
MAX_CONNECTIONS = 100
PI = 3.14159
DATABASE_URL = "postgresql://localhost/mydb"
```

## Deleting Variables

Use `del` to remove a name:

```python
temp = 42
del temp
# print(temp)  # NameError: name 'temp' is not defined
```
Usually you will use it more with container items than simple variables.
