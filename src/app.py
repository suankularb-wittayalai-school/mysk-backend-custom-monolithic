from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from utils.database import engine


app = FastAPI()

cors = CORSMiddleware(app, allow_origins=["*"])

con = engine.connect()


@app.get("/")
def healthCheck():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host=os.environ.get("HOST"), port=int(os.environ.get("PORT")))
