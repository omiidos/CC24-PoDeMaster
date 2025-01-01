import requests

def test_api():
    # Test the root endpoint
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Pokémon API!",
                               "details": "This API allows you to manage Pokémon and users. Navigate to /docs for the Swagger UI or /redoc for the ReDoc UI."}

    # Test adding a Pokémon
    response = requests.post("http://localhost:8000/users/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    assert "user_id" in response.json()
    user_id = response.json()["user_id"]

    login_response = requests.post("http://localhost:8000/users/login", data={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    # Send the request to add a Pokémon
    response = requests.post("http://localhost:8000/pokemons/pokemon", json={
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

    # Assertions for the response
    assert response.status_code == 201
    assert "poke_id" in response.json()
    assert "name" in response.json()

    # Verify that the response matches the Pokémon data you added
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



    # Test retrieving the Pokémon
    poke_id = response.json()["poke_id"]
    get_pokemon_response = requests.get(f"http://localhost:8000/pokemons/pokemon/1", 
                                        headers={"Authorization": f"Bearer {token}"},
                                        params={"user_id": user_id})
    assert get_pokemon_response.status_code == 200
