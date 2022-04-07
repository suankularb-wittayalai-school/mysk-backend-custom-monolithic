from fastapi import APIRouter, Depends, HTTPException
from utils.response import APIResponse
from utils.response import InternalCode as ic
from utils.schema.classroom.classroom import *
from utils import models, database
from utils.crud import classroom 
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List

CLASSROOM = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@CLASSROOM.post("/create")
def create_classroom(query: QueryClassroom, db: Session = Depends(get_db)):
	response = classroom.create_classroom(db, query)
	return APIResponse(success=True, status_code=201, internal_code=ic.IC_OBJECT_CREATED, body={
			"room_number": response.room_number,
			"year": response.year,
			"semester": response.semester
		})

@CLASSROOM.get("/{room_number}")
def read_classroom(room_number: str):
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@CLASSROOM.post("/update")
def update_classroom():
	return APIResponse(success=False, status_code=501, internal_code=ic.IC_FOR_FUTURE_IMPLEMENTATION, detail="for_future_implementation")

@CLASSROOM.delete("/delete")
def delete_classroom(room_number: str, db: Session = Depends(get_db)):
	response = classroom.delete_classroom(db, room_number)
	if response:
		return APIResponse(success=True, status_code=200, internal_code=ic.IC_OBJECT_DELETED)
	return APIResponse(success=False, status_code=404, internal_code=ic.IC_OBJECT_NOT_FOUND, detail="object_not_found")

