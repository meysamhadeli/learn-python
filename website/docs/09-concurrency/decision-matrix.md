# Concurrency Decision Matrix

This page is the synthesis step for the chapter. Instead of learning one tool in isolation, you use it to choose an approach based on workload, coordination needs, and runtime constraints.

If the earlier concurrency pages explain how each tool works, this page explains how to decide between them in practice.

## Which Tool for Which Problem?

| Workload Type | Recommended Tool | Reason |
|---------------|-----------------|--------|
| Many I/O operations, high concurrency | `asyncio` | Single thread, no OS overhead, scales to thousands of connections |
| I/O-bound, existing sync code | `threading` / `ThreadPoolExecutor` | GIL released during I/O, simpler than rewriting async |
| CPU-bound computation | `multiprocessing` / `ProcessPoolExecutor` | Each process bypasses the GIL |
| CPU-bound, Python 3.13+ | free-threading (`python3.13t`) | True parallelism without process overhead |
| Mixed: async event loop + CPU work | `asyncio` + `run_in_executor` | Offloads blocking code without freezing the event loop |

## The `run_in_executor` Pattern

The most common pattern for mixing `asyncio` with blocking code (CPU-bound or legacy sync libraries):

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def blocking_io(url: str) -> str:
    time.sleep(1)   # simulates blocking I/O (legacy library)
    return f"Data from {url}"

def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))

async def main():
    loop = asyncio.get_running_loop()

    # Run blocking I/O in a thread pool — doesn't block the event loop
    with ThreadPoolExecutor(max_workers=5) as thread_pool:
        result = await loop.run_in_executor(thread_pool, blocking_io, "https://api.example.com")
        print(result)

    # Run CPU-bound work in a process pool — true parallelism
    with ProcessPoolExecutor() as process_pool:
        result = await loop.run_in_executor(process_pool, cpu_heavy, 10_000_000)
        print(result)

asyncio.run(main())
```

## Flow Chart

Use this decision flow when choosing a concurrency strategy:

1. **Is the task I/O-bound or CPU-bound?**
   - If **I/O-bound** → continue to step 2
   - If **CPU-bound** → use `ProcessPoolExecutor` (or free-threading on 3.13t)

2. **Is the codebase async-first or sync-first?**
   - If **async** → use `asyncio` with `await`
   - If **sync** → use `ThreadPoolExecutor`

3. **Do you need to mix async with CPU work?**
   - Use `loop.run_in_executor(ProcessPoolExecutor(), ...)` to offload from the event loop

## Quick Reference

```python
# asyncio — 1000 concurrent I/O tasks
import asyncio, httpx

async def main():
    async with httpx.AsyncClient() as client:
        responses = await asyncio.gather(
            *[client.get(url) for url in urls]
        )

# ThreadPoolExecutor — blocking I/O
from concurrent.futures import ThreadPoolExecutor
import requests

with ThreadPoolExecutor(max_workers=10) as pool:
    results = list(pool.map(requests.get, urls))

# ProcessPoolExecutor — CPU
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    results = list(pool.map(compute, data_chunks))
```

## Performance Expectations

| Approach | Overhead | Scales to |
|----------|---------|-----------|
| `asyncio` | Very low (coroutine switch ~μs) | Tens of thousands of connections |
| `threading` | Low (OS thread switch ~μs) | Hundreds of threads |
| `multiprocessing` | High (process spawn ~50ms) | CPU count processes |
