from typing import Union, Optional, Dict

from fastapi import FastAPI

app = FastAPI()

# Endpoint for the root URL
@app.get("/", response_model=Dict[str, str])
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}

# Endpoint to get an item by ID
@app.get("/items/{item_id}", response_model=Dict[str, Union[int, str, None]])
def read_item(item_id: int, q: Union[str, None] = None) -> Dict[str, Union[int, str, None]]:
    return {"item_id": item_id, "q": q}

# Endpoint to get a user by ID
@app.get("/users/{user_id}", response_model=Dict[str, Union[int, str, None]])
def read_user(user_id: int, q: Optional[str] = None) -> Dict[str, Union[int, str, None]]:
    return {"user_id": user_id, "q": q}

# Endpoint to create a new item
@app.post("/items/", response_model=Dict[str, Union[int, str, float, bool, None]])
def create_item(item_id: int, name: str, price: float, is_offer: Optional[bool] = None) -> Dict[str, Union[int, str, float, bool, None]]:
    return {"item_id": item_id, "name": name, "price": price, "is_offer": is_offer}

# Endpoint to update an existing item
@app.put("/items/{item_id}", response_model=Dict[str, Union[int, str, float, None]])
def update_item(item_id: int, name: Optional[str] = None, price: Optional[float] = None) -> Dict[str, Union[int, str, float, None]]:
    return {"item_id": item_id, "name": name, "price": price}

# Endpoint to delete an item
@app.delete("/items/{item_id}", response_model=Dict[str, Union[int, str]])
def delete_item(item_id: int) -> Dict[str, Union[int, str]]:
    return {"item_id": item_id, "status": "deleted"}