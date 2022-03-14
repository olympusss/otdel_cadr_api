from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import ThirdDetailSchema
import crud


third_detail_router = APIRouter()

@third_detail_router.get("/get-third-detail")
async def get_third_detail(student_id: int, db: Session = Depends(get_db)):
    result = await crud.read_third_detail(db=db, student_id=student_id)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@third_detail_router.post("/add-third-detail")
async def add_third_detail(req: ThirdDetailSchema, db: Session = Depends(get_db)):
    result = await crud.create_third_detail(db=db, req=req)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@third_detail_router.put("/update-third-detail")
async def update_third_detail(id: int, req: ThirdDetailSchema, db: Session = Depends(get_db)):
    result = await crud.update_third_detail(db=db, id=id, req=req)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED