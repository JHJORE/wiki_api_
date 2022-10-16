from aenum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Wiki(Base):
    __tablename__ = "Wiki"

    WikiId = Column(Integer, primary_key = True, index = True)
    Title = Column(String, unique = True)
    Title_Count= Column(String)