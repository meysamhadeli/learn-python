# Dictionaries

Dictionaries are one of Python's most important data structures because they let you attach meaning to values through keys. When you need lookup by name, ID, or label, a dictionary is often the most natural fit.

This page is easiest to understand if you think of a dictionary as a mapping from keys to values rather than as a sequence with positions.

## What is a Dictionary?

A dictionary is a **mutable mapping** of unique keys to values. As of Python 3.7+, dictionaries preserve **insertion order**. Lookup by key is O(1) on average (backed by a hash table). Keys must be hashable — strings, numbers, and tuples of hashables all work; lists and dicts cannot be keys.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)
```

## Accessing Values

```python
person = {"name": "Alice", "age": 30}

# Direct access — raises KeyError if the key doesn't exist
print(person["name"])          # "Alice"

# Safe access with a default
print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"

# Check if a key exists before accessing
if "age" in person:
    print(person["age"])
```

## Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30}

# Add or update a key
person["email"] = "alice@example.com"
person["age"] = 31

# Merge another dict (Python 3.9+ syntax)
person |= {"city": "Boston", "lang": "Python"}

# update() works in all versions
person.update({"country": "US"})

# Remove a key
del person["lang"]                      # raises KeyError if missing
email = person.pop("email")             # remove and return value
removed = person.pop("missing", None)   # safe remove with default

# Remove last inserted item (Python 3.7+ order is guaranteed)
last_key, last_val = person.popitem()
```

## Iterating

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:                 # iterate over keys (default)
    print(key)

for key in person.keys():          # explicit keys view
    print(key)

for value in person.values():      # values view
    print(value)

for key, value in person.items():  # key-value pairs
    print(f"{key}: {value}")
```

The views returned by `.keys()`, `.values()`, and `.items()` are **live views** — they reflect changes to the dict without creating a copy.

## Dict Comprehensions

```python
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert a dictionary (assuming unique values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Filter while building
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

## Merging Dictionaries

```python
defaults = {"color": "blue", "size": 10, "visible": True}
overrides = {"size": 20, "opacity": 0.8}

# Python 3.9+ — | operator
merged = defaults | overrides
# {"color": "blue", "size": 20, "visible": True, "opacity": 0.8}

# Older style
merged = {**defaults, **overrides}   # right side wins on conflict
```

## `setdefault` and `defaultdict`

`setdefault` is useful for grouping — it inserts a default value only if the key is missing, then returns the value:

```python
groups = {}
for word in ["apple", "ant", "banana", "bear"]:
    groups.setdefault(word[0], []).append(word)
# {"a": ["apple", "ant"], "b": ["banana", "bear"]}
```

For this pattern, `collections.defaultdict` is even cleaner — see the [Collections Module](./collections-module) page.
