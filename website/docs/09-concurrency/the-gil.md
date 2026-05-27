# The GIL

The GIL is one of the most discussed parts of Python concurrency, but it is often explained too vaguely. The important question is not simply whether the GIL exists, but what kinds of workloads it limits and what kinds it does not.

Read this page as a decision aid: it helps explain why threads behave differently for CPU-bound work and I/O-bound work in CPython.

## What is the GIL?

The **Global Interpreter Lock (GIL)** is a mutex in CPython — the standard Python interpreter — that allows only one thread to execute Python bytecode at a time. It exists to protect CPython's internal data structures (reference counts, memory allocator) from concurrent modification, which would otherwise cause crashes and memory corruption.

The GIL is a **CPython implementation detail**, not a language requirement. Other implementations — Jython (JVM), IronPython (.NET), PyPy-STM — do not have a GIL.

## What the GIL Prevents

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1   # read-modify-write, but GIL makes each bytecode step atomic

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# counter may not be 4_000_000 — the GIL does NOT make compound operations atomic!
# counter += 1 is three bytecodes: LOAD, ADD, STORE — threads can interleave between them
```

## The GIL is Released During I/O

CPython releases the GIL whenever a thread performs I/O — network reads, file reads, `time.sleep()`. This is why threading works well for I/O-bound tasks: while one thread waits for a network response, other threads can execute Python code.

```python
# Threads work well here — GIL is released during urlopen
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return len(r.read())

with ThreadPoolExecutor(max_workers=10) as pool:
    sizes = list(pool.map(fetch, ["https://python.org"] * 10))
```

## The GIL Does Not Help CPU-Bound Code

For CPU-intensive work, threads do not run in parallel — only one thread runs at a time even on multi-core systems:

```python
# This is NOT parallelized — 4 threads, but still uses 1 core
def cpu_task():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

# Use multiprocessing instead — each process has its own GIL
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(lambda _: cpu_task(), range(4)))
```

## Python 3.13 — Free-Threading (Experimental)

Python 3.13 introduced an experimental **free-threaded build** (`python3.13t`) with the GIL disabled. See the [Free-Threading](./free-threading) page for details. This is opt-in for now; the standard CPython 3.13 still has the GIL.

## C Extensions and the GIL

Many C extensions — notably NumPy — release the GIL during heavy computation, allowing genuine parallelism with Python threads:

```python
import numpy as np
import threading

# NumPy releases the GIL during C-level operations
def matmul():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)   # GIL is released here

threads = [threading.Thread(target=matmul) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
# These DO run in parallel — NumPy bypasses the GIL
```

## Summary

| Workload | Best Tool | Why |
|----------|-----------|-----|
| I/O-bound (network, files) | `asyncio` or `threading` | GIL released during I/O |
| CPU-bound (computation) | `multiprocessing` | Each process has own GIL |
| Mixed | `asyncio` + executor | Run blocking code in thread pool |
| NumPy/C extensions | `threading` | C code can release the GIL |
