import pytest

from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.asyncio
async def test_organizations_using_house():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        ...


@pytest.mark.asyncio
async def test_organizations_using_activity():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        ...


@pytest.mark.asyncio
async def test_organizations_using_coordinate():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        ...


@pytest.mark.asyncio
async def test_organizations_using_id():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        ...


@pytest.mark.asyncio
async def test_organizations_using_name():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(transport=ASGITransport(app),
                           base_url='http://test') as ac:
        ...
