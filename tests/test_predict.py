from fastapi.testclient import TestClient
from app.main import app
import pytest

client=TestClient(app)


def test_predict_positif(monkeypatch):
    def fake_predict(text):
        return [[{"label": "1 star", "score": 1}]]
    
    monkeypatch.setattr("app.main.predict_emotion",fake_predict)

    res = client.post("/predict", json={"text":"hello"})
    assert res.status_code == 200
    assert res.json()["var"] == "positif"

def test_predict_negatif(monkeypatch):
    def fake_predict(text):
        return [[{"label":"1","score":2}]]
    
    monkeypatch.setattr("app.main.predict_emotion", fake_predict)

    res = client.post("/predict",json={"text":"hello"})
    assert res.status_code == 200
    assert res.json()["var"] == "negatif"

def test_predict_neutre(monkeypatch):
    def fake_predict(text):
        return [[{"label":1,"score":3}]]
    
    monkeypatch.setattr("app.main.predict_emotion",fake_predict)

    res= client.post("/predict",json={"text":"hello"})
    assert res.status_code == 200
    assert res.json()["var"] == "neutre"
