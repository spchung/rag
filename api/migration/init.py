from src.postgres.crud import create_embedding
from src.postgres.database import SessionLocal, engine, get_db
from src.postgres.models import EmbeddingFunction
from sqlalchemy.orm import Session
import logging

db = next(get_db())

'''
Table: embedding_function
'''
EmbeddingFunction.metadata.create_all(bind=engine)

try:
  models = [
    EmbeddingFunction(
      type='huggingface',
      name='sentence-transformers/all-MiniLM-L6-v2',
      dimension=384
    ),
    EmbeddingFunction(
      type='milvus',
      name='DefaultEmbeddingFunction',
      dimension=768
    ),
  ]

  for model in models:
    create_embedding(db, model)
except Exception as e:
  logging.error(e)