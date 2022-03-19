from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from returns import Returns
from models import SignIn, SignUp
import crud


authentication_router = APIRouter()

@authentication_router.post("/sign-up")
async def sign_up(req: SignUp, db: Session = Depends(get_db)):
    result = await crud.create_sign_up(db=db, req=req)
    if result:
        return Returns.token(result)
    else:
        return Returns.USER_EXISTS
    
    
@authentication_router.post("/sign-in")
async def sign_in(req: SignIn, db: Session = Depends(get_db)):
    result = await crud.read_sign_in(db=db, req=req)
    if result:
        return Returns.token(result["token"])
    else:
        return Returns.USER_NOT_FOUND