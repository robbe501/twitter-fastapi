from fastapi import APIRouter
from schemas.schemas import UserSimple
from schemas import schemas
from models import models
from config import database
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from services import user_service
from auth import oauth2

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_user(request: schemas.UserAuth, db: Session = Depends(get_db)):
    return user_service.create(request, db)

@router.get('/{id}', response_model = schemas.UserWithTweets)
def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.UserAuth = Depends(oauth2.get_current_user)):
    return user_service.get_user_by_id(id, db)
