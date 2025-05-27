from pydantic import BaseModel

class Country(BaseModel):
    country: str
    alpha2: str
    alpha3: str
    numeric: str
