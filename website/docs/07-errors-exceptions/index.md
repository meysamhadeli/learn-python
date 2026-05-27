# Errors & Exceptions

## The Exception Hierarchy

Python's exceptions are classes organized in a hierarchy. All exceptions inherit from `BaseException`. The ones you normally handle inherit from `Exception`:

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── TypeError
    ├── ValueError
    ├── NameError
    ├── AttributeError
    ├── IndexError
    ├── KeyError
    ├── FileNotFoundError
    ├── ZeroDivisionError
    ├── RuntimeError
    └── ...
```

## Basic `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")    # Error: division by zero
```

The `as e` clause binds the exception object — it has a `args` attribute and a string representation. Handle the **most specific** exception type you expect; catching `Exception` broadly can hide bugs.

## Multiple Except Clauses

```python
def parse_config(path: str) -> dict:
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON at line {e.lineno}: {e.msg}")
        return {}
    except PermissionError:
        print(f"Permission denied: {path}")
        raise   # re-raise — we can't recover from this
```

To catch multiple types in one clause, use a tuple:

```python
try:
    value = int(user_input)
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")
```

## `else` and `finally`

```python
try:
    result = compute(data)
except ValueError as e:
    print(f"Bad input: {e}")
else:
    # Runs only if NO exception was raised in the try block
    save_result(result)
finally:
    # ALWAYS runs — even if an exception was raised and not caught
    cleanup()
```

Use `finally` for cleanup that must happen regardless: closing connections, releasing locks, writing logs.

## Raising Exceptions

Use `raise` to signal an error condition:

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age must be 0-150, got {age}")
    return age

# Re-raise the current exception (preserve original traceback)
try:
    risky()
except ValueError:
    log_error()
    raise   # re-raises the same ValueError with original traceback
```

## Exception Chaining

When you raise an exception inside an `except` block, Python links them together with `__cause__` or `__context__`:

```python
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    raise ValueError("Could not parse response") from e
    # "The above exception was the direct cause of the following exception"
```

Use `raise ... from None` to suppress the chaining (hide the original exception from the traceback).

## Custom Exceptions

Define custom exception classes to provide richer error information and allow callers to catch specific errors from your library:

```python
class AppError(Exception):
    """Base class for all application errors."""

class InsufficientFundsError(AppError):
    def __init__(self, requested: float, available: float):
        self.requested = requested
        self.available = available
        super().__init__(
            f"Requested {requested:.2f} but only {available:.2f} available"
        )

class AccountLockedError(AppError):
    pass


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance
        self.locked = False

    def withdraw(self, amount: float) -> float:
        if self.locked:
            raise AccountLockedError("Account is locked")
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return amount


account = BankAccount(100.0)
try:
    account.withdraw(150.0)
except InsufficientFundsError as e:
    print(e)                      # Requested 150.00 but only 100.00 available
    print(f"Short by: {e.requested - e.available:.2f}")
except AppError as e:
    print(f"App error: {e}")      # catches any other AppError subclass
```

## Context Managers for Safe Cleanup

Many cleanup scenarios are better expressed with a `with` statement than with `try`/`finally`. See the [Context Managers](../08-pythonic-patterns/context-managers) page.

```python
# Instead of:
lock.acquire()
try:
    critical_section()
finally:
    lock.release()

# Do this:
with lock:
    critical_section()
```
