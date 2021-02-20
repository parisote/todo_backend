from pydantic import BaseModel
from datetime import datetime


class PostItBase(BaseModel):
    message: str
    time_alarm: datetime
    blame_user: str


class PostItCreate(PostItBase):
    message: str
    time_alarm: datetime
    blame_user: str


class PostIt(PostItBase):
    message: str
    time_alarm: datetime
    blame_user: str

    class Config:
        orm_mode = True
