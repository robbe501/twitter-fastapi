from models import models
from schemas import schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all_tweets(db: Session):
    return db.query(models.Tweet).all()

def create(request: schemas.TweetBase, db: Session, current_user):
    user = db.query(models.User).filter(models.User.username == current_user.username).first()
    new_tweet = models.Tweet(tweet = request.tweet, user_id = user.user_id)
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return schemas.TweetBase(tweet_id = str(new_tweet.tweet_id), tweet = request.tweet)


def delete(tweet_id: int, db: Session):
    tweet = db.query(models.Tweet).filter(models.Tweet.tweet_id == tweet_id)

    if not tweet.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Tweet with id {tweet_id} not found")

    tweet.delete(synchronize_session=False)
    db.commit()
    return {"message": "Tweet deleted"}

def update(tweet_id: int, request: schemas.TweetSimple, db: Session):
    tweet = db.query(models.Tweet).filter(models.Tweet.tweet_id == tweet_id)

    if not tweet.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Tweet with id {tweet_id} not found")

    tweet.update({"tweet": request.tweet})
    db.commit()
    return {"message": "Tweet updated"}

def get_tweet_by_id(tweet_id: int, db: Session):
    tweet = db.query(models.Tweet).filter(models.Tweet.tweet_id == tweet_id).first()
    if not tweet:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Tweet with the id {tweet_id} is not available")
    return tweet 