from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar
from pydantic import BaseModel
from tinydb import TinyDB, Query

Schema = TypeVar("Schema", bound=BaseModel)

DBConnections = TinyDB


class DataSource(ABC, Generic[Schema]):
    def __init__(self, connection: DBConnections, model: Schema) -> None:
        self._connection = connection
        self.model = model

    @abstractmethod
    def read_all(self) -> List[Schema]:
        ...

    @abstractmethod
    def read(self, condition: Query) -> List[Schema]:
        ...

    @abstractmethod
    def create(self, new_elemnt: Schema) -> None:
        ...

    @abstractmethod
    def delete(self, condition: Query) -> None:
        ...

    @abstractmethod
    def update(self, condition: Query, new_elemnt: Schema) -> None:
        ...
