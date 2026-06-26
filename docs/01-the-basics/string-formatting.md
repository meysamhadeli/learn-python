# String Formatting

## f-Strings (Recommended)

Use f-strings for most new code.

```python
name = "Alice"
age = 30

print(f"My name is {name} and I am {age} years old.")
# My name is Alice and I am 30 years old.

# Any expression works inside {}
print(f"In 5 years: {age + 5}")
print(f"Uppercase: {name.upper()}")
print(f"Length: {len(name)}")
print(f"{'even' if age % 2 == 0 else 'odd'}")
```

```python
product = "Keyboard"
price = 49.99

print(f"{product} costs ${price}")
```

## Format Specification Mini-Language

After `:` inside `{}`, specify formatting:

```python
pi = 3.14159265

print(f"{pi:.2f}")      # 3.14
print(f"{pi:.4f}")      # 3.1416

print(f"{42:10d}")      # '        42'  (right-aligned, width 10)
print(f"{42:<10d}")     # '42        '  (left-aligned)
print(f"{42:^10d}")     # '    42    '  (centered)
print(f"{42:010d}")     # '0000000042' (zero-padded)

print(f"{1000000:,}")   # 1,000,000

ratio = 0.756
print(f"{ratio:.1%}")   # 75.6%
```

## Debugging with `=`

Python 3.8+ added `=` for quick debugging:

```python
x = 42
y = [1, 2, 3]
print(f"{x=}")          # x=42
print(f"{y=}")          # y=[1, 2, 3]
print(f"{x * 2 + 1=}")  # x * 2 + 1=85
```

## Other Formatting Approaches

You will still see older styles in existing code:

```python
print("Hello, {}!".format("World"))
print("{name} is {age}".format(name="Alice", age=30))

print("Hello, %s! You are %d years old." % ("Alice", 30))
```

For `logging`, `%` formatting is still common:

```python
import logging
logging.debug("User %s logged in from %s", username, ip_address)
```

Practical rule: use f-strings in everyday code, recognize `.format()` and `%` in older code.
