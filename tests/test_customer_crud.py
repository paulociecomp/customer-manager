from app.domain.customer.customer_model import Customer
import asynctest
import pytest

payload = {
        "corporate_name":"My company",
        "phone": "55 9197643433",
        "revenue": 10.0,
        "city": "BelHell",
        "postal_code": "123123",
        "state": "PA",
        "street": "baker",
        "number": "00",
        "dstrict": "13",
        "country": "brazil",
    }

@pytest.mark.asyncio
async def test_create(test_client):
    response = await test_client.post("/customers", json=payload)

    assert response.status_code == 201
    assert response.json()['corporate_name'] == 'My company'
    assert response.json()['phone'] == "55 9197643433"
    assert response.json()['revenue'] == 10.0
    assert response.json()['city'] == "BelHell"
    assert response.json()['postal_code'] == "123123"
    assert response.json()['state'] == "PA"
    assert response.json()['street'] == "baker"
    assert response.json()['number'] == "00"
    assert response.json()['dstrict'] == "13"
    assert response.json()['country'] == "brazil"


@pytest.mark.asyncio
async def test_show(test_client):
    customer = await Customer.create(**payload)

    response = await test_client.get(f'/customers/{customer.id}')

    assert response.status_code == 200
    assert response.json()['corporate_name'] == 'My company'
    assert response.json()['phone'] == "55 9197643433"
    assert response.json()['revenue'] == 10.0
    assert response.json()['city'] == "BelHell"
    assert response.json()['postal_code'] == "123123"
    assert response.json()['state'] == "PA"
    assert response.json()['street'] == "baker"
    assert response.json()['number'] == "00"
    assert response.json()['dstrict'] == "13"
    assert response.json()['country'] == "brazil"


@pytest.mark.asyncio
async def test_update(test_client):
    payload = {
        "corporate_name":"My New Company",
        "phone": "55 9197643433",
        "revenue": 100000.0,
        "city": "Londres",
        "postal_code": "123123",
        "state": "PA",
        "street": "baker",
        "number": "00",
        "dstrict": "13",
        "country": "brazil",
    }

    customer = await Customer.create(**payload)

    response = await test_client.put(f'/customers/{customer.id}', json=payload)

    assert response.status_code == 201
    assert response.json()['corporate_name'] == 'My New Company'
    assert response.json()['phone'] == "55 9197643433"
    assert response.json()['revenue'] == 100000.0
    assert response.json()['city'] == "Londres"
    assert response.json()['postal_code'] == "123123"
    assert response.json()['state'] == "PA"
    assert response.json()['street'] == "baker"
    assert response.json()['number'] == "00"
    assert response.json()['dstrict'] == "13"
    assert response.json()['country'] == "brazil"


@pytest.mark.asyncio
async def test_delete(test_client):
    customer = await Customer.create(**payload)

    response = await test_client.delete(f'/customers/{customer.id}')

    assert response.status_code == 200

    response = await test_client.get(f'/customers/{customer.id}')

    assert response.status_code == 404