from postgres.crud import create_embedding
from postgres.database import SessionLocal, engine, get_db
from postgres.models import EmbeddingFunction
from sqlalchemy.orm import Session
db = next(get_db())

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