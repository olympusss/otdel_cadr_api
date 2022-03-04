from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import ParentSchema
import crud

parent_router = APIRouter()

@parent_router.get("/get-parent-status")
async def get_parent_status(db: Session = Depends(get_db)):
    result = await crud.read_parent_status(db=db)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
@parent_router.get("/get-current-parents")
async def get_cuurrent_parents(student_id: int, db: Session = Depends(get_db)):
    result = await crud.read_current_parents(db=db, student_id=student_id)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@parent_router.post("/add-parent")
async def add_parent(parent: ParentSchema,db: Session = Depends(get_db)):
    result = await crud.create_parent(db=db, parent=parent)
    if result:
        return Returns.id(result)
    else:
        return Returns.NOT_INSERTED
    
    
@parent_router.delete("/delete-parent")
async def delete_parent(id: int, db: Session = Depends(get_db)):
    result = await crud.delete_parent(db=db, id=id)
    if result:
        return Returns.DELETED
    else:
        return Returns.NOT_DELETED