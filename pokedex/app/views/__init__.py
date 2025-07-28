from fastapi import APIRouter
from app.controllers import get_all_pokemon, get_pokemon_details

pokemon_router = APIRouter()  # Cria um agrupamento de rotas

@pokemon_router.get("/")
async def list_pokemon():
    return await get_all_pokemon()

# @pokemon_router.get("/{identifier}")
# async def get_pokemon(identifier: str):
#     from app.controllers import get_pokemon_by_name_or_id
#     return await get_pokemon_by_name_or_id(identifier)

@pokemon_router.get("/{identifier}")
async def pokemon_details(identifier: str):
    return await get_pokemon_details(identifier)