from src.conftest import TestBaseConfigDriver
from src.logs.test_logger import log


class TestLogIn(TestBaseConfigDriver):

    def test_should_validate_api(self, api_test):
        assert api_test.status_code == 200
        assert api_test.json()['args']['test'] == "123"
        assert api_test.json()['headers']['host'] != ""
        assert api_test.json()['url'] == "https://postman-echo.com/get?test=123"
        log.info('*** API test is run. ***')
