import httpx

POKEMON_API = "https://pokeapi.co/api/v2"
STARTER_LIMIT = 151 # Limit to 151th pokemons

async def get_regions():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{POKEMON_API}/region")
        res.raise_for_status()
        data = res.json()

        return [region["name"] for region in data["results"]]


async def get_starter_pokemon():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{POKEMON_API}/pokemon?limit={STARTER_LIMIT}")
        res.raise_for_status()
        data = res.json()

        return [p["name"] for p in data["results"]]
