# Multiprocessing

Multiprocessing trades simplicity of shared memory for real parallel execution across CPU cores. That tradeoff matters because it changes both performance and program design.

The main lesson here is when the extra process overhead is justified by CPU-bound workloads.

## When to Use Multiprocessing

`multiprocessing` creates separate OS processes — each has its own Python interpreter and its own GIL. This enables **true CPU parallelism** across multiple cores, which is impossible with threads due to the GIL.

Use `multiprocessing` for **CPU-bound** tasks: numerical computation, image processing, data parsing, compression.

## `ProcessPoolExecutor` — Recommended

```python
from concurrent.futures import ProcessPoolExecutor
import time

def cpu_task(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":   # Required on Windows — guards against infinite spawning
    numbers = [10_000_000] * 4

    start = time.perf_counter()
    with ProcessPoolExecutor() as executor:
        # By default uses cpu_count() workers
        results = list(executor.map(cpu_task, numbers))
    print(f"Done in {time.perf_counter() - start:.2f}s")
    print(results)
```

The `if __name__ == "__main__":` guard is **mandatory** on Windows. Without it, each spawned process re-imports the main module and recursively spawns more processes.

## Low-Level `multiprocessing.Pool`

```python
from multiprocessing import Pool

def process_chunk(chunk: list[int]) -> int:
    return sum(chunk)

if __name__ == "__main__":
    data = list(range(1_000_000))
    chunk_size = len(data) // 4
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(processes=4) as pool:
        partial_sums = pool.map(process_chunk, chunks)
    print(sum(partial_sums))   # 499999500000
```

## Sharing State Between Processes

Processes do **not** share memory by default — data is pickled and copied when passed to workers. Avoid shared state; prefer returning results. When you truly need shared state, use `multiprocessing.Value` and `multiprocessing.Array`:

```python
from multiprocessing import Process, Value, Lock

def increment(counter, lock, n):
    for _ in range(n):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = Value("i", 0)    # shared integer (typecode "i")
    lock = Lock()

    processes = [Process(target=increment, args=(counter, lock, 10_000)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(counter.value)   # 40000
```

## `multiprocessing.Queue` for Communication

For producer-consumer patterns between processes:

```python
from multiprocessing import Process, Queue

def producer(q: Queue):
    for i in range(5):
        q.put(i)
    q.put(None)   # sentinel

def consumer(q: Queue):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
```

## Performance Considerations

- **Startup cost** — spawning a process is expensive (tens of milliseconds). Only worth it for tasks that take seconds, not microseconds.
- **Serialization cost** — all arguments and results are pickled. Large data (big NumPy arrays) can negate the parallelism benefit. Use `shared_memory` (Python 3.8+) for large arrays.
- **Rule of thumb** — pool size = `os.cpu_count()` for CPU-bound; I/O-bound tasks don't benefit from more processes.
