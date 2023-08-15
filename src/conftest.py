import logging
import pytest
import yaml
import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestBaseConfigDriver:
    pass


@pytest.fixture(scope="session")
def read_yaml_file():
    # os.chdir(r'/src/tests/')
    with open('src/resource/resource.yml') as file:
        yaml_file = yaml.safe_load(file)
        return yaml_file


@pytest.fixture(scope="session")
def api_get_1():
    path = "/posts/1"
    response = requests.get(BASE_URL + path)
    return response


@pytest.fixture(scope="session")
def api_get_2():
    path = "/posts/2"
    response = requests.get(BASE_URL + path)
    return response


@pytest.fixture(scope="session")
def api_get_photo():
    path = "/photos/1"
    response = requests.get(BASE_URL + path)
    url = response.json()['url']
    return response, url


@pytest.fixture(scope="session")
def api_get_photo_1(api_get_photo):
    path = f"{api_get_photo[1]}"
    response = requests.get(path)
    return response


@pytest.fixture(scope="session")
def api_post_1():
    path = "/posts"
    response = requests.post(BASE_URL + path)
    return response


@pytest.fixture(scope="session")
def api_put_1():
    path = "/posts/1"
    response = requests.put(BASE_URL + path)
    return response
