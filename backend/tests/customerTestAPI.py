from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_customers():
    response = client.get("/api/customers")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_customer():

    response = client.post(
        "/api/customers",
        json={
            "name": "Joe Smith",
            "email": "joe@email.com"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Joe Smith"
    assert data["email"] == "joe@email.com"

def test_get_customer():

    create_response = client.post(
        "/api/customers",
        json={
            "name": "Bob",
            "email": "bob@email.com"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.get(
        f"/api/customers/{customer_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id

def test_get_missing_customer():

    response = client.get(
        "/api/customers/9999"
    )

    assert response.status_code == 404