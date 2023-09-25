# Asyncio - lesson 2.1

> Reading

We will try to build our minimal aync package, after all there is no better way than to learn something by writing it ourselves :)

Look at the following lines of code.

```
import threading


def countdown(start: int) -> None:
    for counter in range(start):
        print("Down", counter)


def countup(stop: int) -> None:
    for counter in range(stop):
        print("UP", counter)


threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()

```

We would like to add a `task management` capability to the above code.
let's do it :)
