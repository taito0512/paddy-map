from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_regions():
    response = client.get("/regions")
    assert response.status_code == 200

def test_parcels():
    response = client.get("/parcels?region=82350")
    assert response.status_code == 200

def test_parcels_with_threshold():
    response = client.get("/parcels?region=82350&threshold=0.3")
    data = response.json()
    assert len(data) == 95

