import pytest

def client_payload(
    equipment_id=1,
    borrower_name="Lance",
    loan_days=12,
    purpose="For own use",
    status="PENDING"
):
    return {
        "equipment_id": equipment_id,
        "borrower_name": borrower_name,
        "loan_days": loan_days,
        "purpose": purpose,
        "status": status,
    }

def test_create_client(client):
    response = client.post("/api/loans", json=client_payload())

    assert response.status_code == 201
    assert response.json()["equipment_id"] == 1
    assert response.json()["borrower_name"] == "Lance"
    assert response.json()["loan_days"] == 12
    assert response.json()["purpose"] == "For own use"
    assert response.json()["status"] == "PENDING"

def test_create_client_invalid(client):
    response = client.post("/api/loans", json=client_payload(equipment_id=-1))

    assert response.status_code == 422

def test_delete_client(client):
    response = client.post("/api/loans", json=client_payload())
    assert response.status_code == 201

    delete = client.delete("/api/loan/1")
    assert delete.status_code == 204

    retrieve = client.get("/api/loan/1")
    assert retrieve.status_code == 404