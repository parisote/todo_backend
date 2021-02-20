from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, func

Base = declarative_base()


class Post_it(Base):
    __tablename__ = "post_it"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(140))
    time_alarm = Column(DateTime)
    blame_timestamp = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    blame_user = Column(String(255))
