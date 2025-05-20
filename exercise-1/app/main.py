from fastapi import FastAPI, HTTPException
from .utils.cache import user_cache
from .models import User
import uuid
from .services.random_user import fetch_random_users


app = FastAPI()


@app.get("/api/users", response_model=list[User])
async def get_users():
    if "users" in user_cache:
        return user_cache["users"]
    
    try:
        users = []
        for i in range(10):
            base_users = await fetch_random_users()

            for user in base_users:
                users.append({
                    "uuid": str(uuid.uuid4()),
                    "gender": user["gender"],
                    "first_name": user["name"]["first"],
                    "last_name": user["name"]["last"],
                    "email": user["email"],
                    "age": user["dob"]["age"]
                })
            
            user_cache["users"] = users

        return users
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))