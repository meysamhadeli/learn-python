# Falsy Values

## What is Truthiness?

Python's `if` statement and boolean operators do not require an explicit `True` or `False`. Instead, every object has a **truthiness** — it can be evaluated in a boolean context. An object is either **truthy** (behaves like `True`) or **falsy** (behaves like `False`).

This is one of the most Pythonic ideas for beginners to learn early. Instead of writing verbose checks such as `if len(items) > 0`, Python often lets you write the shorter and more natural `if items`.

```python
items = [1, 2, 3]

if items:
    print("We have data")
```

If `items` were empty, that condition would evaluate to `False`.

## The Complete List of Falsy Values

The following values evaluate to `False` in any boolean context. Everything else is truthy.

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

This explains why the same `if value:` pattern works across many types. Python is not asking "is this literally `True`?" It is asking "should this value count as true in a boolean context?"

## Practical Patterns

Truthiness enables clean, idiomatic code:

```python
# Guard against empty collections
def process(items):
    if not items:
        print("Nothing to process")
        return
    for item in items:
        ...

# Default values with 'or'
name = user_input or "Anonymous"  # if user_input is "", use fallback
port = config.get("port") or 8080

# Count truthy values in a list
flags = [True, False, True, None, 1, 0, "yes", ""]
print(sum(bool(f) for f in flags))  # 4
```

These patterns are concise, but they must still match your intent. For example, `port = config.get("port") or 8080` treats `0` as missing because `0` is falsy. That may be correct, or it may hide a real value.

When `None` specifically means "missing", be explicit:

```python
port = config.get("port")
if port is None:
    port = 8080
```

## Custom Truthiness

You can control how your own classes behave in boolean context by implementing `__bool__` (or `__len__` as a fallback — Python calls `len(obj) != 0` if `__bool__` is not defined):

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

This works because Python first looks for `__bool__()`. If that method is not defined, it falls back to `__len__()` and treats zero length as falsy.

The practical takeaway is simple:

- empty containers are falsy
- zero numeric values are falsy
- `None` is falsy
- most other values are truthy

Once that rule feels natural, your conditions become much easier to read.
