from calendar import c
from typing import List
from app import schemas
import pytest

def test_get_all_posts(authorized_client, test_post):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    post_map = map(validate, res.json())
    post_list = list(post_map)
    # print(res.json())
    # posts = schemas.PostOut(**res.json())
    # assert len(res.json()) == len(test_post)
    assert post_list[0].Post.id == test_post[0].id
    assert post_list[0].Post.title == test_post[0].title
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_post):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_post(authorized_client, test_post):
    res = authorized_client.get(f"/posts/{test_post[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_post[0].id
    assert post.Post.title == test_post[0].title
    assert res.status_code == 200

def test_get_one_post_not_exist(authorized_client, test_post):
    res = authorized_client.get(f"/posts/999")
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_post):
    res = authorized_client.get(f"/posts/{test_post[0].id}")
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_post[0].id
    assert post.Post.title == test_post[0].title
    assert post.Post.content == test_post[0].content
    assert res.status_code == 200

@pytest.mark.parametrize("title, content, published", [
    ("Test Post 4", "This is a test post 4", True),
    ("Test Post 5", "This is a test post 5", False),
    ("Test Post 6", "This is a test post 6", True),])
def test_create_post(authorized_client, test_user, title, content, published):
    post_data = {"title": title, "content": content, "published": published}
    res = authorized_client.post("/posts/", json=post_data)
    created_post = schemas.Post(**res.json())
    assert created_post.title == post_data['title']
    assert created_post.content == post_data['content']
    assert created_post.published == post_data['published']
    assert created_post.owner_id == test_user['id']
    assert res.status_code == 201

def test_create_post_default_published_true(authorized_client, test_user, test_post):
    post_data = {"title": "title", "content": "content", "published": True}
    res = authorized_client.post("/posts/", json=post_data)
    created_post = schemas.Post(**res.json())
    assert created_post.title == 'title'
    assert created_post.content == 'content'
    assert created_post.published == True
    assert res.status_code == 201


def test_unauthorized_user_create_post(client, test_user ,test_post):
    post_data = {"title": "title", "content": "content", "published": True}
    res = client.post("/posts/", json=post_data)
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_user ,test_post):
    res = client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code == 401

def test_delete_post_successful(authorized_client, test_user ,test_post):
    res = authorized_client.delete(f"/posts/{test_post[0].id}")
    assert res.status_code == 204


def test_delete_post_not_exist(authorized_client, test_user ,test_post):
    res = authorized_client.delete("/posts/9999999999999")
    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_user, test_user2,test_post):
    res = authorized_client.delete(f"/posts/{test_post[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_post):
    post_data = {"title": "updated title", "content": "updated content","id": test_post[0].id}
    res = authorized_client.put(f"/posts/{test_post[0].id}", json=post_data)
    updated_post = schemas.Post(**res.json())
    # print(updated_post)
    assert updated_post.title == 'updated title'
    assert updated_post.content == 'updated content'
    assert res.status_code == 200

def test_update_other_user_post(authorized_client, test_user, test_user2, test_post):
    post_data = {"title": "updated other user title", "content": "updated other user content","id": test_post[3].id}
    res = authorized_client.put(f"/posts/{test_post[3].id}", json=post_data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_post):
    post_data = {"title": "unauthorized user updated title", "content": "unauthorized user updated content","id": test_post[0].id}
    res = client.put(f"/posts/{test_post[0].id}", json=post_data)
    assert res.status_code == 401

