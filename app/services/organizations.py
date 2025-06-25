from sqlalchemy import select, and_, func

from app.api.request_model import SearchCircle, SearchRectangle
from app.database.database import get_database
from app.database.model import Organizations, Houses, Activities


async def get_organizations_using_house(id: int) -> list:
    try:
        db = next(get_database())
        statement = select(Organizations).join(Houses).where(Houses.id == id)
        scalars_result = db.scalars(statement)
        return scalars_result.all()
    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()


async def get_organizations_using_activity(id: int) -> list:
    try:
        db = next(get_database())
        statement = (select(Organizations)
                     .join(Activities)
                     .where(Activities.id == id))
        scalars_result = db.scalars(statement)
        return scalars_result.all()
    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()


async def get_organizations_using_coordinate(
        cerch_params: SearchCircle | SearchRectangle) -> list:
    try:
        db = next(get_database())
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
            scalars_result = db.scalars(statement)
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
            result = db.scalars(statement)
        return result.all()

    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()


async def get_organizations_using_id(id: int) -> list:
    try:
        db = next(get_database())
        statement = select(Organizations).where(Organizations.id == id)
        scalars_result = db.scalars(statement)
        return scalars_result.all()
    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()


async def get_organizations_using_name(name: str) -> list:
    try:
        db = next(get_database())
        statement = select(Organizations).where(Organizations.names == name)
        scalars_result = db.scalars(statement)
        return scalars_result.all()
    except Exception as err:
        db.rollback()
        print(f'Ошибка: {err}')
    finally:
        db.close()
