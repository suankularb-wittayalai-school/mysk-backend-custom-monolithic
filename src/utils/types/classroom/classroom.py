from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from student_teacher.teacher import Teacher
from student_teacher.student import Student

from schedule.schedule import Schedule
from student_teacher.contacts import Contact

from subject.room_subject import RoomSubject


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
