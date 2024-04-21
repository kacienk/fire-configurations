from fastapi import FastAPI

from app.endpoints.nodes import router as nodes_router


app = FastAPI()
app.include_router(nodes_router, prefix="/api/v1")
