from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.database.postgres import crud, schemas
from src.database.postgres.db import engine, get_db

router = APIRouter(
  prefix="/embedding_function",
  tags=["embedding_function"] 
)

@router.post("/", response_model=schemas.EmbeddingFunction)
def create_embedding(embedding: schemas.EmbeddingFunctionCreate, db: Session = Depends(get_db)):
  return crud.create_embedding(db=db, embedding=embedding)

@router.get("/{embedding_id}", response_model=schemas.EmbeddingFunction)
def read_embedding(embedding_id: int, db: Session = Depends(get_db)):
  db_embedding = crud.get_embedding(db, embedding_id=embedding_id)
  if db_embedding is None:
      raise HTTPException(status_code=404, detail="Embedding not found")
  return db_embedding

@router.get("/", response_model=list[schemas.EmbeddingFunction])
def read_embeddings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  embeddings = crud.get_embeddings(db, skip=skip, limit=limit)
  return embeddings