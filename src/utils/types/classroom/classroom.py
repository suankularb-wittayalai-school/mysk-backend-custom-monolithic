from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from student_teacher.teacher import Teacher
from student_teacher.student import Student

# from subject.subjects import Subject
from schedule.schedule import Schedule
from student_teacher.contacts import Contact


class Classroom(BaseModel):
    id: int
    number: int
    year: int
    term: int
    students: List[Student]
    advisors: List[Teacher]
    schedule: Schedule 
    contacts: List[Contact]