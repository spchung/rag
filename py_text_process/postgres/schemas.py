from pydantic import BaseModel

class EmbeddingFunctionBase(BaseModel):
  type: str
  name: str
  dimension: int

class EmbeddingFunctionCreate(EmbeddingFunctionBase):
  pass

class EmbeddingFunction(EmbeddingFunctionBase):
  id: int

  class Config:
    from_attributes = True