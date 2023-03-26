import requests




# testing ulr and status from console
def test_valid_url(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code
