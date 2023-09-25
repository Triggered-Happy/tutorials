import asyncio
from time import perf_counter
from typing import Callable, List
from cusumer import Cusumer
from work_task import WorkTask
from producer import Producer

NUM_WORKERS = 25
WORK_QUEUE_MAX_SIZE = 100


class JobController:
    def __init__(
        self,
        tasks_batch: List[WorkTask],
        task_completed_callback: Callable,
        job_completed_callback: Callable,
    ) -> None:
        self.tasks_batch = tasks_batch
        self.task_completed_callback = task_completed_callback
        self.job_completed_callback = job_completed_callback

    async def _run_job(self) -> None:
        work_queue = asyncio.Queue(maxsize=WORK_QUEUE_MAX_SIZE)
        tasks = []

        producer_completed = asyncio.Event()
        producer_completed.clear()
        tasks.append(
            asyncio.create_task(
                Producer(self.tasks_batch, work_queue, producer_completed).produce()
            )
        )
        for _ in range(NUM_WORKERS):
            tasks.append(
                asyncio.create_task(
                    Cusumer(work_queue, self.task_completed_callback).consume()
                )
            )

        await producer_completed.wait()
        await work_queue.join()
        for task in tasks:
            task.cancel()

    def run(self) -> None:
        start = perf_counter()
        asyncio.run(self._run_job())
        end = perf_counter()
        self.job_completed_callback({"elapsed_secs": end - start})
