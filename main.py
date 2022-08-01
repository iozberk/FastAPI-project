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

post_example = [{"title" : "First Post Title", "content" : "First Post Content", "id": 1},
                {"title" : "Second Post Title", "content" : "Second Post Content", "id": 2},
                {"title" : "Last Post Title", "content" : "Last Post Content", "id": 3}]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": post_example}

@app.post("/posts")
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
