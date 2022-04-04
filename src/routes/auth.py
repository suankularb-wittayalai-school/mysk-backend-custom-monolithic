from fastapi import APIRouter, Depends
from utils.response import APIResponse
from utils.response import InternalCode as ic
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
    response = auth.register_student(db, query)
    if response == 1: 
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS)
    if response == -1:
        return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_ALREADY_EXISTED, detail="object_alredy_existed")
    return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")


@AUTH.post("/teacher/register")
def create_student(query: user.QueryUserTeacher, db: Session = Depends(get_db)):
    response = auth.register_teacher(db, query)
    if response == 1: 
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS)
    if response == -1:
        return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_ALREADY_EXISTED, detail="object_alredy_existed")
    return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@AUTH.post("/token")
def login(query: user.QueryLogin, db: Session = Depends(get_db)):
    user = get_user(db=db, query=query)
    if not user:
        return APIResponse(success=False, status_code=401, internal_code=ic.IC_INVALID_CREDENTIALS, detail="invalid_credentials")
    access_token = manager.create_access_token(data=dict(email=user.email, role=user.role))
    return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS, body={"access_token": access_token, "token_type": "bearer"})
