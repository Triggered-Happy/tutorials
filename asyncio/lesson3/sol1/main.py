import asyncio
from functools import partial
from random import seed
from uuid import uuid4
from work_task import WorkTask

from controller import JobController


def task_completed_callback_handler(job_id: str, callback_message: str) -> None:
    print(f"Task job id={job_id}: {callback_message}")


def job_completed_callback_handler(job_id: str, callback_message: str) -> None:
    print(f"Job {job_id} completed: {callback_message}")


def main(job_id: str, tasks_size: int) -> None:
    print(f"Starting Job {job_id}")
    task_callback = partial(task_completed_callback_handler, job_id)
    job_callback = partial(job_completed_callback_handler, job_id)

    tasks_data = [
        WorkTask(id=uuid4(), number=i, exec=asyncio.sleep) for i in range(tasks_size)
    ]

    JobController(tasks_data, task_callback, job_callback).run()


if __name__ == "__main__":
    seed(0)
    main(job_id=str(uuid4()), tasks_size=10)
