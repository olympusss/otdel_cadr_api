from operator import imod
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
import crud
from returns import Returns

faculty_router = APIRouter()

@faculty_router.get("/get-faculties")
async def get_faculties(db: Session = Depends(get_db)):
    result = crud.read_faculties(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL