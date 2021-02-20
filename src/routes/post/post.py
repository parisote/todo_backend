from fastapi import APIRouter
from fastapi_sqlalchemy import db


from models import post_it as Post_it
from src.schemas.schemas_post_it import PostItCreate as SchemaPostIt
from src.schemas.schemas_post_it import PostIt

routes = APIRouter()


@routes.post("/create_post", response_model=PostIt)
async def create_post(post_it: SchemaPostIt):
    post_it_obj = Post_it.Post_it(message=post_it.message, time_alarm=post_it.time_alarm, blame_user='Automatic')
    db.session.add(post_it_obj)
    db.session.commit()
    db.session.refresh(post_it_obj)
    return post_it_obj


@routes.get("/get_post")
async def get_post():
    return db.session.query(Post_it.Post_it).all()
