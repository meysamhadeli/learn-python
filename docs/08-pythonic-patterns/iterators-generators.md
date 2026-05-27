# Iterators & Generators

## The Iterator Protocol

An **iterable** is any object you can loop over — lists, tuples, strings, files, ranges. An **iterator** is an object with a `__next__()` method that returns the next value and raises `StopIteration` when exhausted.

`iter()` converts an iterable into an iterator; `next()` retrieves the next value:

```python
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# next(it)        # StopIteration

# A for loop is just:
# it = iter(lst)
# while True:
#     try: value = next(it)
#     except StopIteration: break
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

Writing the full iterator class above is verbose. A **generator function** using `yield` does the same in far fewer lines:

```python
def countdown(start: int):
    while start >= 0:
        yield start   # suspends here, returns value; resumes on next()
        start -= 1

for n in countdown(3):
    print(n)    # 3, 2, 1, 0
```

When Python sees `yield` in a function, calling that function returns a **generator object** — it does not execute the body immediately. The body runs step-by-step as `next()` is called on the generator.

## Generators are Lazy

Generators produce values on demand. They do not compute the whole sequence upfront, making them ideal for large or infinite sequences:

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

A generator expression is the lazy equivalent of a list comprehension. Use `()` instead of `[]`:

```python
numbers = range(1_000_000)

# List comprehension — creates full list in memory immediately
squares_list = [x**2 for x in numbers]

# Generator expression — lazy, one value at a time
squares_gen = (x**2 for x in numbers)

# Useful in function calls — no double parentheses needed in sum()
total = sum(x**2 for x in range(1_000))
```

## `yield from`

`yield from` delegates to another iterable or generator — flattening or chaining:

```python
def chain(*iterables):
    for it in iterables:
        yield from it    # same as: for item in it: yield item

list(chain([1, 2], "abc", range(3)))
# [1, 2, 'a', 'b', 'c', 0, 1, 2]

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recursive
        else:
            yield item

list(flatten([1, [2, [3, 4]], 5]))
# [1, 2, 3, 4, 5]
```

## `send()` — Coroutines

Generators can receive values via `send()`. This enables cooperative coroutines (though `async`/`await` is now preferred for that):

```python
def running_average():
    total = 0.0
    count = 0
    while True:
        value = yield (total / count if count else None)
        total += value
        count += 1

avg = running_average()
next(avg)               # prime the generator (advance to first yield)
avg.send(10)            # total=10, count=1
avg.send(20)            # total=30, count=2
print(avg.send(30))     # 20.0  — (10+20+30)/3
```
