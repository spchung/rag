from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from postgres import crud, models, schemas
from postgres.database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/embeddings/", response_model=schemas.EmbeddingFunction)
def create_item(item: schemas.EmbeddingFunctionCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=schemas.EmbeddingFunction)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=list[schemas.EmbeddingFunction])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items