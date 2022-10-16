from sqlalchemy.orm import Session
import models
import schemas

def get_Wiki(db: Session, Wikiid: int):
    return db.query(models.Wiki).filter(models.Wiki.WikiId == Wikiid).first()
    

def get_WikiByTitle(db: Session, Title: str):
    return db.query(models.Wiki).filter(models.Wiki.Title.like(f"%{Title}")).first()

def create_Wiki(db: Session, Wiki: schemas.WikiCreate):
    db_Wiki = models.Wiki(Title=Wiki.Title, Title_Count=Wiki.Title_Count)
    db.add(db_Wiki)
    db.commit()
    db.refresh(db_Wiki)
    return db_Wiki