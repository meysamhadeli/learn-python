# Async / Await

`async` and `await` are mainly for I/O-heavy concurrency, not CPU-heavy speedups.

## How asyncio Works

`asyncio` uses a single-threaded event loop. Coroutines pause at `await` so other work can run.

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

Use `asyncio.run()` at top level. In notebooks, usually use `await` directly.

## Concurrency with `asyncio.gather()`

Use `asyncio.gather()` to run multiple coroutines concurrently:

```python
import asyncio
import time

async def fetch(url: str) -> str:
    await asyncio.sleep(1)    # simulate network request
    return f"Data from {url}"

async def main():
    start = time.perf_counter()
    r1, r2 = await asyncio.gather(
        fetch("https://api.example.com/users"),
        fetch("https://api.example.com/posts"),
    )
    print(f"Done in {time.perf_counter() - start:.2f}s")

asyncio.run(main())
```

## Tasks

`asyncio.create_task()` schedules a coroutine immediately:

```python
async def main():
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
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

## Common Pitfalls

- **Blocking calls inside coroutines** — `time.sleep()`, file reads, CPU work block the entire event loop. Use `await asyncio.sleep()`, async libraries, or `loop.run_in_executor()` to offload.
- **Not awaiting a coroutine** — calling `fetch(url)` without `await` creates the coroutine object but never runs it.
- **Shared mutable state** — coroutines share memory; protect shared state with `asyncio.Lock()` when needed.
