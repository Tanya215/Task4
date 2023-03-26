import requests
import pytest


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def test_valid_url(url, status_code):
    r = requests.get(url)
    assert r.status_code == int(status_code)
