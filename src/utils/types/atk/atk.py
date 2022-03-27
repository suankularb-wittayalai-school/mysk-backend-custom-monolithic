from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

from student_teacher.people import People

class MethodEnum(str, Enum):
    oral = "oral"
    injection = "injection"

class AtkRecord(BaseModel):
    id: int
    tester: People
    result: bool
    date: str
    method: MethodEnum
    place: str
    evidence: str 
    