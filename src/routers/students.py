from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns 
from models import StudentSchema, FilterSchema
import crud

student_router = APIRouter()

@student_router.post("/add-student")
async def add_student(student: StudentSchema, db: Session = Depends(get_db)):
    result = await crud.create_student(db=db, student=student)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@student_router.get("/get-students")
async def get_student(page: int, limit: int, db: Session = Depends(get_db)):
    result = await crud.read_students(db=db, page=page, limit=limit)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@student_router.post("/get-filter-students")
async def get_filter_student(filter: FilterSchema, db: Session = Depends(get_db)):
    result = await crud.read_filter_students(db=db, filter=filter)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@student_router.get("/get-current-student")
async def get_current_student(id: int, db: Session = Depends(get_db)):
    result = await crud.read_current_student(db=db, id=id)
    if result:
        return Returns.object(result)
    else:
        return Returns.STUDENT_NOT_FOUND
    
    
@student_router.put("/update-student")
async def update_student(id: int, student: StudentSchema, db: Session = Depends(get_db)):
    result = await crud.update_student(db=db, id=id, student=student)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
    
@student_router.delete("/delete-student")
async def delete_student(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_student(db=db, id=id)
    if result:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED
    
    
@student_router.post("/upload-image")
async def upload_image(
        student_id: int, 
        db: Session = Depends(get_db),
        file: UploadFile = File(...)
    ):
    result = await crud.create_student_image(db=db, student_id=student_id, file=file)
    if result:
        return Returns.INSERTED
    else:
        return Returns.NOT_INSERTED