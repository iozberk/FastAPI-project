

import json


def test_vote_on_post(authorized_client, test_post):
    res = authorized_client.post("/vote/", json={"post_id": test_post[3].id, "dir": 1})
    assert res.status_code == 201
    print(res.json())
    assert res.json()['message'] == "successfully added vote"