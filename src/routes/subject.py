from fastapi import APIRouter, Depends, HTTPException
from utils.response import APIResponse
from utils.response import InternalCode as ic
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
from routes.auth import manager
from utils import models

SUBJECT = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@SUBJECT.post("/create")
def create_subject():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@SUBJECT.get("/")
def read_subject():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@SUBJECT.post("/update")
def update_subject():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@SUBJECT.delete("/delete")
def delete_subject():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@SUBJECT.post("/teacher")
def read_subject_from_teacher():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@SUBJECT.post("/teacher/update")
def update_teacher_subject():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")