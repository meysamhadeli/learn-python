# itertools & functools

These modules are small toolboxes for iteration, caching, and function composition.

## `itertools` — Efficient Iteration

`itertools` gives you lazy iterator helpers.

### Common Helpers

```python
import itertools

list(itertools.chain([1, 2], [3, 4], [5]))   # [1, 2, 3, 4, 5]

nested = [[1, 2], [3, 4], [5]]
list(itertools.chain.from_iterable(nested))  # [1, 2, 3, 4, 5]

list(itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-"))
first_five = list(itertools.islice(range(1_000_000), 5))   # [0, 1, 2, 3, 4]

list(itertools.takewhile(lambda x: x < 5, range(10)))  # [0, 1, 2, 3, 4]
list(itertools.dropwhile(lambda x: x < 5, range(10)))  # [5, 6, 7, 8, 9]

list(itertools.product([1, 2], ["a", "b"]))

list(itertools.combinations([1, 2, 3], 2))
for batch in itertools.batched(range(10), 3):
    print(batch)
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
```

### `reduce` — Fold Over a Sequence

```python
from functools import reduce
import operator

# Sum — same as sum([1,2,3,4,5])
reduce(operator.add, [1, 2, 3, 4, 5])    # 15

reduce(operator.mul, [1, 2, 3, 4, 5])    # 120
```

Prefer built-in `sum()`, `max()`, `min()` where possible — `reduce` is for custom fold operations.
