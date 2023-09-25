# FastApi - lesson 1.1

### Intro

#

> Reading

Read: https://fastapi.tiangolo.com/python-types/

Read: https://fastapi.tiangolo.com/tutorial/

Read: Tinydb documantion.

#

> Exercise

Shaked is a special person. In fact, one of the special ones in the department. Shaked has a great love for keeping equipment (any equipment, really.).

In this task, we have to write a server that will help Shaked manage his equipment.
To accomplish this task, a FASTAPI server was built. The server will refer to a DB (TinyDB), to provide persistence.

The FASTAPI server should be written so that there are 5 endpoints:

1. Returning all the equipment list that is in the DB.

```
@router.get("/", status_code=status.HTTP_200_OK)
def index() -> List[Item]:
    ...
```

2. Returning equipment by name.

```
@router.get("/items/{item_name}", status_code=status.HTTP_200_OK)
def query_item_by_name(item_name: str) -> Item:
    ...
```

3. Adding new equipment.

```
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def add_item(item: Item) -> None:
    ...
```

4. Deleting equipment by name.

```
@router.delete(
    "/delete/{item_name}",
    status_code=status.HTTP_200_OK,
)
def delte_item(item_name: str) -> None:
    ...
```

5. Equipment update.

```
@router.put("/update/{item_name}")
def update(
    item_name: str = None,
    item_price: Optional[float] = None,
    item_count: Optional[int] = None,
    status_code=status.HTTP_200_OK,
) -> None:
    ...
```

Remarks:

1. The structure of an item is:

```
class Item(BaseModel):
    name: str
    price: float
    count: int
```

2. You can assume that there are not several pieces of equipment that have the (name is unique).

3. Although we are working with one DB at the moment, this may have changed later. Therefore, we would like to write the server so that it is open to extensions and can work with any DB.

4. Don't forget to work with linters, formatter, TDD (system test and unit test).
