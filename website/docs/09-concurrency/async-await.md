# Async / Await

`async` and `await` are best understood as a model for cooperative I/O concurrency, not as a universal speed feature. They help when many tasks spend time waiting, but they do not automatically improve CPU-heavy work.

This page is mainly about learning the event-loop mental model so that coroutine behavior feels predictable instead of mysterious.

## How asyncio Works

Python's `asyncio` library provides a single-threaded **event loop** that runs cooperative coroutines. A **coroutine** is a function defined with `async def` — it can `await` other coroutines, pausing execution without blocking the thread. When a coroutine awaits I/O, the event loop runs other ready coroutines instead of sitting idle.

This makes `asyncio` ideal for **I/O-bound** workloads: thousands of simultaneous HTTP requests, database queries, WebSocket connections — all in a single thread.

## Basic Coroutine

```python
import asyncio

async def greet(name: str) -> str:
    await asyncio.sleep(1)   # non-blocking wait (simulates I/O)
    return f"Hello, {name}!"

async def main():
    result = await greet("Alice")
    print(result)

asyncio.run(main())   # Entry point — creates and runs the event loop
```

`asyncio.run()` is the correct entry point for top-level code. Never call it from inside a running event loop (e.g., in Jupyter use `await main()` instead).

## Concurrency with `asyncio.gather()`

To run multiple coroutines **concurrently**, use `asyncio.gather()` — it starts all of them and waits until all complete:

```python
import asyncio
import time

async def fetch(url: str) -> str:
    await asyncio.sleep(1)    # simulate network request
    return f"Data from {url}"

async def main():
    start = time.perf_counter()

    # Sequential — total ~2s
    r1 = await fetch("https://api.example.com/users")
    r2 = await fetch("https://api.example.com/posts")

    # Concurrent — total ~1s
    r1, r2 = await asyncio.gather(
        fetch("https://api.example.com/users"),
        fetch("https://api.example.com/posts"),
    )
    print(f"Done in {time.perf_counter() - start:.2f}s")

asyncio.run(main())
```

## Tasks

`asyncio.create_task()` schedules a coroutine to run on the event loop immediately — it does not block until the `await`:

```python
async def main():
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    # Both are now scheduled. Do other work...
    result1 = await task1
    result2 = await task2
```

## Real HTTP with `httpx`

```python
import asyncio
import httpx

async def get_post(client: httpx.AsyncClient, post_id: int) -> dict:
    response = await client.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )
    response.raise_for_status()
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        posts = await asyncio.gather(
            *[get_post(client, i) for i in range(1, 6)]
        )
    for post in posts:
        print(post["title"])

asyncio.run(main())
```

## Async Generators and Context Managers

```python
async def async_range(n: int):
    for i in range(n):
        await asyncio.sleep(0)   # yield control to event loop
        yield i

async def main():
    async for value in async_range(5):
        print(value)

    # Async context manager
    async with httpx.AsyncClient() as client:
        ...
```

## Common Pitfalls

- **Blocking calls inside coroutines** — `time.sleep()`, file reads, CPU work block the entire event loop. Use `await asyncio.sleep()`, async libraries, or `loop.run_in_executor()` to offload.
- **Not awaiting a coroutine** — calling `fetch(url)` without `await` creates the coroutine object but never runs it.
- **Shared mutable state** — coroutines share memory; protect shared state with `asyncio.Lock()` when needed.
