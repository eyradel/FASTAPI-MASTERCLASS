from fastapi import APIRouter,Query,Body,Path
from pydantic import BaseModel
from typing import Optional,List,Dict






router = APIRouter(prefix='/blog',tags=['blog'])
class Image(BaseModel):
    url:str
    alias:str

class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool]
    nb_comments:int
    tags:List[str]=[]
    metadata:Dict[str,str]={'key','value'}
    image:Optional[Image] = None

@router.post('/new')
def create_blog(blog:BlogModel,id:int,version:int=1,comment_title:int=Path(gt=5,le=2)):
    return {
        'id':id,
        'data':blog,
        'version':version,
        'comment-title':comment_title}


@router.post('/new/{id}/comment')
def create_comment(blog:BlogModel,id:int,comment_id:int=Query
                   (None,
                    title='id of the current',
                    description='Some description for comment_id',
                    alias='comment Id',
                    deprecated=True
                ),content:str=Body(...,min_length=10,max_length=50,pattern='^[a-z\s]*$'),v:Optional[List[str]]=Query(['1','3','2'])):
    return {
        'blog':blog,
        'id':id,
        'comment_id':comment_id,
        'content':content,
        'v':v
    }

def required_functionality():
    return {'message':'learning fastapi is important'}