from typing import List
from schemas import ArticleBase,ArticleDisplay
from fastapi import APIRouter,Depends,Header,Cookie,Form,File,UploadFile
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from fastapi.responses import Response,HTMLResponse,PlainTextResponse

from typing import Optional,List

router = APIRouter(prefix='/product',tags=['product'])

products = ['watch','laptop','phone']


@router.post('/new')
def create_product(name:str = Form(...)):
    products.append(name)
    return products

@router.get('/all')
def get_all_products():
    data = " ".join(products)
    return Response(content=data,media_type="text/plain")


@router.get('/withheader')
def get_products(response = Response,custom_header:Optional[List[str]] = Header(None),test_cookie:Optional[str] = Cookie(None)):
    if custom_header:
        response = response.header['custom_response_header']  =", ".join(custom_header)
    # if test_cookie:
    #     response.set_cookie(key="test_cookie",value="test_cookie_value")
    return {
        'data':products,
        'custom_header':custom_header,
        'test_cookie':test_cookie
              }



@router.get('/{id}',responses={
    200:{
        "content":{
            "text/html":{
                "<div>Product not found</div>"
            }
        },
        "description":"Product not found"
        
    },
    404:{
        "content":{
            "text/plain":{
                "Product not found"
            }
        },
        "description":"Product not found"
    }

})
def get_product(id:int):
    product = products[id]
    if id > len(products):
        out = f"Product with id {id} not found"
        return PlainTextResponse(content=out,status_code=404,media_type="text/plain")
    else:
        out = f""" 
        <head>
        <style>
        .product{{
        width: 500px;
        height: 30px; 
        border: 2px solid black;
        margin-bottom: 5px;
        padding: 5px;
        }}
        </style>
        </head>
        <body>
        <div class="product">
        <h1>{product}</h1>
        </div>
        </body>
        """
    return Response(content=out,media_type="text/plain")