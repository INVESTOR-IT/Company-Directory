from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.api import organizations
from app.database.database import get_database
from app.services.exceptions import APIError

app = FastAPI()


@app.exception_handler(APIError)
async def api_error_handler(request: Request, exc: APIError):
    '''
    Обрабатывает кастомные APIError и возвращает их в формате ErrorResponse.
    '''
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_error_response().model_dump()
    )


@app.middleware('http')
async def middleware(request: Request, call_next):
    try:
        request.state.db = next(get_database())
        response = await call_next(request)
        return response
    except Exception as err:
        request.state.db.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return APIError
    finally:
        request.state.db.close()


app.include_router(organizations.router)
