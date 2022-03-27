from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

from student_teacher.person import Person


class ATKMethodEnum(str, Enum):
    oral = "oral"
    rt = "rtpcr"
    nasal = "nasal"
    other = "other"


class AtkRecord(BaseModel):
    id: int
    tester: Person
    result: bool
    date: str
    method: ATKMethodEnum
    place: str
    evidence: str
