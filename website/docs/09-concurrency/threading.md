# Threading

Threads are useful when a program spends much of its time waiting on external work such as network I/O, file I/O, or blocking library calls. They are less useful when pure Python code is trying to saturate CPU cores.

This page should be read together with the GIL page, because thread behavior makes the most sense once that runtime constraint is clear.

## When to Use Threads

Python threads are best for **I/O-bound** work — network requests, database queries, file reads — where the program spends most of its time waiting. Because of the GIL, threads do **not** parallelize CPU-bound computation; use `multiprocessing` for that.

## `ThreadPoolExecutor` — Recommended

`concurrent.futures.ThreadPoolExecutor` is the high-level API. Prefer it over manual `threading.Thread` management:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read(200).decode()

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]

with ThreadPoolExecutor(max_workers=3) as executor:
    # map — preserves order, blocks until all done
    for result in executor.map(fetch, urls):
        print(result[:50])

    # submit + as_completed — returns results as they finish
    futures = {executor.submit(fetch, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
            print(f"{url}: {len(data)} bytes")
        except Exception as e:
            print(f"{url} failed: {e}")
```

## Manual Threads

Use `threading.Thread` when you need fine-grained control:

```python
import threading
import time

results = {}

def worker(name: str, duration: float):
    time.sleep(duration)
    results[name] = f"{name} finished after {duration}s"

threads = [
    threading.Thread(target=worker, args=(f"T{i}", 0.1 * i))
    for i in range(1, 4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()    # wait for all to finish

print(results)
```

## Thread Safety with Locks

When multiple threads write to shared data, use a `Lock` to prevent race conditions:

```python
import threading

counter = 0
lock = threading.Lock()

def increment(n: int):
    global counter
    for _ in range(n):
        with lock:
            counter += 1   # only one thread at a time

threads = [threading.Thread(target=increment, args=(10_000,)) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)   # Always 50000 — safe with lock
```

Without the lock, threads would read and write `counter` simultaneously, causing lost updates (the count would be unpredictably less than 50000).

## Thread-Safe Queues

`queue.Queue` is the recommended way to communicate between threads — it is internally thread-safe:

```python
import queue
import threading

task_queue: queue.Queue = queue.Queue()

def producer():
    for i in range(5):
        task_queue.put(i)
    task_queue.put(None)   # sentinel to signal done

def consumer():
    while True:
        item = task_queue.get()
        if item is None:
            break
        print(f"Processing {item}")
        task_queue.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join(); t2.join()
```

## `threading.local()` — Thread-Local Storage

`threading.local()` creates an object where each thread has its own isolated attribute values:

```python
import threading

local_data = threading.local()

def worker():
    local_data.value = threading.current_thread().name
    print(local_data.value)

threads = [threading.Thread(target=worker) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```
