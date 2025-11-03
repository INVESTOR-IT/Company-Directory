import pytest

from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.asyncio
async def test_organizations_using_house():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='http://test'
    ) as ac:
        response = await ac.get('/organizations_using_house/1')
        assert response.status_code == 200
        response_organization = response.json()[0]
        assert response_organization.get('id', None) == 1
        assert isinstance(response_organization.get('name', None), str)
        assert isinstance(response_organization.get('phones', None), list)
        assert isinstance(response_organization.get('houses_id', None), int)
        assert isinstance(response_organization.get('activities_id', None), int)


@pytest.mark.asyncio
async def test_organizations_using_activity():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='http://test'
    ) as ac:
        response = await ac.get('/organizations_using_activity/3')
        assert response.status_code == 200
        response_organization = response.json()[0]
        assert response_organization.get('id', None) == 2
        assert isinstance(response_organization.get('name', None), str)
        assert isinstance(response_organization.get('phones', None), list)
        assert isinstance(response_organization.get('houses_id', None), int)
        assert isinstance(response_organization.get('activities_id', None), int)


@pytest.mark.asyncio
async def test_organizations_using_coordinate():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='http://test'
    ) as ac:
        response = await ac.post(
            '/organizations_using_coordinate',
            json={
                'longitude': 50,
                'latitude': 50,
                'radius': 10
            }
        )
        assert response.status_code == 200
        response_organization = response.json()[0]
        assert len(response.json()) == 3
        assert response_organization.get('id', None) == 2
        assert isinstance(response_organization.get('name', None), str)
        assert isinstance(response_organization.get('phones', None), list)
        assert isinstance(response_organization.get('houses_id', None), int)
        assert isinstance(response_organization.get('activities_id', None), int)


@pytest.mark.asyncio
async def test_organizations_using_id():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='http://test'
    ) as ac:
        response = await ac.get('/organizations_using_id/1')
        assert response.status_code == 200
        response_organization = response.json()[0]
        assert response_organization.get('id', None) == 1
        assert isinstance(response_organization.get('name', None), str)
        assert isinstance(response_organization.get('phones', None), list)
        assert isinstance(response_organization.get('houses_id', None), int)
        assert isinstance(response_organization.get('activities_id', None), int)


@pytest.mark.asyncio
async def test_organizations_using_name():
    '''
    Позже будет подробная doc
    '''

    async with AsyncClient(
        transport=ASGITransport(app),
        base_url='http://test'
    ) as ac:
        response = await ac.get('/organizations_using_name/а')
        assert response.status_code == 200
        response_organization = response.json()[0]
        assert len(response.json()) == 3
        assert response_organization.get('id', None) == 1
        assert isinstance(response_organization.get('name', None), str)
        assert isinstance(response_organization.get('phones', None), list)
        assert isinstance(response_organization.get('houses_id', None), int)
        assert isinstance(response_organization.get('activities_id', None), int)
