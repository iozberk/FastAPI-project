from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating : Optional [int] = None

class UserCreate(BaseModel):
    email = str
    password = str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


# class UpdatePost(PostBase):
#     pass

class Post(PostBase):
    class Config:
        orm_mode = True


    





