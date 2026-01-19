from fastapi import FastAPI
from schemas import Country
import httpx

app = FastAPI()

@app.get('/')
async def main():
    return {'Hello': 'World!'}


@app.get('/nations/{code_country}', response_model=Country)
async def nation(code_country: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://restcountries.com/v3.1/alpha/{code_country}')
        data = response.json()[0]
    
    clean_data = {
        'nombre': data['name']['common'],
        'capital': data['capital'],
        'region': data['region'],
        'poblacion': data['population']
    }

    return clean_data