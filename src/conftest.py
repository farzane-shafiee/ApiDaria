import pytest
import yaml
import requests
from src.db_connection_handler.db_handler import MySQLManager
import os
from dotenv import load_dotenv

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestBaseConfigDriver:
    mysql_manager = None

    @classmethod
    def setup_class(cls):
        """
        Remote and connect to device_data.
        """
        load_dotenv()
        cls.initialize_mysql_manager()

    @classmethod
    def initialize_mysql_manager(cls):
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_port = os.environ.get('DB_PORT')
        db_database = os.environ.get('DB_DATABASE')

        # Check if environment variables are not None
        assert db_host is not None, 'DB_HOST is not set'
        assert db_user is not None, 'DB_USER is not set'
        assert db_password is not None, 'DB_PASSWORD is not set'
        assert db_port is not None, 'DB_PORT is not set'
        assert db_database is not None, 'DB_DATABASE is not set'

        # Connect to Mysql
        cls.mysql_manager = MySQLManager(
            host=db_host,
            user=db_user,
            password=db_password,
            port=int(db_port),
            database=db_database,
        )
        cls.mysql_manager.connect()


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
