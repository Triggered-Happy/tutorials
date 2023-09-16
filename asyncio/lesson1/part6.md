# Asyncio - lesson 1.6

### Producer-Consumer model

In computing, the producer-consumer problem (also known as the bounded-buffer problem) is a family of problems described by Edsger W. Dijkstra since 1965.

A producer submits work to be done to a queue (or multiple producers even). In our example, we will work with one producer.

```
class Producer:
    def __init__(
        self,
        tasks_batch: List[WorkTask],
        work_queue: asyncio.Queue,
        producer_completed: asyncio.Event,
    ) -> None:
        ...

    async def produce(self) -> None:
        ...
```

The queue (also called the work queue) holds all the work to be done. Every element in the queue is called 'work item'.

One or more consumers watch the queue. In our example, we will work with 25 consumers who are asynchronous running and looking for items on the queue.
If the work item is available in the queue, one of the consumers grabs the work item and performs the work.
when one consumer does the work of one work item, he comes back and looks for the next item on the work.

```
class Cusumer:
    def __init__(
        self,
        work_queue: asyncio.Queue,
        callback: Callable[[str], None],
    ) -> None:
        ...

    async def consume(self) -> None:
       ....

```

In order to control all the consumers\producer creations, handling task and more we recommands to work with:

```
class JobController:
    def __init__(
        self,
        tasks_batch: List[WorkTask],
        task_completed_callback: Callable,
        job_completed_callback: Callable,
    ) -> None:
        ...

    async def _run_job(self) -> None:
        ...

    def run(self) -> None:
        ...

```

Once the producer is done creating work items to the queue and the queue is empty we are done.

All the work (the creation of tasks and their execution by consumers) is called a `job`. Each work task is called a `Task`. After performing a single task by the consumer, a callback must be performed. And after the end of the entire job, another callback must be made.

```
def task_completed_callback_handler(job_id: str, callback_message: str) -> None:
    print(f"Task completed in {job_id}: {callback_message}")


def job_completed_callback_handler(job_id: str, callback_message: str) -> None:
    print(f"Job {job_id} completed: {callback_message}")

```

Output for exmaple:

```
Starting Job b13fecc3-5632-4abb-acf6-ef9c43afebc3
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('7fc1c8b4-32e3-4adc-8bfd-4c873ea2df15'), number=3, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.2604037)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('f3fa5c9a-9e7f-47ca-9619-6ce6fa137c81'), number=7, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.32249)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('3ec1dc8d-8fc5-482c-83b8-56f293463f38'), number=5, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.431357)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('3300aa8d-10d3-48cb-9e78-8bf67e7f97ac'), number=2, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.432644)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('d78bcd31-98f7-4573-87e6-893b43b8b28b'), number=8, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.49359460000000005)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('aa8d09d0-7ca3-4976-8b5b-c42b2bbe796a'), number=4, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.5258444)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('7b205345-f034-4c50-a132-18c8413b6b80'), number=9, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.6038920999999999)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('927cccd4-e0a8-4acf-ae3e-1f68789ec857'), number=1, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.776207)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('ca58436b-22fa-4739-9e2c-4a2ccb5795f6'), number=6, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.8072273)
Task job id=b13fecc3-5632-4abb-acf6-ef9c43afebc3: WorkTaskResult(id=UUID('8ab4ef54-9706-4cae-a36b-d15c93edabf8'), number=0, exec=<function sleep at 0x0000020D6C2AD940>, time_secs=0.8701545)
Job b13fecc3-5632-4abb-acf6-ef9c43afebc3 completed: {'elapsed_secs': 0.8731075}
```

Comments:

1. Usful constant:
   ```
   NUM_WORKERS = 25
   WORK_QUEUE_MAX_SIZE = 100
   ```
2. Don't measure time with time.time(). Think why!
3. Make sure you kill all open tasks when finished.
4. Read about `asyncio.Queue` and think how to use it. Use `asyncio.Queue.join` and `asyncio.Queue.task_done()`
