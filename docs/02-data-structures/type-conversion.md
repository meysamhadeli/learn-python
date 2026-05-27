# Type Conversion

## Explicit vs Implicit Conversion

Python performs **almost no implicit type coercion**. Unlike JavaScript (where `"5" + 1 = "51"`) or C (where types are silently cast), Python raises a `TypeError` when you mix incompatible types:

```python
# This fails — Python won't silently convert
# print("Age: " + 30)   # TypeError: can only concatenate str (not "int") to str

# You must convert explicitly:
print("Age: " + str(30))  # "Age: 30"
print(f"Age: {30}")       # better — f-strings handle conversion automatically
```

## Numeric Conversions

```python
# String to number
x = int("42")           # 42
y = float("3.14")       # 3.14
z = int("0xFF", 16)     # 255  — parse hex string
b = int("1010", 2)      # 10   — parse binary string

# Number to string
s = str(100)            # "100"
s = str(3.14)           # "3.14"
s = hex(255)            # "0xff"
s = bin(10)             # "0b1010"
s = oct(8)              # "0o10"

# Between numeric types
i = int(3.9)            # 3    — truncates toward zero (not rounds!)
f = float(7)            # 7.0
c = complex(3)          # (3+0j)
```

**`int()` truncates, it does not round:**

```python
print(int(3.9))    # 3  — NOT 4
print(int(-3.9))   # -3 — NOT -4

# To round: use round()
print(round(3.9))  # 4
print(round(3.5))  # 4  — rounds to even (banker's rounding)
```

## Collection Conversions

```python
# To list
from_tuple  = list((1, 2, 3))      # [1, 2, 3]
from_set    = list({3, 1, 2})      # order not guaranteed
from_string = list("hello")        # ['h', 'e', 'l', 'l', 'o']
from_range  = list(range(5))       # [0, 1, 2, 3, 4]
from_dict   = list({"a": 1, "b": 2})  # ['a', 'b']  — keys only!

# To tuple
t = tuple([1, 2, 3])      # (1, 2, 3)

# To set — deduplicates
unique = set([1, 2, 2, 3, 3])  # {1, 2, 3}

# To dict — from key-value pairs
d = dict([("a", 1), ("b", 2)])
d = dict(zip(["a", "b"], [1, 2]))
```

## Boolean Conversion

```python
# Any object can be converted to bool
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hi"))    # True
print(bool([]))      # False
print(bool([0]))     # True  — a list with one element, even if that element is 0
```

See the [Falsy Values](../01-the-basics/falsy-values) page for the full rules.

## `isinstance()` vs Type Conversion

Before converting, you sometimes want to check the type first:

```python
def process(value):
    if isinstance(value, str):
        value = int(value)
    return value * 2

# isinstance() accepts a tuple of types:
def is_numeric(x):
    return isinstance(x, (int, float, complex))
```

Use `isinstance()` rather than `type(x) == int` — it correctly handles subclasses.
