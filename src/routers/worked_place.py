from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import WorkedPlaceSchema
import crud


worked_place_router = APIRouter()

@worked_place_router.post("/add-worked-places")
async def add_worked_places(req: WorkedPlaceSchema, db: Session = Depends(get_db)):
    result = await crud.create_worked_place(db=db, req=req)
    if result:
        return Returns.id(result)
    else:
        return Returns.NULL
    
    
@worked_place_router.get("/get-worked-places")
async def get_worked_places(student_id: int, db: Session = Depends(get_db)):
    result = await crud.read_worked_places(db=db, student_id=student_id)
    if result:
        return Returns.object(result)
    else:
        return Returns.NULL
    
    
@worked_place_router.put("/update-worked-place")
async def update_worked_place(id: int, req: WorkedPlaceSchema, db: Session = Depends(get_db)):
    result = await crud.update_worked_place(db=db, id=id, req=req)
    if result:
        return Returns.UPDATED
    else:
        return Returns.NOT_UPDATED
