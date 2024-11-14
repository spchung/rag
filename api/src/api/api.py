from fastapi import Depends, HTTPException, APIRouter
from .endpoints import embedding_function

api_router = APIRouter()

api_router.include_router(embedding_function.router)