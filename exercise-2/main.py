from fastapi import FastAPI
from models import Trainer
from services.random_user import get_all_names
from services.pokeapi import get_regions, get_starter_pokemon
from utils.generator import generate_trainers
from fastapi.responses import JSONResponse 

app = FastAPI()

@app.get("/trainers", response_model=list[Trainer])
async def get_trainers():
    names = await get_all_names(1500)
    regions, starters = await get_regions(), await get_starter_pokemon()
    trainers = generate_trainers(names, regions, starters, total=15000)

    return JSONResponse(content=trainers)