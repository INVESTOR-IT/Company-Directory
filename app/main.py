from fastapi import FastAPI, Request
from loguru import logger

from app.api import organizations
from app.database.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.middleware('http')
async def middleware(request: Request, call_next):
    logger.info(request)
    response = await call_next(request)
    return response

app.include_router(organizations.router)
