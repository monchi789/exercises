from fastapi import FastAPI, HTTPException
from .utils.cache import user_cache
from .models import User
from .services.jsonplaceholder import fetch_jsonplaceholder_users
import random
from datetime import datetime, timedelta


app = FastAPI()


@app.get("/api/users", response_model=list[User])
async def get_users():
    if "users" in user_cache:
        return user_cache["users"]

    try:
        users = []
        base_users = await fetch_jsonplaceholder_users()

        for i in range(8000):
            user_template = random.choice(base_users)
            users.append({
                "id": i + 1,
                "name": user_template["name"],
                "username": f"{user_template['username']}_{i}",
                "email": f"{user_template['email'].split('@')[0]}+{i}@example.com",
                "phone": user_template["phone"],
                "company": user_template["company"]["name"],
                "subscription_tier": random.choice(["basic", "premium", "enterprise"]),
                "last_login": (datetime.utcnow() - timedelta(days=random.randint(0, 30))).isoformat()
            })
            
        user_cache["users"] = users

        return users

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))