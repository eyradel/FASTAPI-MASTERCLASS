from fastapi import APIRouter,Depends
from schemas import UserBase,UserDisplay
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(prefix='/user',tags=['user'])

#create user
@router.post('/',response_model=UserDisplay)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)

#update user
@router.put('/{id}/update')
def update_user(id:int,request:UserBase,db:Session=Depends(get_db)):
    return db_user.update_user(db,id,request)

#delete user

@router.delete('/{id}/delete')
def delete(id:int,db:Session=Depends(get_db)):
    return db_user.delete_user(db,id)


#read all users
@router.get('/user',response_model=List[UserDisplay]) 
def get_all_users(db:Session=Depends(get_db)):
    return db_user.get_all_users(db)

#get user

@router.get('/{id}',response_model=UserDisplay)
def get_user(id:int,db:Session=Depends(get_db)):
    return db_user.get_user(db,id)
