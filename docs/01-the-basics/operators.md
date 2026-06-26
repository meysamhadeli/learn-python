# Operators

## Arithmetic Operators

Python arithmetic mostly works as expected. The main rules to remember are `/`, `//`, `%`, and `**`.

```python
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   — always float
print(7 // 2)   # 3     — floor division
print(7 % 2)    # 1     — modulo (remainder)
print(7 ** 2)   # 49    — exponentiation
```

`//` rounds toward negative infinity:

```python
print(-7 // 2)   # -4  (not -3)
print(7 // -2)   # -4
```

## Comparison & Logical Operators

Comparisons return booleans. Python also supports chained comparisons:

```python
x = 7
print(x > 5)          # True
print(x != 10)        # True
print(0 < x < 10)     # True  — equivalent to (0 < x) and (x < 10)
print(1 < 2 < 3 < 4)  # True  — any number of chained comparisons
```

Logical operators use words, not symbols:

```python
print(x > 5 and x < 10)   # True
print(x > 10 or x < 5)    # False
print(not x == 7)          # False
```

`and` and `or` short-circuit and return actual values:

```python
name = ""
result = name or "Anonymous"   # "Anonymous" — name is falsy
items = [1, 2, 3]
first = items and items[0]     # 1 — items is truthy, so evaluates items[0]
```

## Assignment Operators

Augmented assignment is common:

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

Lists often update in place:

```python
numbers = [1, 2]
alias = numbers

numbers += [3]
print(alias)  # [1, 2, 3]
```

## Identity and Membership Operators

`is` checks identity. `in` checks membership.

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

Use `==` for values and `is` for singletons like `None`.

## Walrus Operator `:=` (Python 3.8+)

The walrus operator assigns and returns a value in one expression:

```python
data = [1, 2, 3, 4, 5]

if (n := len(data)) > 3:
    print(f"List has {n} items")
```

Useful in `while` loops:

```python
import sys

while line := sys.stdin.readline():
    process(line)
```
Use it when it improves clarity, not just to be clever.

## Bitwise Operators

Bitwise operators matter in lower-level or protocol-heavy code:

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
