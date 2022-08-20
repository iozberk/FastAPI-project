from fastapi.testclient import TestClient
from app.main import app
import requests 
client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "PytestUserCreate123@pytest.com", "password": "Password1!", "phone_number" : "555-555-5555"})
    assert response.status_code == 201

