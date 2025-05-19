from fastapi import FastAPI, HTTPException
from .utils.cache import user_cache
from .models import User
from .services.jsonplaceholder import fetch_jsonplaceholder_users
from .services.random_data import fetch_random_users
import random
from datetime import datetime, timedelta
import asyncio
import httpx


app = FastAPI()

async def fetch_with_retry(batch, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return await fetch_random_users(batch=batch)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429 and attempt < retries - 1:
                await asyncio.sleep(delay * (2 ** attempt))  # Exponential backoff
            else:
                raise

@app.get("/api/users", response_model=list[User])
async def get_users():
    if "users" in user_cache:
        return user_cache["users"]

    try:
        base_users = await fetch_jsonplaceholder_users()
        users = []

        for i in range(2):
            for idx, user in enumerate(base_users):
                #print(users)
                #print(idx)
                print(i)
                users.append({
                    "id": i + 1,
                    "name": user["name"],
                    "username": user["username"],
                    "email": user["email"],
                    "phone": user["phone"],
                    "company": user["company"]["name"],
                    "subscription_tier": random.choice(["basic", "premium", "enterprise"]),
                    "last_login": datetime.utcnow() - timedelta(days=random.randint(0, 30))
                })
        
        user_cache["users"] = users

        return users

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))