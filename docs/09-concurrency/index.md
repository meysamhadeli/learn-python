# Chapter IX: Concurrency

Python concurrency choices and when they actually matter.

Do not spend your first hour here unless your immediate work depends on it. Most Python learners need only one idea at the start: choose concurrency based on workload, not fashion.

## Decision rules

- are you waiting on I/O or doing CPU-heavy work?
- async is usually for high-concurrency I/O
- threads are fine for blocking I/O and integration code
- processes are for CPU-heavy work

By the end of the chapter, you should be able to choose an approach for a problem instead of guessing between `asyncio`, threads, and processes.

## Sections

- [The GIL](./the-gil)
- [Async / Await](./async-await)
- [Threading](./threading)
- [Multiprocessing](./multiprocessing)
- [Free-Threading](./free-threading)
- [Decision Matrix](./decision-matrix)
