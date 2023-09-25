# Asyncio - lesson 1.4

### Tasks and coroutines

> Exercise

Run the following code:

```
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

```

1. Why do we use await `asyncio.sleep(0.0000001)` ?
2. Do the coroutines `create_file` run efficiently in terms of I\O bounds? Explain.
3. Improve the code to deal with the previous problem.
