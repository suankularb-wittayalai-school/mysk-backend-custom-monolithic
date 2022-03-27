from .people import People

from pydantic import BaseModel
from typing import List, Optional

from subject.subject_group import SubjectGroup

class Teacher(BaseModel):
    """
    Teacher model
    """
    id: str
    people: People
    teacher_id: str
    subject_groups: List[SubjectGroup]