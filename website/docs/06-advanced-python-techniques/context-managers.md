# Context Managers

Context managers give Python a clean, explicit way to manage setup and cleanup. They are one of the clearest examples of Python turning a common error-prone pattern into readable syntax.

Whenever code needs paired actions like open and close, acquire and release, or start and cleanup, this page explains the preferred model.

## What is a Context Manager?

A context manager is the object behind Python's `with` statement.

Use `with` when code has a clear setup step and a matching cleanup step. Open a file, use it, then close it. Acquire a lock, use it, then release it. Start a timer, run code, then stop it.

Read `with` like this:

- enter setup
- run the block
- always clean up at the end

That is why `with` is often easier to read than `try/finally`.

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Hello!")
```

How to read that line:

- `open("data.txt", "w", encoding="utf-8")` creates the resource
- `as f` stores that resource in `f`
- when the block ends, Python closes the file automatically

This is roughly equivalent to:

```python
file = open("data.txt", "w", encoding="utf-8")
try:
    file.write("Hello!")
finally:
    file.close()
```

Under the hood, a context manager defines `__enter__` and `__exit__`. Python calls `__enter__` at the start of the block and `__exit__` at the end, even if an exception happens.

## Implementing with a Class

```python
class ManagedFile:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with ManagedFile("notes.txt", "w") as f:
    f.write("Hello from a custom context manager")
```

This custom class behaves like `open(...)`: `__enter__` prepares the resource and returns it, and `__exit__` cleans it up.

The `__exit__` method receives `(exc_type, exc_val, exc_tb)`. If no exception happened, all three are `None`. Return `True` to suppress an exception. Return `False` or `None` to let it propagate.

## Implementing with `@contextmanager`

`contextlib.contextmanager` lets you write a context manager as a generator — usually much shorter than a class:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str = ""):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label or 'Elapsed'}: {elapsed:.4f}s")

with timer("Sum"):
    total = sum(range(1_000_000))
# Sum: 0.0234s
```

Everything before `yield` acts like `__enter__`. Everything after `yield` acts like `__exit__`. Use `try/finally` so cleanup still happens if the block raises an exception.

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
