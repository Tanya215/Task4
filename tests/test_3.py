import requests
import pytest

url_main = 'https://jsonplaceholder.typicode.com'


# test_1 - Test verifies that status code is succeeded
def test_status_code():
    target_url = url_main + f"/todos/1"
    r = requests.get(target_url)
    assert r.status_code == 200


# test_2 - Test verifies that each id something is posted
@pytest.mark.parametrize("userid", [2, 3, 4])
def test_post_by_user(userid):
    target_url = url_main + f"/posts" + f"/{userid}"
    r = requests.get(target_url)
    assert len(r.json())


# test_3 - Test verifies that each post has comments
@pytest.mark.parametrize("postid", [4, 5, 6])
def test_comments_by_post(postid):
    target_url = url_main + f"/posts" + f"/{postid}" + f"/comments"
    r = requests.get(target_url)
    assert len(r.json())


# test_4 - Test verifies that 10 users are found
def test_amount_users():
    target_url = url_main + f"/users"
    r = requests.get(target_url)
    assert len(r.json()) == 10


# test_5 - Test verifies that 100 albums are found
def test_amount_albums():
    target_url = url_main + f"/albums"
    r = requests.get(target_url)
    assert len(r.json()) == 100
