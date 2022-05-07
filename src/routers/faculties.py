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
    
    
@faculty_router.put("/update-faculty")
async def update_faculty(id: int, faculty: FacultySchema, db: Session = Depends(get_db)):
    result = await crud.update_faculty(db=db, id=id, faculty=faculty)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@faculty_router.delete("/delete-faculty")
async def delete_faculty(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_faculty(db=db, id=id)
    if result:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED