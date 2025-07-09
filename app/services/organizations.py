from sqlalchemy import select, and_, func
from sqlalchemy.orm import Session
from fastapi import HTTPException
from loguru import logger

from app.api.request_model import SearchCircle, SearchRectangle
from app.database.model import Organizations, Houses, Activities
from app.services.exceptions import NotFoundError, APIError


async def get_organizations_using_house(id: int, session: Session) -> list:
    statement = select(Houses).where(Houses.id == id)
    scalars_result = session.scalars(statement).all()

    if not scalars_result:
        return NotFoundError(message='Данного здания нет')

    statement = select(Organizations).join(Houses).where(Houses.id == id)
    scalars_result = session.scalars(statement).all()
    return scalars_result


async def get_organizations_using_activity(id: int, session: Session) -> list:
    try:
        statement = select(Activities).where(Activities.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return NotFoundError(message='Данной деятельности нет')

        statement = (select(Organizations)
                     .join(Activities)
                     .where(Activities.id == id))
        scalars_result = session.scalars(statement).all()
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return APIError
    finally:
        session.close()


async def get_organizations_using_coordinate(
        cerch_params: SearchCircle | SearchRectangle, session: Session) -> list:
    try:
        if isinstance(cerch_params, SearchCircle):
            statement = select(Organizations).join(Houses).where(
                cerch_params.radius >= func.pow(
                    func.pow(Houses.longitude - cerch_params.longitude, 2) +
                    func.pow(Houses.latitude - cerch_params.latitude, 2), 0.5))
            scalars_result = session.scalars(statement).all()
        else:
            limit_height = (cerch_params.longitude - cerch_params.height,
                            cerch_params.longitude + cerch_params.height)
            limit_width = (cerch_params.latitude - cerch_params.width,
                           cerch_params.latitude + cerch_params.width)

            statement = select(Organizations).join(Houses).where(
                and_(and_(Houses.longitude >= limit_height[0],
                          Houses.longitude <= limit_height[1]),
                     and_(Houses.latitude >= limit_width[0],
                          Houses.latitude <= limit_width[1]))
            )
            scalars_result = session.scalars(statement).all()
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return APIError
    finally:
        session.close()


async def get_organizations_using_id(id: int, session: Session) -> list:
    try:
        statement = select(Organizations).where(Organizations.id == id)
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return NotFoundError(message='Нет данной организации')
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return APIError
    finally:
        session.close()


async def get_organizations_using_name(name: str, session: Session) -> list:
    try:
        statement = select(Organizations).where(func.lower(Organizations.names)
                                                .like(f'%{name.lower()}%'))
        scalars_result = session.scalars(statement).all()

        if not scalars_result:
            return NotFoundError(message='Нет данной организации')
        return scalars_result
    except Exception as err:
        session.rollback()
        logger.error(f'Ошибка запроса в БД, {err}')
        return APIError
    finally:
        session.close()
