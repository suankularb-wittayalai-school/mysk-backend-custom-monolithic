from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from dotenv import load_dotenv

from types.student_teacher.people import People
import os

load_dotenv()

metadata = MetaData()
engine = create_engine(os.environ.get("DATABASE_URL"))

person = Table(
    "person",
    metadata,
    Column("id", Integer, primary_key=True),
)
