from sqlalchemy.orm import Session
from typing import List
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from utils import models
from utils.schema.student_teacher import student, contacts, teacher
from utils.schema.auth import user

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

# def create_contact_type(db: Session):
# 	q = [
# 		{"name": "Phone"},
# 		{"name": "Email"},
# 		{"name": "Facebook"},
# 		{"name": "Line"},
# 		{"name": "Instagram"},
# 		{"name": "Twitter"},
# 		{"name": "Website"},
# 		{"name": "Discord"},
# 		{"name": "Other"},
# 	]
# 	a = db.query(models.ContactType).all()
# 	if not a: 
# 		for i in q: 
# 			db.add(models.ContactType(name=i["name"]))
			
# 	db.commit()
# 	return db.query(models.ContactType).all()