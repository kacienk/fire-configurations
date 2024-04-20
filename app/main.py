import os

from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI


app = FastAPI()


client = AsyncIOMotorClient(os.environ["MONGO_CONNECTION"])
db = client.get_database("configurations")
student_collection = db.get_collection("nodes")


@app.get("/nodes")
def get_node(path: str | None = None):
    return {"Hello": "World"}
