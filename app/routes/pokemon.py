# app/routes/pokemon.py
from fastapi import APIRouter
from app.models.pokemon import Pokemon, pokemon_db  # Example models and in-memory DB

router = APIRouter()

# Get all Pokémon
@router.get("/")
async def get_pokemons():
    return pokemon_db

# Create a new Pokémon
@router.post("/", status_code=201)
async def create_pokemon(pokemon: Pokemon):
    pokemon_db.append(pokemon)
    return pokemon
