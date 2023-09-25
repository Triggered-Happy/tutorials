import asyncio
import time


async def create_file(name) -> None:
    with open(name, mode="w") as f:
        for i in range(1_000):
            f.write("hello async\n")
            await asyncio.sleep(0.0000001)
        print(f"File {name} is ready")


async def main():
    start = time.perf_counter()
    await create_file("one.txt")
    await create_file("two.txt")
    await create_file("three.txt")
    end = time.perf_counter()
    print(f"time: {end- start}")


async def main_imporoved() -> None:
    start = time.perf_counter()

    t1 = asyncio.create_task(create_file("one.txt"))
    t2 = asyncio.create_task(create_file("two.txt"))
    t3 = asyncio.create_task(create_file("three.txt"))

    for t in [t1, t2, t3]:
        await t

    end = time.perf_counter()
    print(f"time: {end- start}")


async def main_imporoved_2() -> None:
    start = time.perf_counter()

    t1 = asyncio.create_task(create_file("one.txt"))
    t2 = asyncio.create_task(create_file("two.txt"))
    t3 = asyncio.create_task(create_file("three.txt"))
    await asyncio.gather(*[t1, t2, t3])
    end = time.perf_counter()
    print(f"time: {end- start}")


asyncio.run(main_imporoved_2())
