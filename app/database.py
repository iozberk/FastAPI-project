from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open('dbpass.txt') as f:
    lines = f.readlines() 
    db_password = lines[0]
    f.close()

SQLALCHEMY_DATABASE_URL = "postgresql://jjgpbdxckpkhrq:6c81246e0c47cfbda0202661616ff7cb659346a5c97b556cde0dbde9616ab79d@ec2-176-34-215-248.eu-west-1.compute.amazonaws.com:5432/dc02oh10ouo2a2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
