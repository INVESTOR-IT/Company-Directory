from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from loguru import logger

from app.api import organizations
from app.database.database import engine
from app.database.model import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Запуск сервера')
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info('База данных инициализирована')
    except Exception as err:
        logger.error(f'Не удалось инициализировать базу данных: {err}')
        raise
    yield
    logger.info('Завершение работы сервера')


app = FastAPI(title='Асинхронный сервис компании',
              lifespan=lifespan)


@app.middleware('http')
async def middleware(request: Request, call_next):
    logger.info(request)
    response = await call_next(request)
    return response

app.include_router(organizations.router)


@app.get('/', tags=['Root'])
async def root():
    return RedirectResponse(url='/docs')
