
def test_create(test_client):
    response = test_client.post("/customers", json={
        "corporate_name":"Teste", "phone": "55 9197643433", "revenue": 10.0 })

    assert response.status_code == 201
    assert response.json()['corporate_name'] == 'Teste'
    assert response.json()['phone'] == "55 9197643433"
    assert response.json()['revenue'] == 10.0


def test_show(test_client):
    response = test_client.post("/customers", json={
        "corporate_name":"Teste 2", "phone": "55 65534533", "revenue": 12.21 })

    customer_id = response.json()['id']

    response = test_client.get(f'/customers/{customer_id}')

    assert response.status_code == 200
    assert response.json()['corporate_name'] == 'Teste 2'
    assert response.json()['phone'] == "55 65534533"
    assert response.json()['revenue'] == 12.21


def test_update(test_client):
    response = test_client.post("/customers", json={
        "corporate_name":"Teste 2", "phone": "55 65534533", "revenue": 12.21 })

    customer_id = response.json()['id']

    response = test_client.put(f'/customers/{customer_id}', json={
        "corporate_name":"Teste 3", "phone": "55 7665534533", "revenue": 10000.21 })

    assert response.status_code == 201
    assert response.json()['corporate_name'] == 'Teste 3'
    assert response.json()['phone'] == "55 7665534533"
    assert response.json()['revenue'] == 10000.21


def test_delete(test_client):
    response = test_client.post("/customers", json={
        "corporate_name":"Teste 2", "phone": "55 65534533", "revenue": 12.21 })

    customer_id = response.json()['id']

    response = test_client.delete(f'/customers/{customer_id}')

    assert response.status_code == 200

    response = test_client.get(f'/customers/{customer_id}')

    assert response.status_code == 404