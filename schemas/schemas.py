from typing import List, Optional
from pydantic import BaseModel

class TweetBase(BaseModel):
    tweet_id: str
    tweet: str
    class Config():
        from_attributes = True

class UserBase(BaseModel):
    user_id: str
    username:str
    password:str
    class Config():
        from_attributes = True
        
class UserAuth(BaseModel):
    username:str
    password:str
    class Config():
        from_attributes = True
        

class TweetSimple(BaseModel):
    tweet: str
    class Config():
        from_attributes = True        
 
class UserSimple(BaseModel):
    username: str
    class Config():
        from_attributes = True
           
class TweetWithUser(BaseModel):
    tweet: str
    user: UserSimple
    class Config():
        from_attributes = True        
 
class UserWithTweets(BaseModel):
    username:str
    tweets : List[TweetSimple] = []
    class Config():
        from_attributes = True 
           
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

