from sqlalchemy.orm import Session
from typing import List
from argon2 import PasswordHasher

from . import models
from .schema.student_teacher import student, contacts
from .schema.auth import user

def create_student(db: Session, student: student.QueryStudent):
	a = student.dict()
	a.pop('contact', None); a.pop('std_id', None)
	std = models.Person(**a)
	std.prefix_th = std.prefix_th.value
	std.prefix_en = std.prefix_en.value
	db.add(std)
	db.commit()
	db.refresh(std)
	std.student_assigned = models.Student(student_id=student.std_id)
	for i in student.contact:
		i = i.dict()
		q = i.pop('type', None)
		ctc = models.Contact(**i)
		ctc.contact_type = db.query(models.ContactType).filter(models.ContactType.name == q.value).first()
		std.contact_list.append(ctc)

	db.commit()
	return student

def get_student(db: Session, std_id: str):
	person = db.query(models.Student).filter(models.Student.student_id == std_id).first()
	if person is not None:
		return person.student_extends
	return {"success":False}

def get_student_contacts(db: Session, std_id: str):
	std = db.query(models.Student).filter(models.Student.student_id == std_id).first()
	if std is not None:
		return [{"name": i.name, "value": i.value} for i in std.student_extends.contact_list]
	return {"success":False}

def update_student_contacts(db: Session, std_id: str, contact: List[contacts.QueryContact]):
	std = db.query(models.Student).filter(models.Student.student_id == std_id).first()
	if std is not None:
		person = std.student_extends
		person.contact_list = []
		for i in contact:
			i = i.dict()
			q = i.pop('type', None)
			ctc = models.Contact(**i, person=person)
			ctc.contact_type = db.query(models.ContactType).filter(models.ContactType.name == q.value).first()
			person.contact_list.append(ctc)
		db.commit()
		db.query(models.Contact).filter(models.Contact.person == None).delete(); db.commit()
		return {"success":True}
	return {"success":False}

		

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
	if not a: 
		for i in q: 
			db.add(models.ContactType(name=i["name"]))
			
	db.commit()
	return db.query(models.ContactType).all()

def register_student(db: Session, query: user.QueryUser):
	std = db.query(models.Student).filter(models.Student.student_id == query.std_id).first()
	if std is not None:
		ph = PasswordHasher()
		user = models.User(
			password=ph.hash(query.password),
			email=query.email,
			role=query.role.value,
			student=std
		)
		db.add(user)
		return user
	return {"success":False}