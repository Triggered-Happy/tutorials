# Asyncio - lesson 2.1

<p>
In this chapter, we will talk about the comparison of Asyncio vs Threading
</p>

Read: https://superfastpython.com/asyncio-vs-threading/

<details>
    <summary>
    1. Explain about the disadvantage of running code using a thread? 
    </summary>
    Refer to scalability, GIL, thread cancellation ... 
</details>

<details>
    <summary>
    2. Figure out how to switch between tasks without threading or multiprocessing.
    </summary>
    Scheduling callbacks :)
</details>

#

We will try to build our aync package, after all there is no better way than to learn something by writing it ourselves :)

Look at the following lines of code.

```
import threading


def countdown(start: int) -> None:
    for counter in range(start):
        print("Down", counter)


def countup(stop: int) -> None:
    for counter in range(stop):
        print("UP", counter)


# Concurrent execution - classic solution: use threads

threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()

```

We would like to add a task management capability to the above code.
let's do it :)
