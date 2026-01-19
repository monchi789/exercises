import httpx
from schemas import PokemonClean
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/{name_pokemon}', response_model=PokemonClean)
async def get_pokemon(name_pokemon: str):
    async with httpx.AsyncClient() as client: 
        response = await client.get(f'https://pokeapi.co/api/v2/pokemon/{name_pokemon}')
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail='Pokemon not found')
        
        data = response.json()

        

    all_skills = [item['ability']['name'] for item in data['abilities']]

    clean_data = {
        'name': data['name'],
        'audio_cry': data['cries']['latest'],
        'skills': all_skills
    }

    return clean_data