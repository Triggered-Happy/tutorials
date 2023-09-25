import asyncio
import random
from time import perf_counter
from typing import Callable
from work_task import WorkTask, WorkTaskResult


class Cusumer:
    def __init__(
        self,
        work_queue: asyncio.Queue,
        callback: Callable[[str], None],
    ) -> None:
        self.work_queue = work_queue
        self.callback = callback

    async def consume(self) -> None:
        while True:
            task_data: WorkTask = await self.work_queue.get()

            start = perf_counter()
            await task_data.exec(random.random())
            end = perf_counter()

            self.callback(
                repr(
                    WorkTaskResult(
                        id=task_data.id,
                        number=task_data.number,
                        time_secs=end - start,
                        exec=task_data.exec,
                    )
                )
            )
            self.work_queue.task_done()
