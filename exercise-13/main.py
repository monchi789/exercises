from fastapi import FastAPI, HTTPException
from schemas import Resumen
import httpx

app = FastAPI()

@app.get('/')
def main():
    return {'Hello': 'World'}


@app.get('/series/{id}')
async def get_series(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://api.tvmaze.com/shows/{id}')

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail='Serie inexistente')
        
        data = response.json()
        
        episodes = await client.get(f'https://api.tvmaze.com/shows/{id}/episodes')
    
    clean_data = {
        'nombre': data['name'],
        'idioma': data['language'],
        'estado': data['status'],
        'total_episodes': len(episodes.json())
    }

    return clean_data