# String Formatting

## f-Strings (Recommended)

Introduced in Python 3.6, **f-strings** (formatted string literals) are the recommended way to embed expressions inside strings. Prefix the string with `f` or `F` and place any valid Python expression inside `{}`:

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

## Format Specification Mini-Language

After a colon inside `{}` you can specify how the value should be formatted:

```python
pi = 3.14159265

# Decimal places
print(f"{pi:.2f}")      # 3.14
print(f"{pi:.4f}")      # 3.1416

# Width and padding
print(f"{42:10d}")      # '        42'  (right-aligned, width 10)
print(f"{42:<10d}")     # '42        '  (left-aligned)
print(f"{42:^10d}")     # '    42    '  (centered)
print(f"{42:010d}")     # '0000000042' (zero-padded)

# Thousands separator
print(f"{1000000:,}")   # 1,000,000

# Percentage
ratio = 0.756
print(f"{ratio:.1%}")   # 75.6%

# Scientific notation
print(f"{0.000123:.2e}")  # 1.23e-04
```

## Debugging with `=`

Python 3.8+ added a handy `=` specifier that prints the expression and its value — great for quick debugging:

```python
x = 42
y = [1, 2, 3]
print(f"{x=}")          # x=42
print(f"{y=}")          # y=[1, 2, 3]
print(f"{x * 2 + 1=}")  # x * 2 + 1=85
```

## Other Formatting Approaches

While f-strings are preferred for new code, you may encounter older styles in existing codebases:

```python
# str.format() — Python 2.6+
print("Hello, {}!".format("World"))
print("{name} is {age}".format(name="Alice", age=30))

# % formatting — oldest style, still common in logging
print("Hello, %s! You are %d years old." % ("Alice", 30))
```

For **logging**, the `%`-style is intentionally used because `logging` can skip the formatting entirely when the log level is disabled:

```python
import logging
logging.debug("User %s logged in from %s", username, ip_address)
# String is only formatted if DEBUG level is active
```
