# Comprehensions

Comprehensions are a compact way to build collections from other iterables.

They work best when the transformation stays simple and readable.

## List Comprehensions

General form: `[expression for item in iterable if condition]`

```python
squares = [x**2 for x in range(10)]

evens = [x for x in range(20) if x % 2 == 0]

words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
```

Nested comprehensions are possible, but use them carefully:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [n for row in matrix for n in row]
```

## Dict Comprehensions

```python
words = ["Python", "is", "great"]
lengths = {word: len(word) for word in words}

prices = {"apple": 1.0, "banana": 0.5, "cherry": 2.0}
expensive = {k: v for k, v in prices.items() if v > 0.8}
```

## Set Comprehensions

```python
unique = {x**2 for x in [-2, -1, 0, 1, 2]}
words = ["apple", "ant", "banana", "avocado"]
first_letters = {w[0] for w in words}  # {"a", "b"}
```

## Generator Expressions

A generator expression uses `()` and produces values lazily:

```python
big_list = [x**2 for x in range(1_000_000)]

gen = (x**2 for x in range(1_000_000))  # barely any memory used

total = sum(x**2 for x in range(1_000_000))
```

## When to Use Comprehensions

Use comprehensions for simple transforms and filters. Use a normal loop when logic becomes hard to read.

```python
doubles = [x * 2 for x in data if x > 0]

result = []
for item in data:
    processed = transform(item)
    if validate(processed):
        log(processed)
        result.append(processed)
```
