import httpx
from fastapi import FastAPI, HTTPException
from schemas import PokemonClean

app = FastAPI()

@app.get('/pokemon/{name_pokemon}', response_model=PokemonClean)
async def main(name_pokemon: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://pokeapi.co/api/v2/pokemon/{name_pokemon}')
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail='Pokemon not found')
        data = response.json()
    
    all_skills = [item['ability']['name'] for item in data['abilities']]
    all_types = [item['type']['name'] for item in data['types']]

    clean_data = {
        'name': data['name'],
        'audio_cry': data['cries']['latest'],
        'skills': all_skills,
        'shiny_image': data['sprites']['front_shiny'],
        'elemental_types': all_types
    }

    return clean_data
