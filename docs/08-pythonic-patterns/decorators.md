# Decorators

## What is a Decorator?

A decorator is a function that takes another function as input and returns a new function that wraps the original — adding behavior before or after it runs without modifying the original source. The `@decorator` syntax is just syntactic sugar for `func = decorator(func)`.

## A Basic Decorator

```python
import functools

def log_calls(func):
    @functools.wraps(func)   # preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 4)
# Calling add((3, 4), {})
# add returned 7
```

Always use `@functools.wraps(func)` in the wrapper — without it, the wrapped function loses its name, docstring, and signature, which breaks introspection tools like `help()`.

## Decorator with Arguments

To add parameters, add another layer of nesting:

```python
def retry(times: int = 3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def fetch_data(url: str) -> str:
    # Might raise ConnectionError
    ...
```

## Stacking Decorators

Multiple decorators are applied bottom-up — the one closest to `def` is applied first:

```python
@log_calls
@retry(times=2)
def risky_operation():
    ...

# Equivalent to:
# risky_operation = log_calls(retry(times=2)(risky_operation))
```

## Class-Based Decorator

A class can be a decorator by implementing `__call__`:

```python
class Memoize:
    """Cache the return value of expensive function calls."""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.cache: dict = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(35))   # Fast — results are cached
```

Note: Python's standard library already provides `@functools.lru_cache` and `@functools.cache` for memoization.

## Practical Decorators from the Standard Library

```python
import functools

# Cache all calls indefinitely
@functools.cache
def expensive(n: int) -> int:
    return sum(range(n))

# Cache with a maximum size (LRU eviction)
@functools.lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

# Mark a method as a property (computed once, then cached)
class Circle:
    def __init__(self, r): self._r = r

    @functools.cached_property
    def area(self):
        import math
        return math.pi * self._r ** 2

c = Circle(5)
print(c.area)   # computed
print(c.area)   # returned from cache
```

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
