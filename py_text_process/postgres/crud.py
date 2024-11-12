from sqlalchemy.orm import Session
from . import models, schemas

def get_embedding(db: Session, embedding_id: int):
  return db.query(models.EmbeddingFunction).filter(models.EmbeddingFunction.id == embedding_id).first()

def get_embeddings(db: Session, skip: int = 0, limit: int = 10):
  return db.query(models.EmbeddingFunction).offset(skip).limit(limit).all()

def create_embedding(db: Session, embedding: schemas.EmbeddingFunctionCreate):
  db_embedding = models.EmbeddingFunction(
    type=embedding.type,
    name=embedding.name, 
    dimension=embedding.dimension
  )
  db.add(db_embedding)
  db.commit()
  db.refresh(db_embedding)
  return db_embedding