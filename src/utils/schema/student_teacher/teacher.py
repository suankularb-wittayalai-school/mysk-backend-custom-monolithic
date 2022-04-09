from ..student_teacher.person import *

from pydantic import BaseModel
from typing import List, Optional

from ..subject.subject_group import SubjectGroup


class Teacher(BaseModel):
    """
    Teacher model
    """

    id: str
    people: Person
    teacher_id: str
    subject_groups: List[SubjectGroup]

class QueryTeacher(QueryPerson):
    prefix_th: ThaiPrefix
    prefix_en: EnglishPrefix
    teacher_id: str