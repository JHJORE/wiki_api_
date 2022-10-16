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

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@app.post("/wiki/", response_model=schemas.Wiki)
def create_Wiki(Wiki: schemas.WikiCreate, db: Session = Depends(get_db)):
    db_Wiki = crud.get_WikiByTitle(db, Title=Wiki.Title)
    if db_Wiki:
        raise HTTPException(status_code=400, detail="Page already registered")
    return crud.create_Wiki(db=db, Wiki=Wiki)



@app.get("/wiki/{Wikiid}", response_model=schemas.Wiki)
def read_Wiki(Wikiid: int, db: Session = Depends(get_db)):
    db_Wiki = crud.get_Wiki(db, Wikiid=Wikiid)
    if db_Wiki is None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    return db_Wiki
    
@app.get("/wiki/titles/{WikiTitle}", response_model=schemas.Wiki)
def read_Wiki_By_Name(WikiTitle: str, db: Session = Depends(get_db)):
    db_Wiki = crud.get_WikiByTitle(db, Title=WikiTitle)
    if db_Wiki is None:
        raise HTTPException(status_code=404, detail="Wiki not found")
    return db_Wiki

