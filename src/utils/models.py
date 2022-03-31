from sqlalchemy import *
from sqlalchemy.orm import relationship

from .database import Base
from datetime import datetime

class ContactType(Base):
	__tablename__ = "contact_type"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(50), nullable=False)


class Contact(Base):
	__tablename__ = "contact"

	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	type_id = Column(Integer, ForeignKey("contact_type.id"))
	value = Column(String(50), nullable=False)
	person = Column(Integer, ForeignKey("person.id"))

	contact_type = relationship("ContactType", backref="ctc", uselist=False)

class Person(Base):
	__tablename__ = "person"

	id = Column(Integer, primary_key=True)
	prefix_th = Column(String)
	first_name_th = Column(String)
	middle_name_th = Column(String, nullable=True)
	last_name_th = Column(String)
	prefix_en = Column(String)
	first_name_en = Column(String)
	middle_name_en = Column(String, nullable=True)
	last_name_en = Column(String)
	birthdate = Column(DateTime)
	citizen_id = Column(String)

	contact_list = relationship("Contact", backref="contacts")
	student_assigned = relationship("Student", backref="student_extends", uselist=False)
	teacher_assigned = relationship("Teacher", backref="teacher_extends", uselist=False)

class Student(Base):
	__tablename__ = "student"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	student_id = Column(String)

class Teacher(Base):
	__tablename__ = "teacher"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	teacher_id = Column(String)

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	password = Column(String)
	email = Column(String)
	role = Column(String)
	# permission_gid = Column(Integer, ForeignKey("person.id"))
	student_uid = Column(Integer, ForeignKey("student.id"), nullable=True)
	teacher_uid = Column(Integer, ForeignKey("teacher.id"), nullable=True)

	last_login = Column(DateTime, nullable=True)
	last_logout = Column(DateTime, nullable=True)
	is_verified = Column(Boolean, default=False)
	is_locked = Column(Boolean, default=False)
	is_active = Column(Boolean, default=False)

	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow)

	student = relationship("Student", backref="user_assigned", uselist=False)
	teacher = relationship("Teacher", backref="user_assigned", uselist=False)