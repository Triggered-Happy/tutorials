# Asyncio - lesson 4.2

### Advance - future

Read about how to calculate pi approximately on Didi's Monte Carlo algorithm.
Read about the algorithm and not about its implementation in Python.

Albert is a nice guy, but likes the value of pie.
In this exercise we will try to help Albert.
Because the task of evaluating pi is computationally difficult,
we will try to write a program that calculates the value of pi and then runs another coroutine.

```
import asyncio
from random import random

async def sleep_task():
    await asyncio.sleep(2)
    return "Task completed"


async def estimate_pi(number_of_points: int = 1000000) -> float:
    ...


# Function that returns a Future
def create_future_task():
    ...

async def main() -> None:
    future = create_future_task()
    print("Pi estimation in progress ...")

    coroutine_result = await sleep_task()
    print("Coroutine Result:", coroutine_result)

    future_result = await future
    print("Pi estimation:", future_result)


asyncio.run(main())

```
