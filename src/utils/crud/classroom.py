from sqlalchemy import and_, or_
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

def read_advisors(db: Session, room_number: str):
	classroom = db.query(models.Classroom).filter(models.Classroom.room_number == room_number).first()
	if classroom:
		a = [t.teacher_extends for t in classroom.advisors]
		a = [
			{
	            "prefix_th":r.prefix_th,
	            "prefix_en":r.prefix_en,
	            "first_name_th":r.first_name_th,
	            "middle_name_th":r.middle_name_th,
	            "last_name_th":r.last_name_th,
	            "first_name_en":r.first_name_en,
	            "middle_name_en":r.middle_name_en,
	            "last_name_en":r.last_name_en,
	            "birthdate":r.birthdate.isoformat(),
	        } for r in a
		]
		return a
	return 0

def update_advisor_in_classroom(db: Session, room_number: str, teacher_id: List[str]):
	teachers = db.query(models.Teacher).filter(or_(models.Teacher.teacher_id == t for t in teacher_id)).all()
	classroom = db.query(models.Classroom).filter(models.Classroom.room_number == room_number).first()
	if classroom:
		classroom.advisors = teachers
		db.commit()
		return teachers
	return 0

def update_classroom():
	pass

def delete_classroom(db: Session, room_number: str):
	obj = db.query(models.Classroom).filter(models.Classroom.room_number == room_number).first()
	if obj:
		db.delete(obj)
		db.commit()
		return 1
	return 0

