import requests
import pytest
from http import HTTPStatus

url_main = 'https://jsonplaceholder.typicode.com'


# test_1 - Test verifies that status code is succeeded
def test_status_code():
    target_url = f"{url_main}/todos/1"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK


# test_2 - Test verifies that each id something is posted
@pytest.mark.parametrize("userid", [2, 3, 4])
def test_post_by_user(userid):
    target_url = f"{url_main}/posts/{userid}"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json())


# test_3 - Test verifies that each post has comments
@pytest.mark.parametrize("postid", [4, 5, 6])
def test_comments_by_post(postid):
    target_url = f"{url_main}/posts/{postid}/comments"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json())


# test_4 - Test verifies that 10 users are found
def test_amount_users():
    target_url = f"{url_main}/users"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 10


# test_5 - Test verifies that 100 albums are found
def test_amount_albums():
    target_url = f"{url_main}/albums"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 100

# test_6 - Test verifies that 100 posts are found
def test_amount_posts():
    target_url = f"{url_main}/posts"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 100