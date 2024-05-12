# Asyncio - lesson 4.2

### Advance - future

#

> Reading

Read about how to calculate pi approximately on Didi's Monte Carlo algorithm.
Read about the algorithm and not about its implementation in Python.

#

> Exercise

Albert is a nice guy, but likes the value of pie.

In this exercise we will try to help Albert.
Because the task of evaluating pi is computationally difficult,

we will try to write a program that calculates the value of pi and then runs another coroutine. Help him complete it:

```
import asyncio
from random import random

async def sleep_task():
    await asyncio.sleep(2)
    return "Task completed"


async def estimate_pi(number_of_points: int = 1000000) -> float:
    # Write you code here


# Function that returns a Future
def create_future_task():
    # Write you code here

async def main() -> None:
    # Write you code here
    print("Pi estimation in progress ...")

    coroutine_result = await sleep_task()
    print("Coroutine Result:", coroutine_result)

    # Write you code here
    print("Pi estimation:", future_result)


asyncio.run(main())

```

**_Notes:_**
* IDK how but you managed to pick one of the worse problems to tackle with async code. One of the most important distinctions to teach people that are just being introduced into the world of concurrency is when to use async, threading, or multiprocessing, this not only fails to do so but points them at the wrong direction.
