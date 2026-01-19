from pydantic import BaseModel

class Country(BaseModel):
    nombre: str
    capital: list[str]
    region: str
    poblacion: int
