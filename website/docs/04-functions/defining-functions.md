# Defining Functions

## The `def` Statement

Functions are defined with `def`, followed by a name, parentheses for parameters, a colon, and an indented body. They are **first-class objects** — you can assign them to variables, pass them as arguments, and return them from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")    # "Hello, Alice!"
print(message)

# Assigning a function to a variable
say_hi = greet
print(say_hi("Bob"))        # "Hello, Bob!"
```

## Return Values

Every function returns a value. If there is no `return` statement (or `return` with no value), the function returns `None`:

```python
def add(a, b):
    return a + b

def log(message):
    print(message)          # no return → returns None implicitly

result = log("hello")
print(result)               # None
```

A function can return **multiple values** — Python packs them into a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns (min, max) tuple

low, high = min_max([3, 1, 4, 1, 5, 9])
print(low, high)    # 1 9

# Or capture as a tuple:
result = min_max([3, 1, 4])
print(type(result))  # <class 'tuple'>
```

## Docstrings

Document your function's purpose, parameters, and return value with a docstring — a string literal as the first statement in the body. Tools like `help()`, IDEs, and `pydoc` read these:

```python
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.

    Args:
        a: The dividend.
        b: The divisor. Must not be zero.

    Returns:
        The result of a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

help(divide)        # prints the docstring
print(divide.__doc__)  # access programmatically
```

## Functions as Objects

Since functions are first-class objects, they can be passed around like any other value:

```python
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply(double, 5))     # 10
print(apply(str, 42))       # "42"

# Store functions in a list
transformations = [str.upper, str.strip, str.title]
text = "  hello world  "
for fn in transformations:
    print(fn(text))
```

## Nested Functions

Functions can be defined inside other functions. Inner functions have access to the enclosing function's variables (closure):

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured from the enclosing scope
    return multiply

triple = make_multiplier(3)
print(triple(10))   # 30
print(triple(5))    # 15
```
