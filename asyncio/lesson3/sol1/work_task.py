from dataclasses import dataclass
from uuid import UUID


@dataclass
class WorkTask:
    id: UUID
    number: int
    exec: callable


@dataclass
class WorkTaskResult(WorkTask):
    time_secs: int
