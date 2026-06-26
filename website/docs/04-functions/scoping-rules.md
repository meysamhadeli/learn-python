# Scoping Rules (LEGB)

LEGB explains where Python looks up names.

## The LEGB Rule

Python searches in this order:

1. **L — Local** — names defined inside the current function
2. **E — Enclosing** — names in any enclosing functions (for nested functions)
3. **G — Global** — names defined at the module level
4. **B — Built-in** — names in Python's built-in namespace (`len`, `print`, `range`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # "local"   — L wins

    inner()
    print(x)        # "enclosing" — E wins

outer()
print(x)            # "global"  — G
```

## The `global` Keyword

Assignment inside a function creates a local variable unless you declare `global`:

```python
counter = 0

def increment():
    global counter      # without this, we'd create a local 'counter'
    counter += 1

increment()
increment()
print(counter)  # 2
```

## The `nonlocal` Keyword

`nonlocal` lets an inner function modify a variable from an enclosing function:

```python
def make_counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count      # modify the enclosing 'count'
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset

inc, reset = make_counter(10)
print(inc())    # 11
print(inc())    # 12
print(inc(5))   # 17
reset()
print(inc())    # 11
```

## Closures

A closure keeps access to variables from an outer function even after that function returns:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured in the closure
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

## A Common Closure Gotcha — Late Binding

Closures in loops use late binding unless you capture values explicitly:

```python
funcs = [lambda: i for i in range(5)]
for f in funcs:
    print(f())   # 4, 4, 4, 4, 4

funcs = [lambda i=i: i for i in range(5)]
for f in funcs:
    print(f())   # 0, 1, 2, 3, 4
```

## Variable Scope and the `UnboundLocalError`

If a function assigns to a name, Python treats that name as local throughout the function:

```python
x = 10

def bad():
    print(x)    # UnboundLocalError — x is treated as local because of the line below
    x = 20

# Fix: declare global, or avoid the re-assignment
def good():
    global x
    print(x)    # 10
    x = 20
```
