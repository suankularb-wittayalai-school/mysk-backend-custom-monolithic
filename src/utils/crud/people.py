from sqlalchemy.orm import Session
from typing import List
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

from utils import models
from utils.schema.student_teacher import student, contacts, teacher
from utils.schema.auth import user

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
	return 0

def get_student_contacts(db: Session, std_id: str):
	std = db.query(models.Student).filter(models.Student.student_id == std_id).first()
	if std is not None:
		return [{"name": i.name, "type":i.contact_type, "value": i.value} for i in std.student_extends.contact_list]
	return 0

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
		return 1
	return 0

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
	return 0
def get_teacher_contacts(db: Session, teacher_id: str):
	tch = db.query(models.Teacher).filter(models.Teacher.teacher_id == teacher_id).first()
	if tch is not None:
		return [{"name": i.name, "type":i.contact_type, "value": i.value} for i in tch.teacher_extends.contact_list]
	return 0

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
		return 1
	return 0