# FILEPATH: /Users/tyronsamaroo/Code/Python/fastapi-demo/test_main.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "q": None}

def test_create_item():
    response = client.post("/items/", json={"item_id": 1, "name": "Test Item", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Test Item", "price": 10.0, "is_offer": None}

def test_update_item():
    response = client.put("/items/1", json={"name": "Updated Item", "price": 20.0})
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Updated Item", "price": 20.0}

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "status": "deleted"}