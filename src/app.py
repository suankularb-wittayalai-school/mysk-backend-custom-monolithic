from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
import os

from utils import models
from utils.database import engine

from routes.v1 import V1

load_dotenv()

app = FastAPI()

cors = CORSMiddleware(app, allow_origins=["*"])

@app.get("/")
def health_check():
    return {"success": True}

app.include_router(V1, prefix="/api/v1")
if __name__ == "__main__":
    uvicorn.run("app:app", host=os.environ.get("HOST"), port=int(os.environ.get("PORT")), reload=True)
