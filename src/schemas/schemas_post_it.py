from pydantic import BaseModel
from datetime import datetime


class PostIt(BaseModel):
    message: str
    time_alarm: datetime
    blame_user: str

    class Config:
        orm_mode = True
