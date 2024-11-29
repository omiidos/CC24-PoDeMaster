# app/models/pokemon.py
from pydantic import BaseModel
from typing import Optional

# Pokemon model
class Pokemon(BaseModel):
    pokedex_number: int
    name: str
    type1: str
    type2: Optional[str] = None
    level: int
    caught_in_game: str
    ot: str
    shiny: bool = False  # Optional field for shiny Pokémon

class PokemonInDB(Pokemon):
    poke_id: str

# In-memory "database" for Pokémon
pokemon_db = []
