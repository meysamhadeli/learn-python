# Comprehensions

Comprehensions are a compact way to build collections from other iterables. They are one of Python's most recognizable idioms, but they work best when they stay readable and focused on a single transformation.

The goal here is to understand why comprehensions feel natural in Python, and also where a normal loop is the better choice.

## What Are Comprehensions?

Comprehensions are concise expressions for building new collections by transforming and filtering existing iterables. They replace verbose `for` loops and are generally faster because they are optimized at the bytecode level.

## List Comprehensions

The general form is `[expression for item in iterable if condition]`. The `if` clause is optional.

```python
# Basic — square each number
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With filter — only even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]

# Equivalent for-loop (less idiomatic):
result = []
for x in range(10):
    result.append(x**2)
```

**Nested comprehensions** — process 2D data:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten
flat = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(3)]
```

## Dict Comprehensions

```python
# Map word → length
words = ["Python", "is", "great"]
lengths = {word: len(word) for word in words}
# {"Python": 6, "is": 2, "great": 5}

# Filter a dict
prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
expensive = {k: v for k, v in prices.items() if v > 0.8}
# {"apple": 1.0, "cherry": 2.0}
```

## Set Comprehensions

```python
# Unique squares — duplicates automatically removed
unique = {x**2 for x in [-2, -1, 0, 1, 2]}
# {0, 1, 4}

# All unique first letters
words = ["apple", "ant", "banana", "avocado"]
first_letters = {w[0] for w in words}  # {"a", "b"}
```

## Generator Expressions

A **generator expression** looks like a list comprehension but uses parentheses `()`. It does **not** build the collection in memory — it produces values lazily, one at a time. Use these when you only need to iterate once or when the collection would be very large.

```python
# List comprehension — builds all 1M items in memory immediately
big_list = [x**2 for x in range(1_000_000)]

# Generator expression — computes each value on demand
gen = (x**2 for x in range(1_000_000))  # barely any memory used

# Works with any function that accepts an iterable
total = sum(x**2 for x in range(1_000_000))
maximum = max(len(line) for line in open("file.txt"))
any_even = any(x % 2 == 0 for x in range(100))
```

When you pass a generator expression as the only argument to a function, you can omit the extra parentheses: `sum(x**2 for x in range(10))`.

## When to Use Comprehensions

Use comprehensions when the logic is simple and readable. If you need side effects (like printing), multiple conditions, or complex logic, a regular `for` loop is clearer:

```python
# Fine as a comprehension
doubles = [x * 2 for x in data if x > 0]

# Too complex — use a loop instead
result = []
for item in data:
    processed = transform(item)
    if validate(processed):
        log(processed)
        result.append(processed)
```
