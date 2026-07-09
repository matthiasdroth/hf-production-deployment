from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "application": "Production HuggingFace Model API",
        "status": "running",
    }

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict():
    response = client.post("/predict", json={"text": "4+4=8."})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] in ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    assert 0.0 <= result["score"] <= 1.0