from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password1 = utils.hash(user.password1)
    hashed_password2 = utils.hash(user.password2)
    user.password1 = hashed_password1
    user.password2 = hashed_password2

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User id: {id} was NOT find")
    print(user)
    return user