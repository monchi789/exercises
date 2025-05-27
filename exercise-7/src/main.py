from fastapi import FastAPI
from .services.scrapping import get_countries

app = FastAPI()


@app.get('/')
def hello():
    return get_countries()