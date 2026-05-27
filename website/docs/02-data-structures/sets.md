# Sets

Sets are designed for uniqueness and fast membership testing. They are less about storing values in order and more about answering questions like "have I seen this before?" or "what values overlap between these groups?"

That is why sets become especially useful in validation, deduplication, and comparison tasks.

## What is a Set?

A set is an **unordered collection of unique, hashable objects**. Sets are backed by a hash table, giving O(1) average-case performance for membership tests, insertion, and deletion. Because sets are unordered, they do not support indexing or slicing.

The primary use cases for sets are:
- **Deduplication** — removing duplicates from any sequence
- **Membership testing** — `x in my_set` is O(1) vs O(n) for a list
- **Set operations** — unions, intersections, and differences

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

Set algebra is built directly into Python:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union — all elements from both
print(a | b)         # {1, 2, 3, 4, 5, 6}
print(a.union(b))    # same

# Intersection — only elements in both
print(a & b)              # {3, 4}
print(a.intersection(b))  # same

# Difference — in a but not in b
print(a - b)              # {1, 2}
print(a.difference(b))    # same

# Symmetric difference — in either, but not both
print(a ^ b)                        # {1, 2, 5, 6}
print(a.symmetric_difference(b))    # same
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
# Deduplication while preserving order (Python 3.7+)
def deduplicate(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]

# Fast membership test
VALID_EXTENSIONS = {".py", ".txt", ".json", ".yaml"}
filename = "script.py"
if filename.endswith(tuple(VALID_EXTENSIONS)):
    print("Valid file")

# Find common elements between two lists efficiently
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common = set(list_a) & set(list_b)  # {3, 4, 5}
only_in_a = set(list_a) - set(list_b)  # {1, 2}
```

## Frozensets

A `frozenset` is an **immutable** set — it can be used as a dictionary key or stored in another set:

```python
fs = frozenset([1, 2, 3])
d = {fs: "value"}       # works because frozenset is hashable
# fs.add(4)             # AttributeError — frozensets are immutable
```
