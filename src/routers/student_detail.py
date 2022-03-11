from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import StudentDetailSchema
import crud


student_detail_router = APIRouter()

@student_detail_router.get("/get-region")
async def get_region(db: Session = Depends(get_db)):
    result = await crud.read_region(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@student_detail_router.get("/get-student-detail")
async def get_student_detail(student_id: int, db: Session = Depends(get_db)):
    result = await crud.read_student_detail(db=db, student_id=student_id)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@student_detail_router.post("/add-student-detail")
async def add_student_detail(req: StudentDetailSchema, db: Session = Depends(get_db)):
    result = await crud.create_student_detail(db=db, req=req)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@student_detail_router.put("/update-student-detail")
async def update_student_detail(id: int, req: StudentDetailSchema, db: Session = Depends(get_db)):
    result = await crud.update_student_detail(db=db, req=req, id=id)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED