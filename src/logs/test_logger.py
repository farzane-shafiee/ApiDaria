import logging


log = logging.getLogger(__name__)

log.setLevel(logging.INFO)
test_filehandler = logging.FileHandler(filename='src/logs/test.log', mode='a')
test_formatter = logging.Formatter('%(asctime)s   -   %(levelname)s   -   %(funcName)s   -   %(message)s')
test_filehandler.setFormatter(test_formatter)
log.addHandler(test_filehandler)
