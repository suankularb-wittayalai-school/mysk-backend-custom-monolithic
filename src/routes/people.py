from fastapi import APIRouter, Depends, HTTPException
from utils.response import APIResponse
from utils.response import InternalCode as ic
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
    response = people.get_student(db=db, std_id=std_id)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS, body={
            "prefix_th":response.prefix_th,
            "prefix_en":response.prefix_en,
            "first_name_th":response.first_name_th,
            "middle_name_th":response.middle_name_th,
            "last_name_th":response.last_name_th,
            "first_name_en":response.first_name_en,
            "middle_name_en":response.middle_name_en,
            "last_name_en":response.last_name_en,
            "birthdate":response.birthdate.isoformat(),
            "citizen_id":response.citizen_id,
        })
    return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@PEOPLE.post("/student/add")
def create_student(person: student.QueryStudent, db: Session = Depends(get_db)):
    response = people.create_student(db, person)
    return APIResponse(status_code=201, internal_code=ic.IC_OBJECT_CREATED, body={
            "prefix_th":response.prefix_th,
            "prefix_en":response.prefix_en,
            "first_name_th":response.first_name_th,
            "middle_name_th":response.middle_name_th,
            "last_name_th":response.last_name_th,
            "first_name_en":response.first_name_en,
            "middle_name_en":response.middle_name_en,
            "last_name_en":response.last_name_en,
            "birthdate":response.birthdate.isoformat(),
            "citizen_id":response.citizen_id,
            "std_id":person.std_id
        })

@PEOPLE.get("/student/contacts/{std_id}")
def get_student_contacts(std_id: str, db: Session = Depends(get_db)):
    response = people.get_student_contacts(db, std_id)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS, body=response)
    raise APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@PEOPLE.post("/student/contacts/update")
def update_student_contacts(std_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    response = people.update_student_contacts(db, std_id, contact)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_OBJECT_UPDATED, body=contact)
    return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@PEOPLE.get("/teacher/{teacher_id}")
def get_teacher_from_teacher_id(teacher_id: str, db: Session = Depends(get_db)):
    response = people.get_teacher(db=db, teacher_id=teacher_id)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS, body={
            "prefix_th":response.prefix_th,
            "prefix_en":response.prefix_en,
            "first_name_th":response.first_name_th,
            "middle_name_th":response.middle_name_th,
            "last_name_th":response.last_name_th,
            "first_name_en":response.first_name_en,
            "middle_name_en":response.middle_name_en,
            "last_name_en":response.last_name_en,
            "birthdate":response.birthdate.isoformat(),
            "citizen_id":response.citizen_id,
        })
    return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@PEOPLE.post("/teacher/add")
def create_teacher(person: teacher.QueryTeacher, db: Session = Depends(get_db)):
    response = people.create_teacher(db, person)
    return APIResponse(status_code=201, content={
            "prefix_th":response.prefix_th,
            "prefix_en":response.prefix_en,
            "first_name_th":response.first_name_th,
            "middle_name_th":response.middle_name_th,
            "last_name_th":response.last_name_th,
            "first_name_en":response.first_name_en,
            "middle_name_en":response.middle_name_en,
            "last_name_en":response.last_name_en,
            "birthdate":response.birthdate.isoformat(),
            "citizen_id":response.citizen_id,
            "teacher_id":person.teacher_id
        })

@PEOPLE.get("/teacher/contacts/{teacher_id}")
def get_teacher_contacts(teacher_id: str, db: Session = Depends(get_db)):
    response = people.get_teacher_contacts(db, teacher_id)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_GENERIC_SUCCESS, body=response)
    raise APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

@PEOPLE.post("/teacher/contacts/update")
def update_teacher_contacts(teacher_id: str, contact: List[contacts.QueryContact], db: Session = Depends(get_db)):
    response = people.update_teacher_contacts(db, teacher_id, contact)
    if response:
        return APIResponse(status_code=200, internal_code=ic.IC_OBJECT_UPDATED, body=contact)
    raise APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

# @PEOPLE.get("/test")
# def test(db: Session = Depends(get_db)):
#     return people.create_contact_type(db=db)