# Iterators & Generators

Iterators and generators explain how Python processes data lazily instead of building everything in memory first.

## The Iterator Protocol

An iterable can be looped over. An iterator produces one item at a time.

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it)        # StopIteration
```

## Implementing a Custom Iterator

```python
class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self   # the iterator IS the object

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n)    # 3, 2, 1, 0
```

## Generator Functions

Generator functions use `yield` and are usually easier than writing iterator classes:

```python
def countdown(start: int):
    while start >= 0:
        yield start
        start -= 1

for n in countdown(3):
    print(n)    # 3, 2, 1, 0
```

## Generators are Lazy

Generators produce values on demand, which is useful for large or infinite sequences:

```python
def fibonacci():
    a, b = 0, 1
    while True:            # infinite sequence!
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(8):
    print(next(fib), end=" ")   # 0 1 1 2 3 5 8 13
```

## Generator Expressions

A generator expression is the lazy version of a list comprehension:

```python
numbers = range(1_000_000)

squares_list = [x**2 for x in numbers]

squares_gen = (x**2 for x in numbers)

total = sum(x**2 for x in range(1_000))
```

## `yield from`

`yield from` delegates to another iterable:

```python
def chain(*iterables):
    for it in iterables:
        yield from it

list(chain([1, 2], "abc", range(3)))
# [1, 2, 'a', 'b', 'c', 0, 1, 2]
```

In practice, generators matter most for streaming data, reading files, paging API results, and memory-efficient pipelines.
