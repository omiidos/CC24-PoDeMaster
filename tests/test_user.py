# tests/test_user.py
import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import app  # This should now work


client = TestClient(app)

def test_register_user():
    user_data = {"username": "ash_ketchum", "password": "pikachu123"}
    response = client.post("/users/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

def test_login_user():
    user_data = {"username": "ash_ketchum", "password": "pikachu123"}
    response = client.post("/users/login", data=user_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
