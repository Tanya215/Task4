import requests
import pytest
from http import HTTPStatus

response_1_2 = requests.get('https://api.openbrewerydb.org/v1/breweries/random')
url_3_4_5 = 'https://api.openbrewerydb.org/v1/breweries'


# test_1 - Test verifies that status code is succeeded
def test_status_code():
    assert response_1_2.status_code == HTTPStatus.OK


# test_2  - Test verifies that something is returned for random request
def test_random_return():
    assert response_1_2.status_code == HTTPStatus.OK
    assert len(response_1_2.json())


# test_3  - Test verifies that something found for each state
@pytest.mark.parametrize("state", ["new_york", "california", "texas"])
def test_search_item_by_state(state):
    target_url = f"{url_3_4_5}?by_state={state}"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json())


# test_4  - Test verifies that valid amount breweries is found
@pytest.mark.parametrize("per_page", [4, 5, 6])
def test_amount_per_page(per_page):
    target_url = f"{url_3_4_5}?per_page={per_page}"
    response = requests.get(target_url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == per_page


# test_5  - Test verifies that per_page and size return the same values
@pytest.mark.parametrize("per_page_size", [7, 8, 9])
def test_per_page_and_size(per_page_size):
    target_url_per_page = f"{url_3_4_5}?per_page={per_page_size}"
    target_url_size = f"{response_1_2.url}?size={per_page_size}"
    resp_per_page = requests.get(target_url_per_page)
    resp_size = requests.get(target_url_size)
    assert resp_per_page.status_code == HTTPStatus.OK
    assert resp_size.status_code == HTTPStatus.OK
    assert len(resp_per_page.json()) == len(resp_size.json())


# test_6  - Test verifies that max amount of items per_page is 200
def test_max_items_per_page():
    target_url_per_page = f"{url_3_4_5}?per_page=201"
    resp = requests.get(target_url_per_page)
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json()) == 200
