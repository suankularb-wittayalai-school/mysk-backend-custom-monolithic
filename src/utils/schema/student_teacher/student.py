from .person import Person, QueryPerson
from .contacts import QueryContact

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import date, datetime

class StudentThaiPrefix(Enum):
    """
    Thai prefix for student's name (our school is a boy's school)
    """

    Master = "เด็กชาย"
    Mr = "นาย"

class StudentEnglishPrefix(Enum):
    """
    English prefix for student's name (our school is a boy's school)
    """
    Master = "Master."
    Mr = "Mr."
    

class Student(Person):
    """
    Student model
    """
    prefix_th: StudentThaiPrefix
    prefix_en: StudentEnglishPrefix
    std_id: str

class QueryStudent(QueryPerson):
    prefix_th: StudentThaiPrefix
    prefix_en: StudentEnglishPrefix
    std_id: str