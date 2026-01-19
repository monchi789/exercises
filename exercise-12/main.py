from fastapi import FastAPI, HTTPException
from schemas import Satellite
import httpx

app = FastAPI()

@app.get('/')
def main():
    return {'Hello': 'World'}

@app.get('/orbit/{satellite_id}', response_model=Satellite)
async def get_satellites(satellite_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://api.wheretheiss.at/v1/satellites/{satellite_id}')

        if response.status_code == 404:
            raise HTTPException(status_code=404, detail='Objeto fuera de seguimiento')

        data = response.json()

    clean_data = {
        'nombre': data['name'],
        'latitud': data['latitude'],
        'longitud': data['longitude'],
        'altitud_km': data['altitude']
    }
    return clean_data