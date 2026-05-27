# Chapter IX: Concurrency

Python's concurrency model and when to use each tool.

Concurrency is where Python learners often need a decision framework, not just syntax. This chapter explains the major tools Python offers and, more importantly, the tradeoffs between them.

The central questions are:

- are you waiting on I/O or doing CPU-heavy work?
- do you need shared memory, isolation, or simple coordination?
- does the Global Interpreter Lock matter for this workload?

By the end of the chapter, you should be able to choose an approach for a problem instead of guessing between `asyncio`, threads, and processes.

## Sections

- [The GIL](./the-gil)
- [Async / Await](./async-await)
- [Threading](./threading)
- [Multiprocessing](./multiprocessing)
- [Free-Threading](./free-threading)
- [Decision Matrix](./decision-matrix)
