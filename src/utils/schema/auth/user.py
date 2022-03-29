from student_teacher.student import Student
from student_teacher.teacher import Teacher


from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime

class Permission(BaseModel):
    """
    Permission model
    """
    id: str
    name: str
    description: Optional[str]

class PermissionGroup(BaseModel):
    """
    Permission group model
    """
    id: str
    name: str
    description: Optional[str]
    permissions: List[Permission]

class RoleChoice(str, Enum):
    """
    Role choice
    """
    student = "student"
    teacher = "teacher"

class User(BaseModel):
    """
    User model
    """
    id: str
    password : str
    email: str
    role: str
    permission: PermissionGroup
    student: Optional[Student]
    teacher: Optional[Teacher]

    last_login: Optional[datetime]
    last_logout: Optional[datetime]
    is_verified: bool
    is_locked: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime


    

    
    