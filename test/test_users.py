from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, engine, Base


# with open('dburl.txt') as f:
#     lines = f.readlines() 
#     pasw = lines[0]
#     f.close()

# SQLALCHEMY_DATABASE_URL = f'postgres://postgres:{pasw}@localhost:5432/fastapi'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)

# # Dependency
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "PytestUserCreate12345@pytest.com", "password": "Password1!", "phone_number" : "555-555-5555"})
    assert response.status_code == 201

