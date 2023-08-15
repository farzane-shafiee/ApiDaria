from src.conftest import TestBaseConfigDriver
from src.logs.test_logger import log


class TestLogIn(TestBaseConfigDriver):

    def test_validate_api_get_1(self, api_get_1):
        assert api_get_1.status_code == 200
        assert api_get_1.json()['userId'] == 1
        assert api_get_1.json()['id'] == 1
        assert api_get_1.json()['title'] != ""
        assert api_get_1.json()['body'] != ""
        log.info('*** API api_get_1 is run. ***')

    def test_validate_api_get_2(self, api_get_2):
        assert api_get_2.status_code == 200
        assert api_get_2.json()['userId'] == 1
        assert api_get_2.json()['id'] == 2
        assert api_get_2.json()['title'] != ""
        assert api_get_2.json()['body'] != ""
        log.info('*** API api_get_2 is run. ***')

    def test_validate_api_get_photo(self, api_get_photo):
        assert api_get_photo[0].status_code == 200
        assert api_get_photo[0].json()['albumId'] == 1
        assert api_get_photo[0].json()['id'] == 1
        assert api_get_photo[0].json()['title'] != ""
        log.info('*** API api_get_photo is run. ***')

    def test_validate_api_get_photo_1(self, api_get_photo_1):
        assert api_get_photo_1.status_code == 200
        # assert api_get_photo_1.json()['albumId'] == 1
        # assert api_get_photo_1.json()['id'] == 1
        # assert api_get_photo_1.json()['title'] != ""
        log.info('*** API api_get_photo_1 is run. ***')

    def test_validate_api_post_1(self, api_post_1):
        assert api_post_1.status_code == 201
        assert api_post_1.json()['id'] == 101
        log.info('*** API api_post_1 is run. ***')

    def test_validate_api_put_1(self, api_put_1):
        assert api_put_1.status_code == 200
        assert api_put_1.json()['id'] == 1
        log.info('*** API api_put_1 is run. ***')