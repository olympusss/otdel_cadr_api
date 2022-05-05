from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
import crud
from returns import Returns
from models import FacultySchema

faculty_router = APIRouter()

@faculty_router.get("/get-faculties")
async def get_faculties(db: Session = Depends(get_db)):
    result = await crud.read_faculties(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@faculty_router.post("/add-faculty")
async def add_faculty(faculty: FacultySchema, db: Session = Depends(get_db)):
    result = await crud.create_faculty(db=db, faculty=faculty)
    if result:
        return Returns.id(result)
    else:
        return Returns.NULL