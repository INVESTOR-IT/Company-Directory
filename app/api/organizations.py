from fastapi import APIRouter, Body
from typing import Annotated

import app.services.organizations as org

from app.api.request_model import SearchCircle, SearchRectangle
from app.database.database import get_database
from app.database.model import Organizations, Houses, Activities

router = APIRouter()


@router.get('/start')
async def start() -> dict:
    try:
        db = next(get_database())

        activities_1_lvl = (Activities(names='Еда'), Activities(names='Автомобили'))

        for activity in activities_1_lvl:
            db.add(activity)
        db.flush()

        activities_2_lvl = (Activities(names='Мясная продукция', parent_id=activities_1_lvl[0].id),
                            Activities(names='Молочная продукция', parent_id=activities_1_lvl[0].id),
                            Activities(names='Легковые', parent_id=activities_1_lvl[1].id),
                            Activities(names='Грузовые', parent_id=activities_1_lvl[1].id))

        for activity in activities_2_lvl:
            db.add(activity)
        db.flush()

        activities_3_lvl = (Activities(names='Запчасти', parent_id=activities_2_lvl[2].id),
                            Activities(names='Аксесуары', parent_id=activities_2_lvl[2].id))

        for activity in activities_3_lvl:
            db.add(activity)
        db.flush()

        houses = (Houses(address='г. Москва, Верхняя улица, д 1', longitude=55, latitude=40),
                  Houses(address='г. Москва, Нижняя улица, д 2', longitude=50, latitude=45),
                  Houses(address='г. Москва, Правая улица, д 3', longitude=40, latitude=50),
                  Houses(address='г. Москва, Левая улица, д 4', longitude=50, latitude=40))

        for house in houses:
            db.add(house)
        db.flush()

        organizations = (Organizations(names='Мясная',
                                       phones='+71234567890;+73243432421',
                                       houses_id=houses[0].id,
                                       activities_id=activities_2_lvl[0].id
                                       ),
                         Organizations(names='Столовая',
                                       phones='+73132125412;+71231414132',
                                       houses_id=houses[1].id,
                                       activities_id=activities_1_lvl[0].id
                                       ),
                         Organizations(names='Рено',
                                       phones='+71432214132',
                                       houses_id=houses[3].id,
                                       activities_id=activities_2_lvl[2].id
                                       ),
                         Organizations(names='Все для машин',
                                       phones='+71234567890;+73243432421',
                                       houses_id=houses[2].id,
                                       activities_id=activities_3_lvl[1].id
                                       ))

        for organization in organizations:
            db.add(organization)
        db.flush()
        db.commit()

    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()

    return {'message': 'Все готово, БД пополнилась!'}


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
