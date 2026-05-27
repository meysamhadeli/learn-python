# Operators

## Arithmetic Operators

Python's arithmetic operators work as expected, with a few worth noting: `/` always produces a float (true division), `//` performs floor division (rounds toward negative infinity), and `**` is the power operator.

```python
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   — always float
print(7 // 2)   # 3     — floor division
print(7 % 2)    # 1     — modulo (remainder)
print(7 ** 2)   # 49    — exponentiation
```

Floor division rounds toward **negative infinity**, not zero:

```python
print(-7 // 2)   # -4  (not -3)
print(7 // -2)   # -4
```

That "rounds toward negative infinity" detail is easy to miss. If you expected truncation toward zero, negative examples can look surprising at first.

## Comparison & Logical Operators

Comparison operators return `True` or `False`. Python supports **chained comparisons**, which read naturally and are more efficient than separate `and` comparisons:

```python
x = 7
print(x > 5)          # True
print(x != 10)        # True
print(0 < x < 10)     # True  — equivalent to (0 < x) and (x < 10)
print(1 < 2 < 3 < 4)  # True  — any number of chained comparisons
```

Logical operators use English words, not symbols:

```python
print(x > 5 and x < 10)   # True
print(x > 10 or x < 5)    # False
print(not x == 7)          # False
```

**Short-circuit evaluation:** `and` stops at the first falsy value; `or` stops at the first truthy value. They return the actual value that determined the outcome (not just `True`/`False`):

```python
name = ""
result = name or "Anonymous"   # "Anonymous" — name is falsy
items = [1, 2, 3]
first = items and items[0]     # 1 — items is truthy, so evaluates items[0]
```

This "return the actual value" behavior is why expressions like `user_name or "Anonymous"` are so common in Python. The operators are not limited to plain booleans; they also help choose between real values.

## Assignment Operators

Augmented assignment operators update a variable in place. Under the hood, `x += 5` calls `x.__iadd__(5)` if available (which modifies the object in-place for mutable types like lists) or falls back to `x = x + 5`:

```python
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0  (always float)
x //= 2   # x = 3.0
x **= 3   # x = 27.0
x %= 5    # x = 2.0
```

For immutable types like integers and strings, this usually means rebinding the name to a new value. For mutable types like lists, the operation may update the existing object in place.

```python
numbers = [1, 2]
alias = numbers

numbers += [3]
print(alias)  # [1, 2, 3]
```

That behavior connects directly to the reference model explained in the Variables page.

## Identity and Membership Operators

`is` tests whether two variables refer to the **same object** in memory (not just equal values). `in` tests for membership in a sequence, set, or dict:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # True  — equal values
print(a is b)    # False — different objects

# 'is' is appropriate for singletons:
result = None
print(result is None)     # True  (correct)
print(result is not None) # False

# Membership — O(1) for sets and dict keys, O(n) for lists
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)    # True
print("grape" not in fruits) # True
```

Use `==` when you care about value equality, and `is` when you care about object identity. Beginners often write `x is 5` or `name is "Alice"`, but value comparisons should normally use `==`.

## Walrus Operator `:=` (Python 3.8+)

The walrus operator assigns a value **and** returns it as an expression. This is useful for avoiding redundant calls or extra temporary variables:

```python
data = [1, 2, 3, 4, 5]

# Without walrus: len() called twice or needs a temp variable
if len(data) > 3:
    print(f"List has {len(data)} items")

# With walrus: computed once, used twice
if (n := len(data)) > 3:
    print(f"List has {n} items")
```

It is especially useful in `while` loops that read until a sentinel value:

```python
import sys

while line := sys.stdin.readline():
    process(line)

# Reading file in chunks without while True + break:
with open("large_file.bin", "rb") as f:
    while chunk := f.read(8192):
        process(chunk)
```

And in comprehensions where you want to compute a value once and filter by it:

```python
results = [y for x in range(20) if (y := x ** 2) > 50]
```

Use this operator with restraint. It is most helpful when it removes repeated work and keeps the code easier to read. If it makes the condition harder to understand, a normal assignment is better.

## Bitwise Operators

Python integers support bitwise operations, which operate on the binary representation:

```python
a = 0b1100   # 12
b = 0b1010   # 10

print(a & b)   # 0b1000 = 8   (AND)
print(a | b)   # 0b1110 = 14  (OR)
print(a ^ b)   # 0b0110 = 6   (XOR)
print(~a)      # -13           (NOT — inverts all bits, two's complement)
print(a << 2)  # 48            (left shift by 2)
print(a >> 1)  # 6             (right shift by 1)
```

These operators are less common in beginner application code, but they appear in low-level programming, flags, permissions, binary protocols, and performance-sensitive logic.
