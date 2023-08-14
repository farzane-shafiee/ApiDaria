import logging
import pytest
import yaml
import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://postman-echo.com"


class TestBaseConfigDriver:
    pass


@pytest.fixture(scope="session")
def read_yaml_file():
    # os.chdir(r'/src/tests/')
    with open('src/resource/resource.yml') as file:
        yaml_file = yaml.safe_load(file)
        return yaml_file


@pytest.fixture(scope="session")
def api_test():
    path = "/get?test=123"
    response = requests.get(BASE_URL + path)
    print(f"R {response.json()}")
    return response
