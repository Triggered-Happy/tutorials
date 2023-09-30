Q1. What are coroutines in asyncio, and how do they differ from threads?

Answer: Coroutines in asyncio are functions that can be suspended and resumed. They are used for cooperative multitasking within a single thread, unlike threads that are managed by the operating system and can run in separate processes.

Q2. What is the Global Interpreter Lock (GIL), and how does it affect threads in Python?

Answer: The Global Interpreter Lock (GIL) restricts the execution of Python code to one thread at a time, even in multi-threaded programs. This limitation can impact the parallelism of threads.

Q3. Can asyncio tasks suffer from race conditions and deadlocks?

Answer: Yes, both coroutines and threads can suffer from race conditions and deadlocks, depending on how concurrency is managed and synchronized.
