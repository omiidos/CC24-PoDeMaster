from app.models.pokemon import Pokemon, PokemonInDB
import uuid

# In-memory Pokémon storage for demonstration purposes
fake_pokemon_db = {}

class PokemonService:

    # Add a Pokémon to the user's collection
    async def add_pokemon(self, user_id: str, pokemon: Pokemon) -> PokemonInDB:
        pokemon_id = str(uuid.uuid4())
        pokemon_entry = PokemonInDB(**pokemon.model_dump(), poke_id=pokemon_id)
        if user_id not in fake_pokemon_db:
            fake_pokemon_db[user_id] = []
        fake_pokemon_db[user_id].append(pokemon_entry)
        return pokemon_entry

    # Get a Pokémon based on its number
    async def get_pokemon(self, user_id: str, number: int):
        user_pokemon = fake_pokemon_db.get(user_id, [])
        matching_pokemon = [pokemon for pokemon in user_pokemon if pokemon.pokedex_number == number]
        if not matching_pokemon:
            return None
        return matching_pokemon

    # Get all Pokémon for a user
    async def get_user_pokemon(self, user_id: str):
        return fake_pokemon_db.get(user_id, [])

    # Search for a Pokémon by name
    async def search_pokemon(self, user_id: str, name: str):
        user_pokemon = fake_pokemon_db.get(user_id, [])
        matching_pokemon = [pokemon for pokemon in user_pokemon if pokemon.name.lower() == name.lower()]
        if not matching_pokemon:
            return None
        return matching_pokemon
    
    # Delete a Pokémon based on its id from users collection
    async def delete_pokemon(self, user_id: str, poke_id: str):
        user_pokemon = fake_pokemon_db.get(user_id, [])
        for pokemon in user_pokemon:
            if pokemon.poke_id == poke_id:
                user_pokemon.remove(pokemon)
                return True
        raise ValueError("Pokémon not found")
    
    async def count_unique_pokemon(self, user_id: str) -> int:
        user_pokemon = fake_pokemon_db.get(user_id, [])
        unique_pokemon_numbers = {pokemon.pokedex_number for pokemon in user_pokemon}
        return len(unique_pokemon_numbers)

    
    async def get_ordered_pokemon(self, user_id: str):
        user_pokemon = fake_pokemon_db.get(user_id, [])
        return sorted(user_pokemon, key=lambda pokemon: pokemon.pokedex_number)
    
    async def get_pokedex_completion_percentage(self, user_id: str) -> dict:
        unique_pokemon_count = await self.count_unique_pokemon(user_id)
        unique_percentage = (unique_pokemon_count / 1025) * 100
        return {
            "unique_pokemon_count": unique_pokemon_count,
            "max_pokemon_count": 1025,
            "unique_pokedex_completion_percentage": unique_percentage
        }