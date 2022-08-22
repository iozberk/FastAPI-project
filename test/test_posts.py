

def test_get_all_posts(authorized_client, test_post):
    res = authorized_client.get("/posts/")
    print(res.json())
    assert res.status_code == 200