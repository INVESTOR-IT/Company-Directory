from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

import app.services.organizations as org

from app.api.request_model import SearchCircle, SearchRectangle
from app.api.response_model import Organization
from app.database.database import get_database

router = APIRouter()


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


@router.post(path='/organizations_using_coordinate',
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
