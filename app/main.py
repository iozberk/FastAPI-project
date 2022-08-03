import time
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import os

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional [int] = None

# try:
#     conn = psycopg2.connect(host = "ec2-176-34-215-248.eu-west-1.compute.amazonaws.com",database = "dc02oh10ouo2a2", user= "jjgpbdxckpkhrq", password="6c81246e0c47cfbda0202661616ff7cb659346a5c97b556cde0dbde9616ab79d", sslmode='require')
#     cursor = conn.cursor()
#     print("Database connection was successfully")
# except(Exception) as error:
#     print("Error while connecting to PostgreSQL", error)
#     print(error)


while(True):
    try:
        with open('dbpass.txt') as f:
            lines = f.readlines() 
        dbpassword = lines[0]
        f.close()
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres",
        password=dbpassword, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfully")
        # cursor.execute("SELECT * FROM posts")
        # posts = cursor.fetchall()
        # conn.close()
        break
    except (Exception) as error:
        print("Error while connecting to PostgreSQL", error)
        print(error)
        time.sleep(2)

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
    cursor.execute(""" SELECT * FROM post """)
    posts = cursor.fetchall()
    # print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0,100000)
    # my_posts.append(post_dict)
    new_post = cursor.execute(""" INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNING *  """, (post.title, post.content, post.published))
    new_post = cursor.fetchone() 
    conn.commit()

    return {"data": new_post} 
 
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    
    post = find_post(id) 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post id: {id} was NOT find")
    print(post)
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
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= {"Post does NOT exist"})
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}