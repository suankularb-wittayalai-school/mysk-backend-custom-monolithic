from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date
from enum import Enum, IntEnum

from .contacts import Contact, QueryContact


class ThaiPrefix(Enum):
    """
    Thai prefix for name
    """

    Master = "เด็กชาย"
    Mr = "นาย"
    Mrs = "นาง"
    Miss = "นางสาว"


class EnglishPrefix(Enum):
    """
    English prefix for name
    """

    Mr = "Mr."
    Mrs = "Mrs."
    Miss = "Miss."
    Master = "Master."


class Person(BaseModel):
    id: int
    prefix_th: ThaiPrefix
    prefix_en: EnglishPrefix
    first_name_th: str
    last_name_th: str
    middle_name_th: Optional[str]
    first_name_en: str
    last_name_en: str
    middle_name_en: Optional[str]
    birthdate: date
    citizen_id: str
    contact: List[Contact] = []
    class Config:
        orm_mode = True


class QueryPerson(BaseModel):
    prefix_th: ThaiPrefix
    prefix_en: EnglishPrefix
    first_name_th: str
    last_name_th: str
    middle_name_th: Optional[str]
    first_name_en: str
    last_name_en: str
    middle_name_en: Optional[str]
    birthdate: date
    citizen_id: str
    contact: List[QueryContact] = []
    class Config:
        orm_mode = True

