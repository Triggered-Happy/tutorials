import asyncio
from typing import List
from work_task import WorkTask


class Producer:
    def __init__(
        self,
        tasks_batch: List[WorkTask],
        work_queue: asyncio.Queue,
        producer_completed: asyncio.Event,
    ) -> None:
        self.tasks_batch = tasks_batch
        self.work_queue = work_queue
        self.producer_completed = producer_completed

    async def produce(self) -> None:
        for data in self.tasks_batch:
            await self.work_queue.put(data)
        self.producer_completed.set()
