from pydantic import BaseModel
from typing import List, Optional

from student_teacher.people import People

class VaccineProvider(BaseModel):
    id: int
    name: str

class Vaccine(BaseModel):
    id: int
    taker: People
    dose: int
    provider: VaccineProvider
    date: str
    note: Optional[str]