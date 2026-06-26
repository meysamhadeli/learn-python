# Sets

Sets are for uniqueness and fast membership tests.

## What is a Set?

A set is an unordered collection of unique, hashable objects.

```python
colors = {"red", "green", "blue"}
from_list = set([1, 2, 2, 3, 3])   # {1, 2, 3} — duplicates removed
empty = set()                        # NOT {} — that creates an empty dict!
```

## Adding and Removing Elements

```python
s = {1, 2, 3}

s.add(4)          # add a single element
s.update([5, 6])  # add multiple elements

s.remove(3)       # raises KeyError if not present
s.discard(99)     # safe — no error if not present
s.pop()           # remove and return an arbitrary element (order is undefined)
s.clear()         # remove all elements
```

## Set Operations

Set algebra is built in:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)         # {1, 2, 3, 4, 5, 6}

print(a & b)              # {3, 4}

print(a - b)              # {1, 2}

print(a ^ b)                        # {1, 2, 5, 6}
```

## Set Comparisons

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))     # True  — all of a is in b
print(a <= b)            # True  — same as issubset
print(b.issuperset(a))   # True  — b contains all of a
print(a.isdisjoint({6, 7}))  # True — no elements in common
```

## Practical Uses

```python
def deduplicate(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

VALID_EXTENSIONS = {".py", ".txt", ".json", ".yaml"}
filename = "script.py"
if filename.endswith(tuple(VALID_EXTENSIONS)):
    print("Valid file")
```

## Frozensets

A `frozenset` is an immutable set:

```python
fs = frozenset([1, 2, 3])
d = {fs: "value"}       # works because frozenset is hashable
```
