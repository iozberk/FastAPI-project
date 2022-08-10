from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open('dburl.txt') as f:
    lines = f.readlines() 
    SQLALCHEMY_DATABASE_URL = lines[0]
    f.close()

# with open('dbpass.txt') as f:
#     lines = f.readlines() 
#     pasw = lines[0]
#     f.close()

# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{pasw}@localhost/fastapi"

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
