from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    username:str
    email:str
    password:str

class Article(BaseModel):
    title:str
    content:str
    publised:bool
    model_config={
        "from_attributes":True
    }


class UserDisplay(BaseModel):
    username:str
    email:str
    items:List[Article] = []
    model_config={
        "from_attributes":True
    }



class User(BaseModel):
    id:int
    username:str
    model_config={
        "from_attributes":True
    }


class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    creator_id:int


class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    model_config={
        "from_attributes":True
    }

class ProductBase(BaseModel):
    title:str
    description:str
    price:float