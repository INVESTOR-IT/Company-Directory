from fastapi import APIRouter


router = APIRouter()


@router.get('/organizations_using_house/{house}', tags=['Organizations'])
async def get_organizations_using_house(house: str) -> list:
    ...


@router.get('/organizations_using_activity/{activity}', tags=['Organizations'])
async def get_organizations_using_activity(activity: str) -> list:
    ...


@router.get('/organizations_using_coordinate/', tags=['Organizations'])
async def get_organizations_using_coordinate(сentre: float,
                                             edge: float) -> list:
    ...


@router.get('/organizations_using_id/{id}', tags=['Organizations'])
async def get_organizations_using_id(id: int) -> dict:
    ...


@router.get('/organizations_using_name/{name}', tags=['Organizations'])
async def get_organizations_using_name(name: str) -> dict:
    ...
