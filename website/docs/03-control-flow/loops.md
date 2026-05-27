# Loops

## `for` Loops

Python's `for` loop iterates over any **iterable** — lists, strings, ranges, dicts, files, generators, and anything that implements the iterator protocol:

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
for char in "Python":
    print(char)

# Iterate over a range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # start, stop (exclusive), step
    print(i)               # 2, 4, 6, 8
```

## `enumerate()` — Index + Value

When you need both the index and the value, use `enumerate()` instead of indexing manually:

```python
fruits = ["apple", "banana", "cherry"]

# Don't do this:
for i in range(len(fruits)):
    print(i, fruits[i])

# Do this:
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Start the counter at a different value
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

## `zip()` — Parallel Iteration

`zip()` pairs elements from multiple iterables and stops when the shortest is exhausted:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 80, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Unzip (transpose)
pairs = [(1, "a"), (2, "b"), (3, "c")]
numbers, letters = zip(*pairs)  # (1, 2, 3), ('a', 'b', 'c')
```

## `while` Loops

`while` repeats as long as its condition is truthy:

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Reading until a condition
total = 0
while True:
    value = int(input("Enter number (0 to stop): "))
    if value == 0:
        break
    total += value
print(f"Total: {total}")
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

# Loop else: useful for search patterns
def find_prime(numbers):
    for n in numbers:
        if n < 2:
            continue
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break       # n is not prime
        else:
            print(f"{n} is prime")  # only runs if inner loop didn't break
```

## Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 30, "city": "NY"}

for key in person:           # keys (default)
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

# Modify values (never add/remove keys during iteration)
person = {k: v * 2 if isinstance(v, int) else v for k, v in person.items()}
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
