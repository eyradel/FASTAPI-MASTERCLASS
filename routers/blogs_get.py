from fastapi import APIRouter,Response,status,Depends
from enum import Enum
from routers.blog_post import required_functionality
from typing import Optional

router = APIRouter(prefix='/blogs',tags=['blog'])

class BlogType(str, Enum):
    short='short'
    story='story'
    howto='howto'



@router.get('/{id}/comment/{comment_id}',tags=['blog','comment'])
def get_comment(id:int,comment_id:int,valid:bool=True,username:Optional[str]=None):
    """
    simulates retrieving of a comment
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, username {username}'}

@router.get('/all',tags=['blog'],summary='retrieve all blogs',description='gets all blogs', response_description='get all blogs')
def get_all_blogs(page:int=1,page_size:Optional[int]=None,req_paramter:dict=Depends(required_functionality)):
    return {
        'message':f'All {page_size} blogs on page {page}',
        'req':req_paramter
        
        }

@router.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message':f'Blog type {type.value}'}


@router.get('/blog/{id}',status_code=status.HTTP_200_OK)
def get_blog(id: int,response:Response):
    if id > 6:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error ':f'blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
    return {'message':f'hello world {id}'}


