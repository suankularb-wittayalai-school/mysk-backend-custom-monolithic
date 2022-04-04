from fastapi import APIRouter, Depends
from utils.schema.student_teacher import student, contacts, teacher
from utils.schema.auth import user
from utils import models, database
from utils.crud import auth
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
from fastapi_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

manager = LoginManager(os.environ.get("SECRET_KEY"), '/auth/token')
AUTH = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@manager.user_loader()
def get_user(query: user.QueryLogin, db: Session = Depends(get_db)):
    return auth.login(db=db, query=query)
# Users
@AUTH.post("/student/register")
def create_student(query: user.QueryUser, db: Session = Depends(get_db)):
    return auth.register_student(db, query)

@AUTH.post("/teacher/register")
def create_student(query: user.QueryUserTeacher, db: Session = Depends(get_db)):
    return auth.register_teacher(db, query)

@AUTH.post("/token")
def login(query: user.QueryLogin, db: Session = Depends(get_db)):
    user = get_user(db=db, query=query)
    if not user:
        return {"success":False}
    access_token = manager.create_access_token(data=dict(email=user.email, role=user.role))
    return {"success":True, "access_token": access_token, "token_type": 'bearer'}
