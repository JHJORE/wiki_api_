from cgitb import html
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wiki/", response_model=schemas.Wiki)
def create_Wiki(Wiki: schemas.WikiCreate, db: Session = Depends(get_db)):
    return crud.create_Wiki(db=db, Wiki=Wiki)

# @app.get("/wiki/{Wikiid}", response_model=schemas.Wiki)
# def read_Wiki(Wikiid: int, db: Session = Depends(get_db)):
#     print("success")
#     db_Wiki = crud.get_Wiki(db, Wikiid=Wikiid)
#     if db_Wiki is None:
#         raise HTTPException(status_code=404, detail="Wiki not found")
#     return db_Wiki
    
@app.get("/wiki/titles/{WikiTitle}", response_model=schemas.Wiki)
def read_Wiki_By_Name(WikiTitle: str, db: Session = Depends(get_db)):
    db_Wiki = crud.get_WikiByTitle(db, Title=WikiTitle)
    if db_Wiki is None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    return db_Wiki

