import asyncio
from random import random


async def sleep_task():
    await asyncio.sleep(2)
    return "Task completed"


async def estimate_pi(number_of_points: int = 1000000) -> float:
    points = [(random(), random()) for _ in range(number_of_points)]
    number_of_points_in_circle = sum([1 for x, y in points if (x**2 + y**2) < 1])
    return (number_of_points_in_circle / number_of_points) * 4


# Function that returns a Future
def create_future_task():
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    async def calc_pi() -> None:
        result = await estimate_pi()
        future.set_result(result)

    asyncio.ensure_future(calc_pi())
    return future


async def main() -> None:
    future = create_future_task()
    print("Pi estimation in progress ...")

    coroutine_result = await sleep_task()
    print("Coroutine Result:", coroutine_result)

    future_result = await future
    print("Pi estimation:", future_result)


asyncio.run(main())
