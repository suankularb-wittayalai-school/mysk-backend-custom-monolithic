from fastapi import APIRouter, Depends
# from utils.database import engine
from utils.schema.student_teacher.student import QueryStudent
from utils import models, database, crud
from utils.database import SessionLocal, engine
from sqlalchemy.orm import Session

V1 = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Users

# return people in the database if method is get
@V1.get("/studentTeacher/student/getStudentFromStdId/{std_id}", tags=["studentTeacher"])
def get_student_from_std_id(std_id: str, db: Session = Depends(get_db)):
    return crud.get_student(db=db, std_id=std_id)


@V1.post("/studentTeacher/student/add", tags=["studentTeacher"])
def create_student(person: QueryStudent, db: Session = Depends(get_db)):
    return crud.create_student(db, person)

@V1.get("/test")
def test(db: Session = Depends(get_db)):
    return crud.create_contact_type(db=db)