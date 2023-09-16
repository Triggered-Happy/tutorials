import time
from collections import deque
from heapq import heappush, heappop


class Scheduler:
    def __init__(self) -> None:
        self.ready = deque()  # Functions ready to execute
        self.sleeping = []  # Sleeping functions
        self.sequence = 0

    def call_soon(self, func) -> None:
        self.ready.append(func)

    def call_later(self, delay: int, func) -> None:
        self.sequence += 1
        deadline = time.time() + delay  # Expiration time
        heappush(self.sleeping, (deadline, self.sequence, func))

    def run(self) -> None:
        while self.ready or self.sleeping:
            if not self.ready:
                # find the nearst deadline
                deadline, _, func = heappop(self.sleeping)
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
