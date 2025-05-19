from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone: str
    company: str
    subscription_tier: str
    last_login: datetime
