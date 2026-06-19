## Free-Threading (Python 3.13+)

Free-threading is one of the biggest recent changes in CPython, but it should be approached as an evolving runtime option, not as a blanket replacement for every concurrency strategy. The model is promising, but the ecosystem is still adapting.

This page is meant to help you understand what changes conceptually once the GIL is removed and what practical cautions still remain.

### The Experimental GIL-Free Build

Python 3.13 ships with an **experimental free-threaded build** that removes the GIL, allowing Python threads to execute genuinely in parallel on multiple CPU cores. This is the most significant change to CPython's threading model in its history.

The free-threaded build is opt-in: download `python3.13t` (the `t` suffix means free-threaded). The standard `python3.13` still has the GIL.

```bash
## Check if running in free-threaded mode
python3.13t -c "import sys; print(sys._is_gil_enabled())"   # False
python3.13  -c "import sys; print(sys._is_gil_enabled())"   # True
```

### CPU Parallelism with Threads

Without the GIL, CPU-bound threads genuinely run in parallel:

```python
import threading
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

## In standard CPython: ~4x slower than single thread (GIL overhead)
## In free-threaded 3.13t: ~4x faster than single thread (true parallelism)
start = time.perf_counter()
results = []
lock = threading.Lock()

def run(n):
    value = cpu_task(n)
    with lock:
        results.append(value)

threads = [threading.Thread(target=run, args=(10_000_000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"{time.perf_counter() - start:.2f}s")
```

### Thread Safety Implications

Removing the GIL does **not** make Python thread-safe. It means you must now be more careful about concurrent access to shared data structures, because the GIL previously provided implicit synchronization for many operations.

```python
## UNSAFE in free-threaded mode — concurrent list mutation
shared = []

def appender():
    for i in range(10_000):
        shared.append(i)   # not atomic without GIL

## SAFE — use a lock
lock = threading.Lock()

def safe_appender():
    for i in range(10_000):
        with lock:
            shared.append(i)
```

Python's built-in types (`dict`, `list`, `set`) are being made internally thread-safe for 3.13+, but complex compound operations (read-modify-write) still require explicit synchronization.

### Compatibility Status

- **Pure Python code** works as-is in free-threaded mode.
- **C extensions** must be explicitly marked as supporting free-threading (`Py_TPFLAGS_DEFAULT` → `Py_GIL_DISABLED`). Many popular packages (NumPy, Cython) are working on compatibility.
- Check https://py-free-threading.github.io/ for a compatibility matrix of popular packages.

### When to Use Free-Threading

Free-threading is experimental in 3.13 and will stabilize over the 3.14-3.15 cycle. For production workloads now, prefer `multiprocessing` for CPU parallelism. Follow free-threading for projects targeting future Python versions where it becomes stable.

> **Note**: Free-threading is experimental in 3.13. Extension modules must be updated to be thread-safe. Performance characteristics are still evolving.