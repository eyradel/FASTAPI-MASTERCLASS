from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from auth.oauth2 import create_access_token
from db import models
from fastapi.exceptions import HTTPException
from db.hash import Hash

router = APIRouter(prefix='/auth',tags=['authentication'])


@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user  = db.query(models.DbUser).filter(models.DbUser.username==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail='Invalid credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail='Invalid credentials')
    access_token = create_access_token(data={'sub':request.username})
    return {'access_token':access_token,'token_type':'bearer'}  


