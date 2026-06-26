# Built-in Data Types

Python's core built-in types cover most day-one work. Python is dynamically typed, so values carry their type at runtime.

```python
value = 10
print(type(value))

value = "ten"
print(type(value))
```

## int

`int` has arbitrary precision.

```python
count = 42
big_number = 10 ** 100        # a googol — no problem
binary = 0b1010               # 10 in binary
hexadecimal = 0xFF            # 255 in hex
```

Use `/` for float division and `//` for floor division:

```python
print(7 // 2)   # 3   (floor division — always int)
print(7 / 2)    # 3.5 (true division — always float)
print(7 % 2)    # 1   (remainder)
```

## float

`float` is fast and common, but it is not exact for decimal fractions.

```python
pi = 3.14159
small = 1.5e-4      # scientific notation: 0.00015
large = 6.022e23    # Avogadro's number
```

Classic gotcha:

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False!
```

For exact decimal arithmetic, use `decimal.Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — exact
```

## complex

Python also has native `complex` numbers, mostly useful in scientific code:

```python
c = 3 + 4j
print(c.real)    # 3.0
print(c.imag)    # 4.0
print(abs(c))    # 5.0 — Euclidean magnitude: sqrt(3² + 4²)
print(c * 2)     # (6+8j)
```

## str

Strings are immutable Unicode text.

```python
text = "Python"
print(text[0])       # 'P'       — indexing from 0
print(text[-1])      # 'n'       — negative indexes from the end
print(text[1:4])     # 'yth'     — slicing [start:stop]
print(text[::-1])    # 'nohtyP'  — reverse via step
print(len(text))     # 6
```

Common string methods:

```python
s = "  Hello, World!  "
print(s.strip())            # "Hello, World!"
print(s.lower())            # "  hello, world!  "
print(s.replace("World", "Python"))  # "  Hello, Python!  "
print("Hello, World!".split(", "))   # ['Hello', 'World!']
print("-".join(["a", "b", "c"]))     # "a-b-c"
print("hello".startswith("he"))      # True
```

Useful literal forms:

```python
single = 'Hello'
double = "Hello"              # identical
multiline = """Line 1
Line 2"""
raw = r"C:\Users\Name"        # backslashes are literal — no escape processing
```

Strings cannot be changed in place.

## bool

`bool` has two values: `True` and `False`.

```python
print(True + True)    # 2
print(True * 5)       # 5
print(sum([True, False, True, True]))  # 3  — counts Trues
```

## None

`None` means "no value":

```python
result = None

if result is None:           # always use 'is', not '=='
    print("No result yet")

def find(items, target):
    for item in items:
        if item == target:
            return item
    # implicitly returns None if not found
```
Use `is None`, not `== None`.
