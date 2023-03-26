import requests
import pytest
from http import HTTPStatus

response_1_2_3_6 = requests.get('https://dog.ceo/api/breeds/image/random')
response_4 = requests.get('https://dog.ceo/api/breed/hound/list')
response_5 = requests.get('https://dog.ceo/api/breed/hound')


# help function for test_3
def specified_amount_images(url_test, number):
    target_url = f"{url_test}/{number}"
    return target_url


# help function for test_5
def specified_sub_breed_dog(url_test, breed):
    target_url = f"{url_test}/{breed}/images/random"
    return target_url


# test_1 - Test verifies that status code is succeeded
def test_status_code():
    assert response_1_2_3_6.status_code == HTTPStatus.OK


# test_2 - Test verifies that status in response is success
def test_status_random():
    assert response_1_2_3_6.status_code == HTTPStatus.OK
    assert response_1_2_3_6.json()['status'] == 'success'


# test_3 - Test verifies that correct amount of images is returned for each request
@pytest.mark.parametrize("number", [2, 3, 40])
def test_number_images(number):
    assert response_1_2_3_6.status_code == HTTPStatus.OK
    resp = requests.get(specified_amount_images(response_1_2_3_6.url, number))
    assert len(resp.json()['message']) == number


# test_4 - Test verifies that each sub_breed exists in the system for Hound breed
@pytest.mark.parametrize('sub_breed',
                         ["afghan",
                          "basset",
                          "blood",
                          "english",
                          "ibizan",
                          "plott",
                          "walker"]
                         )
def test_sub_breeds_hound(sub_breed):
    assert response_4.status_code == HTTPStatus.OK
    assert sub_breed in response_4.json()['message']


# test_5 - Test verifies that for each sub_breed there is at least one image
@pytest.mark.parametrize('sub_breed',
                         ["afghan",
                          "basset",
                          "blood",
                          "english",
                          "ibizan",
                          "plott",
                          "walker"]
                         )
def test_dog_for_sub_breed(sub_breed):
    response = requests.get(specified_sub_breed_dog(response_5.url, sub_breed))
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['message'])


# test_6 - Test verifies that response can return max 50 images
def test_max_images():
    resp = requests.get(specified_amount_images(response_1_2_3_6.url, 51))
    assert resp.status_code == HTTPStatus.OK
    assert len(resp.json()['message']) == 50
