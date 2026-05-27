# itertools & functools

## `itertools` — Efficient Iteration

`itertools` provides composable, lazy iterators for common looping patterns. All functions return iterators — they produce values on demand without creating intermediate lists.

### Combining Iterables

```python
import itertools

# chain — concatenate multiple iterables
list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]

# chain.from_iterable — flatten one level of nesting
nested = [[1, 2], [3, 4], [5]]
list(itertools.chain.from_iterable(nested))  # [1, 2, 3, 4, 5]

# zip_longest — zip but pad shorter iterables
list(itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))
# [(1, 'a'), (2, 'b'), (3, '-')]
```

### Slicing and Filtering

```python
# islice — lazy slice of any iterable (no index required)
first_five = list(itertools.islice(range(1_000_000), 5))   # [0, 1, 2, 3, 4]

# takewhile / dropwhile
list(itertools.takewhile(lambda x: x < 5, range(10)))  # [0, 1, 2, 3, 4]
list(itertools.dropwhile(lambda x: x < 5, range(10)))  # [5, 6, 7, 8, 9]

# filterfalse — opposite of filter()
list(itertools.filterfalse(str.isdigit, "a1b2c3"))  # ['a', 'b', 'c']
```

### Combinatorics

```python
# product — Cartesian product
list(itertools.product([1, 2], ["a", "b"]))
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

# combinations — unique pairs without repetition
list(itertools.combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# permutations — ordered arrangements
list(itertools.permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# combinations_with_replacement
list(itertools.combinations_with_replacement("AB", 2))
# [('A','A'), ('A','B'), ('B','B')]
```

### Grouping

```python
# groupby — groups consecutive items with the same key (sort first!)
data = [("Alice", "Eng"), ("Bob", "Eng"), ("Carol", "HR"), ("Dave", "HR")]
data.sort(key=lambda x: x[1])

for dept, members in itertools.groupby(data, key=lambda x: x[1]):
    print(dept, [m[0] for m in members])
# Eng ['Alice', 'Bob']
# HR  ['Carol', 'Dave']
```

### Batching (Python 3.12+)

```python
# batched — split iterable into fixed-size chunks
for batch in itertools.batched(range(10), 3):
    print(batch)   # (0,1,2) then (3,4,5) then (6,7,8) then (9,)
```

## `functools` — Higher-Order Functions

### Caching

```python
import functools

@functools.cache                  # unlimited cache — Python 3.9+
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

@functools.lru_cache(maxsize=128) # bounded LRU cache
def expensive(x: int) -> int:
    return sum(range(x))

# cached_property — computed once per instance, then stored
class Circle:
    def __init__(self, r): self.r = r

    @functools.cached_property
    def area(self):
        import math
        return math.pi * self.r ** 2
```

### `partial` — Partial Application

```python
from functools import partial

def power(base: float, exponent: float) -> float:
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)

print(square(5))    # 25.0
print(cube(3))      # 27.0

# Useful with map/sorted
from functools import partial
import operator

multiply_by_3 = partial(operator.mul, 3)
list(map(multiply_by_3, [1, 2, 3, 4]))   # [3, 6, 9, 12]
```

### `reduce` — Fold Over a Sequence

```python
from functools import reduce
import operator

# Sum — same as sum([1,2,3,4,5])
reduce(operator.add, [1, 2, 3, 4, 5])    # 15

# Product of list
reduce(operator.mul, [1, 2, 3, 4, 5])    # 120

# Max — same as max([3,1,4,1,5,9])
reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5, 9])  # 9
```

Prefer built-in `sum()`, `max()`, `min()` where possible — `reduce` is for custom fold operations.

### `total_ordering`

See the [Magic Methods](../06-oop/magic-methods) page — `@total_ordering` generates comparison methods from `__eq__` and `__lt__`.
```

```python
import functools

# lru_cache — memoize function results
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# cache (Python 3.9+) — unbounded lru_cache
@functools.cache
def expensive(x):
    return x ** 2

# reduce — fold a sequence into a single value
from functools import reduce
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])  # 120

# partial — pre-fill arguments
from functools import partial
power_of_two = partial(pow, 2)
print(power_of_two(10))  # 1024
```
