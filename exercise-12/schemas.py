from pydantic import BaseModel

class Satellite(BaseModel):
    nombre: str
    latitud: float
    longitud: float
    altitud_km: float
