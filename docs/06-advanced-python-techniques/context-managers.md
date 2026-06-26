# Context Managers

Context managers give Python a clean, explicit way to manage setup and cleanup. They are one of the clearest examples of Python turning a common error-prone pattern into readable syntax.

Whenever code needs paired actions like open and close, acquire and release, or start and cleanup, this page explains the preferred model.

## What is a Context Manager?

A context manager is an object that defines `__enter__` and `__exit__` methods. The `with` statement calls `__enter__` on entry and guarantees that `__exit__` is called on exit — even if an exception occurs. This makes resource management safe and explicit.

```python
# Classic example: file handling
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello!")
# File is closed here — guaranteed, even if write() raised
```

## Implementing with a Class

```python
class DatabaseConnection:
    def __init__(self, url: str):
        self.url = url
        self.conn = None

    def __enter__(self):
        print(f"Connecting to {self.url}")
        self.conn = self._connect(self.url)
        return self.conn    # bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        if self.conn:
            self.conn.close()
        # Return True to suppress the exception; False (or None) to propagate it
        return False

with DatabaseConnection("postgresql://localhost/mydb") as conn:
    conn.execute("SELECT 1")
```

The `__exit__` method receives `(exc_type, exc_val, exc_tb)` — all `None` if no exception occurred. Return `True` to suppress the exception; return `False` or `None` to let it propagate.

## Implementing with `@contextmanager`

`contextlib.contextmanager` lets you write a context manager as a generator — usually much shorter than a class:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str = ""):
    start = time.perf_counter()
    try:
        yield   # code inside the 'with' block runs here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label or 'Elapsed'}: {elapsed:.4f}s")

with timer("Sum"):
    total = sum(range(1_000_000))
# Sum: 0.0234s
```

Everything before `yield` is `__enter__`; everything in `finally` after `yield` is `__exit__`. Use `try/finally` to guarantee cleanup even when the `with` block raises.

## Yielding a Value

The `yield` expression can return a value that is bound to the `as` variable:

```python
from contextlib import contextmanager

@contextmanager
def temp_file(name: str):
    from pathlib import Path
    p = Path(name)
    try:
        yield p         # bound to the 'as' variable
    finally:
        p.unlink(missing_ok=True)   # always delete on exit

with temp_file("scratch.txt") as path:
    path.write_text("temporary data")
    # file is deleted after this block
```

## Useful Context Managers from the Standard Library

```python
import contextlib

# Suppress specific exceptions
with contextlib.suppress(FileNotFoundError):
    Path("nonexistent.txt").unlink()   # no exception raised

# Redirect stdout to a string
import io
with contextlib.redirect_stdout(io.StringIO()) as buf:
    print("captured")
print(buf.getvalue())   # "captured\n"

# Manage multiple context managers at once
with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ["a.txt", "b.txt"]]
    # all files closed on exit
```

## Threading Lock Example

A common use of `with` for safe concurrent access:

```python
import threading

lock = threading.Lock()

shared_data = []

def append_safely(value):
    with lock:           # __enter__ acquires, __exit__ releases
        shared_data.append(value)
```
