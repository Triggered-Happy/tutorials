# Asyncio - lesson 1.4

### Caution ! 

> Exercise

Without running, what is the expected output for the following piece of code?

It can go wrong when two coroutines enter a deadlock : )

```
import asyncio


async def foo():
    await boo()


async def boo():
    await foo()


async def main():
    await asyncio.gather(*[foo(), boo()])


asyncio.run(main())
```

**_Notes:_**
* I mean, this is just the same as normal functions, It would end in a maximum recursion error, if that is the intended outcome
