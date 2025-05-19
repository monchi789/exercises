from pydantic import BaseModel, EmailStr


class User(BaseModel):
    uuid: str
    gender: str
    first_name: str
    last_name: str
    email: EmailStr
    age: int