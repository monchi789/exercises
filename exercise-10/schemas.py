from pydantic import BaseModel

class Planet(BaseModel):
    nombre: str
    tipo: str
    dimension: str
    poblacion_actual: int
