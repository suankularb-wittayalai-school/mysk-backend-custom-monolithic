
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os

# load_dotenv()

# DATABASE_URL = os.environ.get("DATABASE_URL")

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
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
from enum import Enum
from dotenv import load_dotenv
import os

# from utils.types.student_teacher.contacts import ContactType

# from types.student_teacher.person import Person

load_dotenv()

metadata = MetaData()
engine = create_engine(
    os.environ.get("DATABASE_URL"), connect_args={"check_same_thread": False}
)

contact_type = Table(
    "contact_type",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
)

contact = Table(
    "contact",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("type", Integer, ForeignKey("contact_type.id"), nullable=False),
    Column("value", String(50), nullable=False),
)

person_contact_types = Table(
    "person_contact_types",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("person_id", Integer, ForeignKey("person.id")),
    Column("contact_type_id", Integer, ForeignKey("contact.id")),
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

# add contact type to database if none exits

# query current contact types
contact_types = engine.execute("SELECT * FROM contact_type").fetchall()

if contact_types == []:
    # add contact types
    engine.execute(
        contact_type.insert(),
        [
            {"name": "Phone"},
            {"name": "Email"},
            {"name": "Facebook"},
            {"name": "Line"},
            {"name": "Instagram"},
            {"name": "Twitter"},
            {"name": "Website"},
            {"name": "Discord"},
            {"name": "Other"},
        ],
    )