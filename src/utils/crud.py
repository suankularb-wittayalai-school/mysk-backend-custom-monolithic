from sqlalchemy.orm import Session
from typing import List
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from . import models
from .schema.student_teacher import student, contacts, teacher
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
		ctc.contact_type = q.value
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
		return [{"name": i.name, "type":i.contact_type, "value": i.value} for i in std.student_extends.contact_list]
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
			ctc.contact_type = q.value
			person.contact_list.append(ctc)
		db.commit()
		db.query(models.Contact).filter(models.Contact.person == None).delete(); db.commit()
		return {"success":True}
	return {"success":False}

def create_teacher(db: Session, teacher: teacher.QueryTeacher):
	a = teacher.dict()
	a.pop('contact', None); a.pop('teacher_id', None)
	tch = models.Person(**a)
	tch.prefix_th = tch.prefix_th.value
	tch.prefix_en = tch.prefix_en.value
	db.add(tch)
	db.commit()
	db.refresh(tch)
	tch.teacher_assigned = models.Teacher(teacher_id=teacher.teacher_id)
	for i in teacher.contact:
		i = i.dict()
		q = i.pop('type', None)
		ctc = models.Contact(**i)
		ctc.contact_type = q.value
		tch.contact_list.append(ctc)

	db.commit()
	return teacher

def get_teacher(db: Session, teacher_id: str):
	person = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
	if person is not None:
		return person.teacher_extends
	return {"success":False}

def get_teacher_contacts(db: Session, teacher_id: str):
	tch = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
	if tch is not None:
		return [{"name": i.name, "type":i.contact_type, "value": i.value} for i in tch.teacher_extends.contact_list]
	return {"success":False}

def update_teacher_contacts(db: Session, teacher_id: str, contact: List[contacts.QueryContact]):
	tch = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
	if tch is not None:
		person = tch.teacher_extends
		person.contact_list = []
		for i in contact:
			i = i.dict()
			q = i.pop('type', None)
			ctc = models.Contact(**i, person=person)
			ctc.contact_type = q.value
			person.contact_list.append(ctc)
		db.commit()
		db.query(models.Contact).filter(models.Contact.person == None).delete(); db.commit()
		return {"success":True}
	return {"success":False}

def register_student(db: Session, query: user.QueryUser):
	std = db.query(models.Student).filter(models.Student.student_id == query.std_id).first()
	if std is not None and std.user_assigned == []:
		ph = PasswordHasher()
		user = models.User(
			password=ph.hash(query.password),
			email=query.email,
			role=query.role.value,
			student=std
		)
		db.add(user)
		db.commit()
		db.refresh(user)
		return user
	return {"success":False}

def register_teacher(db: Session, query: user.QueryUserTeacher):
	teacher = db.query(models.Teacher).filter(models.Teacher.teacher_id == query.teacher_id).first()
	if teacher is not None and teacher.user_assigned == []:
		ph = PasswordHasher()
		user = models.User(
			password=ph.hash(query.password),
			email=query.email,
			role=query.role.value,
			teacher=teacher
		)
		db.add(user)
		db.commit()
		db.refresh(user)
		return user
	return {"success":False}

def login(db: Session, query: user.QueryLogin):
	ph = PasswordHasher()
	std = db.query(models.User) \
		.join(models.Student) \
		.filter(models.User.student, 
				(models.Student.student_id == query.username) | (models.User.email == query.username)).first()
	teacher = db.query(models.User) \
		.join(models.Teacher) \
		.filter(models.User.teacher, 
				(models.Teacher.teacher_id == query.username) | (models.User.email == query.username)).first()
	if std:
		try:
			ph.verify(std.password, query.password)
			return std
		except VerificationError:
			return 0 
	elif teacher:
		try:
			ph.verify(teacher.password, query.password)
			return teacher
		except VerificationError:
			return 0 
	return 0


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