# app/models/pokemon.py
from pydantic import BaseModel

# Pokemon model
class Pokemon(BaseModel):
    name: str
    type: str
    level: int
    caught_in_game: str
    shiny: bool = False  # Optional field for shiny Pokémon

# In-memory "database" for Pokémon
pokemon_db = []
