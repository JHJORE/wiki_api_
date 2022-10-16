from typing import List
from pydantic import BaseModel

class WikiBase(BaseModel):
    Title_Count: int
    Title : str
    
class WikiCreate(WikiBase):
    pass

class Wiki(WikiBase):
    WikiId: int
    class Config:
        orm_mode = True