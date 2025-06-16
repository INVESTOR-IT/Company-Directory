from pydantic import BaseModel, Field


class SearchCoordinates(BaseModel):
    longitude: float = Field(ge=-180.0, le=180.0, description='Долгота точки поиска')
    latitude: float = Field(ge=-180.0, le=180.0, description='Широта точки поиска')


class SearchCircle(SearchCoordinates):
    radius: float = Field(gt=0.0, description='Радиус круга в метрах')


class SearchRectangle(SearchCoordinates):
    width: float = Field(gt=0.0, description='Ширина прямоугольника в метрах')
    height: float = Field(gt=0.0, description='Высота прямоугольника в метрах')
