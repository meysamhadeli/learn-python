# The GIL

The GIL matters mainly when choosing between threads, processes, and async code.

## What is the GIL?

The **Global Interpreter Lock (GIL)** in CPython allows only one thread to execute Python bytecode at a time.

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

# counter may not be 4_000_000
```

## The GIL is Released During I/O

CPython releases the GIL during I/O, so threads work well for network and file operations.

```python
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return len(r.read())

with ThreadPoolExecutor(max_workers=10) as pool:
    sizes = list(pool.map(fetch, ["https://python.org"] * 10))
```

## The GIL Does Not Help CPU-Bound Code

For CPU-heavy Python code, threads do not give true parallelism:

```python
def cpu_task():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(lambda _: cpu_task(), range(4)))
```

## Python 3.13 — Free-Threading (Experimental)

Python 3.13 introduced an experimental free-threaded build, but the normal CPython build still uses the GIL.

## C Extensions and the GIL

Some C extensions such as NumPy release the GIL during heavy work:

```python
import numpy as np
import threading

def matmul():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)   # GIL is released here

threads = [threading.Thread(target=matmul) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Summary

| Workload | Best Tool | Why |
|----------|-----------|-----|
| I/O-bound (network, files) | `asyncio` or `threading` | GIL released during I/O |
| CPU-bound (computation) | `multiprocessing` | Each process has own GIL |
| Mixed | `asyncio` + executor | Run blocking code in thread pool |
| NumPy/C extensions | `threading` | C code can release the GIL |
