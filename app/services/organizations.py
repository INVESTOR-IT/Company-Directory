from sqlalchemy import select, and_, func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from loguru import logger

from app.api.request_model import SearchCircle, SearchRectangle
from app.database.database import get_database
from app.database.model import Organizations, Houses, Activities


async def get_organizations_using_house(id: int, session: Session) -> list:
    try:
        statement = select(Houses).where(Houses.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail='Данного здания нет')

        statement = select(Organizations).join(Houses).where(Houses.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail='Организации в здании отсутствуют')

        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return HTTPException(status_code=500, detail='Ошибка запроса')
    finally:
        session.close()


async def get_organizations_using_activity(id: int, session: Session) -> list:
    try:
        statement = select(Activities).where(Activities.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail='Данной деятельности нет')

        statement = (select(Organizations)
                     .join(Activities)
                     .where(Activities.id == id))
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail=('Организации данной '
                                         'деятельностью не занимаются'))
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return HTTPException(status_code=500, detail='Ошибка запроса')
    finally:
        session.close()


async def get_organizations_using_coordinate(
        cerch_params: SearchCircle | SearchRectangle, session: Session) -> list:
    try:
        if isinstance(cerch_params, SearchCircle):
            result = []
            limit_height = (cerch_params.longitude - cerch_params.radius,
                            cerch_params.longitude + cerch_params.radius)
            limit_width = (cerch_params.latitude - cerch_params.radius,
                           cerch_params.latitude + cerch_params.radius)
            statement = select(Houses).where(
                and_(and_(Houses.longitude >= limit_height[0],
                          Houses.longitude <= limit_height[1]),
                     and_(Houses.latitude >= limit_width[0],
                          Houses.latitude <= limit_width[1]))
            )
            scalars_result = session.scalars(statement)
            for house in scalars_result:
                if cerch_params.radius >= (
                    (house.longitude - cerch_params.longitude) ** 2
                        + (house.latitude - cerch_params.latitude) ** 2) ** 0.5:
                    result.append(house)
        else:
            limit_height = (cerch_params.longitude - cerch_params.height,
                            cerch_params.longitude + cerch_params.height)
            limit_width = (cerch_params.latitude - cerch_params.width,
                           cerch_params.latitude + cerch_params.width)

            statement = select(Houses).where(
                and_(and_(Houses.longitude >= limit_height[0],
                          Houses.longitude <= limit_height[1]),
                     and_(Houses.latitude >= limit_width[0],
                          Houses.latitude <= limit_width[1]))
            )
            result = session.scalars(statement).all()
        if result:
            return result
        return HTTPException(status_code=204,
                             detail='В этой области нет организаций')
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return HTTPException(status_code=500, detail='Ошибка запроса')
    finally:
        session.close()


async def get_organizations_using_id(id: int, session: Session) -> list:
    try:
        statement = select(Organizations).where(Organizations.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail=('Нет данной организации'))
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return HTTPException(status_code=500, detail='Ошибка запроса')
    finally:
        session.close()


async def get_organizations_using_name(name: str, session: Session) -> list:
    try:
        statement = select(Organizations).where(Organizations.names == name)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return HTTPException(status_code=204,
                                 detail=('Нет данной организации'))
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return HTTPException(status_code=500, detail='Ошибка запроса')
    finally:
        session.close()
