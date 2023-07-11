# models.py

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from config.database import Base

from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


    
class User(Base):
    __tablename__ = "user"
    
    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    
    tweets: Mapped[List["Tweet"]] = relationship(back_populates="user")
    
class Tweet(Base):
    __tablename__ = "tweet"
    
    tweet_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tweet = Column(String(140)) 
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))  
    
    user: Mapped["User"] = relationship(back_populates="tweets")
     
    
