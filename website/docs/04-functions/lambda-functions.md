# Lambda Functions

## What is a Lambda?

A **lambda** is an anonymous, single-expression function. It is written `lambda parameters: expression` and can be defined inline wherever a function object is expected. The expression is evaluated and returned automatically — no `return` keyword.

```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7
```

Lambdas are syntactically limited to a **single expression** — no assignments, no `if`/`else` blocks (though the ternary conditional works), no loops.

## When to Use Lambdas

Lambdas shine as short **callback functions** passed to higher-order functions. The most common use case is a `key` argument for sorting:

```python
# Sort by string length
words = ["banana", "apple", "cherry", "date"]
words.sort(key=lambda w: len(w))
print(words)   # ['date', 'apple', 'banana', 'cherry']

# Sort by the second element of each tuple
pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)   # [(2, 1), (4, 2), (1, 3)]

# Sort by multiple fields (last name, then first name)
people = [("Alice", "Smith"), ("Bob", "Jones"), ("Carol", "Smith")]
people.sort(key=lambda p: (p[1], p[0]))
```

## Lambdas with `map()` and `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10, 12]

evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

In modern Python, **list comprehensions are usually preferred** over `map`/`filter` with lambdas:

```python
doubled = [x * 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

## Lambdas vs Named Functions

Use a named function when:
- You need more than one expression
- The function will be reused
- Readability matters more than brevity

```python
# Lambda — fine for one-off sort key
items.sort(key=lambda x: x.priority)

# Named function — better when the logic is complex or reused
def sort_key(item):
    return (item.priority, item.created_at, item.name)

items.sort(key=sort_key)
```

PEP 8 advises **against** assigning a lambda to a variable (use `def` instead), because `def` gives the function a proper name, which makes stack traces and `repr()` outputs clearer:

```python
# Discouraged by PEP 8:
square = lambda x: x ** 2

# Preferred:
def square(x):
    return x ** 2
```
