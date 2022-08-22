import pytest
from app import models

@pytest.fixture()
def test_vote(test_post, session, test_user):
    vote = models.Vote(post_id=test_post[3].id, user_id = test_user['id'])
    session.add(vote)
    session.commit()
    return vote


def test_vote_on_post(authorized_client, test_post):
    res = authorized_client.post("/vote/", json={"post_id": test_post[3].id, "dir": 1})
    assert res.status_code == 201
    # print(res.json())
    assert res.json()['message'] == "successfully added vote"

def test_vote_twice_post(authorized_client, test_post,test_vote):
    res = authorized_client.post("/vote/", json={"post_id": test_post[3].id, "dir": 1})
    assert res.status_code == 409
    

def test_vote_delete(authorized_client, test_post,test_vote):
    res = authorized_client.post("/vote/", json={"post_id": test_post[3].id, "dir": 0})
    assert res.status_code == 201
    assert res.json()['message'] == "successfully deleted vote"

def test_delete_vote_not_exist(authorized_client, test_post):
    res = authorized_client.post("/vote/", json={"post_id": test_post[3].id, "dir": 0})
    assert res.status_code == 404




