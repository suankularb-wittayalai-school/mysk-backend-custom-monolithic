from fastapi import APIRouter, Depends
from utils.schema.student_teacher import student, contacts, teacher
from utils.schema.auth import user
from utils import models, database
from utils.crud import people 
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List

PEOPLE = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# return people in the database if method is get
@PEOPLE.get("/student/{std_id}")
def get_student_from_std_id(std_id: str, db: Session = Depends(get_db)):
    return people.get_student(db=db, std_id=std_id)

@PEOPLE.post("/student/add")
def create_student(person: student.QueryStudent, db: Session = Depends(get_db)):
    return people.create_student(db, person)

@PEOPLE.get("/student/contacts/{std_id}")
def get_student_contacts(std_id: str, db: Session = Depends(get_db)):
    return people.get_student_contacts(db, std_id)

@PEOPLE.post("/student/contacts/update")
def update_student_contacts(std_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    return people.update_student_contacts(db, std_id, contact)

@PEOPLE.get("/teacher/{teacher_id}")
def get_teacher_from_teacher_id(teacher_id: str, db: Session = Depends(get_db)):
    return people.get_teacher(db=db, teacher_id=teacher_id)

@PEOPLE.post("/teacher/add")
def create_teacher(person: teacher.QueryTeacher, db: Session = Depends(get_db)):
    return people.create_teacher(db, person)

@PEOPLE.get("/teacher/contacts/{teacher_id}")
def get_teacher_contacts(teacher_id: str, db: Session = Depends(get_db)):
    return people.get_teacher_contacts(db, teacher_id)

@PEOPLE.post("/teacher/contacts/update")
def update_teacher_contacts(teacher_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    return people.update_teacher_contacts(db, teacher_id, contact)

# @PEOPLE.get("/test")
# def test(db: Session = Depends(get_db)):
#     return people.create_contact_type(db=db)