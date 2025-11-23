from fastapi.testclient import TestClient
from app.main import app

client= TestClient(app)


def test_login():
    res = client.post("/login", json={"username": "mariam", "password": "mariam"})
    assert res.status_code == 200
    assert "token" in res.json()

def failed_login():
    res = client.post("/login", json={"username": "wrong", "password": "wrong"})
    assert res.status_code == 200
    assert res.json() == "not working"