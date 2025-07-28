import httpx
from fastapi import HTTPException

BASE_URL = "https://pokeapi.co/api/v2"

async def fetch_pokemon_list(limit=20, offset=0):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/pokemon?limit={limit}&offset={offset}")
        return response.json()
    
async def fetch_pokemon_by_name_or_id(identifier: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/pokemon/{identifier.lower()}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Pokémon não encontrado")
        return response.json()