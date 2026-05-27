# Built-in Data Types

Python has a small set of built-in types that cover almost every need. They are all objects — even `int` and `bool` — and every value carries its type with it at runtime.

That last point is important: Python is **dynamically typed**, which means values know their own type while the variable name does not permanently lock to one type.

```python
value = 10
print(type(value))

value = "ten"
print(type(value))
```

This flexibility is convenient, but it also means you need to pay attention to what kind of value a variable holds at a given moment.

## int

Python integers have **arbitrary precision** — they grow as large as your memory allows, with no overflow and no need to choose between `int` and `long` as in languages like Java or C.

```python
count = 42
big_number = 10 ** 100        # a googol — no problem
binary = 0b1010               # 10 in binary
hexadecimal = 0xFF            # 255 in hex
```

Arithmetic on integers is exact. For floating-point results, use `/`:

```python
print(7 // 2)   # 3   (floor division — always int)
print(7 / 2)    # 3.5 (true division — always float)
print(7 % 2)    # 1   (remainder)
```

If you are learning from calculator examples, remember this rule from the Python tutorial: `/` means real division, while `//` means floor division. Mixing them up is a very common source of off-by-one style mistakes.

## float

Floats are **IEEE 754 double-precision** numbers (64-bit). They can represent an enormous range of values but with limited precision — about 15–17 significant decimal digits.

```python
pi = 3.14159
small = 1.5e-4      # scientific notation: 0.00015
large = 6.022e23    # Avogadro's number
```

**The classic gotcha:**

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False!
```

This is a consequence of binary floating-point, not a Python bug. For exact decimal arithmetic use `decimal.Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — exact
```

This is why equality comparisons with floats should be treated carefully. For many real-world tasks, you compare within a tolerance instead of expecting perfect decimal precision.

## complex

Python has **native complex number support** — useful in signal processing, scientific computing, and some mathematical algorithms.

```python
c = 3 + 4j
print(c.real)    # 3.0
print(c.imag)    # 4.0
print(abs(c))    # 5.0 — Euclidean magnitude: sqrt(3² + 4²)
print(c * 2)     # (6+8j)
```

The `j` suffix (not `i`) denotes the imaginary part. Complex arithmetic follows standard mathematical rules.

If you are not doing math-heavy work, you may rarely use `complex` directly. It is still useful to know that Python includes it natively instead of treating it as a special library-only feature.

## str

Strings are **immutable sequences of Unicode characters**. "Immutable" means once created, their content cannot change — any operation that appears to modify a string actually creates a new one.

```python
text = "Python"
print(text[0])       # 'P'       — indexing from 0
print(text[-1])      # 'n'       — negative indexes from the end
print(text[1:4])     # 'yth'     — slicing [start:stop]
print(text[::-1])    # 'nohtyP'  — reverse via step
print(len(text))     # 6
```

Strings support many built-in methods:

```python
s = "  Hello, World!  "
print(s.strip())            # "Hello, World!"
print(s.lower())            # "  hello, world!  "
print(s.replace("World", "Python"))  # "  Hello, Python!  "
print("Hello, World!".split(", "))   # ['Hello', 'World!']
print("-".join(["a", "b", "c"]))     # "a-b-c"
print("hello".startswith("he"))      # True
```

String literals can be written in several ways:

```python
single = 'Hello'
double = "Hello"              # identical
multiline = """Line 1
Line 2"""
raw = r"C:\Users\Name"        # backslashes are literal — no escape processing
byte_str = b"binary data"     # bytes object, not str
```

Two details from the Python tutorial matter a lot here:

- strings are sequences, so indexing and slicing work naturally
- strings are immutable, so operations create new strings instead of changing the old one in place

```python
word = "Python"
new_word = "J" + word[1:]

print(word)      # Python
print(new_word)  # Jython
```

Beginners often expect `word[0] = "J"` to work, but it fails because strings cannot be modified character by character.

## bool

`bool` is a **subclass of `int`** — `True` equals `1` and `False` equals `0`. This means booleans work in arithmetic:

```python
print(True + True)    # 2
print(True * 5)       # 5
print(sum([True, False, True, True]))  # 3  — counts Trues

is_adult = age >= 18  # comparison returns a bool
```

Boolean values are created by comparisons, `not`, membership tests (`in`), and truthiness checks (`bool(value)`).

In practice, `bool` appears everywhere because `if`, `while`, and logical expressions all depend on it. Even when you do not write `True` or `False` yourself, Python is constantly producing boolean results behind the scenes.

## None

`None` is Python's null value — the sole instance of `NoneType`. It represents the absence of a value and is what functions return when they have no explicit `return` statement.

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

`None` is a **singleton** — there is only one `None` object in any Python process. That is why `is None` is correct and `== None` is discouraged (a custom class could override `__eq__` to return `True` when compared to `None`).

Treat `None` as "no value yet" or "nothing was found". That makes it easier to read functions and conditionals:

```python
user = None

if user is None:
    print("Please log in first")
```
