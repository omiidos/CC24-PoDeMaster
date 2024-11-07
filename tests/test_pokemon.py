# tests/test_pokemon.py
import pytest
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import app 

client = TestClient(app)

def test_get_pokemons():
    response = client.get("/pokemons/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_pokemon():
    pokemon_data = {
        "name": "Pikachu",
        "type": "Electric",
        "level": 5,
        "caught_in_game": "Pokémon Sword",
        "shiny": True
    }
    response = client.post("/pokemons/", json=pokemon_data)
    assert response.status_code == 201
    assert response.json()["name"] == pokemon_data["name"]
    assert response.json()["shiny"] == pokemon_data["shiny"]
