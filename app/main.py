# app/main.py
from fastapi import FastAPI
from app.routes import pokemon, user

# Create FastAPI app instance
app = FastAPI()

# Include Pokémon and User routes
app.include_router(pokemon.router, prefix="/pokemons", tags=["Pokemons"])
app.include_router(user.router, prefix="/users", tags=["Users"])
