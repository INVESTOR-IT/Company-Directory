from fastapi import FastAPI, Request
from loguru import logger

from app.api import organizations

app = FastAPI()


@app.middleware('http')
async def middleware(request: Request, call_next):
    logger.info(request)
    response = await call_next(request)
    return response

app.include_router(organizations.router)
