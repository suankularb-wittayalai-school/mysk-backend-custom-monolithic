from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date
from enum import Enum, IntEnum

class ContactType(str, Enum):
    """
    Contact type
    """
    Phone = "phone"
    Email = "email"
    Facebook = "facebook"
    Line = "line"
    Other = "other"

class Contact(BaseModel):
    id: str
    name: str
    type: ContactType
    value: str