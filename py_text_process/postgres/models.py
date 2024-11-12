from sqlalchemy import Column, Integer, String
from .database import Base

class EmbeddingFunction(Base):
    __tablename__ = "embedding_function"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    name = Column(String)
    dimension = Column(Integer)