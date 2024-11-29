import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import fake_users_db
from app.services.pokemon_service import fake_pokemon_db

client = TestClient(app)

def test_register_user():
    fake_users_db.clear()
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    #assert #response.json() == {"username": "testuser"}
    assert "user_id" in response.json()

def test_login_user():
    fake_users_db.clear()
    # First, register the user
    client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    #response = client.post("/login", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()