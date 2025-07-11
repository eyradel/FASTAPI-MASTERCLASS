from fastapi import FastAPI,status,Response,Request,HTTPException
from fastapi.responses import JSONResponse,PlainTextResponse,RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from enum import Enum
from routers import blogs_get,blog_post,user,article,product,file
from db import models
from db.database import engine
from exceptions import StoryException
from auth import authentication
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.include_router(blogs_get.router)
app.include_router(article.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(file.router)



@app.get('/')
def index():
    return RedirectResponse(url='/docs')
@app.exception_handler(StoryException)
def story_exception_handler(request:Request,exc:StoryException):
    return JSONResponse(status_code=418,
                        content={'detail':exc.name})

@app.exception_handler(HTTPException)
def custom_handler(request:Request,exc:StoryException):
    return PlainTextResponse(str(exc),status_code=400)

models.Base.metadata.create_all(engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.mount('/files',StaticFiles(directory='files'), name='files')