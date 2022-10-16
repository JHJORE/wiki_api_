from sqlalchemy.orm import Session
import models
import schemas

def get_Wiki(db: Session, id: int):
    return db.query(models.Wiki).filter(models.Wiki.WikiId == id).first()
    

def get_WikiByName(db: Session, CompanyName: str):
    return db.query(models.Company).filter(models.Company.CompanyName.like(f"%{CompanyName}")).first()

def create_Wiki(db: Session, Wiki: schemas.WikiCreate):
    db_Wiki = models.Wiki(OrgNumber = Wiki.Tilte, CompanyName = Wiki.Title_Count)
    db.add(db_Wiki)
    db.commit()
    db.refresh(db_Wiki)
    return db_Wiki