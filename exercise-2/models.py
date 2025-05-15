from pydantic import BaseModel


class Trainer(BaseModel):
    trainer_id: int
    name: str
    region: str
    starter_pokemon: str
    age: int
    email: str
    uuid: str