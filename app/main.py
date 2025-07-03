from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api import organizations
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


app.include_router(organizations.router)
