# Hito 3 - PoDeMaster API

## Overview
As mentioned in Hito 2 I decided to use FastAPI for our project to allow users to perform operations such as login, registration, and functionality like trading. It relies on JWT authentication, password hashing, and an in-memory database for user storage. 
Furhtermore we chose FastAPI because it is a modern, fast, web framework for building APIs with Python 3.7+ based on standard Python type hints. It is easy to use, has automatic interactive API documentation, and is built on top of Starlette for the web parts and Pydantic for the data parts. Additionaly it is widely used and therefore has a great community support. Another argument is that it supports async/await natively for non-blocking operations.

This project uses an in-memory database for user storage, defined in `app/models/user.py`. The database (`fake_users_db`) stores user information temporarily while the application is running. For now we also use a in-memory database for pokemon storage for each user, defined in `app/models/pokemon.py`. The database (`fake_pokemon_db`) stores pokemon information temporarily while the application is running.

The PoDeMaster API allows you to manage Pokémon and users. It provides endpoints for user registration, login, adding, retrieving, searching, and deleting Pokémon. The API is built using FastAPI and provides automatic interactive API documentation with Swagger UI and ReDoc.

---
## Application Structure
The application is structured to separate the business logic from the API logic. This ensures a clean and maintainable codebase. The business logic is implemented in the `services` directory, while the API routes are defined in the `routes` directory.

- **Business Logic:** The business logic is implemented in the `services` directory. This includes functions for user registration, authentication, Pokémon management, and more. These functions interact with the in-memory databases and perform the necessary operations.
- **API Logic:** The API routes are defined in the `routes` directory. These routes handle HTTP requests and responses, and they call the appropriate business logic functions from the `services` directory.
- **Logging:** The application uses the `logging` module to log API activity. Each request and response is logged with the request method, URL, and response status code.


## API Documentation

### User Routes

#### Register User
- **URL**: `/users/register`
- **Method**: `POST`
- **Request Body**: `{"username": "string", "password": "string"}`
- **Response**: `{"username": "string", "user_id": "string"}`

#### Login User
- **URL**: `/users/login`
- **Method**: `POST`
- **Request Body**: `{"username": "string", "password": "string"}`
- **Response**: `{"access_token": "string", "token_type": "bearer"}`

### Pokémon Routes

#### Add Pokémon
- **URL**: `/pokemons/pokemon`
- **Method**: `POST`
- **Request Body**: `"pokedex_number": int, "name": "string", "type1": "str", "type2": "string (Optional)", "level": "int", "caught_in_game": "str", "ot": "str", "shiny": "boolean"`
- **Response**: `"pokedex_number": int, "name": "string", "type1": "str", "type2": "string (Optional)", "level": "int", "caught_in_game": "str", "ot": "str", "shiny": "boolean", "poke_id": "string"`

#### Get Pokémon
- **URL**: `/pokemons/pokemon/{number}`
- **Method**: `GET`
- **Response**: `"pokedex_number": "integer", "name": "string", "type1": "string", "type2": "string (optional)", "level": "integer", "caught_in_game": "string", "ot": "string", "shiny": "boolean", "poke_id": "string"`

#### Get All Pokémon for a User
- **URL**: `/pokemons/user/{user_id}/pokemon`
- **Method**: `GET`
- **Request Headers**: `Authorization: Bearer <access_token>`
- **Response**: `"pokedex_number": "integer", "name": "string", "type1": "string", "type2": "string (optional)", "level": "integer", "caught_in_game": "string", "ot": "string", "shiny": "boolean", "poke_id": "string"`

#### Search Pokémon by Name
- **URL**: `/pokemons/search`
- **Method**: `GET`
- **Request Headers**: `Authorization: Bearer <access_token>`
- **Request Parameters**: `"user_id" : "string", "name": "string"`
- **Response**: `"pokedex_number": "integer", "name": "string", "type1": "string", "type2": "string (optional)", "level": "integer", "caught_in_game": "string", "ot": "string", "shiny": "boolean", "poke_id": "string"`

#### Delete Pokémon by
- **URL**: `/pokemons/pokemon/{poke_id}`
- **Method**: `DELETE`
- **Request Headers**: `Authorization: Bearer <access_token>`
- **Request Parameters**: `"user_id" : "string", "poke_id": "string"`
- **Response**: `"detail": "Pokémon deleted"`


## Testing and Running
To run the tests, use the following command in the root directory:
`pytest`

To start the application, use the following command in the root directory: 
`python -m uvicorn app.main:app --reload`
