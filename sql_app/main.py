from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/wiki/", response_model= schemas.Wiki)
def create_Company(Wiki: schemas.WikiCreate, db: Session = Depends(get_db)):
    return crud.create_Wiki(db=db, Wiki=Wiki)


@app.get("/wiki/{Wiki_id}", response_model=schemas.Wiki)
def read_Company(Wiki_id: int, db: Session = Depends(get_db)):
    db_Wiki = crud.get_Wiki(db, OrgNumber_id=Wiki_id)
    if db_Wiki is None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    return db_Wiki
    
@app.get("/wiki/{WikiTitle}", response_model=schemas.Wiki)
def read_Wiki_By_Name(WikiTitle: str, db: Session = Depends(get_db)):
    db_Wiki = crud.get_WikiByName(db, WikiTitle=WikiTitle)
    if db_Wiki is None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    return db_Wiki

