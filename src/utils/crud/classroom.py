from sqlalchemy.orm import Session
from typing import List
from utils import models

from utils.schema.classroom import classroom

def create_classroom(db: Session, query: classroom.QueryClassroom):
	classroom = models.Classroom(
		room_number=query.room_number,
		year=query.year,
		semester=query.semester
	)
	db.add(classroom)
	db.commit()
	db.refresh(classroom)
	return classroom

def read_classroom(room_number: str):
	pass

def update_classroom():
	pass

def delete_classroom(db: Session, room_number: str):
	obj = db.query(models.Classroom).filter(models.Classroom.room_number == room_number).first()
	if obj:
		db.delete(obj)
		db.commit()
		return 1
	return 0

