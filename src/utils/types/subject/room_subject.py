from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from student_teacher.teacher import Teacher
from subject.subjects import Subject


class RoomSubject(BaseModel):
    id: int
    subject: Subject
    teachers: List[Teacher]
    coteachers: Optional[List[Teacher]] = None
    ggc_code: str
    ggc_link: str
    gg_meet_link: str