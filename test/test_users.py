from app import schemas
from .database import client, session


def test_login_user(client):
    res = client.post("/login/", json={"username": "ismail@ismail.com", "password": "Password1!"})
    assert res.status_code == 200
    
def test_create_user(client):
    response = client.post("/users/", json={"username": "aaa@gmail.com", "password": "Password1!", "phone_number" : "555-555-5555"})
    assert response.status_code == 201

