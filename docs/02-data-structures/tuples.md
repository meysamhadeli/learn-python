# Tuples

## What is a Tuple?

A tuple is an **ordered, immutable** sequence. Once created, its contents cannot change. Tuples are slightly more memory-efficient than lists and can be used as dictionary keys or set members (because they are hashable, provided all their elements are also hashable).

```python
point = (10, 20)
rgb = (255, 128, 0)
single = (42,)        # trailing comma is REQUIRED for single-element tuples
empty = ()
no_parens = 1, 2, 3   # parentheses are optional — this is also a tuple
```

**A common mistake:**

```python
x = (42)    # This is NOT a tuple — just the integer 42 in parentheses
x = (42,)   # This IS a tuple with one element
```

## Immutability

Tuples cannot be modified after creation:

```python
t = (1, 2, 3)
# t[0] = 99       # TypeError: 'tuple' object does not support item assignment
# t.append(4)     # AttributeError: 'tuple' object has no attribute 'append'
```

However, if a tuple contains a mutable object (like a list), that object can still be modified:

```python
t = ([1, 2], [3, 4])
t[0].append(99)
print(t)   # ([1, 2, 99], [3, 4]) — the list inside was mutated
```

## Unpacking

Tuple unpacking is one of Python's most useful features:

```python
point = (10, 20)
x, y = point         # basic unpacking

# Ignore values with _
first, _, third = (1, 2, 3)

# Star unpacking — collect remaining items
head, *tail = (1, 2, 3, 4, 5)    # head=1, tail=[2,3,4,5]
*init, last = (1, 2, 3, 4, 5)    # init=[1,2,3,4], last=5
first, *middle, last = range(10)  # first=0, middle=[1..8], last=9

# Swap without a temp variable
a, b = 10, 20
a, b = b, a   # a=20, b=10
```

## Returning Multiple Values

Functions can return multiple values as a tuple — the most common tuple use case:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)   # 1 9
```

## Tuples as Dictionary Keys

Because tuples are hashable, they can be used as dictionary keys — lists cannot:

```python
# Coordinate lookup
distances = {
    (0, 0): 0,
    (1, 0): 1,
    (0, 1): 1,
    (1, 1): 1.414,
}

print(distances[(1, 1)])  # 1.414

# This would fail:
# {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
```

## Named Tuples

For tuples with many fields, `namedtuple` or `dataclass` give field names without sacrificing performance:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)    # 10 20
print(p[0])        # 10  — still indexable
print(p)           # Point(x=10, y=20)
```
