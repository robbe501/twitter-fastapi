from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.database import get_db, db_engine
from models import models
from routers import tweet_router, user_router, auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
   "http://192.168.211.:8000",
   "http://localhost",
   "http://localhost:3000",
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
models.Base.metadata.create_all(db_engine)

app.include_router(tweet_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)



