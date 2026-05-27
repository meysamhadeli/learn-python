# If / Else

Conditional logic is how a program starts making decisions. The important skill is not just writing conditions, but reading them clearly and predicting which branch will run for a given input.

This page connects directly to truthiness from Chapter I, because Python conditions often depend on values that are not literally `True` or `False`.

## Basic Conditional

Python uses indentation to delimit blocks — there are no curly braces. The `elif` keyword replaces `else if`:

```python
age = 20

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

Python evaluates each condition in order and executes the first matching block. The `else` block is optional. You can have as many `elif` branches as you need.

## Truthy and Falsy Conditions

Any expression can be used as a condition — Python will evaluate its truthiness:

```python
name = input("Enter name: ")

if name:                     # equivalent to: if name != ""
    print(f"Hello, {name}!")
else:
    print("No name entered")

items = []
if not items:                # equivalent to: if len(items) == 0
    print("List is empty")
```

## Conditional Expression (Ternary)

Python has a one-line conditional expression: `value_if_true if condition else value_if_false`.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"

# Useful in assignments and function arguments
label = "yes" if is_active else "no"
print("on" if enabled else "off")
```

Keep ternary expressions short and readable. If the condition or the values are complex, use a regular `if`/`else` block.

## Nested Conditions

```python
x = 15

if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Non-positive")
```

Flatten nested conditions with `and` when possible:

```python
if x > 0 and x % 2 == 0:
    print("Positive even")
```

## Multiple Conditions

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
```

For large numbers of discrete values, `match`/`case` (Python 3.10+) or a dictionary lookup is often cleaner:

```python
grade_map = {range(90, 101): "A", range(80, 90): "B", range(70, 80): "C"}
grade = next((g for r, g in grade_map.items() if score in r), "F")
```
