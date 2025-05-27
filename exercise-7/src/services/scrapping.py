from bs4 import BeautifulSoup
import requests
import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "countries_cache.json"
CACHE_DURATION = timedelta(hours=24)

def getHTMLDocument(url: str):
    response = requests.get(url)
    return response.text

def get_countries():
    # Verifica si el caché existe y es válido
    if os.path.exists(CACHE_FILE):
        mtime = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
        if datetime.now() - mtime < CACHE_DURATION:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    # Si no hay caché válido, hace scraping
    url = getHTMLDocument('https://www.iban.com/country-codes')
    soup = BeautifulSoup(url, 'html.parser')
    countries = []
    for row in soup.select('tbody tr'):
        row_text = [x.text for x in row.find_all('td')]
        countries.append({
            "country": row_text[0],
            "alpha2": row_text[1],
            "alpha3": row_text[2],
            "numeric": row_text[3]
        })
    # Guarda en caché
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)
    return countries