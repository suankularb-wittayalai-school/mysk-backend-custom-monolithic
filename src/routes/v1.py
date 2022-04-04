from fastapi import APIRouter, Depends
# from utils.database import engine
from utils.schema.student_teacher import student, contacts, teacher
from utils.schema.auth import user
from utils import models, database, crud
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
from fastapi_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

manager = LoginManager(os.environ.get("SECRET_KEY"), '/auth/token')
V1 = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@manager.user_loader()
def get_user(query: user.QueryLogin, db: Session = Depends(get_db)):
    return crud.login(db=db, query=query)

# Users
@V1.post("/auth/student/register", tags=["auth"])
def create_student(query: user.QueryUser, db: Session = Depends(get_db)):
    return crud.register_student(db, query)

@V1.post("/auth/teacher/register", tags=["auth"])
def create_student(query: user.QueryUserTeacher, db: Session = Depends(get_db)):
    return crud.register_teacher(db, query)

@V1.post("/auth/token", tags=["auth"])
def login(query: user.QueryLogin, db: Session = Depends(get_db)):
    user = get_user(db=db, query=query)
    if not user:
        return {"success":False}
    access_token = manager.create_access_token(data=dict(email=user.email, role=user.role))
    return {"success":True, "access_token": access_token, "token_type": 'bearer'}

# return people in the database if method is get
@V1.get("/studentTeacher/student/{std_id}", tags=["studentTeacher"])
def get_student_from_std_id(std_id: str, db: Session = Depends(get_db)):
    return crud.get_student(db=db, std_id=std_id)

@V1.post("/studentTeacher/student/add", tags=["studentTeacher"])
def create_student(person: student.QueryStudent, db: Session = Depends(get_db)):
    return crud.create_student(db, person)

@V1.get("/studentTeacher/student/contacts/{std_id}", tags=["studentTeacher"])
def get_student_contacts(std_id: str, db: Session = Depends(get_db)):
    return crud.get_student_contacts(db, std_id)

@V1.post("/studentTeacher/student/contacts/update", tags=["studentTeacher"])
def update_student_contacts(std_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    return crud.update_student_contacts(db, std_id, contact)

@V1.get("/studentTeacher/teacher/{teacher_id}", tags=["studentTeacher"])
def get_teacher_from_teacher_id(teacher_id: str, db: Session = Depends(get_db)):
    return crud.get_teacher(db=db, teacher_id=teacher_id)

@V1.post("/studentTeacher/teacher/add", tags=["studentTeacher"])
def create_teacher(person: teacher.QueryTeacher, db: Session = Depends(get_db)):
    return crud.create_teacher(db, person)

@V1.get("/studentTeacher/teacher/contacts/{teacher_id}", tags=["studentTeacher"])
def get_teacher_contacts(teacher_id: str, db: Session = Depends(get_db)):
    return crud.get_teacher_contacts(db, teacher_id)

@V1.post("/studentTeacher/teacher/contacts/update", tags=["studentTeacher"])
def update_teacher_contacts(teacher_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    return crud.update_teacher_contacts(db, teacher_id, contact)

@V1.get("/test")
def test(db: Session = Depends(get_db)):
    return crud.create_contact_type(db=db)