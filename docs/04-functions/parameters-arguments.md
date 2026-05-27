# Parameters & Arguments

This page explains one of the most important parts of Python function design: how callers provide data to a function and how the function definition controls that calling style.

The details matter because many real bugs come from argument ordering, mutable defaults, or APIs that are technically valid but hard to call correctly.

## Positional Parameters

The simplest parameters — arguments are matched left to right by position:

```python
def power(base, exponent):
    return base ** exponent

power(2, 10)    # 1024 — base=2, exponent=10
```

## Default Parameter Values

Parameters can have default values, making them optional at the call site:

```python
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

greet("Alice")                    # "Hello, Alice!"
greet("Bob", "Hi")                # "Hi, Bob!"
greet("Carol", punctuation=".")   # "Hello, Carol."
```

**The mutable default trap** — the default value is evaluated **once** when the function is defined, not on each call. Using a mutable object (list, dict) as a default creates a shared state across calls:

```python
# WRONG — the list is shared across all calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))   # ["a"]
print(add_item("b"))   # ["a", "b"]  — unexpected!

# CORRECT — use None as sentinel, create fresh object inside
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Keyword Arguments

At the call site, you can pass any argument by name, which makes the code more readable and lets you pass arguments out of order:

```python
def connect(host, port, timeout=30, ssl=True):
    ...

connect("db.example.com", 5432)
connect(port=5432, host="db.example.com", ssl=False)
connect("db.example.com", 5432, timeout=60)
```

## `*args` — Variable Positional Arguments

Prefix a parameter with `*` to collect any number of positional arguments into a **tuple**:

```python
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)          # 6
total(10, 20, 30, 40)   # 100

# Spread a sequence with *
nums = [1, 2, 3, 4, 5]
print(total(*nums))     # 15
```

## `**kwargs` — Variable Keyword Arguments

Prefix a parameter with `**` to collect any number of keyword arguments into a **dict**:

```python
def describe(**attributes):
    for key, value in attributes.items():
        print(f"  {key}: {value}")

describe(name="Alice", age=30, city="New York")
# name: Alice
# age: 30
# city: New York

# Spread a dict with **
config = {"host": "localhost", "port": 8080}
connect(**config)   # equivalent to connect(host="localhost", port=8080)
```

## Keyword-Only and Positional-Only Parameters

Python lets you enforce how arguments must be passed:

```python
# Parameters after * must be passed by keyword
def fetch(url, *, timeout=30, retries=3):
    ...

fetch("https://api.example.com")              # OK
fetch("https://api.example.com", timeout=60)  # OK
# fetch("https://api.example.com", 60)        # TypeError

# Parameters before / must be passed positionally (Python 3.8+)
def normalize(x, y, /, *, precision=2):
    ...

normalize(3.0, 4.0)                    # OK
# normalize(x=3.0, y=4.0)             # TypeError — positional-only
normalize(3.0, 4.0, precision=4)      # OK
```

## Full Signature

The complete parameter order is:

```python
def func(pos_only, /, standard, *, kw_only):
    ...

# Or with variadic:
def full(pos_only, /, positional, *args, kw_only, **kwargs):
    ...
```
