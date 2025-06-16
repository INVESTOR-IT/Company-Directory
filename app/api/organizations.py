from fastapi import APIRouter, Body
from typing import Annotated

from app.api.request_model import SearchCircle, SearchRectangle

router = APIRouter()


@router.get('/organizations_using_house/{house_id}', tags=['Organizations'])
async def get_organizations_using_house(house_id: int) -> list:
    ...


@router.get('/organizations_using_activity/{activity_id}', tags=['Organizations'])
async def get_organizations_using_activity(activity_id: int) -> list:
    ...


@router.get('/organizations_using_coordinate/', tags=['Organizations'])
async def get_organizations_using_coordinate(
        cerch_params: Annotated[SearchCircle | SearchRectangle, Body()]
) -> list:
    ...


@router.get('/organizations_using_id/{id}', tags=['Organizations'])
async def get_organizations_using_id(id: int) -> dict:
    ...


@router.get('/organizations_using_name/{name}', tags=['Organizations'])
async def get_organizations_using_name(name: str) -> dict:
    ...
