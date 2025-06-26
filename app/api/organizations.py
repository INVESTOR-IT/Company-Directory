from fastapi import APIRouter, Body
from typing import Annotated

import app.services.organizations as org

from app.api.request_model import SearchCircle, SearchRectangle

router = APIRouter()


@router.get('/organizations_using_house/{house_id}', tags=['Organizations'])
async def get_organizations_using_house(house_id: int):
    '''
    Возвращает все организации находящиеся в данном здании

    Args:
        id: ID здания

    Returns: 
        Список всех организаций в этом здании'''
    return await org.get_organizations_using_house(house_id)


@router.get('/organizations_using_activity/{activity_id}', tags=['Organizations'])
async def get_organizations_using_activity(activity_id: int):
    '''
    Возвращает все организации занимающеся данной деятельностью

    Args:
        id: ID деятельности

    Returns: 
        Список всех организаций занимающеся данной деятельностью'''
    return await org.get_organizations_using_activity(activity_id)


@router.get('/organizations_using_coordinate/', tags=['Organizations'])
async def get_organizations_using_coordinate(
        cerch_params: Annotated[SearchCircle | SearchRectangle, Body()]):
    '''
    Возвращает все организации попавшие в область поиска круга/квадрата

    Args:
        cerch_params: SearchCircle или SearchRectangle

    Returns: 
        Список всех организаций в область поиска круга/квадрата'''
    return await org.get_organizations_using_coordinate(cerch_params)


@router.get('/organizations_using_id/{id}', tags=['Organizations'])
async def get_organizations_using_id(id: int):
    '''
    Возвращает организацию по указанному id 

    Args:
        id: ID орагнизации

    Returns: 
        Список организации'''
    return await org.get_organizations_using_id(id)


@router.get('/organizations_using_name/{name}', tags=['Organizations'])
async def get_organizations_using_name(name: str):
    '''
    Возвращает организацию по указанному названию

    Args:
        name: Название орагнизации

    Returns: 
        Список организации'''
    return await org.get_organizations_using_name(name)
