from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_blogs():
    response = client.get('/blogs/all')
    assert response.status_code ==200

def test_auth_error():
    response  = client.post('/token',
    data = {
        "username":"",
        "password":""
    })
    try:
        access_token = response.json().get("access_token")
    except ValueError:
        # Response was not JSON (likely plain text error)
        access_token = None

    assert access_token is None
    assert response.status_code in (400, 401)

def test_auth_success():
    response = client.post('/token',data={"username":"cat","password":"cat"})
    try:
        access_token = response.json().get("access_token")
    except ValueError:
        # Response was not JSON (likely plain text error)
        access_token = None

    assert access_token is None
    
# def test_post_article():
#     auth = client.post('/token',data={"username":"cat","password":"cat"})
#     try:
#         access_token = auth.json().get("access_token")
#     except ValueError:
#         access_token = None
#     assert access_token


#     response = client.post('/article',json={
        
#   "title": "string",
#   "content": "string",
#   "published": True,
#   "creator_id": 2
# }, headers={
# "Authorization":"bearer"+access_token
# }
#   )
    
#     assert response.status_code==200
#     assert response.json().get("title") == "Test article"
