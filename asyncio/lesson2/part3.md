# Asyncio - lesson 2.3

> Reading

The following code is one suggestion to improve the problem from the previous exercise. Look at the following lines of code:

```
import time
from collections import deque


class Scheduler:
    def __init__(self) -> None:
        self.ready = deque()
        self.sleeping = []

    def call_soon(self, func) -> None:
        self.ready.append(func)

    def call_later(self, delay: int, func) -> None:
        deadline = time.time() + delay
        self.sleeping.append((deadline, func))
        self.sleeping.sort()

    def run(self) -> None:
        while self.ready or self.sleeping:
            if not self.ready:
                # find the nearst deadline
                deadline, func = self.sleeping.pop(0)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)
            while self.ready:
                func = self.ready.popleft()
                func()


sched = Scheduler()


def countdown(start: int) -> None:
    if start > 0:
        print("DOWN", start)
        sched.call_later(4, lambda: countdown(start - 1))


def countup(stop: int) -> None:
    def _run(x: int) -> None:
        if x < stop:
            print("UP", x)
            sched.call_later(1, lambda: _run(x + 1))

    _run(0)


sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(20))
sched.run()
```

#

> Exercise

1. Without exectue this lines of code. Try to figure out what will be the output.
   <br>
   What is wired about these lines? (Hint, try to think about a priority queue also about edge cases)

2. Try changing the code to overcome the previous issue.
