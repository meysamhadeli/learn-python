# Dictionaries

Dictionaries map keys to values and are one of Python's most important data structures.

## What is a Dictionary?

A dictionary is a mutable mapping of unique keys to values. Lookups are fast, keys must be hashable, and insertion order is preserved.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Alice", age=30)
```

## Accessing Values

```python
person = {"name": "Alice", "age": 30}

print(person["name"])          # "Alice"

print(person.get("email"))          # None
print(person.get("email", "N/A"))   # "N/A"

if "age" in person:
    print(person["age"])
```

## Modifying Dictionaries

```python
person = {"name": "Alice", "age": 30}

person["email"] = "alice@example.com"
person["age"] = 31

person |= {"city": "Boston", "lang": "Python"}

person.update({"country": "US"})

del person["lang"]                      # raises KeyError if missing
email = person.pop("email")             # remove and return value
removed = person.pop("missing", None)   # safe remove with default
```

## Iterating

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:                 # iterate over keys (default)
    print(key)

for value in person.values():      # values view
    print(value)

for key, value in person.items():  # key-value pairs
    print(f"{key}: {value}")
```

## Dict Comprehensions

```python
squares = {x: x**2 for x in range(6)}

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

## Merging Dictionaries

```python
defaults = {"color": "blue", "size": 10, "visible": True}
overrides = {"size": 20, "opacity": 0.8}

merged = defaults | overrides
```

## `setdefault` and `defaultdict`

`setdefault()` is useful for grouping:

```python
groups = {}
for word in ["apple", "ant", "banana", "bear"]:
    groups.setdefault(word[0], []).append(word)
```

For heavy grouping code, `collections.defaultdict` is often cleaner.
