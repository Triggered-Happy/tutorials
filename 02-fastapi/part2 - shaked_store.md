# FastApi - lesson 1.1

### Intro

#

> Reading

Read: Tinydb documantion.

#

> Exercise

Shaked is a special person. In fact, one of the special ones in the department. Shaked has a great love for keeping items (any item, really.).

In this task, we have to write a server that will help Shaked manage his items.
To accomplish this task, a FASTAPI server was built. The server will refer to a DB (TinyDB), to provide persistence.

#

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

#

The FASTAPI server should be written so that there are 5 endpoints:

1. Returning all the items that is in the DB.

```
Route path: /
Return: List[Item]
http method: GET
```

2. Returning equipment by name.

```
Route path: /items/{item_name}
Path parameters item_name
Return: Item
http method: GET
```

3. Adding new equipment.

```
Route path: /
Query parameters: item
Return: None
http method: POST
```

4. Deleting equipment by name.

```
Route path: /delete/{item_name}
Path parameters item_name
Return: None
http method: DELETE
```

5. Equipment update.

```
Route path: /update/{item_name}
Path parameters item_name
Query parameters: item_price, item_count
Return: None
http method: PUT
```
