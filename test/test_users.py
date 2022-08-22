import pytest
from jose import jwt
from app.config import settings
from app import schemas
from .database import client, session


@pytest.fixture
def test_user(client):
    user_data = {"email": "aaa@gmail.com", "password": "Password1!", "phone_number" : "555-555-5555"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

    
def test_create_user(client):
    res = client.post("/users/", json={"email": "aaa@gmail.com", "password": "Password1!", "phone_number" : "555-555-5555"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "aaa@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200