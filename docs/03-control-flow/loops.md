# Loops

Python loops are mostly about iterating over values directly, not manually managing indexes.

## `for` Loops

`for` works with any iterable: lists, strings, ranges, dicts, files, and generators.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for char in "Python":
    print(char)

for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # start, stop (exclusive), step
    print(i)               # 2, 4, 6, 8
```

## `enumerate()` — Index + Value

Use `enumerate()` when you need both index and value:

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

## `zip()` — Parallel Iteration

`zip()` pairs elements from multiple iterables:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## `while` Loops

`while` repeats while a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## `break`, `continue`, and `else`

- `break` — immediately exits the innermost loop
- `continue` — skip the rest of the current iteration and go to the next
- `else` on a loop — executes if the loop completed **without** hitting a `break`

```python
for n in range(10):
    if n == 3:
        continue    # skip 3
    if n == 7:
        break       # stop at 7
    print(n)        # prints 0, 1, 2, 4, 5, 6
```

## Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:           # keys (default)
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")
```

## `reversed()` and `sorted()`

```python
items = [3, 1, 4, 1, 5, 9]

for x in reversed(items):   # iterate backward — no copy needed
    print(x)

for x in sorted(items):     # iterate in sorted order — returns new list
    print(x)

for x in sorted(items, reverse=True, key=abs):
    print(x)
```
