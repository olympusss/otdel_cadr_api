from unittest import result
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import DetailSchema
import crud


detail_router = APIRouter()

@detail_router.get("/get-detail")
async def get_detail(student_id: int, db: Session = Depends(get_db)):
    result = await crud.read_detail(db=db, student_id=student_id)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@detail_router.post("/add-detail")
async def add_detail(req: DetailSchema, db: Session = Depends(get_db)):
    result = await crud.create_detail(db=db, req=req)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@detail_router.put("/update-detail")
async def update_detail(id: int, req: DetailSchema, db: Session = Depends(get_db)):
    result = await crud.update_detail(db=db, id=id, req=req)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED