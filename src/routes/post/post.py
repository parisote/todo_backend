from fastapi import APIRouter
from fastapi_sqlalchemy import db


from models.post_it import Post_it as ModelPostIt
from src.schemas.schemas_post_it import PostIt

routes = APIRouter()


@routes.post("/create_post", response_model=PostIt)
async def create_post(post_it: PostIt):
    post_it_obj = ModelPostIt(message=post_it.message, time_alarm=post_it.time_alarm, blame_user='Automatic')
    db.session.add(post_it_obj)
    db.session.commit()
    db.session.refresh(post_it_obj)
    return post_it_obj


@routes.get("/get_post")
async def get_post():
    return db.session.query(ModelPostIt).all()
