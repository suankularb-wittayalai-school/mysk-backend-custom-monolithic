from sqlalchemy import *
from sqlalchemy.orm import relationship

from .database import Base
from datetime import datetime

schedule_teacher_assoc = Table(
		"schedule_teacher_assoc",
		Base.metadata,
		Column("schedule_id", ForeignKey("schedule_item.id")),
		Column("teacher_id", ForeignKey("teacher.id"))
)

subject_teacher_assoc = Table(
		"subject_teacher_assoc",
		Base.metadata,
		Column("subject_id", ForeignKey("subject.id")),
		Column("teacher_id", ForeignKey("teacher.id"))
)

subject_co_teacher_assoc = Table(
		"subject_co_teacher_assoc",
		Base.metadata,
		Column("subject_id", ForeignKey("subject.id")),
		Column("teacher_id", ForeignKey("teacher.id"))
)

subject_sgroup_assoc = Table(
		"subject_sgroup_assoc",
		Base.metadata,
		Column("subject_id", ForeignKey("subject.id")),
		Column("subject_group_id", ForeignKey("subject_group.id"))
)

teacher_sgroup_assoc = Table(
		"teacher_sgroup_assoc",
		Base.metadata,
		Column("teacher_id", ForeignKey("teacher.id")),
		Column("subject_group_id", ForeignKey("subject_group.id"))
)

schedule_item_teacher_assoc = Table(
		"schedule_item_teacher_assoc",
		Base.metadata,
		Column("schedule_item_id", ForeignKey("schedule_item.id")),
		Column("teacher_id", ForeignKey("teacher.id")),
)
class Contact(Base):
	__tablename__ = "contact"

	id = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	value = Column(String(50), nullable=False)
	person = Column(Integer, ForeignKey("person.id"))

	room_id = Column(Integer, ForeignKey("classroom.id"))
	contact_type = Column(String(50), nullable=False)

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

	def __repr__(self):
		return f"{self.prefix_th} {self.first_name_th} {self.middle_name_th} {self.last_name_th}"
		
class Student(Base):
	__tablename__ = "student"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	student_id = Column(String)
	room_id = Column(Integer, ForeignKey("classroom.id"))

	def __repr__(self):
		return f"{self.student_id}"

class Teacher(Base):
	__tablename__ = "teacher"
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	teacher_id = Column(String)
	room_id = Column(Integer, ForeignKey("classroom.id"))
	group = relationship("SubjectGroup", secondary=teacher_sgroup_assoc)

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

class Classroom(Base):
	__tablename__ = "classroom"
	id = Column(Integer, primary_key=True)
	room_number = Column(String)
	year = Column(Integer)
	semester = Column(Integer)

	students = relationship("Student", backref="room_assigned")
	advisors = relationship("Teacher", backref="room_assigned")
	contacts = relationship("Contact", backref="room_assigned")

class Schedule(Base):
	__tablename__ = "schedule"
	id = Column(Integer, primary_key=True)
	schedule_rows = relationship("ScheduleRow", backref="schedule_table")
	year = Column(Integer)
	semester = Column(Integer)

class ScheduleRow(Base):
	__tablename__ = "schedule_row"
	id = Column(Integer, primary_key=True)
	schedule_uid = Column(Integer, ForeignKey("schedule.id"))
	day = Column(Integer)
	n_periods = Column(Integer)
	schedule_items = relationship("ScheduleItem", backref="schedule_row")

class ScheduleItem(Base):
	__tablename__ = "schedule_item"
	id = Column(Integer, primary_key=True)
	schedule_row_uid = Column(Integer, ForeignKey("schedule_row.id"))
	teacher_uid = Column(Integer, ForeignKey("teacher.id"))
	day = Column(Integer)
	start_time = Column(Integer)
	duration = Column(Integer)
	room = Column(String)

	teacher = relationship("Teacher", secondary=schedule_item_teacher_assoc)
	co_teacher = relationship("Teacher", secondary=schedule_teacher_assoc)

class SubjectGroup(Base):
	__tablename__ = "subject_group"
	id = Column(Integer, primary_key=True)
	subject_uid = Column(Integer, ForeignKey("subject.id"))
	name_th = Column(String)
	name_en = Column(String)

class Subject(Base):
	__tablename__ = "subject"
	id = Column(Integer, primary_key=True)
	name_th = Column(String)
	name_en = Column(String)
	subject_code_th = Column(String)
	subject_code_en = Column(String)
	subject_type_th = Column(String)
	subject_type_en = Column(String)
	credit = Column(Float)
	teacher = relationship("Teacher", secondary=subject_teacher_assoc)
	co_teacher = relationship("Teacher", secondary=subject_co_teacher_assoc)
	description_th = Column(String)
	description_en = Column(String)
	year = Column(Integer)
	semester = Column(Integer)
	group = relationship("SubjectGroup", secondary=subject_sgroup_assoc)
	syllabus = Column(String)