import re
from textwrap import indent
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional [int] = None

# class UpdatePost(BaseModel):    

my_posts = [{"title" : "First Post Title", "content" : "First Post Content", "id": 1},
                {"title" : "Second Post Title", "content" : "Second Post Content", "id": 2},
                {"title" : "Last Post Title", "content" : "Last Post Content", "id": 3}]

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    # print(post.title)
    # print(post.content)
    # print(post.published)
    # print(post.dict())
    my_posts.append(post_dict)
    return {"data": post_dict}
 
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    
    post = find_post(id) 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post id: {id} was NOT find")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"post_detail": f"Post id: {id} was not find"}
    print(post)
    # return {"post_detail": f"Post id: {id} | and it returned by ID"}
    return {"post_detail": post}

@app.delete("posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= {"Post does NOT exist"})

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id : int, post: Post):
    return {"message": "post updated"}

# Branch test


