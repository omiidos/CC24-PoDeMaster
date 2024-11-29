import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import fake_users_db
from app.services.pokemon_service import fake_pokemon_db


client = TestClient(app)

# Test the add_pokemon function
def test_add_pokemon():
    fake_users_db.clear()
    fake_pokemon_db.clear()
    # First, register and login the user
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    response = client.post("/pokemons/pokemon", json={
        "pokedex_number": 1,
        "name": "Bulbasaur",
        "type1": "Grass",
        "type2": "Poison",
        "level": 5,
        "caught_in_game": "Red",
        "ot": "Ash",
        "shiny": False
    }, 
    headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    assert response.status_code == 201
    assert "poke_id" in response.json()
    assert "name" in response.json()
    # To be completely sure that the Pokémon was added, check the response
    assert response.json() == {
        "pokedex_number": 1,
        "name": "Bulbasaur",
        "type1": "Grass",
        "type2": "Poison",
        "level": 5,
        "caught_in_game": "Red",
        "ot": "Ash",
        "shiny": False,
        "poke_id": response.json()["poke_id"]
        }

# Test the get_pokemon function
def test_get_pokemon():
    fake_users_db.clear()
    fake_pokemon_db.clear()
    # First, register and login the user
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    token = login_response.json()["access_token"]

    # Add a Pokémon
    response = client.post("/pokemons/pokemon", json={
        "pokedex_number": 25,
        "name": "Pikachu",
        "type1": "Electric",
        "level": 10,
        "caught_in_game": "Yellow",
        "ot": "Ash",
        "shiny": False
    }, headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    # Log the response
    print(response.json())
    assert response.status_code == 201
    assert "poke_id" in response.json()
    assert "name" in response.json()
    pokedex_number = response.json()["pokedex_number"]

    # Get the Pokémon with its pokedex number
    response = client.get(f"/pokemons/pokemon/{pokedex_number}", headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    # Log the response
    print(response.json())
    assert response.status_code == 200

# Test the get_user_pokemon function
def test_get_user_pokemon():
    fake_users_db.clear()
    fake_pokemon_db.clear()
    # First, register and login the user
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    token = login_response.json()["access_token"]

    # Add first Pokémon
    response = client.post("/pokemons/pokemon", json={
        "pokedex_number": 25,
        "name": "Pikachu",
        "type1": "Electric",
        "level": 10,
        "caught_in_game": "Yellow",
        "ot": "Ash",
        "shiny": False
    }, headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})

    # Add second Pokémon
    response1 = client.post("/pokemons/pokemon", json={
        "pokedex_number": 150,
        "name": "Mewtwo",
        "type1": "Psychic",
        "level": 100,
        "caught_in_game": "Yellow",
        "ot": "Ash",
        "shiny": False
    }, headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    #print(response1.json())

    response = client.get(f"/pokemons/user/{user_id}/pokemon", headers={"Authorization": f"Bearer {token}"})#, params={"user_id": user_id})
    print(response.json())
    print(fake_pokemon_db)
    assert response.status_code == 200
    # assert it returns both pokemons
    assert response.json() == [{
        "pokedex_number": 25,
        "name": "Pikachu",
        "type1": "Electric",
        "type2": None,
        "level": 10,
        "caught_in_game": "Yellow",
        "ot": "Ash",
        "shiny": False,
        "poke_id": response.json()[0]["poke_id"]
    }, {
        "pokedex_number": 150,
        "name": "Mewtwo",
        "type1": "Psychic",
        "type2": None,
        "level": 100,
        "caught_in_game": "Yellow",
        "ot": "Ash",
        "shiny": False,
        "poke_id": response.json()[1]["poke_id"]
    }]

# Test the search_pokemon function
def test_search_pokemon():
    fake_users_db.clear()
    fake_pokemon_db.clear()
    # First, register and login the user
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    token = login_response.json()["access_token"]

    # Add a Pokémon
    client.post("/pokemons/pokemon", json={
        "pokedex_number": 1,
        "name": "Bulbasaur",
        "type1": "Grass",
        "type2": "Poison",
        "level": 5,
        "caught_in_game": "Red",
        "ot": "Ash",
        "shiny": False
    }, headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})


    response = client.get("/pokemons/search", params={"user_id": user_id, "name": "Bulbasaur"})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [{
        "pokedex_number": 1,
        "name": "Bulbasaur",
        "type1": "Grass",
        "type2": "Poison",
        "level": 5,
        "caught_in_game": "Red",
        "ot": "Ash",
        "shiny": False,
        "poke_id": response.json()[0]["poke_id"]
    }]

# Test the delete_pokemon function
def test_delete_pokemon():
    fake_users_db.clear()
    fake_pokemon_db.clear()
    # First, register and login the user
    response = client.post("/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = client.post("/users/login", data={"username": "testuser", "password": "testpass"})
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    token = login_response.json()["access_token"]

    # Add a Pokémon
    response = client.post("/pokemons/pokemon", json={
        "pokedex_number": 1,
        "name": "Bulbasaur",
        "type1": "Grass",
        "type2": "Poison",
        "level": 5,
        "caught_in_game": "Red",
        "ot": "Ash",
        "shiny": False
    }, headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    assert response.status_code == 201
    assert "poke_id" in response.json()
    poke_id = response.json()["poke_id"]

    # Delete the Pokémon
    response = client.delete(f"/pokemons/pokemon/{poke_id}", headers={"Authorization": f"Bearer {token}"}, params={"user_id": user_id})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"detail": "Pokémon deleted"}

    # Check that the Pokémon was deleted
    response = client.get(f"/pokemons/user/{user_id}/pokemon", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404
    assert response.json() == {"detail": "No Pokémon found"}