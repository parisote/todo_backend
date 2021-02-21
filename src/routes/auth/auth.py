from fastapi import Depends, status, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
import os
from dotenv import load_dotenv
import rootpath

routes = APIRouter()
load_dotenv(os.path.join(rootpath.detect(), ".env"))
# SECRET = os.environ["SECRET_KEY"]
SECRET = "your-secret-key"
manager = LoginManager(SECRET, tokenUrl="/auth/login", use_cookie=True)
manager.cookie_name = "post-it"

DB = {"paris": {"password": "tomas"}}


@manager.user_loader
def load_user(username: str):
    user = DB.get(username)
    return user


@routes.post("/auth/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    user = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data=dict(sub=username)
    )
    resp = RedirectResponse(url="/private", status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp, access_token)
    return resp


@routes.get("/private")
def getPrivateendpoint(user=Depends(manager)):
    return {'user': user}
