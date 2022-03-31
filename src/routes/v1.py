from fastapi import APIRouter, Depends
# from utils.database import engine
from utils.schema.student_teacher import student, contacts
from utils.schema.auth import user
from utils import models, database, crud
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List

V1 = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users

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

@V1.post("/auth/student/register", tags=["auth"])
def create_student(query: user.QueryUser, db: Session = Depends(get_db)):
    return crud.register_student(db, query)

@V1.post("/auth/token", tags=["auth"])
def login():
    # TODO: please create login here, student only for now
    pass

@V1.get("/test")
def test(db: Session = Depends(get_db)):
    return crud.create_contact_type(db=db)