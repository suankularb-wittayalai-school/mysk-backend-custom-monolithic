from .person import Person

from pydantic import BaseModel
from typing import List, Optional


class Student(BaseModel):
    """
    Student model
    """

    id: str
    people: Person
    std_id: str
