from sqlalchemy import *
from sqlalchemy.orm import relationship

from .database import Base

class ContactType(Base):
	__tablename__ = "contact_type"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(50), nullable=False)

	contacts = relationship("Contact", back_populates="contact_type")

class Contact(Base):
	__tablename__ = "contact"

	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	type = Column(Integer, ForeignKey("contact_type.id"), nullable=False)
	value = Column(String(50), nullable=False)
	person = Column(Integer, ForeignKey("person.id"), nullable=False)

	contact_type = relationship("ContactType", back_populates="contacts")
	contact_assigned = relationship("Person", back_populates="contact_list")

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

	contact_list = relationship("Contact", back_populates="contact_assigned")
	student_assigned = relationship("Student", back_populates="student_extends")
	teacher_assigned = relationship("Teacher", back_populates="teacher_extends")

class Student(Base):
	__tablename__ = "student"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	student_id = Column(String)

	student_extends = relationship("Person", back_populates="student_assigned")

class Teacher(Base):
	__tablename__ = "teacher"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	teacher_id = Column(String)

	teacher_extends = relationship("Person", back_populates="teacher_assigned")

