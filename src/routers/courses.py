from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
import crud
from models import CourseSchema

course_router = APIRouter()

@course_router.get("/get-courses")
async def get_courses(db: Session = Depends(get_db)):
    result = await crud.read_courses(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@course_router.post("/add-course")
async def add_course(course: CourseSchema, db: Session = Depends(get_db)):
    result = await crud.create_course(db=db, course=course)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@course_router.put("/update-course")
async def update_course(id: int, course: CourseSchema, db: Session = Depends(get_db)):
    result = await crud.update_course(db=db, course=course, id=id)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@course_router.delete("/delete-course")
async def delete_course(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_course(db=db, id=id)
    if result:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED
