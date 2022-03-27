from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from schedule.scheduleItem import ScheduleItem

class ScheduleRow(BaseModel):
    id: int
    day: int
    n_periods: int
    schedule_items: List[ScheduleItem]

class Schedule(BaseModel):
    id: int
    schedule_rows: List[ScheduleRow]
    year: int
    term: int