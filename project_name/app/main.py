import uvicorn
from fastapi import FastAPI

from project_name.config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello world"}


@app.get("/config/")
async def config():
    return settings


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
