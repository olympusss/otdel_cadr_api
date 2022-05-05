from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import DeanSchema
import crud


dean_router = APIRouter()

@dean_router.post("/add-dean")
async def add_dean(dean: DeanSchema, db: Session = Depends(get_db)):
    result = await crud.create_dean(db=db, dean=dean)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@dean_router.get("/get-deans")
async def get_deans(db: Session = Depends(get_db)):
    result = await crud.read_deans(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@dean_router.put("/update-dean")
async def update_dean(id: int, dean: DeanSchema, db: Session = Depends(get_db)):
    result = await crud.update_dean(db=db, dean=dean, id=id)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
    
@dean_router.delete("/delete-dean")
async def delete_dean(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_dean(db=db, id=id)
    if result:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED