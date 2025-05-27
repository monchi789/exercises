from bs4 import BeautifulSoup
import requests

data_raw = []
countries = []


def getHTMLDocument(url: str):
    response = requests.get(url)
    return response.text


def get_countries():
    url = getHTMLDocument('https://www.iban.com/country-codes')
    soup = BeautifulSoup(url, 'html.parser')

    for row in soup.select('tbody tr'):
        row_text = [x.text for x in row.find_all('td')]
        data_raw.append(row_text)


    for i in data_raw:
        countries.append({
            "country": i[0],
            "alpha2": i[1],
            "alpha3": i[2],
            "numeric": i[3]
        })
    
    return countries