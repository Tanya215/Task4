import requests
import pytest

r_1_2 = requests.get('https://api.openbrewerydb.org/v1/breweries/random')
url_3_4_5 = 'https://api.openbrewerydb.org/v1/breweries'


# test_1 - Test verifies that status code is succeeded
def test_status_code():
    assert r_1_2.status_code == 200


# test_2  - Test verifies that something is returned for random request
def test_random_return():
    assert len(r_1_2.json())


# test_3  - Test verifies that something found for each state
@pytest.mark.parametrize("state", ["new_york", "california", "texas"])
def test_search_item_by_state(state):
    target_url = url_3_4_5 + f"?by_state={state}"
    r = requests.get(target_url)
    assert len(r.json())


# test_4  - Test verifies that valid amount breweries is found
@pytest.mark.parametrize("per_page", [4, 5, 6])
def test_amount_per_page(per_page):
    target_url = url_3_4_5 + f"?per_page={per_page}"
    r = requests.get(target_url)
    assert len(r.json()) == per_page


# test_5  - Test verifies that per_page and size return the same values
@pytest.mark.parametrize("per_page_size", [7, 8, 9])
def test_per_page_and_size(per_page_size):
    target_url_per_page = url_3_4_5 + f"?per_page={per_page_size}"
    target_url_size = r_1_2.url + f"?size={per_page_size}"
    r_per_page = requests.get(target_url_per_page)
    r_size = requests.get(target_url_size)
    assert len(r_per_page.json()) == len(r_size.json())
