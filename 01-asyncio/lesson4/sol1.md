Q1: What is a Future object in asyncio, and how does it differ from a coroutine object?

A1: A Future object in asyncio is an awaitable that represents some ongoing process that may or may not have finished. Unlike a coroutine object, awaiting a Future does not execute a block of code. Instead, it allows your code to wait for the process to complete and retrieve its result or handle any exceptions.

Q2: Can a Future object that is done change back to not being done in asyncio?

A2: No, once a Future object is done (i.e., the represented process has finished), it cannot change back to not being done. The transition to being done is a one-time occurrence.

Q3: What is the significance of the distinction between a Coroutine and a Future in asyncio?

A3: The distinction is important. A Coroutine's code is not executed until it is awaited, allowing you to control when it runs. In contrast, a Future represents something that is already executing or ongoing, and it allows your code to wait for its completion, check its status, and retrieve its result. Understanding this difference is crucial when working with asynchronous code in asyncio.

**_Notes:**
* A3 - What? Based on my previous assumption that you are confusing between Task and Coroutine this is just completly wrong and even if that assumption is worng then this answer is lacking.
* A1 - Opaquely worded, especially the last sentance. Shares the same problem as A3 that was mentioned above.
