from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

from utils import models
from utils.database import engine

from routes import people, auth, subject, classroom

load_dotenv()

app = FastAPI()


@app.get("/")
def health_check():
    return {"success": True}

app.include_router(auth.AUTH, prefix="/api/v1/auth", tags=["auth"])
app.include_router(classroom.CLASSROOM, prefix="/api/v1/classroom", tags=["classroom"])
app.include_router(people.PEOPLE, prefix="/api/v1/people", tags=["people"])
app.include_router(subject.SUBJECT, prefix="/api/v1/subject", tags=["subject"])

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=os.environ.get("HOST"),
        port=int(os.environ.get("PORT")),
        reload=True,
    )
