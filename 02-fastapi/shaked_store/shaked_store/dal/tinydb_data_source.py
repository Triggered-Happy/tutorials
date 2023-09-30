from typing import Generic, List

from tinydb import Query
from .exceptions import (
    ExistingItemException,
    NonExistingItemException,
)
from .data_source import DBConnections, DataSource, Schema


class TinyDataSource(DataSource[Schema], Generic[Schema]):
    def __init__(self, connection: DBConnections, model: Schema) -> None:
        super().__init__(connection, model)

    def read_all(self) -> List[Schema]:
        documents = self._connection.all()
        return [self.model.parse_obj(document) for document in documents]

    def read(self, condition: Query) -> List[Schema]:
        documents = self._connection.search(condition)
        if documents == []:
            raise NonExistingItemException()
        return [self.model.parse_obj(document) for document in documents]

    def update(self, condition: Query, new_elemnt: Schema) -> None:
        if self._connection.update(dict(new_elemnt), condition) == []:
            raise NonExistingItemException()

    def create(self, new_elemnt: Schema) -> None:
        try:
            self.read(Query().name == new_elemnt.name)
        except NonExistingItemException:
            self._connection.insert(dict(new_elemnt))
            return
        raise ExistingItemException()

    def delete(self, condition: Query) -> None:
        if self._connection.remove(condition) == []:
            raise NonExistingItemException()
