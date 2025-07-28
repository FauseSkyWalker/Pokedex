from app.services.pokeapi import fetch_pokemon_list
from app.services.pokeapi import fetch_pokemon_by_name_or_id

def extract_id_from_url(url):
    # Pega o ID do Pokémon a partir da URL (ex: .../pokemon/1/)
    return int(url.rstrip("/").split("/")[-1])

async def get_all_pokemon():
    raw_data = await fetch_pokemon_list(limit=20)
    results = raw_data["results"]

    refined = []
    for pokemon in results:
        poke_id = extract_id_from_url(pokemon["url"])
        refined.append({
            "name": pokemon["name"],
            "id": poke_id,
            "sprite": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
        })

    return refined

async def get_pokemon_by_name_or_id(identifier: str):
    data = await fetch_pokemon_by_name_or_id(identifier)
    
    # Formata os dados principais para resposta
    pokemon = {
        "name": data["name"],
        "id": data["id"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "sprite": data["sprites"]["front_default"]
    }

    return pokemon

async def get_pokemon_details(identifier: str):
    data = await fetch_pokemon_by_name_or_id(identifier)
    
    pokemon = {
        "name": data["name"],
        "id": data["id"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
        "sprite": data["sprites"]["front_default"]
    }
    return pokemon