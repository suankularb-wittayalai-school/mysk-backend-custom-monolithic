from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

cors = CORSMiddleware(app, allow_origins=["*"])


@app.get("/")
def healthCheck():
    return {"status": "OK"}
