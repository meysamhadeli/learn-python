# Falsy Values

## What is Truthiness?

In Python, values can be truthy or falsy in `if`, `while`, `and`, and `or` expressions.

```python
items = [1, 2, 3]

if items:
    print("We have data")
```

## The Complete List of Falsy Values

These values are falsy. Most other values are truthy.

| Value | Type |
|-------|------|
| `False` | bool |
| `None` | NoneType |
| `0` | int |
| `0.0` | float |
| `0j` | complex |
| `""` | str (empty) |
| `[]` | list (empty) |
| `()` | tuple (empty) |
| `{}` | dict (empty) |
| `set()` | set (empty) |
| `b""` | bytes (empty) |

```python
# All of these branches are skipped:
if False: ...
if None: ...
if 0: ...
if "": ...
if []: ...
if {}: ...
```

## Practical Patterns

Truthiness leads to short, idiomatic checks:

```python
def process(items):
    if not items:
        print("Nothing to process")
        return
    for item in items:
        ...

name = user_input or "Anonymous"  # if user_input is "", use fallback
port = config.get("port") or 8080
```

Be careful: `x or default` also treats `0`, `""`, and `[]` as missing.

When only `None` means missing, be explicit:

```python
port = config.get("port")
if port is None:
    port = 8080
```

## Custom Truthiness

Custom classes can define truthiness with `__bool__` or `__len__`:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0

account = BankAccount(0)
if not account:
    print("Account is empty")  # This prints

class Queue:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)  # falsy when empty

q = Queue([])
if not q:
    print("Queue is empty")     # This prints
```

Practical rule: empty containers, zero numbers, and `None` are falsy.

Once that rule feels natural, your conditions become much easier to read.
