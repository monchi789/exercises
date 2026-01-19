from pydantic import BaseModel

class PokemonClean(BaseModel):
    name: str
    audio_cry: str
    skills: list[str]
