# Scoping Rules (LEGB)

Scoping rules explain where Python looks for names and why some assignments behave differently than beginners expect. This is one of the most important mental models in the language because it affects functions, closures, imports, and debugging.

If a name lookup or reassignment has ever felt surprising, LEGB is usually the reason.

## The LEGB Rule

When Python encounters a name (variable, function, class), it searches four scopes in order until it finds the name or raises a `NameError`:

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

By default, assignment inside a function creates a **new local variable** — it does not modify the global. To modify a global variable, you must declare it with `global`:

```python
counter = 0

def increment():
    global counter      # without this, we'd create a local 'counter'
    counter += 1

increment()
increment()
print(counter)  # 2
```

Use `global` sparingly. Shared mutable global state makes code harder to test and reason about. Prefer passing values as arguments and returning updated values.

## The `nonlocal` Keyword

`nonlocal` allows an inner function to modify a variable in an **enclosing** (but not global) scope. This is the key mechanism behind closures with state:

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

A **closure** is a function that "closes over" variables from its enclosing scope — those variables continue to exist even after the outer function returns:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' is captured in the closure
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Inspect captured variables
print(double.__closure__[0].cell_contents)  # 2
```

## A Common Closure Gotcha — Late Binding

Variables in closures are looked up at **call time**, not at definition time. This catches many developers off guard in loops:

```python
# BUG — all functions print 4
funcs = [lambda: i for i in range(5)]
for f in funcs:
    print(f())   # 4, 4, 4, 4, 4

# FIX — capture the current value of i with a default argument
funcs = [lambda i=i: i for i in range(5)]
for f in funcs:
    print(f())   # 0, 1, 2, 3, 4
```

## Variable Scope and the `UnboundLocalError`

If you assign to a name anywhere in a function, Python treats it as local **everywhere** in that function — even before the assignment:

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
