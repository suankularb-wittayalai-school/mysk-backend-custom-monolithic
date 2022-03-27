from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from student_teacher.teacher import Teacher
from subject.subject_group import SubjectGroup

class SubjectTypesTH(str, Enum):
    """
    SubjectTypes
    """
    core = "รายวิชาพื้นฐาน"
    elective = "วิชาเลือก"
    additional = "วิชาเพิ่มเติม"
    development = "กิจกรรมพัฒนาผู้เรียน"

# I named this myself so idk if it is official
class SubjectTypesEN(str, Enum):
    """
    SubjectTypes
    """
    core = "Core"
    elective = "Elective"
    additional = "Additional"
    development = "Activity and Development"

class Subject(BaseModel):
    id: int
    name_th: str
    name_en: str
    code_th: str
    code_en: str
    type_th: SubjectTypesTH # รายวิชาเพิ่มเติม | รายวิชาพื้นฐาน | กิจกรรมพัฒนาผู้เรียน | วิชาเลือก
    type_en: SubjectTypesEN 
    credit: float
    # this include every teacher who teach this subject
    teacher: List[Teacher]
    coteachers: Optional[List[Teacher]] = None 

    description_th: Optional[str]
    description_en: Optional[str]
    year: int
    semester: int
    group: SubjectGroup
    syllabus: Optional[str] # url to the syllabus
