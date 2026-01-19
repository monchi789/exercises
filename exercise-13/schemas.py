from pydantic import BaseModel

class Resumen(BaseModel):
    nombre: str
    idioma: str
    estado: str
    total_episodios: int
