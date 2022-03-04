from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
import crud


student_detail_router = APIRouter()

@student_detail_router.get("/get-region")
async def get_region(db: Session = Depends(get_db)):
    result = await crud.read_region(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL