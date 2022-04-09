from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from utils.schema.student_teacher.teacher import Teacher
from utils.schema.subject.subjects import Subject


class RoomSubject(BaseModel):
    id: int
    subject: Subject
    teachers: List[Teacher]
    coteachers: Optional[List[Teacher]] = None
    ggc_code: str
    ggc_link: str
    gg_meet_link: str