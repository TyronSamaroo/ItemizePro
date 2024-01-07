from typing import Union, Optional, Dict, List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, Item as ItemModel
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost:3000",  # React app is served from this URL
    # Add other origins if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint for the root URL
@app.get("/", response_model=Dict[str, str])
def read_root() -> Dict[str, str]:
    return {"Hello": "World"}

@app.get("/items/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    items = db.query(ItemModel).all()
    return items
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