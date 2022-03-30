from sqlalchemy.orm import Session

from . import models
from .schema.student_teacher import student, contacts

def create_student(db: Session, student: student.QueryStudent):
	a = student.dict()
	a.pop('contact', None); a.pop('std_id', None)
	std = models.Person(**a)
	std.prefix_th = std.prefix_th.value
	std.prefix_en = std.prefix_en.value
	db.add(std)
	db.commit()
	db.refresh(std)
	db.add(models.Student(person_id=std.id, student_id=student.std_id))
	for i in student.contact:
		ctc = models.Contact(**i.dict(), person=std.id)
		ctc.type = ctc.type.value
		db.add(ctc)
	db.commit()
	return student

def get_student(db: Session, std_id: str):
	person = db.query(models.Student).filter(models.Student.student_id == std_id).first()
	return db.query(models.Person).filter(models.Person.id == person.person_id).first()

def create_contact_type(db: Session):
	q = [
		{"name": "Phone"},
		{"name": "Email"},
		{"name": "Facebook"},
		{"name": "Line"},
		{"name": "Instagram"},
		{"name": "Twitter"},
		{"name": "Website"},
		{"name": "Discord"},
		{"name": "Other"},
	]
	a = db.query(models.ContactType).all()
	if a == []:
		for i in q:
			db.add(models.ContactType(name=i["name"]))
			
	db.commit()
	return db.query(models.ContactType).all()