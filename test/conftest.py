from turtle import title
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_user(client):
    user_data = {"email": "aaa@gmail.com", "password": "Password1!", "phone_number" : "555-555-5555"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def test_user2(client):
    user_data = {"email": "aaa2@gmail.com", "password": "Password1!", "phone_number" : "555-555-5555"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers,"Authorization": f"Bearer {token}"}
    return client

@pytest.fixture
def test_post(test_user, session, test_user2):
    post_data = [{"title": "Test Post 1", "content": "This is a test post 1", "owner_id": test_user['id']},
                 {"title": "Test Post 2", "content": "This is a test post 2", "owner_id": test_user['id']},
                 {"title": "Test Post 3", "content": "This is a test post 3", "owner_id": test_user['id']},
                 {"title": "Test Post 4", "content": "This is a test post 4", "owner_id": test_user2['id']}]
    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model,post_data)
    posts = list(post_map)
    session.add_all(posts)
    # session.add_all(models.Post(title= 'Test Post 1', content = 'This is a test post 1', owner_id =  test_user['id']),
    #                 models.Post(title= 'Test Post 2', content = 'This is a test post 2', owner_id = test_user['id']),
    #                 models.Post(title= 'Test Post 3', content = 'This is a test post 3', owner_id = test_user['id']),) 
    session.commit()
    posts = session.query(models.Post).all()                    

    return posts


