from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

import app.services.organizations as org

from app.api.request_model import SearchCircle, SearchRectangle
from app.api.response_model import Organization
from app.database.database import get_database
from app.database.model import Organizations, Houses, Activities

router = APIRouter()


@router.get('/start')
async def start(session: Annotated[Session, Depends(get_database)]) -> dict:
    try:
        activities_1_lvl = (Activities(name='Еда'), Activities(name='Автомобили'))

        for activity in activities_1_lvl:
            session.add(activity)
        await session.flush()

        activities_2_lvl = (Activities(name='Мясная продукция', parent_id=activities_1_lvl[0].id),
                            Activities(name='Молочная продукция', parent_id=activities_1_lvl[0].id),
                            Activities(name='Легковые', parent_id=activities_1_lvl[1].id),
                            Activities(name='Грузовые', parent_id=activities_1_lvl[1].id))

        for activity in activities_2_lvl:
            session.add(activity)
        await session.flush()

        activities_3_lvl = (Activities(name='Запчасти', parent_id=activities_2_lvl[2].id),
                            Activities(name='Аксесуары', parent_id=activities_2_lvl[2].id))

        for activity in activities_3_lvl:
            session.add(activity)
        await session.flush()

        houses = (Houses(address='г. Москва, Верхняя улица, д 1', longitude=55, latitude=40),
                  Houses(address='г. Москва, Нижняя улица, д 2', longitude=50, latitude=45),
                  Houses(address='г. Москва, Правая улица, д 3', longitude=40, latitude=50),
                  Houses(address='г. Москва, Левая улица, д 4', longitude=50, latitude=40))

        for house in houses:
            session.add(house)
        await session.flush()

        organizations = (Organizations(name='Мясная',
                                       phones='+71234567890;+73243432421',
                                       houses_id=houses[0].id,
                                       activities_id=activities_2_lvl[0].id
                                       ),
                         Organizations(name='Столовая',
                                       phones='+73132125412;+71231414132',
                                       houses_id=houses[1].id,
                                       activities_id=activities_1_lvl[0].id
                                       ),
                         Organizations(name='Рено',
                                       phones='+71432214132',
                                       houses_id=houses[3].id,
                                       activities_id=activities_2_lvl[2].id
                                       ),
                         Organizations(name='Все для машин',
                                       phones='+71234567890;+73243432421',
                                       houses_id=houses[2].id,
                                       activities_id=activities_3_lvl[1].id
                                       ))

        for organization in organizations:
            session.add(organization)
        await session.flush()
        await session.commit()

    except Exception as err:
        await session.rollback()
        print(f'Ошибка: {err}')
    finally:
        await session.close()

    return {'message': 'Все готово, БД пополнилась!'}


@router.get(path='/organizations_using_house/{house_id}',
            tags=['Organizations'],
            response_model=list[Organization])
async def get_organizations_using_house(
        house_id: int,
        session: Annotated[Session, Depends(get_database)]
):
    result = await org.get_organizations_using_house(house_id, session)
    if result is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.get(path='/organizations_using_activity/{activity_id}',
            tags=['Organizations'],
            response_model=list[Organization])
async def get_organizations_using_activity(
        activity_id: int,
        session: Annotated[Session, Depends(get_database)]
):
    result = await org.get_organizations_using_activity(activity_id, session)
    if result is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.get(path='/organizations_using_coordinate',
            tags=['Organizations'])
async def get_organizations_using_coordinate(
        cerch_params: Annotated[SearchCircle | SearchRectangle, Body()],
        session: Annotated[Session, Depends(get_database)]
):
    result = await org.get_organizations_using_coordinate(cerch_params, session)
    if result is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.get(path='/organizations_using_id/{id}',
            tags=['Organizations'],
            response_model=list[Organization])
async def get_organizations_using_id(
        id: int,
        session: Annotated[Session, Depends(get_database)]
):
    result = await org.get_organizations_using_id(id, session)
    if result is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.get(path='/organizations_using_name/{name}',
            tags=['Organizations'],
            response_model=list[Organization])
async def get_organizations_using_name(
        name: str,
        session: Annotated[Session, Depends(get_database)]
):
    result = await org.get_organizations_using_name(name, session)
    if result is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return result
