from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from subject.subjects import Subject
from student_teacher.teacher import Teacher

class ScheduleItem(BaseModel):
    id: int
    subject: Optional[Subject]
    teacher: Teacher
    coteachers: Optional[List[Teacher]] = None
    day: int
    start_time: int
    duration: int
    room: str
    

