from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app import oauth2
from .. import models, schemas, oauth2
from ..database import get_db
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).all()
    return post

@router.post("/", response_model=schemas.Post ,status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    print(user_id)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
 
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post id: {id} was NOT find")
    print(post)
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} does NOT exist")
    post.delete(synchronize_session=False)   
    db.commit() 
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schemas.Post)
def update_post(id : int, updated_post: schemas.Post, db: Session = Depends(get_db), user_id : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= {"Post does NOT exist"})
    post_query.update(updated_post.dict(),synchronize_session=False)   
    db.commit() 
    return post_query.first()
