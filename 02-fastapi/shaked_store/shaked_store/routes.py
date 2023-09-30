from typing import List, Optional

from fastapi import status
from tinydb import TinyDB
from models import Item
from store import Store
from shaked_store.dal.tinydb_data_source import TinyDataSource
from fastapi import APIRouter

router = APIRouter(prefix="/shaked_store")

shaked_store_service = Store(
    dal=TinyDataSource[Item](connection=TinyDB("tiny.json"), model=Item),
)


@router.get("/", status_code=status.HTTP_200_OK)
def index() -> List[Item]:
    return shaked_store_service.get_all()


@router.get("/items/{item_name}", status_code=status.HTTP_200_OK)
def query_item_by_name(item_name: str) -> Item:
    return shaked_store_service.get_item_by_name(item_name)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def add_item(item: Item) -> None:
    shaked_store_service.insert_new_item(item)


@router.delete(
    "/delete/{item_name}",
    status_code=status.HTTP_200_OK,
)
def delte_item(item_name: str) -> None:
    shaked_store_service.delete_item_by_name(item_name)


@router.put("/update/{item_name}")
def update(
    item_name: str = None,
    item_price: Optional[float] = None,
    item_count: Optional[int] = None,
    status_code=status.HTTP_200_OK,
) -> None:
    shaked_store_service.update_by_name(item_name, item_price, item_count)
