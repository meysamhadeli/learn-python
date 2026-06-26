# Chapter VIII: Errors & Exceptions

This chapter is about writing Python that fails clearly and handles expected problems without hiding bugs.

For a 1-2 hour ramp-up, focus on these ideas:

- bugs you should fix
- runtime problems your code should handle deliberately
- catch specific exceptions, not everything
- use `raise` when invalid input or state should stop execution

You do not need the full exception hierarchy memorized. You need a clean mental model for `try`, `except`, `else`, `finally`, and custom exceptions.

## Priority

- Must read now: Basic `try` / `except`, Raising Exceptions
- Read next: `else` and `finally`, Custom Exceptions
- Optional for now: Exception Chaining

## Basic `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError as exc:
    print(f"Error: {exc}")
```

Handle the most specific exception type you expect. Catching `Exception` too early can hide real bugs.

## `else` and `finally`

```python
try:
    result = compute(data)
except ValueError as exc:
    print(f"Bad input: {exc}")
else:
    save_result(result)
finally:
    cleanup()
```

## Raising Exceptions

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError("age must be int")
    if age < 0:
        raise ValueError("age must be non-negative")
```

## Custom Exceptions

```python
class AppError(Exception):
    pass


class AccountLockedError(AppError):
    pass
```

Create custom exceptions when your app or library has domain-specific failure cases that callers may want to handle explicitly.

## Related Topic

Many cleanup scenarios are better expressed with a `with` statement than with `try`/`finally`. See the [Context Managers](../06-advanced-python-techniques/context-managers) page when you continue into advanced topics.
