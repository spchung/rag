from sqlalchemy import Column, Integer, String
from src.database.postgres.db import Base
from sqlalchemy import UniqueConstraint

class EmbeddingFunction(Base):
    __tablename__ = "embedding_function"
    
    __table_args__ = (UniqueConstraint('type', 'name', name='_type_name_uc'),)

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    name = Column(String)
    dimension = Column(Integer)