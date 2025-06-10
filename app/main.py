from fastapi import FastAPI

from app.api import organizations

app = FastAPI()

app.include_router(organizations.router)
