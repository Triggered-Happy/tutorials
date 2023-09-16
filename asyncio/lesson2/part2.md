# Asyncio - lesson 2.2

Look at the following lines of code.

```
import time
from collections import deque


class Scheduler:
    def __init__(self) -> None:
        self.ready = deque()

    def call_soon(self, func) -> None:
        self.ready.append(func)

    def run(self) -> None:
        while self.ready:
            func = self.ready.popleft()
            func()


sched = Scheduler()


def countdown(start: int) -> None:
    if start > 0:
        print("DOWN", start)
        time.sleep(1)
        sched.call_soon(lambda: countdown(start - 1))


def countup(stop: int) -> None:
    def _run(x: int) -> None:
        if x < stop:
            print("UP", x)
            time.sleep(1)
            sched.call_soon(lambda: _run(x + 1))

    _run(0)


sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()

```

<details>
    <summary>
    As you must have noticed, it is possible to start 2 tasks using this code, but they do not run efficiently (in terms of  I\O bound). Why? Explain how you found it?
    </summary>
    Basically, the time.sleep command is I\O bound and therefore blocks us from running other things. This prevents us from improving utilization and improving efficiency.
</details>
<br>

Try changing the code to overcome the previous issue.
