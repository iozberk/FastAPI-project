from typing import List
from app import schemas

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

