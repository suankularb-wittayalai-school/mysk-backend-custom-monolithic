from pydantic import BaseModel
from typing import List, Optional


class SubjectGroup(BaseModel):
    id: int
    name_th: str
    name_en: str
