from pydantic import BaseModel

class Corditane(BaseModel):
    lat: str
    lon: str
    