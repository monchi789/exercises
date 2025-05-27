from fastapi import FastAPI, Query
from .services.scrapping import get_countries
from .models.country import Country


app = FastAPI()


@app.get('/countries', response_model=list[Country])
def countries(
    country: str = Query(None),
    alpha2: str = Query(None), 
    alpha3: str = Query(None),
    numeric: str = Query(None),
):
    countries = get_countries()

    if country:
        countries = [c for c in countries if country.lower() in c['country'].lower()]
    
    if alpha2:
        countries = [c for c in countries if alpha2.lower() in c['alpha2'].lower()]
    
    if alpha3:
        countries = [c for c in countries if alpha3.lower() in c['alpha3'].lower()]
    
    if numeric:
        countries = [c for c in countries if numeric.lower() in c['numeric'].lower()]
    
    
    return countries