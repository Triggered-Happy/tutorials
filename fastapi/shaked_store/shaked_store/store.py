from typing import List, Optional, Union
from fastapi import HTTPException
from shaked_store.dal.data_source import DataSource, Schema
from tinydb import Query
from shaked_store.dal.exceptions import NonExistingItemException, ExistingItemException


class Store:
    def __init__(self, dal: DataSource) -> None:
        self._dal = dal

    def get_all(self) -> List[Schema]:
        return self._dal.read_all()

    def get_item_by_name(self, name: str) -> Schema:
        try:
            documents = self._dal.read(Query().name == name)
        except NonExistingItemException:
            raise HTTPException(
                status_code=404, detail=f"Item with {name} doesn't exist"
            )
        return documents[0]

    def insert_new_item(self, item: Schema) -> Union[HTTPException, None]:
        try:
            self._dal.create(item)
        except ExistingItemException:
            raise HTTPException(
                status_code=400, detail=f"Item with {item.name} already exists"
            )

    def delete_item_by_name(self, name: str) -> Union[HTTPException, None]:
        try:
            self._dal.delete(Query().name == name)
        except NonExistingItemException:
            raise HTTPException(
                status_code=400, detail=f"Item with {name} doesn't exist"
            )

    def update_by_name(
        self,
        item_name: str,
        item_price: Optional[float],
        item_count: Optional[int],
    ) -> None:
        item = self.get_item_by_name(item_name)
        if item_price:
            item.price = item_price
        if item_count:
            item.count = item_count
        self._dal.update(Query().name == item_name, item)
