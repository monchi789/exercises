from fastapi import FastAPI
from .api import router

app = FastAPI(title="Space Launch Analysis API")

app.include_router(router)