from .people import People

from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    """
    Student model
    """
    id: str
    people: People
    std_id: str