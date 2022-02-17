from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
import crud

course_router = APIRouter()

@course_router.get("/get-courses")
async def get_courses(db: Session = Depends(get_db)):
    result = crud.read_courses(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL