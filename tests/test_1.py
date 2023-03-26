import requests
import pytest

r_1_2_3 = requests.get('https://dog.ceo/api/breeds/image/random')
r_4 = requests.get('https://dog.ceo/api/breed/hound/list')
r_5 = requests.get('https://dog.ceo/api/breed/hound')


# help function for test_3
def specified_amount_images(url_test, number):
    target_url = url_test + f"/{number}"
    return target_url


# help function for test_5
def specified_sub_breed_dog(url_test, breed):
    target_url = url_test + f"/{breed}" + f"/images/random"
    return target_url


# test_1 - Test verifies that status code is successful
def test_status_code():
    assert r_1_2_3.status_code == 200


# test_2 - Test verifies that status in response is success
def test_status_random():
    assert r_1_2_3.json()['status'] == 'success'


# test_3 - Test verifies that correct amount of images is returned for each request
@pytest.mark.parametrize("number", [2, 3, 40])
def test_number_images(number):
    r = requests.get(specified_amount_images(r_1_2_3.url, number))
    assert len(r.json()['message']) == number


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
    assert sub_breed in r_4.json()['message']


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
    print(specified_sub_breed_dog(r_5.url, sub_breed))
    r = requests.get(specified_sub_breed_dog(r_5.url, sub_breed))
    assert len(r.json()['message'])
