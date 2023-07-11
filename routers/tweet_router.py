from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from config import database
from schemas import schemas 
from models import models
from schemas.schemas import TweetSimple
from sqlalchemy.orm import joinedload
from services import tweet_service
from auth import oauth2


router = APIRouter(
    prefix="/api/v1/tweets",
    tags=['Tweets']
)

get_db = database.get_db

@router.get('/', response_model = List[schemas.TweetWithUser])
async def get_all_tweets(db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return tweet_service.get_all_tweets(db) 

@router.post('/', status_code = status.HTTP_201_CREATED)
async def create(request: schemas.TweetSimple, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    print(current_user)
    return tweet_service.create(request, db, current_user) 

@router.delete('/{tweet_id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return tweet_service.delete(tweet_id, db)


@router.put('/{tweet_id}', status_code = status.HTTP_202_ACCEPTED)
def update(tweet_id:int, request: schemas.TweetSimple, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return tweet_service.update(tweet_id, request, db)


@router.get('/{tweet_id}', status_code = status.HTTP_200_OK)
def show(tweet_id: int, db: Session = Depends(get_db), current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    return tweet_service.get_tweet_by_id(tweet_id, db)