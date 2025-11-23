from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)


def test_valid_data():
    login= client.post("/login", json={"username": "mariam", "password": "mariam"})
    token = login.json()["token"]

    res = client.get("/data", headers={"token":token})

    assert res.status_code == 200
    assert "username" in res.json()

def test_invalid_data():
    res =client.get("/data", headers={"token":"fake_token"})

    assert res.status_code== 401

