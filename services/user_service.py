
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from fastapi import HTTPException,status
from auth.hashing import Hash

def create(request: schemas.UserAuth, db:Session):
    new_user = models.User(username = request.username, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": request.username}

def get_user_by_id(user_id: int, db:Session):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} is not available")
    return user