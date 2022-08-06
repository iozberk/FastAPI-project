from pydantic import BaseModel, EmailStr, validator


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating : Optional [int] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
class Post(PostBase):
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr
    password1: str
    password2: str

class UserCreate(UserBase):
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v
    

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email : EmailStr
    class Config:
        orm_mode = True
