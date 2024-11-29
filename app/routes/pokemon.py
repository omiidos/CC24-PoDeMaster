
from fastapi import APIRouter, HTTPException, Depends
from app.models.pokemon import Pokemon
from app.services.pokemon_service import PokemonService

router = APIRouter()
pokemon_service = PokemonService()

@router.post("/pokemon", status_code=201, summary="Add a new Pokémon", tags=["pokemon"])
async def add_pokemon(pokemon: Pokemon, user_id: str):
    try:
        pokemon = await pokemon_service.add_pokemon(user_id, pokemon)
        return pokemon 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/pokemon/{number}", summary="Get a Pokémon based on its number", tags=["pokemon"])
async def get_pokemon(user_id: str, number: int):
    pokemon = await pokemon_service.get_pokemon(user_id, number)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    return pokemon

@router.get("/user/{user_id}/pokemon", status_code=200, summary="Get all Pokémon for a user", tags=["pokemon"])
async def get_user_pokemon(user_id: str):
    # Return all Pokémon for a user
    user_pokemon = await pokemon_service.get_user_pokemon(user_id)
    if not user_pokemon:
        raise HTTPException(status_code=404, detail="No Pokémon found")
    return user_pokemon

#@router.get("/missing")
#async def get_missing_pokemon(user_id: int):
#    return pokemon_service.get_missing_pokemon(user_id)

@router.get("/search", status_code=200, summary="Search for a Pokémon by name", tags=["pokemon"])
async def search_pokemon(user_id: str, name: str):
    pokemon = await pokemon_service.search_pokemon(user_id, name)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon

@router.delete("/pokemon/{poke_id}", summary="Delete a Pokémon based on its id", tags=["pokemon"])
async def delete_pokemon(user_id: str, poke_id: str):
    try:
        await pokemon_service.delete_pokemon(user_id, poke_id) 
        return {"detail": "Pokémon deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))