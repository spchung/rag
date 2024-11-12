from fastapi import FastAPI
from src.api.api import api_router

app = FastAPI(
    title="Your API",
    description="Your API Description",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")