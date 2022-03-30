from fastapi import FastAPI
import uvicorn

from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

load_dotenv()

from utils.database import engine
from utils.types.student_teacher.person import QueryPerson


app = FastAPI()

cors = CORSMiddleware(app, allow_origins=["*"])

con = engine.connect()


@app.get("/")
def healthCheck():
    return {"status": "OK"}


# return people in the database if method is get
@app.get("/people")
def getPeople():
    people = con.execute("SELECT * FROM person").fetchall()
    return people


@app.post("/people")
def createPeople(person: QueryPerson):
    data = con.execute(
        """
        INSERT INTO person (prefix_th, first_name_th, middle_name_th, last_name_th, prefix_en, first_name_en, middle_name_en, last_name_en, birthdate, citizen_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        person.prefix_th.value,
        person.first_name_th,
        person.middle_name_th,
        person.last_name_th,
        person.prefix_en.value,
        person.first_name_en,
        person.middle_name_en,
        person.last_name_en,
        person.birthdate,
        person.citizen_id,
    )
    return {"status": "OK", "data": data}


if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get("HOST"), port=int(os.environ.get("PORT")))
