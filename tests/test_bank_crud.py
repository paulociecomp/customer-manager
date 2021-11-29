from app.domain.bank.bank_model import Bank
import asynctest
import pytest

from app.domain.customer.customer_model import Customer


customer_data = {
        "corporate_name":"Space X",
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
    bank_data = {
        "agency": "123123",
        "account": "3445345",
        "bank_code": "231"
    }

    customer = await Customer.create(**customer_data)
    response = await test_client.post(f'/customers/{customer.id}/banks', json=bank_data)

    assert response.status_code == 201
    assert response.json()['agency'] == "123123"
    assert response.json()['account'] == "3445345"
    assert response.json()['bank_code'] == "231"


@pytest.mark.asyncio
async def test_show(test_client):
    bank_data = {
        "agency": "765757",
        "account": "9085643",
        "bank_code": "123"
    }

    customer = await Customer.create(**customer_data)
    bank = await Bank.create(customer_id=customer.id, **bank_data)

    response = await test_client.get(f'/customers/{customer.id}/banks/{bank.id}')

    assert response.status_code == 200
    assert response.json()['agency'] == "765757"
    assert response.json()['account'] == "9085643"
    assert response.json()['bank_code'] == "123"


@pytest.mark.asyncio
async def test_update(test_client):
    bank_data = {
        "agency": "565765",
        "account": "9782342",
        "bank_code": "654"
    }

    customer = await Customer.create(**customer_data)
    bank = await Bank.create(customer_id=customer.id, **bank_data)

    response = await test_client.put(f'/customers/{customer.id}/banks/{bank.id}', json={
        "agency": "88888",
        "account": "11111",
        "bank_code": "444"
    })

    assert response.status_code == 201
    assert response.json()['agency'] == "88888"
    assert response.json()['account'] == "11111"
    assert response.json()['bank_code'] == "444"


@pytest.mark.asyncio
async def test_delete(test_client):
    bank_data = {
        "agency": "565765",
        "account": "9782342",
        "bank_code": "654"
    }

    customer = await Customer.create(**customer_data)
    bank = await Bank.create(customer_id=customer.id, **bank_data)

    response = await test_client.delete(f'/customers/{customer.id}/banks/{bank.id}')

    assert response.status_code == 200
    assert await Bank.get(bank.id) == None
