from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from utils.schema.student_teacher.teacher import Teacher
from utils.schema.student_teacher.student import Student

from utils.schema.schedule.schedule import Schedule
from utils.schema.student_teacher.contacts import Contact

from utils.schema.subject.room_subject import RoomSubject


class Classroom(BaseModel):
    id: int
    number: int
    year: int
    term: int
    students: List[Student]
    advisors: List[Teacher]
    schedule: Schedule
    contacts: List[Contact]
    subjects: List[RoomSubject]

class QueryClassroom(BaseModel):
    room_number: str
    year: int
    semester: int
