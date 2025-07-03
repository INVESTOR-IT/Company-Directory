from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    '''
    Общая модель для ответа об ошибке API.
    '''

    code: str = Field(..., description='Уникальный внутренний код ошибки.')
    message: str = Field(..., description='Cообщение об ошибке.')


class APIError(Exception):
    '''
    Базовый класс для всех кастомных ошибок API.
    Содержит статус код HTTP, внутренний код ошибки и сообщение.
    '''

    def __init__(
        self,
        status_code: int = 500,
        code: str = "INTERNAL_SERVER_ERROR",
        message: str = "Произошла внутренняя ошибка сервера.",
    ):
        self.status_code = status_code
        self.code = code
        self.message = message
        super().__init__(self.message)

    def to_error_response(self):
        return ErrorResponse(
            code=self.code,
            message=self.message,
        )


class BadRequestError(APIError):
    '''
    400 Bad Request: Некорректный запрос.
    '''

    def __init__(self,
                 code: str = 'BAD_REQUEST',
                 message: str = 'Некорректный запрос.'):
        super().__init__(status_code=400, code=code, message=message)


class NotFoundError(APIError):
    '''
    404 Not Found: Ресурс не найден.
    '''

    def __init__(self,
                 code: str = 'NOT_FOUND',
                 message: str = 'Ресурс не найден.'):
        super().__init__(status_code=404, code=code, message=message)
