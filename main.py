from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional [int] = None

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "Your Posts Endpoint"}

@app.post("/createposts")
def create_posts(post: Post):
    print(post.title)
    print(post.content)
    print(post.published)
    print(post.dict())
    return {"data": post}


""" POSTMAN 
{
    "detail": [
        {
            "loc": [
                "body",
                "content"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
"""
