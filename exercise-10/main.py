from fastapi import FastAPI, HTTPException
from schemas import Planet
import httpx

app = FastAPI()

@app.get('/')
async def main():
    return {'message': 'Hello, World!'}

@app.get('/planeta/{id_ubicacion}', response_model=Planet)
async def get_info_planet(id_ubicacion: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://rickandmortyapi.com/api/location/{id_ubicacion}')

        if response == 404:
            raise HTTPException(status_code=404, detail='Ubicación desconocida, Morty')
        
        data = response.json()

    clean_data = {
        'nombre': data['name'],
        'tipo': data['type'],
        'dimension': data['dimension'], 
        'poblacion_actual': len(data['residents'])
    }

    return clean_data