from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    DateTime,
    Boolean,
    Constraint,
)
from sqlalchemy import inspect
from dotenv import load_dotenv

# from types.student_teacher.person import Person
import os

load_dotenv()

metadata = MetaData()
engine = create_engine(os.environ.get("DATABASE_URL"))

contact_types = Table(
    "contact_types",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("type", String(50), nullable=False),
    Column("value", String(50), nullable=False),
)

person_contact_types = Table(
    "person_contact_types",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("person_id", Integer, ForeignKey("person.id")),
    Column("contact_type_id", Integer, ForeignKey("contact_types.id")),
)

person = Table(
    "person",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("prefix_th", String),
    Column("first_name_th", String),
    Column("middle_name_th", String, nullable=True),
    Column("last_name_th", String),
    Column("prefix_en", String),
    Column("first_name_en", String),
    Column("middle_name_en", String, nullable=True),
    Column("last_name_en", String),
    Column("birthdate", DateTime),
    Column("citizen_id", String),
)

student = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("person_id", Integer, ForeignKey("person.id")),
    Column("student_id", String),
)

teacher = Table(
    "teacher",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("person_id", Integer, ForeignKey("person.id")),
    Column("teacher_id", String),
)

metadata.create_all(engine)
